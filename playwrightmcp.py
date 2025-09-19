import asyncio
import os

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams, create_mcp_server_session, mcp_server_tools
from openai_key import OPENAI_API_KEY


async def main() -> None:
    openai_api_key = OPENAI_API_KEY
    if not openai_api_key:
        raise RuntimeError("OPENAI_API_KEY not set in openai_key.py.")
    model_client = OpenAIChatCompletionClient(
        model="gpt-5-mini",
        parallel_tool_calls=False,
        api_key=openai_api_key,  
    )
    params = StdioServerParams(
        command="npx",
        args=["@playwright/mcp@latest"],
        read_timeout_seconds=60,
    )
    async with create_mcp_server_session(params) as session:
        await session.initialize()
        tools = await mcp_server_tools(server_params=params, session=session)
        print(f"Tools: {[tool.name for tool in tools]}")

        mcp_agent = AssistantAgent(
            name="Assistant",
            model_client=model_client,
            tools=tools,  # type: ignore
        )

        user_proxy = UserProxyAgent( name="Student" )

        termination = TextMentionTermination("Thank you")
        team = RoundRobinGroupChat(participants=[user_proxy, mcp_agent], termination_condition=termination)
        await Console(
            team.run_stream(
                task="You are a web browsing assistant"
            )
        )


asyncio.run(main())

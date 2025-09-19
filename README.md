# AIAgent_POC

This repository contains small examples using Microsoft Autogen AgentChat and the Autogen extensions with OpenAI.

## Steps to download / install

Official Autogen AgentChat installation guide:

https://microsoft.github.io/autogen/stable//user-guide/agentchat-user-guide/installation.html

Install the core packages and optional extras used in this project:

```bash
pip install -U "autogen-agentchat"
pip install "autogen-ext[openai]"
```

If you need MCP (Model Context Protocol) server tools:

https://microsoft.github.io/autogen/stable//reference/python/autogen_ext.tools.mcp.html#autogen_ext.tools.mcp.mcp_server_tools

Install the MCP extras:

```bash
pip install -U "autogen-ext[mcp]"
```

## Usage

- Keep your OpenAI API key out of the repository. Store it as an environment variable or in a local file ignored by git (for example, `openai_key.py` is ignored in this repo).
- Example scripts:
  - `scenario1.py` — web browsing agent example (uses MCP web browsing tools)
  - `basics6.py` — filesystem-enabled math tutor example (uses MCP filesystem)

Run an example (from project root):

```bash
python scenario1.py
# or
python basics6.py
```

## Security notes

- Do NOT commit API keys or other secrets. If a secret is accidentally committed, rotate/revoke it immediately.
- This repo already contains a `.gitignore` entry to keep `openai_key.py` out of the repository.

## Next steps

- Add a `requirements.txt` or `pyproject.toml` for reproducible installs.
- Add example environment variable instructions and a sample `.env.example` file.

---

If you want, I can add `requirements.txt`, example `.env` usage, or update README with usage examples and expected outputs.
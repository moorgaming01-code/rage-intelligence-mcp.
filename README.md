
# RAGE Intelligence MCP 🚀

An open-source project researching Rockstar's RAGE game engine using publicly available information.

**New here?** Start with our [Beginner's Guide](README-BEGINNERS.md).

### Useful links
- [Project Vision](docs/PROJECT_VISION.md)
- [Architecture](docs/ARCHITECTURE.md)
- [How to Contribute](CONTRIBUTING.md)
- [Growth Strategy](GROWTH-STRATEGY.md)

---

## 🎮 What is this project?

RAGE Intelligence MCP is a research project that helps people explore and organise information about Rockstar's RAGE technology and publicly documented GTA VI systems.

It uses an MCP server to let compatible AI applications access our research.

Our goal is simple: make game-engine research easier to explore, understand and share.

**Important:** This is an independent project. We are not affiliated with Rockstar Games or Take-Two Interactive.

---

## 🛠️ What have we built?

The project currently has:

- A research knowledge base.
- A system for organising evidence and sources.
- Automatic claim validation.
- A research search tool.
- A working Python MCP server.
- Four working MCP tools.
- Beginner and contributor guides.

### Our four MCP tools

| Tool | What it does |
|---|---|
| `list_claims` | Shows all research claims. |
| `search_claims` | Searches our research. |
| `get_claim` | Finds a specific claim. |
| `validate_knowledge` | Checks our research records and sources. |

All four tools have been tested using MCP Inspector.

---

## 📂 What's inside?

- `docs` — Project information and architecture.
- `research` — Research sources.
- `knowledge` — Research claims and evidence.
- `schemas` — Data validation rules.
- `src` — Python code and MCP server.
- `tests` — Automated tests.

---

## 💻 Getting started

You need:
- Python 3.10 or newer.
- Git.

### Step 1: Download the project

Open PowerShell and run:

```bash
git clone https://github.com/moorgaming01-code/newmpc.git
```

### Step 2: Open the project folder

```bash
cd newmpc
```

### Step 3: Install it

```bash
python -m pip install -e .
```

### Step 4: Check everything works

```bash
rage-knowledge validate
```

### Step 5: View the research

```bash
rage-knowledge list
```

### Step 6: Search the research

```bash
rage-knowledge search streaming
```

### Step 7: Start the MCP server

```bash
python -m rage_intelligence.server
```

Need help connecting an AI application? Follow our [Beginner's Guide](README-BEGINNERS.md).

---

## 🤝 Want to help?

We welcome people interested in:

- Game technology.
- Python programming.
- Artificial intelligence.
- MCP development.
- Research and documentation.
- Testing and improving the project.

You don't need to be an expert to contribute!

Read our [Contributing Guide](CONTRIBUTING.md) to get started.

---

## 🔭 What's next?

We want to:

- Expand our research database.
- Learn more about RAGE technology.
- Add more MCP tools.
- Improve our research and evidence systems.
- Welcome new developers and researchers.
- Build a stronger open-source community.

---

## 🔒 Our rules

We only use publicly available information and lawful research.

We do not use:
- Leaked or private Rockstar source code.
- DRM or anti-cheat bypasses.
- Unauthorised access to game memory.
- Code injection into proprietary games.

We also separate confirmed information from reports, inferences, hypotheses and unknowns.

---

## 📜 License

This project uses the MIT License. See [LICENSE](LICENSE).

Rockstar Games and Grand Theft Auto are trademarks and intellectual property of their respective owners.

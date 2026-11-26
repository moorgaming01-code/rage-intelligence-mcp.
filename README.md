# RAGE Intelligence MCP 🚀

**An open-source research project exploring Rockstar's RAGE game engine using publicly available information.**

New to the project? Start with our [Beginner's Guide](README-BEGINNERS.md).

### Project links
- [Project Vision](docs/PROJECT_VISION.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Contributing Guide](CONTRIBUTING.md)
- [Growth Strategy](GROWTH-STRATEGY.md)

---

## 🎮 What is RAGE Intelligence MCP?

RAGE Intelligence MCP is an independent research project focused on Rockstar's RAGE technology and publicly documented information about GTA VI.

The project organises technical information, research claims, evidence and sources into one structured knowledge base.

It also includes an MCP server that allows compatible AI applications to explore our research.

**Our mission:** Make game-engine research easier to understand, explore and share.

> This is an independent community project. It is not affiliated with, endorsed by, or connected to Rockstar Games or Take-Two Interactive.

---

## 🛠️ What have we built?

The project currently includes:

- A structured research knowledge base.
- An evidence and source tracking system.
- Automatic research claim validation.
- Keyword-based research searching.
- A Python MCP server.
- Four working MCP tools.
- Automated tests.
- Beginner and contributor documentation.

### Our four MCP tools

| Tool | Description |
|---|---|
| `list_claims` | Displays all research claims. |
| `search_claims` | Searches research using keywords. |
| `get_claim` | Retrieves an individual research claim. |
| `validate_knowledge` | Checks research records and source references. |

All four tools have been successfully tested using MCP Inspector.

---

## 📂 Project structure

Here is a simple explanation of the main folders:

| Folder | Purpose |
|---|---|
| `docs/` | Project information and architecture. |
| `research/` | Research sources and references. |
| `knowledge/` | Research claims, evidence and open questions. |
| `schemas/` | Rules for validating research records. |
| `src/` | Python code and MCP server. |
| `tests/` | Automated software tests. |

---

## 💻 Getting started

Want to run the project on your own computer?

Follow these steps.

### Requirements

You will need:

- Python 3.10 or newer.
- Git.
- PowerShell on Windows, or a terminal on another operating system.

### Step 1 — Download the project

Open PowerShell and run:

```bash
git clone https://github.com/moorgaming01-code/newmpc.git
```

### Step 2 — Open the project folder

```bash
cd newmpc
```

### Step 3 — Install the project

```bash
python -m pip install -e .
```

### Step 4 — Validate the knowledge base

```bash
rage-knowledge validate
```

### Step 5 — List research claims

```bash
rage-knowledge list
```

### Step 6 — Search the research

```bash
rage-knowledge search streaming
```

### Step 7 — Start the MCP server

```bash
python -m rage_intelligence.server
```

For help connecting the MCP server to a compatible AI application, follow our [Beginner's Guide](README-BEGINNERS.md).

---

## 🤝 Want to contribute?

We welcome people who are interested in:

- Game-engine technology.
- Python development.
- Artificial intelligence.
- MCP development.
- Technical research.
- Evidence collection.
- Documentation.
- Software testing.

You don't need to be an expert to get involved.

Every useful contribution helps the project grow.

Read our [Contributing Guide](CONTRIBUTING.md) to learn how to participate.

---

## 🔭 What's next?

Our future development goals include:

- Expanding the research knowledge base.
- Researching more RAGE technology subsystems.
- Improving evidence tracking.
- Adding more MCP tools.
- Improving AI-assisted research.
- Welcoming new developers and researchers.
- Building an active open-source community.

Development will remain focused on reliable research, useful software and evidence-based conclusions.

---

## 🔒 Research standards and safety

We only use publicly available information and lawful research methods.

This project does not involve:

- Leaked or private Rockstar source code.
- DRM or anti-cheat bypasses.
- Unauthorised access to protected game memory.
- Code injection into proprietary games.
- Presenting speculation as confirmed technical information.

We clearly distinguish between:

- **Confirmed** — supported by reliable primary evidence.
- **Reported** — information attributed to publications or interviews.
- **Inference** — conclusions drawn from available evidence.
- **Hypothesis** — possibilities that still need investigation.
- **Unknown** — information that has not been established.

Accuracy and transparency come before speculation.

### 📸 See RAGE Intelligence MCP in action

Here is our MCP server connected and successfully running all four tools.

![RAGE Intelligence MCP Inspector Demo](docs/mcp-inspector-demo.png)

---

## 📜 Licence

This project is released under the MIT Licence.

See the [LICENSE](LICENSE) file for details.

Rockstar Games, Grand Theft Auto and related trademarks and intellectual property belong to their respective owners.

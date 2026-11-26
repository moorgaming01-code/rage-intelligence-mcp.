


# RAGE Intelligence MCP

**An open-source, evidence-aware research platform for publicly documented Rockstar RAGE technology.**

New to MCP or GitHub? Start with the [Beginner's Guide](README-BEGINNERS.md).

[Project Vision](docs/PROJECT_VISION.md) · [Architecture](docs/ARCHITECTURE.md) · [Contributing](CONTRIBUTING.md) · [Growth Strategy](GROWTH-STRATEGY.md)

---

## What is RAGE Intelligence MCP?

RAGE Intelligence MCP is an independent research and knowledge platform for studying publicly documented Rockstar Advanced Game Engine (RAGE) technology and publicly observable GTA VI systems.

It combines structured research records, evidence tracking, validation tools, and a Model Context Protocol (MCP) server that allows compatible AI applications to explore the knowledge base.

The goal is to make technical research more organised, traceable, reproducible, and accessible.

> **Important:** This is an independent community project. It is not affiliated with, endorsed by, or connected to Rockstar Games or Take-Two Interactive.

## Current status

**Stage 2 — Knowledge core and MCP server foundation implemented.**

The project currently includes:

- Structured research claim records.
- JSON Schema validation.
- Source-reference validation.
- Keyword-based claim searching.
- A working Python MCP server.
- Four tested MCP tools.
- Beginner setup and contribution documentation.

The MCP server has been connected and tested using MCP Inspector.

### Available MCP tools

| Tool | Purpose |
|---|---|
| `list_claims` | Lists research claims in the knowledge base. |
| `search_claims` | Searches claims using keywords. |
| `get_claim` | Retrieves an individual claim by ID. |
| `validate_knowledge` | Checks claim records and source references. |

These tools expose the project's documented research. They do not provide access to Rockstar's private engine implementation.

## Project principles

1. **Evidence before certainty** — distinguish confirmed facts, reported information, technical inferences, hypotheses, and unknowns.
2. **Public and authorised inputs only** — no leaked or private source code, DRM or anti-cheat bypass, process injection, or unauthorised memory access.
3. **Traceability** — substantive claims should include sources, dates, confidence levels, and review status.
4. **Reproducibility** — document how observations were collected and how conclusions were reached.
5. **Useful openness** — make the research structure and tools understandable to contributors.

## Repository structure

- `docs/` — project vision and architecture.
- `research/` — source register and research references.
- `knowledge/claims/` — structured research claims.
- `knowledge/evidence/` — evidence ledger.
- `knowledge/subsystems/` — subsystem catalogue.
- `knowledge/unknowns/` — open research questions.
- `schemas/` — JSON schemas for knowledge records.
- `src/rage_intelligence/` — Python knowledge core, CLI, and MCP server.
- `tests/` — automated validation tests.
- `README-BEGINNERS.md` — beginner setup guide.
- `CONTRIBUTING.md` — contribution guidelines.
- `GROWTH-STRATEGY.md` — project growth strategy.

## Getting started

### Requirements

- Python 3.10 or newer.
- Git.
- A compatible MCP client if you want to connect the server to an AI application.

### Install

Clone the repository:

```bash
git clone https://github.com/moorgaming01-code/newmpc.git
cd newmpc
```

Install the project:

```bash
python -m pip install -e .
```

### Validate the knowledge base

```bash
rage-knowledge validate
```

### List research claims

```bash
rage-knowledge list
```

### Search research claims

```bash
rage-knowledge search streaming
```

### Run the MCP server

```bash
python -m rage_intelligence.server
```

For MCP client configuration and Windows-specific instructions, see the [Beginner's Guide](README-BEGINNERS.md).

## Research terminology

| Classification | Meaning |
|---|---|
| Confirmed | Directly supported by a primary source or reproducible observation. |
| Reported | Attributed to a publication, interview, or secondary source. |
| Inference | A reasoned conclusion drawn from available evidence. |
| Hypothesis | A testable possibility with incomplete support. |
| Unknown | Not established by available evidence. |

## How to contribute

We welcome people interested in:

- Game-engine technology research.
- Python development.
- MCP integrations.
- Technical documentation.
- Evidence collection and source verification.
- Testing and improving the knowledge base.

Start with [CONTRIBUTING.md](CONTRIBUTING.md).

Good research matters more than big claims. Every contribution should respect the project's evidence standards and safety principles.

## Roadmap

Future development may include:

- Expanded RAGE technology research.
- More structured subsystem records.
- Improved evidence and claim relationships.
- Additional MCP tools.
- Better research discovery and documentation.
- Community contributions and independent verification.

Development priorities will be guided by evidence quality, usefulness, and community feedback.

## Scope and safety

This project focuses on publicly available information and lawful research.

It does not seek to:

- Obtain or distribute leaked Rockstar source code.
- Bypass DRM, anti-cheat, or access controls.
- Inject code into proprietary game processes.
- Access protected game memory without authorisation.
- Present speculation as confirmed GTA VI implementation details.

## License

Released under the MIT License. See [LICENSE](LICENSE).

Rockstar Games, Grand Theft Auto, and related trademarks and intellectual property belong to their respective owners.

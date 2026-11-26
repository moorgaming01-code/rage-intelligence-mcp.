# RAGE Intelligence MCP

An independent, open-source research and knowledge platform for studying Rockstar's RAGE technology and publicly observable GTA VI systems.

> **Scope:** research, evidence management, subsystem modelling, and AI-accessible knowledge tools. This project is not affiliated with Rockstar Games or Take-Two Interactive.

## Project principles

1. **Evidence before certainty** — distinguish confirmed facts, attributed reports, technical inferences, hypotheses, and unknowns.
2. **Public and authorised inputs only** — no leaked/private source code, DRM or anti-cheat bypass, process injection, or unauthorised memory access.
3. **Traceability** — every substantive claim should have a source, date, confidence, and review status.
4. **Reproducibility** — document how observations were collected and how conclusions were reached.
5. **Useful openness** — make the research structure and tooling understandable to contributors.

## Current status

**v0.1 — Knowledge foundation scaffold.** This release establishes the initial folder structure, data conventions, subsystem catalogue, evidence ledger template, and roadmap. It does not claim access to Rockstar's internal engine implementation.

## Repository map

- `docs/` — project vision, architecture, roadmap, contribution guidance.
- `research/` — research notes and source index.
- `knowledge/subsystems/` — subsystem records and dependency model.
- `knowledge/evidence/` — evidence ledger and claim records.
- `knowledge/hypotheses/` — explicitly unverified technical hypotheses.
- `knowledge/unknowns/` — questions requiring further research.
- `schemas/` — JSON schemas for structured knowledge records.
- `src/` — future implementation of the knowledge core and MCP server.
- `tests/` — validation tests.
- `backups/` — local backup instructions; do not commit large or sensitive dumps.

## Quick start

This scaffold is documentation-first. No runtime dependencies are required yet.

1. Read `docs/PROJECT_VISION.md`.
2. Review `knowledge/evidence/EVIDENCE_LEDGER.csv`.
3. Add new claims using `schemas/claim.schema.json`.
4. Keep reported claims attributed to their original publication or interview.
5. Record unknowns rather than filling gaps with guesses.

## Important terminology

- **Confirmed:** directly supported by a primary source or reproducible observation.
- **Reported:** stated by a secondary publication or attributed interview; primary source still needs checking where possible.
- **Inference:** a reasoned conclusion drawn from evidence, not directly stated by a source.
- **Hypothesis:** a testable possibility with incomplete support.
- **Unknown:** not established by available evidence.

## License

MIT. See `LICENSE`. Third-party trademarks and game materials remain the property of their respective owners.

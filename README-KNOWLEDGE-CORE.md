# RAGE Intelligence Knowledge Core v0.1

A small local Python tool for reading, searching and validating structured research claims.

## What it does

- Reads claim records from `knowledge/claims/CLM-*.json`.
- Validates each record against `schemas/claim.schema.json`.
- Checks that referenced source IDs exist in `research/SOURCE_REGISTER.csv`.
- Lists and searches claim records.
- Includes unit tests.

This is a local knowledge-base utility, **not yet an MCP server**. It does not connect to GTA VI, inspect game processes, modify game files, or access Rockstar systems.

## Install

From the repository root:

```bash
python -m venv .venv
```

Activate the environment, then run:

```bash
python -m pip install -e .
```

## Commands

```bash
rage-knowledge validate
rage-knowledge list
rage-knowledge search streaming
```

If the command is not on your PATH, use:

```bash
python -m rage_intelligence.cli validate
python -m rage_intelligence.cli list
python -m rage_intelligence.cli search streaming
```

## Tests

```bash
python -m unittest discover -s tests -v
```

## Expected repository layout

```text
schemas/claim.schema.json
research/SOURCE_REGISTER.csv
knowledge/claims/CLM-0001.json
src/rage_intelligence/
tests/
pyproject.toml
```

The package expects to be run from the repository root, or with `--root PATH`.

## Evidence discipline

A valid JSON record is not automatically a true claim. Schema validation checks structure and source references only; human review is still required to assess whether a source actually supports a claim.

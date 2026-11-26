"""Read and validate local RAGE Intelligence knowledge records."""
from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


class KnowledgeError(Exception):
    """Raised when the local knowledge repository is malformed."""


def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise KnowledgeError(f"Cannot read JSON file {path}: {exc}") from exc


def load_schema(repo_root: Path) -> dict[str, Any]:
    schema_path = repo_root / "schemas" / "claim.schema.json"
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    return schema


def load_source_ids(repo_root: Path) -> set[str]:
    register = repo_root / "research" / "SOURCE_REGISTER.csv"
    if not register.exists():
        raise KnowledgeError(f"Source register not found: {register}")
    try:
        with register.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames or "source_id" not in reader.fieldnames:
                raise KnowledgeError("SOURCE_REGISTER.csv must contain a source_id column.")
            return {
                (row.get("source_id") or "").strip()
                for row in reader
                if (row.get("source_id") or "").strip()
            }
    except OSError as exc:
        raise KnowledgeError(f"Cannot read source register: {exc}") from exc


def claim_files(repo_root: Path) -> list[Path]:
    claims_dir = repo_root / "knowledge" / "claims"
    if not claims_dir.exists():
        return []
    return sorted(claims_dir.glob("CLM-*.json"))


def validate_claims(repo_root: Path) -> list[str]:
    """Return validation errors; an empty list means all discovered claims pass."""
    schema = load_schema(repo_root)
    validator = Draft202012Validator(schema)
    source_ids = load_source_ids(repo_root)
    errors: list[str] = []

    for path in claim_files(repo_root):
        try:
            claim = load_json(path)
        except KnowledgeError as exc:
            errors.append(str(exc))
            continue

        for error in sorted(validator.iter_errors(claim), key=lambda e: list(e.path)):
            location = ".".join(str(part) for part in error.absolute_path) or "(record)"
            errors.append(f"{path}: {location}: {error.message}")

        if isinstance(claim, dict):
            for source_id in claim.get("source_ids", []):
                if source_id not in source_ids:
                    errors.append(f"{path}: source_id {source_id!r} is missing from SOURCE_REGISTER.csv")

            expected_name = f"{claim.get('claim_id', '')}.json"
            if path.name != expected_name:
                errors.append(f"{path}: filename should be {expected_name}")

    if not claim_files(repo_root):
        errors.append(f"No claim records found in {repo_root / 'knowledge' / 'claims'}")
    return errors


def search_claims(repo_root: Path, query: str) -> list[dict[str, Any]]:
    """Case-insensitive search across claim text, scope, status and limitations."""
    needle = query.casefold()
    results = []
    for path in claim_files(repo_root):
        claim = load_json(path)
        searchable = " ".join([
            str(claim.get("claim", "")),
            str(claim.get("scope", "")),
            str(claim.get("status", "")),
            " ".join(claim.get("limitations", [])),
        ]).casefold()
        if needle in searchable:
            results.append(claim)
    return results

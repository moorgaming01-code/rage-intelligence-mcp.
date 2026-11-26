"""Command-line interface for the RAGE Intelligence Knowledge Core."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .core import KnowledgeError, claim_files, load_json, search_claims, validate_claims


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="rage-knowledge",
        description="Inspect and validate the local RAGE Intelligence knowledge base.",
    )
    parser.add_argument(
        "--root", default=".", help="Repository root (default: current directory)"
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate", help="Validate claim JSON and source references")
    sub.add_parser("list", help="List available claim records")
    search = sub.add_parser("search", help="Search claim text and metadata")
    search.add_argument("query", help="Text to search for")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.root).resolve()

    try:
        if args.command == "validate":
            errors = validate_claims(root)
            if errors:
                print("Validation failed:")
                for error in errors:
                    print(f"- {error}")
                return 1
            print("Validation passed. All discovered claim records match the schema and source register.")
            return 0

        if args.command == "list":
            paths = claim_files(root)
            if not paths:
                print("No claim records found.")
                return 0
            for path in paths:
                claim = load_json(path)
                print(f"{claim.get('claim_id', path.stem)} [{claim.get('status', 'unknown')}] — {claim.get('claim', '')}")
            return 0

        if args.command == "search":
            results = search_claims(root, args.query)
            print(json.dumps(results, indent=2, ensure_ascii=False))
            return 0 if results else 1

    except KnowledgeError as exc:
        print(f"Error: {exc}")
        return 2

    return 2


if __name__ == "__main__":
    raise SystemExit(main())

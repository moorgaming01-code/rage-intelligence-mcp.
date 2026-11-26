import json
import tempfile
import unittest
from pathlib import Path

from rage_intelligence.core import search_claims, validate_claims


class KnowledgeCoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "schemas").mkdir()
        (self.root / "research").mkdir()
        (self.root / "knowledge" / "claims").mkdir(parents=True)

        schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "additionalProperties": False,
            "required": ["claim_id", "claim", "status", "confidence", "scope",
                         "source_ids", "limitations", "review_status"],
            "properties": {
                "claim_id": {"type": "string", "pattern": "^CLM-[0-9]{4,}$"},
                "claim": {"type": "string", "minLength": 10},
                "status": {"enum": ["confirmed", "reported", "inference", "hypothesis", "unknown"]},
                "confidence": {"enum": ["low", "medium", "high"]},
                "scope": {"type": "string"},
                "source_ids": {"type": "array", "items": {"type": "string", "pattern": "^SRC-[0-9]{4,}$"}, "uniqueItems": True},
                "limitations": {"type": "array", "items": {"type": "string"}},
                "review_status": {"enum": ["open", "needs_review", "needs_primary_review", "reviewed"]}
            }
        }
        (self.root / "schemas" / "claim.schema.json").write_text(json.dumps(schema), encoding="utf-8")
        (self.root / "research" / "SOURCE_REGISTER.csv").write_text(
            "source_id,title\nSRC-0001,Example source\n", encoding="utf-8"
        )
        claim = {
            "claim_id": "CLM-0001",
            "claim": "Streaming was described as foundational to open-world technology.",
            "status": "reported",
            "confidence": "medium",
            "scope": "Historical RAGE technology",
            "source_ids": ["SRC-0001"],
            "limitations": ["Does not prove the GTA VI implementation."],
            "review_status": "needs_review"
        }
        (self.root / "knowledge" / "claims" / "CLM-0001.json").write_text(
            json.dumps(claim), encoding="utf-8"
        )

    def tearDown(self):
        self.temp.cleanup()

    def test_valid_claim_passes(self):
        self.assertEqual(validate_claims(self.root), [])

    def test_search_finds_claim(self):
        results = search_claims(self.root, "streaming")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["claim_id"], "CLM-0001")

    def test_missing_source_is_reported(self):
        path = self.root / "knowledge" / "claims" / "CLM-0001.json"
        claim = json.loads(path.read_text(encoding="utf-8"))
        claim["source_ids"] = ["SRC-9999"]
        path.write_text(json.dumps(claim), encoding="utf-8")
        errors = validate_claims(self.root)
        self.assertTrue(any("missing from SOURCE_REGISTER.csv" in item for item in errors))


if __name__ == "__main__":
    unittest.main()

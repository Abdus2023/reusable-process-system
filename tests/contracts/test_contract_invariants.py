import unittest

class ContractInvariantTests(unittest.TestCase):
    def test_snapshot_requires_commit_and_tree(self):
        schema = self._load("schemas/repository/repository-snapshot.schema.json")
        self.assertEqual(schema["required"], ["schema", "repository", "ref", "commit", "tree"])

    def test_execution_evidence_declares_immutable_scope(self):
        schema = self._load("schemas/execution/execution-evidence.schema.json")
        self.assertIn("authority", schema["required"])
        self.assertIn("scope", schema["required"])
        self.assertEqual(schema["properties"]["scope"]["required"], ["repository", "commit", "tree"])
        self.assertEqual(schema["properties"]["scope"]["required"], ["repository", "commit", "tree"])

    def test_not_observable_is_not_pass(self):
        schema = self._load("schemas/adapters/adapter-result.schema.json")
        self.assertIn("NOT_OBSERVABLE", schema["properties"]["decision"]["enum"])
        self.assertNotIn("PASS", schema["properties"]["decision"]["enum"])

    def test_verification_has_explicit_non_verified_states(self):
        schema = self._load("schemas/verification/verification-result.schema.json")
        decisions = schema["properties"]["decision"]["enum"]
        for state in ("BLOCKED", "UNKNOWN", "PROVISIONAL", "PARTIALLY_VERIFIED"):
            self.assertIn(state, decisions)

    @staticmethod
    def _load(path):
        import json
        from pathlib import Path
        return json.loads(Path(path).read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
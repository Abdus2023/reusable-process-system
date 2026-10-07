import json
import unittest
from pathlib import Path


class WorktreeBindingSchemaTests(unittest.TestCase):
    def test_schema_is_well_formed(self):
        path = Path("schemas/repository/worktree-binding.schema.json")
        document = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(
            document["properties"]["schema"]["const"],
            "reusable-process-system.worktree-binding/1",
        )
        self.assertEqual(
            set(document["properties"]["status"]["enum"]),
            {"CLEAN", "DIRTY", "NOT_OBSERVABLE", "MISMATCH", "BOUND"},
        )


if __name__ == "__main__":
    unittest.main()

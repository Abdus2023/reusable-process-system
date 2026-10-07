import subprocess
import tempfile
import unittest
from pathlib import Path

from adapters.local.snapshot import resolve_snapshot


class LocalSnapshotResolverTests(unittest.TestCase):
    def test_resolves_commit_and_tree_from_git(self):
        with tempfile.TemporaryDirectory() as tmp:
            cwd = Path(tmp)
            subprocess.run(["git", "init"], cwd=cwd, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=cwd, check=True)
            subprocess.run(["git", "config", "user.name", "Test"], cwd=cwd, check=True)
            (cwd / "file.txt").write_text("snapshot\n", encoding="utf-8")
            subprocess.run(["git", "add", "file.txt"], cwd=cwd, check=True)
            subprocess.run(["git", "commit", "-m", "snapshot"], cwd=cwd, check=True, capture_output=True)

            result = resolve_snapshot(cwd, repository="example/repo", ref="test")
            self.assertEqual(result["schema"], "reusable-process-system.repository-snapshot/1")
            self.assertTrue(result["commit"])
            self.assertTrue(result["tree"])
            self.assertEqual(result["ref"], "test")
            self.assertIn("LOCAL_OBSERVATION_IS_NOT_CI_AUTHORITY", result["limitations"])

    def test_missing_repository_is_not_observable(self):
        result = resolve_snapshot("/does/not/exist", repository="example/repo")
        self.assertEqual(result["commit"], "")
        self.assertIn("SNAPSHOT_NOT_OBSERVABLE", result["limitations"])


if __name__ == "__main__":
    unittest.main()

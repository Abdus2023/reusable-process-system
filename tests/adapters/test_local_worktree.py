import subprocess
import tempfile
import unittest
from pathlib import Path

from adapters.local.worktree import resolve_worktree_binding, validate_execution_target


class LocalWorktreeBindingTests(unittest.TestCase):
    def _repo(self, tmp: str) -> Path:
        cwd = Path(tmp)
        subprocess.run(["git", "init"], cwd=cwd, check=True, capture_output=True)
        subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=cwd, check=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=cwd, check=True)
        (cwd / "file.txt").write_text("committed\n", encoding="utf-8")
        subprocess.run(["git", "add", "file.txt"], cwd=cwd, check=True)
        subprocess.run(["git", "commit", "-m", "snapshot"], cwd=cwd, check=True, capture_output=True)
        return cwd

    def test_clean_worktree_is_bound(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = resolve_worktree_binding(self._repo(tmp))
            self.assertEqual(result["status"], "CLEAN")
            self.assertTrue(result["clean"])

    def test_tracked_change_is_dirty(self):
        with tempfile.TemporaryDirectory() as tmp:
            cwd = self._repo(tmp)
            (cwd / "file.txt").write_text("modified\n", encoding="utf-8")
            result = resolve_worktree_binding(cwd)
            self.assertEqual(result["status"], "DIRTY")
            self.assertFalse(result["clean"])

    def test_untracked_file_is_dirty(self):
        with tempfile.TemporaryDirectory() as tmp:
            cwd = self._repo(tmp)
            (cwd / "generated.txt").write_text("untracked\n", encoding="utf-8")
            result = resolve_worktree_binding(cwd)
            self.assertEqual(result["status"], "DIRTY")
            self.assertFalse(result["clean"])


    def test_execution_target_requires_exact_commit_and_clean_worktree(self):
        with tempfile.TemporaryDirectory() as tmp:
            cwd = self._repo(tmp)
            commit = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=cwd, check=True, capture_output=True, text=True
            ).stdout.strip()
            tree = subprocess.run(
                ["git", "rev-parse", "HEAD^{tree}"],
                cwd=cwd, check=True, capture_output=True, text=True
            ).stdout.strip()
            result = validate_execution_target(
                cwd,
                snapshot={"repository": "example/repo", "commit": commit, "tree": tree},
            )
            self.assertEqual(result["status"], "BOUND")

    def test_execution_target_rejects_commit_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            cwd = self._repo(tmp)
            result = validate_execution_target(
                cwd,
                snapshot={
                    "repository": "example/repo",
                    "commit": "0" * 40,
                    "tree": "0" * 40,
                },
            )
            self.assertEqual(result["status"], "MISMATCH")
            self.assertTrue(result["clean"])

    def test_execution_target_rejects_tree_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            cwd = self._repo(tmp)
            commit = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=cwd, check=True, capture_output=True, text=True
            ).stdout.strip()
            result = validate_execution_target(
                cwd,
                snapshot={"repository": "example/repo", "commit": commit, "tree": "0" * 40},
            )
            self.assertEqual(result["status"], "MISMATCH")
            self.assertEqual(result["reason"], "HEAD_TREE_MISMATCH")

    def test_execution_target_rejects_dirty_worktree(self):
        with tempfile.TemporaryDirectory() as tmp:
            cwd = self._repo(tmp)
            commit = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=cwd, check=True, capture_output=True, text=True
            ).stdout.strip()
            result = validate_execution_target(
                cwd,
                snapshot={"repository": "example/repo", "commit": commit, "tree": "unused"},
            )
            self.assertEqual(result["status"], "BOUND")
            (cwd / "file.txt").write_text("changed\n", encoding="utf-8")
            result = validate_execution_target(
                cwd,
                snapshot={"repository": "example/repo", "commit": commit, "tree": "unused"},
            )
            self.assertEqual(result["status"], "DIRTY")

    def test_missing_repository_is_not_observable(self):
        result = resolve_worktree_binding("/does/not/exist")
        self.assertEqual(result["status"], "NOT_OBSERVABLE")
        self.assertFalse(result["clean"])


if __name__ == "__main__":
    unittest.main()

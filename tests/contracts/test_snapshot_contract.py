import unittest

from contracts.snapshot import validate_snapshot


class SnapshotContractTests(unittest.TestCase):
    def test_complete_snapshot_is_valid(self):
        snapshot = {
            "schema": "reusable-process-system.repository-snapshot/1",
            "repository": "example/repo",
            "ref": "main",
            "commit": "abc",
            "tree": "def",
        }
        self.assertEqual(validate_snapshot(snapshot), (True, "VALID"))

    def test_missing_tree_is_invalid(self):
        snapshot = {
            "schema": "reusable-process-system.repository-snapshot/1",
            "repository": "example/repo",
            "ref": "main",
            "commit": "abc",
        }
        self.assertEqual(
            validate_snapshot(snapshot),
            (False, "MISSING_SNAPSHOT_FIELD:tree"),
        )

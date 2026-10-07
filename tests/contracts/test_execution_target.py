import unittest

from contracts.execution_target import (
    bind_execution_target,
    unbound_execution_target,
    validate_target_contract,
)


class ExecutionTargetContractTests(unittest.TestCase):
    def setUp(self):
        self.snapshot = {
            "repository": "Abdus2023/reusable-process-system",
            "ref": "extract/core-foundation",
            "commit": "a" * 40,
            "tree": "b" * 40,
        }

    def test_snapshot_alone_is_unbound(self):
        target = unbound_execution_target(self.snapshot)
        valid, reason = validate_target_contract(target)
        self.assertTrue(valid, reason)
        self.assertEqual(target["binding"], "UNBOUND")

    def test_bound_requires_worktree_binding(self):
        with self.assertRaisesRegex(ValueError, "WORKTREE_NOT_BOUND"):
            bind_execution_target(
                self.snapshot,
                {"status": "CLEAN"},
            )

    def test_bound_target_is_valid(self):
        target = bind_execution_target(
            self.snapshot,
            {"status": "BOUND"},
        )
        valid, reason = validate_target_contract(target)
        self.assertTrue(valid, reason)
        self.assertEqual(target["binding"], "BOUND")

    def test_missing_identity_rejected(self):
        invalid = {
            "schema": "reusable-process-system.execution-target/1",
            "repository": "repo",
            "binding": "UNBOUND",
        }
        valid, reason = validate_target_contract(invalid)
        self.assertFalse(valid)
        self.assertEqual(reason, "MISSING_FIELD:commit,tree")

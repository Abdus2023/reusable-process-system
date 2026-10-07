import unittest

from contracts.evidence_binding import can_verify, validate_execution_evidence


def evidence(**overrides):
    value = {
        "schema": "reusable-process-system.execution-evidence/1",
        "evidence_id": "sha256:test",
        "authority": "CI",
        "kind": "EXECUTION",
        "status": "PASS",
        "scope": {
            "repository": "Abdus2023/reusable-process-system",
            "ref": "extract/core-foundation",
            "commit": "commit-A",
            "tree": "tree-A",
        },
    }
    value.update(overrides)
    return value


class EvidenceBindingTests(unittest.TestCase):
    target = {
        "repository": "Abdus2023/reusable-process-system",
        "ref": "extract/core-foundation",
        "commit": "commit-A",
        "tree": "tree-A",
    }

    def test_matching_ci_execution_verifies(self):
        ok, reason = can_verify(evidence(), self.target)
        self.assertTrue(ok)
        self.assertEqual(reason, "VERIFIED")

    def test_branch_only_evidence_is_rejected(self):
        item = evidence()
        del item["scope"]["commit"]
        ok, reason = can_verify(item, self.target)
        self.assertFalse(ok)
        self.assertEqual(reason, "MISSING_IMMUTABLE_SCOPE:commit")

    def test_missing_tree_is_rejected(self):
        item = evidence()
        del item["scope"]["tree"]
        ok, reason = can_verify(item, self.target)
        self.assertFalse(ok)
        self.assertEqual(reason, "MISSING_IMMUTABLE_SCOPE:tree")

    def test_not_observable_cannot_verify(self):
        item = evidence(status="NOT_OBSERVABLE")
        ok, reason = can_verify(item, self.target)
        self.assertFalse(ok)
        self.assertEqual(reason, "STATUS_NOT_PASS:NOT_OBSERVABLE")

    def test_local_evidence_cannot_satisfy_ci_requirement(self):
        item = evidence(authority="LOCAL")
        ok, reason = can_verify(item, self.target)
        self.assertFalse(ok)
        self.assertEqual(reason, "AUTHORITY_MISMATCH")

    def test_commit_mismatch_is_rejected(self):
        item = evidence()
        item["scope"]["commit"] = "commit-B"
        ok, reason = can_verify(item, self.target)
        self.assertFalse(ok)
        self.assertEqual(reason, "SCOPE_MISMATCH:commit")

    def test_tree_mismatch_is_rejected(self):
        item = evidence()
        item["scope"]["tree"] = "tree-B"
        ok, reason = can_verify(item, self.target)
        self.assertFalse(ok)
        self.assertEqual(reason, "SCOPE_MISMATCH:tree")

    def test_target_without_commit_or_tree_is_rejected(self):
        target = {"repository": self.target["repository"], "ref": self.target["ref"]}
        ok, reason = can_verify(evidence(), target)
        self.assertFalse(ok)
        self.assertEqual(reason, "TARGET_MISSING_IMMUTABLE_SCOPE:commit,tree")

    def test_validation_rejects_missing_scope(self):
        item = evidence()
        del item["scope"]
        ok, reason = validate_execution_evidence(item)
        self.assertFalse(ok)
        self.assertEqual(reason, "MISSING_FIELD:scope")


if __name__ == "__main__":
    unittest.main()

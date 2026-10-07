import unittest

from contracts.adapter import validate_adapter_result


class AdapterContractTests(unittest.TestCase):
    def test_executed_requires_matching_evidence_id(self):
        result = {
            "schema": "reusable-process-system.adapter-result/1",
            "decision": "EXECUTED",
            "evidence_ids": ["sha256:x"],
            "evidence": {"evidence_id": "sha256:x"},
        }
        self.assertEqual(validate_adapter_result(result), (True, "VALID"))

    def test_executed_without_evidence_is_invalid(self):
        result = {
            "schema": "reusable-process-system.adapter-result/1",
            "decision": "EXECUTED",
        }
        self.assertEqual(
            validate_adapter_result(result),
            (False, "EXECUTED_REQUIRES_EVIDENCE"),
        )

    def test_blocked_does_not_require_evidence(self):
        result = {
            "schema": "reusable-process-system.adapter-result/1",
            "decision": "BLOCKED",
            "reason": "MISSING_IMMUTABLE_SCOPE:commit",
        }
        self.assertEqual(validate_adapter_result(result), (True, "VALID"))

    def test_unknown_decision_is_invalid(self):
        result = {
            "schema": "reusable-process-system.adapter-result/1",
            "decision": "PASS",
        }
        self.assertEqual(
            validate_adapter_result(result),
            (False, "INVALID_DECISION"),
        )


if __name__ == "__main__":
    unittest.main()

import unittest

from adapters.local.process import run_process


SNAPSHOT = {
    "repository": "Abdus2023/reusable-process-system",
    "ref": "extract/core-foundation",
    "commit": "commit-A",
    "tree": "tree-A",
}


class LocalProcessAdapterTests(unittest.TestCase):
    def test_success_emits_bound_local_execution_evidence(self):
        result = run_process(["python", "-c", "print('ok')"], snapshot=SNAPSHOT)
        self.assertEqual(result["decision"], "EXECUTED")
        evidence = result["evidence"]
        self.assertEqual(evidence["authority"], "LOCAL")
        self.assertEqual(evidence["kind"], "EXECUTION")
        self.assertEqual(evidence["status"], "PASS")
        self.assertEqual(evidence["scope"]["commit"], "commit-A")
        self.assertEqual(evidence["scope"]["tree"], "tree-A")

    def test_failure_emits_fail_evidence(self):
        result = run_process(["python", "-c", "raise SystemExit(3)"], snapshot=SNAPSHOT)
        self.assertEqual(result["decision"], "EXECUTED")
        self.assertEqual(result["evidence"]["status"], "FAIL")

    def test_missing_snapshot_scope_blocks(self):
        result = run_process(["python", "-c", "print('ok')"], snapshot={"repository": "r"})
        self.assertEqual(result["decision"], "BLOCKED")
        self.assertEqual(result["reason"], "MISSING_IMMUTABLE_SCOPE:commit,tree")

    def test_empty_command_blocks(self):
        result = run_process([], snapshot=SNAPSHOT)
        self.assertEqual(result["decision"], "BLOCKED")
        self.assertEqual(result["reason"], "EMPTY_COMMAND")

    def test_timeout_is_explicit_failure(self):
        result = run_process(
            ["python", "-c", "import time; time.sleep(1)"],
            snapshot=SNAPSHOT,
            timeout_seconds=0.01,
        )
        self.assertEqual(result["decision"], "FAILED")
        self.assertEqual(result["reason"], "TIMEOUT")


if __name__ == "__main__":
    unittest.main()

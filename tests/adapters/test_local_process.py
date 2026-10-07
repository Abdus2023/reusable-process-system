import sys
import unittest

from adapters.local.process import DEFAULT_OUTPUT_LIMIT, run_process


class LocalProcessAdapterTests(unittest.TestCase):
    def setUp(self):
        self.target = {
            "repository": "repo",
            "commit": "a" * 40,
            "tree": "b" * 40,
            "binding": "BOUND",
        }

    def test_success_emits_local_execution_evidence(self):
        result = run_process([sys.executable, "-c", "print('ok')"], target=self.target)
        self.assertEqual(result["decision"], "EXECUTED")
        self.assertEqual(result["evidence"]["status"], "PASS")
        self.assertEqual(result["evidence"]["authority"], "LOCAL")

    def test_nonzero_exit_emits_fail_evidence(self):
        result = run_process([sys.executable, "-c", "raise SystemExit(3)"], target=self.target)
        self.assertEqual(result["decision"], "EXECUTED")
        self.assertEqual(result["evidence"]["status"], "FAIL")

    def test_unbound_target_is_blocked(self):
        result = run_process(["true"], target=dict(self.target, binding="UNBOUND"))
        self.assertEqual(result["decision"], "BLOCKED")
        self.assertEqual(result["reason"], "EXECUTION_TARGET_NOT_BOUND")

    def test_missing_target_scope_is_blocked(self):
        target = dict(self.target)
        del target["tree"]
        result = run_process(["true"], target=target)
        self.assertEqual(result["decision"], "BLOCKED")
        self.assertIn("MISSING_EXECUTION_TARGET:tree", result["reason"])

    def test_empty_command_is_blocked(self):
        result = run_process([], target=self.target)
        self.assertEqual(result["decision"], "BLOCKED")
        self.assertEqual(result["reason"], "EMPTY_COMMAND")

    def test_invalid_output_limit_is_blocked(self):
        result = run_process(["true"], target=self.target, output_limit=0)
        self.assertEqual(result["decision"], "BLOCKED")
        self.assertEqual(result["reason"], "INVALID_OUTPUT_LIMIT")

    def test_output_is_bounded_and_recorded(self):
        result = run_process(
            [sys.executable, "-c",
             "import sys; sys.stdout.write('x' * 10000); sys.stderr.write('y' * 10000)"],
            target=self.target,
            output_limit=128,
        )
        self.assertEqual(result["decision"], "EXECUTED")
        self.assertEqual(result["evidence"]["limitations"], ["OUTPUT_TRUNCATED"])

    def test_default_output_limit_is_positive(self):
        self.assertGreater(DEFAULT_OUTPUT_LIMIT, 0)

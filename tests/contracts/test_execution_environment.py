import unittest

from contracts.execution_environment import bind_environment, validate_environment_contract


class ExecutionEnvironmentTests(unittest.TestCase):
    def setUp(self):
        self.base = {
            "schema": "reusable-process-system.execution-environment/1",
            "platform": "linux",
            "architecture": "x86_64",
            "runtime": {"name": "python", "version": "3.12"},
            "executable": {"path": "/usr/bin/python3", "identity": "sha256:example"},
            "dependency_state": "OBSERVED",
            "binding": "DECLARED",
        }

    def test_declared_environment_is_valid_but_not_bound(self):
        valid, reason = validate_environment_contract(self.base)
        self.assertTrue(valid)
        self.assertEqual(reason, "VALID")
        self.assertEqual(self.base["binding"], "DECLARED")

    def test_bound_environment_requires_observed_dependencies(self):
        environment = dict(self.base, dependency_state="DECLARED", binding="BOUND")
        valid, reason = validate_environment_contract(environment)
        self.assertFalse(valid)
        self.assertEqual(reason, "BOUND_REQUIRES_OBSERVED_DEPENDENCIES")

    def test_bind_environment_sets_bound(self):
        bound = bind_environment(self.base)
        self.assertEqual(bound["binding"], "BOUND")

    def test_unknown_dependencies_cannot_bind(self):
        environment = dict(self.base, dependency_state="UNKNOWN")
        with self.assertRaisesRegex(ValueError, "DEPENDENCIES_NOT_OBSERVED"):
            bind_environment(environment)

    def test_missing_runtime_is_rejected(self):
        environment = dict(self.base, runtime={})
        valid, reason = validate_environment_contract(environment)
        self.assertFalse(valid)
        self.assertEqual(reason, "MISSING_FIELD:runtime")

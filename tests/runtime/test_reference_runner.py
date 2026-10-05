import unittest

from runtimes.reference.process_runner import plan_next


WORKFLOW = {
    "stages": [
        {"id": "acquire", "required": True},
        {"id": "verify", "required": True},
        {"id": "release", "required": True},
    ]
}


class ReferenceRunnerTests(unittest.TestCase):
    def test_first_incomplete_stage_requires_adapter(self):
        state = {"stages": [
            {"id": "acquire", "status": "PENDING"},
            {"id": "verify", "status": "PENDING"},
            {"id": "release", "status": "PENDING"},
        ]}
        self.assertEqual(plan_next(state, WORKFLOW)["decision"], "ADAPTER_REQUIRED")
        self.assertEqual(plan_next(state, WORKFLOW)["stage"], "acquire")

    def test_blocked_stage_stops_progress(self):
        state = {"stages": [
            {"id": "acquire", "status": "BLOCKED", "blockers": ["missing snapshot"]},
            {"id": "verify", "status": "PENDING"},
            {"id": "release", "status": "PENDING"},
        ]}
        result = plan_next(state, WORKFLOW)
        self.assertEqual(result["decision"], "BLOCKED")
        self.assertEqual(result["blockers"], ["missing snapshot"])

    def test_complete_non_snapshot_requires_evidence(self):
        state = {"stages": [
            {"id": "acquire", "status": "COMPLETE", "evidence_ids": ["e1"]},
            {"id": "verify", "status": "COMPLETE", "evidence_ids": ["e2"]},
            {"id": "release", "status": "PENDING"},
        ]}
        self.assertEqual(plan_next(state, WORKFLOW)["stage"], "release")

    def test_all_complete_releases(self):
        state = {"stages": [
            {"id": "acquire", "status": "COMPLETE", "evidence_ids": ["e1"]},
            {"id": "verify", "status": "COMPLETE", "evidence_ids": ["e2"]},
            {"id": "release", "status": "COMPLETE", "evidence_ids": ["e3"]},
        ]}
        self.assertEqual(plan_next(state, WORKFLOW)["decision"], "READY_FOR_RELEASE")


if __name__ == "__main__":
    unittest.main()

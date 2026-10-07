#!/usr/bin/env python3
"""Dependency-free reference planner for governed process execution.

The reference runner plans the next lifecycle transition only. It does not
fabricate evidence, execute adapters, or assert verification.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

TERMINAL = {"COMPLETE"}
VALID = {"PENDING", "RUNNING", "COMPLETE", "BLOCKED", "FAILED"}


def validate(state: dict, workflow: dict) -> None:
    if not isinstance(state, dict) or not isinstance(workflow, dict):
        raise ValueError("INVALID_INPUT")
    stages = state.get("stages")
    required = workflow.get("stages")
    if not isinstance(stages, list) or not isinstance(required, list):
        raise ValueError("MISSING_STAGES")
    ids = [x.get("id") for x in stages if isinstance(x, dict)]
    if len(ids) != len(set(ids)):
        raise ValueError("DUPLICATE_STAGE")
    required_ids = {x.get("id") for x in required if x.get("required") is True}
    missing = sorted(required_ids - set(ids))
    if missing:
        raise ValueError("REQUIRED_STAGE_ABSENT:" + ",".join(missing))
    for stage in stages:
        status = stage.get("status")
        if status not in VALID:
            raise ValueError("INVALID_STATUS:" + str(stage.get("id")))
        if status == "COMPLETE" and stage.get("id") != "snapshot":
            if not stage.get("evidence_ids"):
                raise ValueError("COMPLETE_WITHOUT_EVIDENCE:" + str(stage.get("id")))


def plan_next(state: dict, workflow: dict) -> dict:
    validate(state, workflow)
    stages = {x["id"]: x for x in state["stages"]}
    for definition in workflow["stages"]:
        stage_id = definition["id"]
        if stage_id not in stages:
            raise ValueError("WORKFLOW_STAGE_ABSENT:" + str(stage_id))
        stage = stages[stage_id]
        if stage["status"] == "BLOCKED":
            return {
                "decision": "BLOCKED",
                "stage": stage_id,
                "blockers": stage.get("blockers", []),
                "message": "Add evidence or change the scoped input; do not override blocked state.",
            }
        if stage["status"] != "COMPLETE":
            return {
                "decision": "ADAPTER_REQUIRED",
                "stage": stage_id,
                "message": "Execute the stage adapter, attach evidence, then re-plan.",
            }
    return {
        "decision": "READY_FOR_RELEASE",
        "message": "All required lifecycle stages are complete with their required evidence.",
    }


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("usage: process-runner.py STATE.json WORKFLOW.json", file=sys.stderr)
        return 2
    state = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    workflow = json.loads(Path(argv[2]).read_text(encoding="utf-8"))
    print(json.dumps(plan_next(state, workflow), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

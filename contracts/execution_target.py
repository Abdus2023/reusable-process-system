"""Execution-target contract.

An execution target carries immutable repository identity plus explicit binding
state. A snapshot alone never authorizes execution.
"""

from __future__ import annotations

from typing import Mapping

BINDINGS = frozenset({"BOUND", "UNBOUND"})
WORKTREE_STATUSES = frozenset(
    {"CLEAN", "DIRTY", "NOT_OBSERVABLE", "MISMATCH", "BOUND"}
)


def validate_target_contract(
    target: Mapping[str, object],
) -> tuple[bool, str]:
    required = ("schema", "repository", "commit", "tree", "binding")
    missing = [key for key in required if not target.get(key)]
    if missing:
        return False, "MISSING_FIELD:" + ",".join(missing)
    if target["schema"] != "reusable-process-system.execution-target/1":
        return False, "INVALID_SCHEMA"
    if target["binding"] not in BINDINGS:
        return False, "INVALID_BINDING"
    status = target.get("worktree_status")
    if status is not None and status not in WORKTREE_STATUSES:
        return False, "INVALID_WORKTREE_STATUS"
    return True, "VALID"


def unbound_execution_target(snapshot: Mapping[str, str]) -> dict[str, str]:
    required = ("repository", "commit", "tree")
    missing = [key for key in required if not snapshot.get(key)]
    if missing:
        raise ValueError("MISSING_IMMUTABLE_SCOPE:" + ",".join(missing))
    return {
        "schema": "reusable-process-system.execution-target/1",
        "repository": snapshot["repository"],
        "ref": snapshot.get("ref", ""),
        "commit": snapshot["commit"],
        "tree": snapshot["tree"],
        "binding": "UNBOUND",
    }


def bind_execution_target(
    snapshot: Mapping[str, str],
    worktree_binding: Mapping[str, object],
) -> dict[str, str]:
    required = ("repository", "commit", "tree")
    missing = [key for key in required if not snapshot.get(key)]
    if missing:
        raise ValueError("MISSING_IMMUTABLE_SCOPE:" + ",".join(missing))
    if worktree_binding.get("status") != "BOUND":
        raise ValueError("WORKTREE_NOT_BOUND")
    return {
        "schema": "reusable-process-system.execution-target/1",
        "repository": snapshot["repository"],
        "ref": snapshot.get("ref", ""),
        "commit": snapshot["commit"],
        "tree": snapshot["tree"],
        "binding": "BOUND",
        "worktree_status": "BOUND",
    }

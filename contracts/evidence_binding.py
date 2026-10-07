"""Pure evidence-binding contracts for repository-scoped verification.

This module does not execute adapters and does not infer missing provenance.
It only evaluates whether already-produced evidence is sufficient for a target.
"""

from __future__ import annotations
from typing import Any, Mapping

REQUIRED_SCOPE = ("repository", "commit", "tree")
AUTHORITIES = frozenset({"CI", "LOCAL", "EXTERNAL", "UNKNOWN"})
KINDS = frozenset({"EXECUTION", "INSPECTION", "OBSERVATION", "ARTIFACT", "UNKNOWN"})
STATUSES = frozenset({"PASS", "FAIL", "BLOCKED", "NOT_OBSERVABLE", "UNKNOWN"})


def validate_execution_evidence(evidence: Mapping[str, Any]) -> tuple[bool, str]:
    required = ("schema", "evidence_id", "authority", "kind", "status", "scope")
    missing = [key for key in required if key not in evidence]
    if missing:
        return False, "MISSING_FIELD:" + ",".join(missing)

    scope = evidence["scope"]
    if not isinstance(scope, Mapping):
        return False, "INVALID_SCOPE"

    missing_scope = [key for key in REQUIRED_SCOPE if not scope.get(key)]
    if missing_scope:
        return False, "MISSING_IMMUTABLE_SCOPE:" + ",".join(missing_scope)

    if evidence["authority"] not in AUTHORITIES:
        return False, "INVALID_AUTHORITY"
    if evidence["kind"] not in KINDS:
        return False, "INVALID_KIND"
    if evidence["status"] not in STATUSES:
        return False, "INVALID_STATUS"
    return True, "VALID"


def can_verify(
    evidence: Mapping[str, Any],
    target: Mapping[str, Any],
    *,
    required_authority: str = "CI",
    required_kind: str = "EXECUTION",
) -> tuple[bool, str]:
    valid, reason = validate_execution_evidence(evidence)
    if not valid:
        return False, reason

    target_missing = [key for key in REQUIRED_SCOPE if not target.get(key)]
    if target_missing:
        return False, "TARGET_MISSING_IMMUTABLE_SCOPE:" + ",".join(target_missing)

    if evidence["status"] != "PASS":
        return False, "STATUS_NOT_PASS:" + evidence["status"]
    if evidence["authority"] != required_authority:
        return False, "AUTHORITY_MISMATCH"
    if evidence["kind"] != required_kind:
        return False, "KIND_MISMATCH"

    scope = evidence["scope"]
    for key in REQUIRED_SCOPE:
        if scope.get(key) != target.get(key):
            return False, "SCOPE_MISMATCH:" + key
    return True, "VERIFIED"

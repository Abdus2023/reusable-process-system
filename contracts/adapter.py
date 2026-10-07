"""Authority-neutral adapter contract.

The contract separates adapter execution from evidence acceptance. Adapters may
produce evidence, but verification decides whether that evidence is sufficient.
"""

from __future__ import annotations

from typing import Any, Mapping, Protocol


ADAPTER_DECISIONS = frozenset({"EXECUTED", "BLOCKED", "NOT_OBSERVABLE", "FAILED"})


class AdapterRequest(Protocol):
    command: list[str]
    snapshot: Mapping[str, str]


class Adapter(Protocol):
    """Minimal adapter interface shared by local/CI/external implementations."""

    authority: str

    def run(self, request: Mapping[str, Any]) -> dict[str, Any]:
        """Execute or explicitly decline, returning an adapter-result record."""
        ...


def validate_adapter_result(result: Mapping[str, Any]) -> tuple[bool, str]:
    required = ("schema", "decision")
    missing = [key for key in required if key not in result]
    if missing:
        return False, "MISSING_FIELD:" + ",".join(missing)

    if result["schema"] != "reusable-process-system.adapter-result/1":
        return False, "INVALID_SCHEMA"
    if result["decision"] not in ADAPTER_DECISIONS:
        return False, "INVALID_DECISION"

    if result["decision"] == "EXECUTED":
        evidence = result.get("evidence")
        if not isinstance(evidence, Mapping):
            return False, "EXECUTED_REQUIRES_EVIDENCE"
        if result.get("evidence_ids") != [evidence.get("evidence_id")]:
            return False, "EVIDENCE_ID_MISMATCH"

    return True, "VALID"

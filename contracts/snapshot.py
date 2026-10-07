"""Repository snapshot contracts.

A snapshot is immutable repository identity plus contextual reference data.
Resolution is deliberately separate from evidence binding.
"""

from __future__ import annotations

from typing import Any, Mapping

REQUIRED_SNAPSHOT = ("repository", "ref", "commit", "tree")


def validate_snapshot(snapshot: Mapping[str, Any]) -> tuple[bool, str]:
    missing = [key for key in REQUIRED_SNAPSHOT if not snapshot.get(key)]
    if missing:
        return False, "MISSING_SNAPSHOT_FIELD:" + ",".join(missing)
    return True, "VALID"

"""Reference local-process adapter.

The adapter is intentionally small: it executes an explicitly supplied command,
captures bounded output, and emits an evidence record bound to the supplied
repository snapshot. It never changes the verification decision itself.
"""

from __future__ import annotations

import hashlib
import subprocess
from typing import Any, Mapping


def run_process(
    command: list[str],
    *,
    snapshot: Mapping[str, str],
    timeout_seconds: float = 30.0,
) -> dict[str, Any]:
    required = ("repository", "commit", "tree")
    missing = [key for key in required if not snapshot.get(key)]
    if missing:
        return {
            "schema": "reusable-process-system.adapter-result/1",
            "decision": "BLOCKED",
            "reason": "MISSING_IMMUTABLE_SCOPE:" + ",".join(missing),
        }

    if not command:
        return {
            "schema": "reusable-process-system.adapter-result/1",
            "decision": "BLOCKED",
            "reason": "EMPTY_COMMAND",
        }

    try:
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired:
        return {
            "schema": "reusable-process-system.adapter-result/1",
            "decision": "FAILED",
            "reason": "TIMEOUT",
        }
    except OSError as exc:
        return {
            "schema": "reusable-process-system.adapter-result/1",
            "decision": "FAILED",
            "reason": "EXECUTION_ERROR:" + type(exc).__name__,
        }

    status = "PASS" if completed.returncode == 0 else "FAIL"
    output = (completed.stdout + completed.stderr).encode("utf-8")
    digest = "sha256:" + hashlib.sha256(output).hexdigest()

    evidence = {
        "schema": "reusable-process-system.execution-evidence/1",
        "evidence_id": digest,
        "authority": "LOCAL",
        "kind": "EXECUTION",
        "status": status,
        "scope": {
            "repository": snapshot["repository"],
            "commit": snapshot["commit"],
            "tree": snapshot["tree"],
        },
        "output_digest": digest,
    }

    return {
        "schema": "reusable-process-system.adapter-result/1",
        "decision": "EXECUTED",
        "evidence_ids": [digest],
        "evidence": evidence,
    }

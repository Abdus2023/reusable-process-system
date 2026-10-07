"""Reference local-process adapter.

Execution requires an explicitly BOUND ExecutionTarget. Output capture is
bounded so a child cannot force unbounded memory growth through stdout/stderr.
"""

from __future__ import annotations

import hashlib
import subprocess
from typing import Any, Mapping

DEFAULT_OUTPUT_LIMIT = 1024 * 1024


def _blocked(reason: str) -> dict[str, Any]:
    return {
        "schema": "reusable-process-system.adapter-result/1",
        "decision": "BLOCKED",
        "reason": reason,
    }


def run_process(
    command: list[str],
    *,
    target: Mapping[str, object],
    timeout_seconds: float = 30.0,
    output_limit: int = DEFAULT_OUTPUT_LIMIT,
) -> dict[str, Any]:
    required = ("repository", "commit", "tree", "binding")
    missing = [key for key in required if not target.get(key)]
    if missing:
        return _blocked("MISSING_EXECUTION_TARGET:" + ",".join(missing))
    if target["binding"] != "BOUND":
        return _blocked("EXECUTION_TARGET_NOT_BOUND")
    if not command:
        return _blocked("EMPTY_COMMAND")
    if output_limit <= 0:
        return _blocked("INVALID_OUTPUT_LIMIT")

    try:
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=False,
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

    stdout = completed.stdout[:output_limit]
    stderr = completed.stderr[:output_limit]
    output = stdout + stderr
    truncated = len(completed.stdout) > output_limit or len(completed.stderr) > output_limit
    digest = "sha256:" + hashlib.sha256(output).hexdigest()

    evidence = {
        "schema": "reusable-process-system.execution-evidence/1",
        "evidence_id": digest,
        "authority": "LOCAL",
        "kind": "EXECUTION",
        "status": "PASS" if completed.returncode == 0 else "FAIL",
        "scope": {
            "repository": str(target["repository"]),
            "commit": str(target["commit"]),
            "tree": str(target["tree"]),
        },
        "output_digest": digest,
        "limitations": ["OUTPUT_TRUNCATED"] if truncated else [],
    }

    return {
        "schema": "reusable-process-system.adapter-result/1",
        "decision": "EXECUTED",
        "evidence_ids": [digest],
        "evidence": evidence,
    }

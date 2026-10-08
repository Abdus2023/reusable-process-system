"""Reference local-process adapter.

Execution requires an explicitly BOUND ExecutionTarget. Output capture uses
streaming reader threads and fixed-size buffers so captured evidence does not
require retaining the child's complete stdout/stderr in memory.
"""

from __future__ import annotations

import hashlib
import subprocess
import threading
from typing import Any, Mapping

DEFAULT_OUTPUT_LIMIT = 1024 * 1024
_READ_CHUNK_SIZE = 64 * 1024


def _blocked(reason: str) -> dict[str, Any]:
    return {
        "schema": "reusable-process-system.adapter-result/1",
        "decision": "BLOCKED",
        "reason": reason,
    }


def _capture_stream(stream: Any, limit: int, sink: bytearray) -> None:
    """Drain a child pipe while retaining at most *limit* bytes."""
    while True:
        chunk = stream.read(_READ_CHUNK_SIZE)
        if not chunk:
            return
        remaining = limit - len(sink)
        if remaining > 0:
            sink.extend(chunk[:remaining])


def _run_bounded(
    command: list[str],
    *,
    timeout_seconds: float,
    output_limit: int,
) -> tuple[int, bytes, bytes, bool]:
    """Run a child while draining stdout/stderr into bounded buffers."""
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.DEVNULL,
    )
    stdout = bytearray()
    stderr = bytearray()
    threads = [
        threading.Thread(
            target=_capture_stream,
            args=(process.stdout, output_limit, stdout),
            daemon=True,
        ),
        threading.Thread(
            target=_capture_stream,
            args=(process.stderr, output_limit, stderr),
            daemon=True,
        ),
    ]
    for thread in threads:
        thread.start()

    timed_out = False
    try:
        process.wait(timeout=timeout_seconds)
    except subprocess.TimeoutExpired:
        timed_out = True
        process.kill()
        process.wait()

    for thread in threads:
        thread.join(timeout=2.0)

    for stream in (process.stdout, process.stderr):
        if stream is not None:
            stream.close()

    return process.returncode, bytes(stdout), bytes(stderr), timed_out


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
    if timeout_seconds <= 0:
        return _blocked("INVALID_TIMEOUT")
    if output_limit <= 0:
        return _blocked("INVALID_OUTPUT_LIMIT")

    try:
        returncode, stdout, stderr, timed_out = _run_bounded(
            command,
            timeout_seconds=timeout_seconds,
            output_limit=output_limit,
        )
    except OSError as exc:
        return {
            "schema": "reusable-process-system.adapter-result/1",
            "decision": "FAILED",
            "reason": "EXECUTION_ERROR:" + type(exc).__name__,
        }

    if timed_out:
        return {
            "schema": "reusable-process-system.adapter-result/1",
            "decision": "FAILED",
            "reason": "TIMEOUT",
        }

    output = stdout + stderr
    truncated = len(stdout) >= output_limit or len(stderr) >= output_limit
    digest = "sha256:" + hashlib.sha256(output).hexdigest()

    evidence = {
        "schema": "reusable-process-system.execution-evidence/1",
        "evidence_id": digest,
        "authority": "LOCAL",
        "kind": "EXECUTION",
        "status": "PASS" if returncode == 0 else "FAIL",
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

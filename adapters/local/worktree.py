"""Local worktree binding checks.

Snapshot identity (commit/tree) is distinct from the content actually visible
to a local process. This module rejects tracked and untracked worktree changes
when a caller requires execution against the committed tree.
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any


def _status(cwd: Path) -> str:
    completed = subprocess.run(
        ["git", "status", "--porcelain=v1", "--untracked-files=all"],
        cwd=cwd,
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise RuntimeError("GIT_STATUS_FAILED")
    return completed.stdout


def resolve_worktree_binding(repository_path: str | Path) -> dict[str, Any]:
    cwd = Path(repository_path)
    if not cwd.is_dir():
        return {
            "schema": "reusable-process-system.worktree-binding/1",
            "status": "NOT_OBSERVABLE",
            "clean": False,
            "reason": "REPOSITORY_PATH_NOT_FOUND",
        }

    try:
        porcelain = _status(cwd)
    except (OSError, RuntimeError):
        return {
            "schema": "reusable-process-system.worktree-binding/1",
            "status": "NOT_OBSERVABLE",
            "clean": False,
            "reason": "WORKTREE_STATUS_NOT_OBSERVABLE",
        }

    if porcelain:
        return {
            "schema": "reusable-process-system.worktree-binding/1",
            "status": "DIRTY",
            "clean": False,
            "reason": "WORKTREE_CONTENT_DIFFERS_FROM_COMMITTED_TREE",
        }

    return {
        "schema": "reusable-process-system.worktree-binding/1",
        "status": "CLEAN",
        "clean": True,
        "reason": "WORKTREE_MATCHES_COMMITTED_TRACKED_AND_UNTRACKED_STATE",
    }

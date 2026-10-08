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


def validate_execution_target(
    repository_path: str | Path,
    *,
    snapshot: dict[str, str],
) -> dict[str, Any]:
    """Bind a clean local worktree to the requested immutable commit."""
    cwd = Path(repository_path)
    required = ("repository", "commit", "tree")
    missing = [key for key in required if not snapshot.get(key)]
    if missing:
        return {
            "schema": "reusable-process-system.worktree-binding/1",
            "status": "NOT_OBSERVABLE",
            "clean": False,
            "reason": "MISSING_SNAPSHOT_FIELD:" + ",".join(missing),
        }

    binding = resolve_worktree_binding(cwd)
    if binding["status"] != "CLEAN":
        return binding

    try:
        completed = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=cwd,
            check=False,
            capture_output=True,
            text=True,
        )
        if completed.returncode != 0:
            raise RuntimeError("GIT_HEAD_NOT_OBSERVABLE")
        head = completed.stdout.strip()
        tree_completed = subprocess.run(
            ["git", "rev-parse", "HEAD^{tree}"],
            cwd=cwd,
            check=False,
            capture_output=True,
            text=True,
        )
        if tree_completed.returncode != 0:
            raise RuntimeError("GIT_TREE_NOT_OBSERVABLE")
        tree = tree_completed.stdout.strip()
    except (OSError, RuntimeError):
        return {
            "schema": "reusable-process-system.worktree-binding/1",
            "status": "NOT_OBSERVABLE",
            "clean": False,
            "reason": "HEAD_NOT_OBSERVABLE",
        }

    if head != snapshot["commit"]:
        return {
            "schema": "reusable-process-system.worktree-binding/1",
            "status": "MISMATCH",
            "clean": True,
            "reason": "HEAD_COMMIT_MISMATCH",
        }

    if tree != snapshot["tree"]:
        return {
            "schema": "reusable-process-system.worktree-binding/1",
            "status": "MISMATCH",
            "clean": True,
            "reason": "HEAD_TREE_MISMATCH",
        }

    return {
        "schema": "reusable-process-system.worktree-binding/1",
        "status": "BOUND",
        "clean": True,
        "reason": "CLEAN_WORKTREE_AT_REQUESTED_COMMIT",
    }


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

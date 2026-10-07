"""Local repository snapshot resolver.

This resolver observes the repository through Git rather than trusting a
caller-supplied commit/tree. It is LOCAL evidence only; it is not a CI
authority and does not establish that remote CI executed the same snapshot.
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any


def _git(cwd: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=cwd,
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise RuntimeError("GIT_COMMAND_FAILED:" + " ".join(args))
    return completed.stdout.strip()


def resolve_snapshot(
    repository_path: str | Path,
    *,
    repository: str,
    ref: str | None = None,
) -> dict[str, Any]:
    cwd = Path(repository_path)
    if not cwd.is_dir():
        return {
            "schema": "reusable-process-system.repository-snapshot/1",
            "repository": repository,
            "ref": ref or "",
            "commit": "",
            "tree": "",
            "source": "LOCAL_GIT",
            "limitations": ["REPOSITORY_PATH_NOT_FOUND"],
        }

    try:
        commit = _git(cwd, "rev-parse", "HEAD")
        tree = _git(cwd, "rev-parse", "HEAD^{tree}")
        resolved_ref = ref or _git(cwd, "symbolic-ref", "--short", "-q", "HEAD")
    except (OSError, RuntimeError):
        return {
            "schema": "reusable-process-system.repository-snapshot/1",
            "repository": repository,
            "ref": ref or "",
            "commit": "",
            "tree": "",
            "source": "LOCAL_GIT",
            "limitations": ["SNAPSHOT_NOT_OBSERVABLE"],
        }

    return {
        "schema": "reusable-process-system.repository-snapshot/1",
        "repository": repository,
        "ref": resolved_ref,
        "commit": commit,
        "tree": tree,
        "source": "LOCAL_GIT",
        "limitations": [
            "LOCAL_OBSERVATION_IS_NOT_CI_AUTHORITY",
            "WORKTREE_CONTENT_MAY_DIFFER_FROM_COMMITTED_TREE",
        ],
    }

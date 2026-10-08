"""Execution-environment contract.

Environment identity is separate from source identity. A BOUND execution
environment requires observable executable/runtime identity and an explicit
dependency-state observation; declarations alone never become VERIFIED.
"""

from __future__ import annotations

from typing import Mapping

DEPENDENCY_STATES = frozenset({"DECLARED", "OBSERVED", "UNKNOWN", "NOT_OBSERVABLE"})
BINDINGS = frozenset({"DECLARED", "BOUND", "UNBOUND", "NOT_OBSERVABLE"})


def validate_environment_contract(
    environment: Mapping[str, object],
) -> tuple[bool, str]:
    required = ("schema", "platform", "architecture", "runtime", "executable", "dependency_state", "binding")
    missing = [key for key in required if not environment.get(key)]
    if missing:
        return False, "MISSING_FIELD:" + ",".join(missing)
    if environment["schema"] != "reusable-process-system.execution-environment/1":
        return False, "INVALID_SCHEMA"
    if environment["dependency_state"] not in DEPENDENCY_STATES:
        return False, "INVALID_DEPENDENCY_STATE"
    if environment["binding"] not in BINDINGS:
        return False, "INVALID_BINDING"
    runtime = environment["runtime"]
    executable = environment["executable"]
    if not isinstance(runtime, Mapping) or not runtime.get("name") or not runtime.get("version"):
        return False, "INVALID_RUNTIME"
    if not isinstance(executable, Mapping) or not executable.get("path") or not executable.get("identity"):
        return False, "INVALID_EXECUTABLE"
    if environment["binding"] == "BOUND" and environment["dependency_state"] != "OBSERVED":
        return False, "BOUND_REQUIRES_OBSERVED_DEPENDENCIES"
    return True, "VALID"


def bind_environment(
    environment: Mapping[str, object],
) -> dict[str, object]:
    valid, reason = validate_environment_contract(environment)
    if not valid:
        raise ValueError(reason)
    if environment["dependency_state"] != "OBSERVED":
        raise ValueError("DEPENDENCIES_NOT_OBSERVED")
    bound = dict(environment)
    bound["binding"] = "BOUND"
    return bound

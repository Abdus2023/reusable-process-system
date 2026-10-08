# Evidence Contract

## Purpose

The reusable process system distinguishes lifecycle planning from external execution and verification.

## Contract

A verification decision may consume execution evidence, but a planner never creates evidence.

An adapter may return one of:

- EXECUTED: external work was performed and evidence identifiers are available.
- BLOCKED: execution could not proceed under the applicable policy or prerequisites.
- NOT_OBSERVABLE: execution may have occurred, but the system has no sufficient observation channel.
- FAILED: execution was attempted and failed.

NOT_OBSERVABLE is not equivalent to PASS.

## Authority

Evidence records identify their authority:

- CI: execution authority capable of establishing CI execution for its own run.
- LOCAL: local inspection/execution; useful diagnostic evidence but not interchangeable with CI authority.
- EXTERNAL: evidence supplied by another explicitly identified authority.
- UNKNOWN: provenance is insufficient.

## Snapshot binding

Repository-scoped execution evidence should bind, where applicable, to:

- repository
- ref
- commit
- tree

A branch/ref alone is insufficient for an immutable verification claim because it can move.

## Non-upgrade rule

The system must not transform:

- missing evidence -> PASS
- NOT_OBSERVABLE -> VERIFIED
- LOCAL inspection -> CI execution

Verification can only derive a stronger decision when the required evidence and authority are present.

## Boundary

Core contracts define the evidence vocabulary and invariants. GitHub, local-shell, CI, GPJK, and Kerno-specific implementations belong outside the core contract layer.
---
name: process-contract-and-composition
description: Define reusable process, skill, tool, adapter, profile, and runtime contracts with explicit composition and authority boundaries.
---

# Process Contract and Composition

## Purpose
Turn process models into composable contracts for skills, tools, workflows, adapters, profiles and runtimes while preventing hidden coupling and semantic authority leakage.

## Activation
Use when defining skill/tool contracts, composing workflows, designing adapters, or deciding whether a capability belongs in core, an integration, profile, adapter or runtime.

Do not treat GPJK as the identity or universal process language of this system.

## Inputs
- Approved process model and version.
- Actor and authority model.
- Tool/skill interfaces, inputs, outputs, errors and side effects.
- Integration/profile/runtime dependencies.
- Security and resource constraints.
- Existing core contracts and schemas.

## Procedure
1. CONTRACT each skill/tool with identity, purpose, triggers, inputs, preconditions, outputs, errors, side effects, permissions and acceptance criteria.
2. Define orchestration handoffs and data contracts between process steps; do not rely on hidden conversational state.
3. Separate generic core contracts from language-specific integration semantics.
4. Place GPJK-specific references, expression rules, value/null/missing semantics, state vocabulary, temporal semantics and conformance fixtures under `integrations/gpjk/`.
5. Place reusable domain methods under `profiles/`; profiles may specialize but MUST NOT silently redefine core semantics.
6. Place external repository, GitHub, worker and authority boundaries behind explicit adapters.
7. Treat runtime orchestration separately from adapters. Rewrite source runners against target state/path contracts; do not copy Kerno path conventions blindly.
8. Define authority and trust for each adapter. An adapter's presence does not grant permission to perform external effects.
9. Specify deterministic input/output and error behavior, idempotency, timeout, retry, resource bounds and cancellation where relevant.
10. Build composition maps and verify every referenced contract/path exists.
11. Reject duplicate or ambiguous ownership. Each semantic rule must have one authoritative owner and explicit dependents.

## Outputs
- Versioned skill/tool/process contracts.
- Composition graph and handoff schemas.
- Core/integration/profile/adapter/runtime boundary matrix.
- Dependency and ownership register.
- Contract validation criteria.

## Failure handling
Stop when core imports GPJK-only semantics, a profile silently changes core meaning, an adapter gains undeclared authority, or a runtime assumes Kerno filesystem state. Keep unresolved ownership as OPEN.

## Acceptance criteria
- Every component has explicit inputs/outputs and authority.
- Core is representation-independent where practical.
- GPJK is isolated behind its integration boundary.
- Profiles and adapters do not redefine core semantics.
- Runtime orchestration is not conflated with external adapters.
- Contracts are versioned and cross-referenced.
- Composition edges resolve to real artifacts.

## Source references
- `AGENTS.md`
- `docs/migration/EXTRACTION-MAPPING.md`
- `docs/migration/DEPENDENCY-AUDIT.md`
- `docs/migration/SEMANTIC-BOUNDARY-REVIEW.md`

## Validation status
The dependency and semantic boundary audits are PARTIALLY_VERIFIED; unresolved implementation dependencies remain.

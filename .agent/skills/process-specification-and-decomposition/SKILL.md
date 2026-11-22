---
name: process-specification-and-decomposition
description: Model and specify reusable processes as explicit, representation-independent structures before implementation.
---

# Process Specification and Decomposition

## Purpose
Transform extracted process knowledge into an explicit process model with stable identity, scope, inputs, outputs, steps, dependencies, constraints, gates and artifacts.

## Activation
Use when modeling a process, formalizing a workflow, decomposing a large process into reusable units, or reviewing whether a process model is implementation-neutral.

Do not use this skill to impose GPJK syntax or semantics on the generic process-system core.

## Inputs
- Classified extraction records and source provenance.
- Process identity/version and intended consumers.
- Goals, scope, actors, inputs/outputs and constraints.
- Candidate steps, dependencies, gates and artifacts.
- Relevant profiles and language integrations.

## Procedure
1. MODEL the process purpose, identity, version, scope and non-scope.
2. Identify actors, roles, authority, preconditions, inputs, outputs and persistent artifacts.
3. Decompose the process into bounded steps, operations, judgments, deterministic computations and human approvals.
4. Define dependencies and ordering explicitly; distinguish required order from optional branches and parallel work.
5. Define state transitions, guards, terminal conditions, retry/recovery behavior and stop conditions.
6. Specify constraints, invariants, acceptance criteria and required evidence for each step.
7. Keep generic process semantics representation-independent where practical.
8. Move process-language-specific references, expressions, value semantics, state vocabularies and temporal rules behind explicit integration interfaces.
9. Record assumptions and unresolved semantics rather than inventing defaults.
10. Validate that the decomposition preserves the parent process objective and that every child unit has a defined input/output contract.

## Outputs
- Process model and specification.
- Decomposition tree or dependency graph.
- State/transition model.
- Constraints, gates and evidence requirements.
- Integration/profile dependencies and unresolved decisions.

## Failure handling
Stop when the process cannot be bounded, a step has no observable output or acceptance criterion, dependencies create unresolved cycles, or a generic core definition depends on GPJK-specific semantics.

## Acceptance criteria
- Process identity, scope and version are explicit.
- Steps are bounded and composable.
- Inputs, outputs, dependencies and gates are specified.
- State transitions and stop conditions are defined.
- Core semantics do not depend on a specific process language.
- Open decisions and assumptions are visible.

## Source references
- `specification/process-system.md`
- `docs/migration/SEMANTIC-BOUNDARY-REVIEW.md`
- `docs/migration/EXTRACTION-MAPPING.md`

## Validation status
The target specification is foundation-only; this skill describes the intended method, not a completed implementation.

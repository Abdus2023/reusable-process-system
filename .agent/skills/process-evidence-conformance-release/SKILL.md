---
name: process-evidence-conformance-release
description: Govern process testing, execution evidence, verification, conformance, packaging, and release gates without overstating claims.
---

# Process Evidence, Conformance and Release

## Purpose
Ensure that process artifacts move from contract to test, verification, conformance and release through explicit evidence rather than inferred status.

## Activation
Use when designing process tests, capturing execution evidence, evaluating conformance, packaging reusable process artifacts, or preparing a release gate.

Do not claim that a schema-valid artifact is semantically conformant, executed, or verified.

## Inputs
- Frozen process/contract revision and implementation identity.
- Registered test cases, fixtures and expected outcomes.
- Execution environment and toolchain identity.
- Evidence records, provenance and integrity data.
- Conformance scope, unsupported-case policy and release criteria.

## Procedure
1. TEST each contract with positive, negative, boundary and failure-path fixtures.
2. Bind execution records to exact source commit/tree, artifact, environment, command, inputs, outputs and test identity.
3. Distinguish OBSERVED, DERIVED, EXECUTED and VERIFIED evidence. Record the authority and method for each.
4. Require CI as execution authority where the project defines CI as authoritative; treat local inspection as diagnostic evidence only.
5. Verify that evidence scope matches the claim. Existence of an evidence record is not enough; inspect provenance, integrity, identity, freshness and independent authority.
6. Conformance runs must execute every registered applicable case. Skipped/unsupported cases remain explicit and cannot be counted as PASS.
7. Keep generic conformance framework separate from GPJK-specific fixtures and reference semantics.
8. PACKAGE only artifacts whose contracts, dependencies, provenance and validation status are known.
9. Run release gates against exact frozen inputs and required evidence.
10. TAG only after release gate approval and record the exact revision.
11. Preserve failures, partial results and open issues. Do not silently retry into a green status or aggregate away unsupported cases.

## Outputs
- Test and execution evidence.
- Conformance result with exact scope and unsupported cases.
- Provenance/integrity record.
- Release-gate assessment.
- Package manifest and immutable release tag.

## Failure handling
Block verification when execution identity is missing, evidence scope differs from claim scope, a digest contract is weak or unspecified, conformance cases are skipped, or CI authority evidence is unavailable. Do not label the system standalone-conformant before bootstrap and runtime tests pass.

## Acceptance criteria
- Test inputs and implementation identity are pinned.
- CI and local diagnostics are distinguished.
- Evidence is scoped, attributable and integrity-checked.
- Schema validity, semantic conformance, execution and verification are separate.
- All applicable conformance cases execute or remain explicit blockers.
- Generic and GPJK conformance are separated.
- Release gate and tag bind to the exact artifact revision.

## Source references
- `README.md`
- `AGENTS.md`
- `docs/migration/DEPENDENCY-AUDIT.md`
- `docs/migration/RUNTIME-CONFORMANCE-AUDIT.md`
- `specification/process-system.md`

## Validation status
The repository declares PROVISIONAL foundation status. No standalone conformance or release pass is claimed.

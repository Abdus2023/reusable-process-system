# M9 Contract CI Evidence

Status: VERIFIED (scoped execution gate)

## Snapshot

- Repository: `Abdus2023/reusable-process-system`
- Ref: `extract/core-foundation`
- Commit: `0eeef8a453964188c0858210bebeb51824da78ba`
- Tree: `c477c01cac0fefa1eb527ad9c17e2e301c7426a2`
- Workflow: `conformance`
- Run: `37734316347`
- Run number: `102`
- Conclusion: `success`

## Jobs

| Job | Result |
|---|---|
| `contract-invariants` | SUCCESS |
| `reference-runtime` | SUCCESS |
| `adapter-contracts` | SUCCESS |
| `gpjk-fixture-shape` | SUCCESS |
| `gpjk-reference-conformance` | SUCCESS |

## Artifact

- Name: `gpjk-reference-conformance-report`
- Artifact ID: `11531360215`
- SHA-256: `03c71bee8df25b39be207455e18a4ec8a3250788ff2db868cc84d6a35c6efbf5`

## Verified Contract Change

The verification-result schema now requires at least one evidence identifier when the decision is `VERIFIED`. The corresponding contract invariant is exercised by the CI `contract-invariants` job.

## Scope

This proves execution of the registered CI jobs for the exact recorded commit and confirms the new verified-result evidence invariant in CI.

It does not prove complete semantic conformance, complete extraction closure, or release readiness.

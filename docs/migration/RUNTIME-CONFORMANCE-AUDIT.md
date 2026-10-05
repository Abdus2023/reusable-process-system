# Runtime and Conformance Dependency Audit

**Source snapshot:** `Abdus2023/Kerno@d1bf55e09de6a88e4a79e01084e1f0ac0cae9c99`  
**Status:** PARTIALLY_VERIFIED

## Runtime findings

| Artifact | Finding | Classification | Target decision |
|---|---|---|---|
| `bin/agent-runner.ts` | Orchestrator with explicit state/evidence discipline, but hard-coded `.agent/state/continuation.json` and `.agent/tools/workflow.json` | RUNTIME / CORE candidate | Rewrite against target paths/contracts |
| `bin/acquire-and-audit.ts` | Couples GitHub acquisition with evidence-bundle construction | COMPOSITE ADAPTER | Split acquisition from audit/bundle composition |
| `bin/adapters/audit-pipeline.ts` | Composes inventory and audit adapters | ADAPTER | Move to repository adapter composition |
| `bin/adapters/evidence-bundle.ts` | Builds snapshot/inventory/audit bundle | ADAPTER | Move to evidence subsystem adapter |
| `bin/adapters/execution-evidence.ts` | Exact commit/tree binding for execution records | CORE CONTRACT + ADAPTER | Preserve contract; rewrite implementation as needed |
| `bin/adapters/execution-verification.ts` | Matches execution claims against exact snapshot/kind | CORE CONTRACT + ADAPTER | Preserve semantics; add complete evidence validation |
| `bin/adapters/github-acquisition.ts` | Pins GitHub ref to exact commit/tree before acquisition | GITHUB ADAPTER | Move under `adapters/github` |

## Runtime boundary

The source runner is not itself an authority for external execution. Its declared role is orchestration:

```
runner
  |
  +--> adapter --> evidence
  |
  +--> state
  |
  +--> gate
```

This distinction should remain in the standalone implementation.

### Runtime hazard

The source `agent-runner.ts` contains a malformed/unreachable-looking control-flow region around its `pending` handling. Static inspection is sufficient to flag this for rewrite, but not sufficient to claim runtime failure without executing it.

**Classification:** OBSERVED source anomaly; runtime behavior OPEN.

## Conformance findings

The conformance directory is explicitly GPJK-oriented. It contains:

- implementation-neutral GPJK fixtures
- a small deterministic reference harness
- extended semantic adapters
- differential conformance specification

Therefore it must be split:

```
conformance/
├── framework/                  # reusable runner/result machinery
└── integrations/gpjk/
    └── conformance/            # GPJK fixture suites + reference semantics
```

The GPJK fixtures are not proof of implementation conformance. They become execution evidence only when actually run against an identified implementation with recorded execution identity.

## Conformance boundary

A full-suite PASS requires every registered case to execute and match its expected result. Skipped/unsupported cases cannot be treated as PASS.

Differential conformance establishes agreement only within the executed fixture scope. It does not establish correctness outside that scope.

## Decision

**Runtime:** extract concepts and contracts; do not mechanically copy the runner.

**Conformance:** extract generic conformance framework separately from GPJK-specific semantic fixtures.

**Gate:** M3 dependency audit is now **PARTIALLY_VERIFIED** with remaining work limited to file-level implementation/schema dependency mapping.

## Next gate

M4 — semantic boundary review.

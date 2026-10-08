# M8 Runtime Reference Audit

**Status:** PARTIALLY_VERIFIED

## Scope

This audit evaluates the Kerno runtime candidates identified during extraction against the standalone Reusable Process Engineering System boundary.

Source:
- repository: `Abdus2023/Kerno`
- ref: `agent/reusable-verification-skills`
- source path: `.agent/bin` and `.agent/adapters`

Target:
- repository: `Abdus2023/reusable-process-system`
- branch: `extract/core-foundation`

## Findings

### 1. `agent-runner.ts` is not extraction-safe

The source runner is coupled to the historical `agent.*` continuation schema and `.agent/tools/workflow.json`. It also contains malformed-looking control flow in the terminal branch: an `if (pending === "snapshot")` block occurs inside `if (!pending)`, where `pending` is necessarily absent.

**Decision:** do not copy verbatim.

A standalone runner must:
1. consume the standalone continuation/process contracts;
2. resolve its workflow from the generic process-system lifecycle;
3. keep execution adapters external;
4. never fabricate evidence;
5. emit explicit BLOCKED/ADAPTER_REQUIRED decisions.

### 2. `acquire-and-audit.ts` is composition logic, not core runtime

The orchestration concept is reusable, but its concrete imports and GitHub acquisition dependency make it an adapter composition boundary.

**Target:** split generic orchestration from `adapters/github` and `adapters/repository`.

### 3. `audit-pipeline.ts` has a stale relative-import boundary

The source file is under `.agent/bin/adapters/` but imports:

`./adapters/repository-inventory.ts`
`./adapters/repo-audit.ts`

Those paths resolve as a nested `adapters/adapters/` location from that file's directory.

**Decision:** treat the source as design evidence, not executable standalone code. Reconstruct imports when implementing the target adapter.

### 4. `evidence-bundle.ts` has the same stale relative-import pattern

It repeats the nested `./adapters/...` imports and embeds historical schema identifiers such as `agent.repository-snapshot/1` and `agent.evidence-bundle/1`.

**Decision:** reconstruct against `schemas/evidence/*` and the standalone evidence contracts. Do not preserve the `agent.*` namespace.

### 5. Execution evidence concepts are reusable

The source `execution-evidence.ts` establishes useful generic fields:
- execution identity;
- execution authority;
- execution kind;
- repository/ref/commit/tree binding;
- status;
- timestamps;
- output digest;
- limitations.

Its historical `agent.execution-evidence/1` namespace must be replaced by the standalone schema namespace.

### 6. Execution verification is reusable but must remain scoped

The source verifier correctly refuses a claim when no matching execution evidence exists and binds evidence to repository, commit, tree, and execution kind.

This is suitable as a core verification contract after namespace normalization. It does **not** establish CI authority by itself; the evidence must come from an observable execution authority.

### 7. GitHub acquisition belongs in an adapter

The pinned-snapshot algorithm is reusable:
1. resolve the requested ref;
2. require exact commit/tree equality;
3. enumerate the tree;
4. fetch blobs at the pinned commit;
5. produce a deterministic file set.

This belongs under `adapters/github`, not core.

### 8. Local audit is not execution authority

The source repository audit uses the local filesystem and local Git state. That is useful diagnostic evidence, but it cannot prove that GitHub Actions executed the target workflow.

The standalone system therefore retains the distinction:

`local inspection != CI execution authority`

### 9. Evidence-record digest is insufficient for cryptographic integrity

The source evidence-record adapter uses FNV-1a as a short digest. That may be useful for local correlation, but it must not be presented as cryptographic integrity.

Any standalone integrity claim requires an explicitly selected cryptographic digest and a defined normalization/canonicalization rule.

## Runtime extraction decisions

| Source candidate | Standalone disposition | Target |
|---|---|---|
| `agent-runner.ts` | Rewrite | `runtimes/reference/` |
| `acquire-and-audit.ts` | Split/recompose | core orchestration + adapters |
| `audit-pipeline.ts` | Reconstruct | `adapters/repository/` |
| `evidence-bundle.ts` | Reconstruct | `adapters/repository/` + core evidence |
| `execution-evidence.ts` | Normalize/extract | `core/evidence/` or `adapters/agent-runtime/` depending on authority boundary |
| `execution-verification.ts` | Normalize/extract | `core/verification/` |
| `github-acquisition.ts` | Extract as adapter | `adapters/github/` |
| local `repo-audit.ts` | Profile/adapter | `profiles/repository-audit/` + adapter |
| local `repository-snapshot.ts` | Extract as repository adapter | `adapters/repository/` |
| local `verification-gate.ts` | Rework | `core/verification/` |

## Required next gate

Before runtime extraction is promoted:

1. define standalone runtime interfaces and schemas;
2. implement the reference runner without Kerno/`.agent` dependencies;
3. implement repository/GitHub adapters separately;
4. add contract tests for snapshot binding and execution evidence;
5. execute the tests under CI;
6. bind results to the exact target commit and tree;
7. inspect the generated report.

## Non-claims

This audit does **not** claim:
- that the extracted runtime is executable;
- that the target branch's GitHub workflow has executed;
- that the GPJK runner is a complete normative implementation;
- that local inspection proves CI execution;
- that schema validity proves semantic conformance.

**Conclusion:** the runtime extraction boundary is sufficiently specified to proceed, but runtime implementation and execution evidence remain open.

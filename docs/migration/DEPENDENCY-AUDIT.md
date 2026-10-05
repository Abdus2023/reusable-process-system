# Dependency Audit — Kerno .agent Extraction

**Source anchor:** `d1bf55e09de6a88e4a79e01084e1f0ac0cae9c99`  
**Audit status:** PARTIALLY_VERIFIED  
**Target:** `Abdus2023/reusable-process-system`

## Findings

| Source area | Classification | Target | Coupling finding | Migration action |
|---|---|---|---|---|
| `skills/skill-creator` | CORE | `core/skills/skill-creator` | Generic skill-construction methodology | Extract |
| `skills/process-kernel` | CORE | `core/skills/process-kernel` | Generic process modeling workflow | Extract |
| `skills/transcript-process-extraction` | CORE | `core/skills/transcript-process-extraction` | Generic transcript extraction | Extract |
| `skills/process-specification` | CORE | `core/skills/process-specification` | Contains GPJK-shaped reference syntax and semantic assumptions | Extract then separate GPJK-specific rules |
| `skills/process-orchestrator` | CORE | `core/orchestration` | Generic lifecycle, but source skill graph is Kerno-oriented | Refactor references |
| `skills/process-conformance` | CORE | `core/conformance` | Generic conformance methodology with GPJK examples | Extract and isolate integration |
| `skills/process-release` | CORE | `core/release` | Generic release methodology | Extract |
| `skills/evidence-led*` | CORE | `core/evidence` | Generic evidence discipline | Extract |
| `skills/execution-*` | CORE | `core/evidence` | Generic execution-evidence boundary | Extract |
| `skills/continuation-controller` | CORE | `core/orchestration` | Generic explicit continuation state | Extract |
| `skills/agent-workflow` | CORE | `core/orchestration` | Contains `.agent/state/continuation.json` path and Kerno adapter references | Refactor paths/authority wording |
| `skills/adapter-contracts` | CORE | `contracts/adapters` | Generic authority/scope rules | Extract |
| `skills/gpjk-*` | GPJK | `integrations/gpjk` | Explicit GPJK semantics | Extract behind integration boundary |
| `skills/repo-*`, `repository-inventory` | PROFILE | `profiles/repository-audit` | Repository-specific methodology, not core semantics | Extract as profile |
| `runtime-trust-design` | PROFILE | `profiles/agent-runtime` | Runtime trust methodology | Extract as profile |
| `protocol-freeze` | PROFILE | `profiles/protocol` | Interoperability/protocol methodology | Extract as profile |
| `federation-design` | PROFILE | `profiles/federation` | Federation methodology | Extract as profile |
| `market-design` | PROFILE | `profiles/market` | Market/settlement methodology | Extract as profile |
| `repo-audit-adapter` | ADAPTER | `adapters/repository` | External repository boundary | Extract/refactor |
| `github-acquisition` | ADAPTER | `adapters/github` | GitHub-specific acquisition | Extract/refactor |
| `.agent/adapters/*.ts` | ADAPTER | `adapters/reference` | Generic adapter prototypes; authority must remain explicit | Extract with hardening |
| `.agent/bin/adapters/*.ts` | ADAPTER | `adapters/reference` or runtime boundary | Runtime implementation mixed with adapter layer | Split after dependency audit |
| `bin/agent-runner.ts` | UNRESOLVED | `runtimes/reference` candidate | Orchestration runner; imports and path assumptions require full audit | Do not copy yet |
| `bin/acquire-and-audit.ts` | UNRESOLVED | `adapters/repository` candidate | Composition function couples GitHub acquisition and evidence bundle | Split responsibilities |
| `conformance/*` | MIXED | `conformance/` + `integrations/gpjk/conformance` | Core harness vs GPJK fixtures not yet fully separated | Audit individually |

## Important source-level hazards

### 1. Verification adapter is not a sufficient generic verifier

The source `verification-gate.ts` only checks that referenced evidence exists and has status `VERIFIED` or `PROVED`. It does not demonstrate scope equality, provenance validity, integrity, or independent authority.

**Target action:** retain the contract concept, redesign implementation against the target evidence schemas.

### 2. Evidence adapter uses a non-cryptographic digest

The source `evidence-record.ts` uses an FNV-1a-derived short identifier.

**Target action:** do not treat that implementation as a canonical integrity mechanism. The reusable system must define a stronger, explicit digest contract before cryptographic identity is claimed.

### 3. Repository audit is local-observation authority

The source `repo-audit.ts` reports `local-filesystem+git` observations. This is useful static evidence but is not CI execution authority.

**Target action:** preserve the authority distinction in the standalone adapter API.

### 4. Runner contains Kerno-era filesystem conventions

`agent-workflow` and `agent-runner` refer to `.agent/state/continuation.json`.

**Target action:** replace hard-coded Kerno layout with a target-project state contract.

### 5. Process specification contains GPJK-shaped semantics

The `process-specification` skill explicitly uses `gpjk:<scope>:<path>` references and discusses three-valued semantics.

**Target action:** keep representation-independent process specification in core; move normative GPJK reference/expression semantics to `integrations/gpjk`.

## Decision

The source is **not safe for mechanical directory copying**.

The correct extraction strategy is:

```
Kerno .agent
   |
   +--> CORE ------------------> core / contracts / schemas
   |
   +--> GPJK ------------------> integrations/gpjk
   |
   +--> PROFILE ---------------> profiles
   |
   +--> ADAPTER ---------------> adapters
   |
   +--> RUNTIME? --------------> audit before placement
   |
   +--> KERNO-SPECIFIC --------> remain in Kerno
```

## Current gate

**M3 — dependency audit: PARTIALLY_VERIFIED**

The primary conceptual and several source-level dependencies have been inspected. Runtime/conformance implementation dependencies remain open. No standalone-conformance claim is made.

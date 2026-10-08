---
name: agent-workflow
description: Orchestrate the reusable process system as a deterministic state machine from repository snapshot through release gate.
---

# Agent Workflow

## Purpose

Run the complete reusable process workflow without relying on conversational memory.

## Workflow

```
SNAPSHOT
  ↓
AUDIT
  ↓
EVIDENCE
  ↓
VERIFY
  ↓
TRUST DESIGN
  ↓
PROTOCOL
  ↓
FEDERATION
  ↓
MARKET
  ↓
ENGINEERING PLAN
  ↓
RELEASE GATE
```

Optional design stages may be skipped when the task does not require them, but snapshot, audit, evidence, verification, engineering plan, and release gate remain explicit.

## State artifact

Persist state at a location configured by the host runtime.

Never rely on previous chat messages as state.

## Stage contract

Every stage records:
- stage ID
- input artifact digest
- output artifact digest
- status
- evidence IDs
- blockers
- timestamp
- tool/authority

## Transition rule

A stage can transition to COMPLETE only when its declared completion condition is satisfied.

A stage can transition to BLOCKED when required evidence is unavailable.

BLOCKED must not be silently converted to COMPLETE.

## Release gate

The release gate checks:
1. exact repository snapshot
2. exact implementation artifact
3. verification evidence
4. unresolved blockers
5. conformance/test evidence where required

## Anti-patterns

Never:
- infer CI success from source inspection
- infer runtime behavior from documentation alone
- inherit a previous conversation's unrecorded state
- call an implementation "verified" because it looks correct
- mix evidence from multiple commits without recording transitions

## Adapter boundary

Runtime-specific adapters are selected by the host configuration. They may provide repository snapshots, observations, execution evidence, or verification operations, but their authority must be explicit.

Local inspection is diagnostic evidence unless an execution authority explicitly establishes execution.

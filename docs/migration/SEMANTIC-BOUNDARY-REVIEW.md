# M4 Semantic Boundary Review

**Source snapshot:** `Abdus2023/Kerno@d1bf55e09de6a88e4a79e01084e1f0ac0cae9c99`  
**Status:** PARTIALLY_VERIFIED

## Boundary decision

The standalone project has three distinct layers:

```
Reusable Process System
        |
        +-- generic process language/contracts
        +-- generic lifecycle/orchestration
        +-- generic evidence/verification/release
        |
        +-- integrations/
              |
              +-- gpjk/
                    GPJK-specific syntax + semantics + conformance
        |
        +-- profiles/
        +-- adapters/
        +-- runtimes/
```

**Identity rule:**

`GPJK != Reusable Process System != Kerno`

The reusable system MUST NOT require GPJK identifiers, GPJK reference syntax, GPJK expression semantics, or GPJK state vocabulary in its generic core.

## Confirmed GPJK leakage in source

### 1. Process specification

The source `process-specification` skill requires references in the form:

`gpjk:<scope>:<path>`

and explicitly requires GPJK three-valued semantics.

**Decision:** retain the generic process-specification workflow in CORE, but move GPJK reference/evaluation rules into `integrations/gpjk`.

The generic skill should instead say that a process may declare references through a selected process-language adapter.

### 2. Generic process model schema

The source process-model schema is generic enough to remain CORE, but its schema identifier currently uses the Kerno domain:

`https://kerno.dev/.agent/tools/process-model.schema.json`

**Decision:** preserve the structural contract while replacing domain-specific identifiers during extraction.

### 3. Generic process decomposition

The decomposition contract separates operations, judgments, deterministic operations, and artifacts. No GPJK-specific semantic requirement was observed.

**Decision:** CORE.

### 4. Generic process/tool/skill contracts

The process-tool and skill-contract schemas are implementation-neutral at the structural level.

**Decision:** CORE, subject to domain-neutral identifiers and path references.

### 5. GPJK semantic skills

Reference resolution, expression evaluation, state machine, authorization, temporal verification, interchange, and governance are GPJK integration material.

**Decision:** `integrations/gpjk/`.

## Normative layering rule

Generic core defines:

- process identity/version
- inputs/outputs
- steps and dependencies
- constraints
- gates
- evidence requirements
- tool contracts
- skill contracts
- lifecycle/orchestration
- conformance framework
- verification/release boundaries

A process-language integration defines:

- reference syntax
- expression language
- value/null/missing/unresolved semantics when normative to that language
- state vocabulary and transition semantics
- language-specific authorization/temporal/interchange/governance rules

An integration MUST NOT silently redefine generic core semantics.

## Required extraction transformation

Do NOT perform:

```
Kerno/.agent/* -> reusable-process-system/.agent/*
```

Instead perform:

```
source artifact
  -> classify responsibility
  -> remove Kerno identity
  -> remove accidental GPJK coupling
  -> preserve normative semantics
  -> assign target layer
  -> validate cross-references
```

## M4 gate

M4 is **PARTIALLY_VERIFIED**.

The architectural boundary is sufficiently established to begin controlled extraction of generic contracts and skills, but GPJK-specific rewrites are required before those artifacts can be treated as standalone core artifacts.

## Next gate

M5 — extraction mapping freeze.

M5 will produce a file-level mapping:

`source path -> target path -> classification -> transformation -> dependency set -> validation gate`

Only after M5 freeze should bulk implementation extraction begin.

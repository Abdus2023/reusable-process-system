# Reusable Process Engineering System

A reusable system for discovering, specifying, decomposing, generating, executing, evidencing, verifying, and releasing governed processes.

## Identity

- **Project:** Reusable Process Engineering System
- **Repository:** `Abdus2023/reusable-process-system`
- **Kind:** generic process-engineering system
- **GPJK:** an integration/specification boundary, not the identity of this project
- **Origin:** extracted from `Abdus2023/Kerno` branch `agent/reusable-verification-skills`

## Architectural boundary

```
GPJK specification
        |
        v
integrations/gpjk
        |
        v
Reusable Process Engineering System
        |
   +----+----+
   v         v
 Kerno     other consumers
```

The system is intentionally broader than any single process representation. GPJK is supported through an explicit integration so that other representations can be supported later.

## Core rule

> NO EVIDENCE -> NO VERIFIED CLAIM

Additional governing distinctions:

- OBSERVED != DERIVED != VERIFIED != EXECUTED
- CI is execution authority; local inspection is diagnostic evidence
- freeze -> formalize -> implement -> test -> release gate -> tag
- core semantics must remain explicit
- profiles and adapters must not silently redefine core semantics

## Lifecycle

```
ACQUIRE -> LABEL -> EXTRACT -> MODEL -> SPECIFY -> DECOMPOSE
    -> CONTRACT -> TEST -> VERIFY -> PACKAGE -> RELEASE
```

## Extraction provenance

Source repository: `Abdus2023/Kerno`  
Source ref: `agent/reusable-verification-skills`  
Source path: `.agent`  
Source anchor: `d1bf55e09de6a88e4a79e01084e1f0ac0cae9c99`

This repository begins as a controlled standalone extraction. Source material is classified before migration into:

1. reusable process-system core
2. GPJK integration
3. reusable profiles
4. adapters
5. Kerno-specific material retained by Kerno

## Status

**PROVISIONAL — foundation only.**

The repository structure and identity boundary are established first. Extracted implementation is not yet claimed to be standalone-conformant until dependency, bootstrap, semantic, conformance, and release gates are executed.

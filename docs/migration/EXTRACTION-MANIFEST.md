# Extraction Manifest v0.1

## Purpose

This manifest governs extraction of Kerno's `.agent` implementation into the standalone Reusable Process Engineering System.

## Source

- Repository: `Abdus2023/Kerno`
- Ref: `agent/reusable-verification-skills`
- Source path: `.agent`
- Source anchor: `d1bf55e09de6a88e4a79e01084e1f0ac0cae9c99`

## Classification

Every source artifact receives exactly one primary classification:

| Classification | Meaning |
|---|---|
| CORE | Generic reusable process-system machinery |
| GPJK | GPJK-specific implementation, semantics, or conformance |
| PROFILE | Reusable methodology/profile layered over the core |
| ADAPTER | External-system/runtime boundary |
| KERNO-SPECIFIC | Material that remains in Kerno |
| UNRESOLVED | Requires source/dependency audit before migration |

## Required audit fields

Each migrated artifact must record:

- source path
- classification
- destination path
- imports/dependencies
- Kerno coupling
- GPJK coupling
- rewrite requirement
- migration action
- verification status

## Migration gates

### M1 — Identity

Prove that:

`reusable-process-system != Kerno`

and

`reusable-process-system != GPJK`

### M2 — Classification

No source artifact is migrated without an explicit classification.

### M3 — Dependency audit

Inspect imports, referenced paths, schemas, skills, tools, runtime assumptions, and Kerno-specific dependencies.

### M4 — Semantic boundary

Core must not redefine GPJK. Profiles and adapters must not silently redefine core semantics.

### M5 — Standalone bootstrap

The extracted project must bootstrap, validate, test, and run conformance without Kerno being present.

## Current status

**PROVISIONAL.**

This is the migration contract. It is not yet the completed file-by-file audit.

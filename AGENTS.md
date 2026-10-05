# AGENTS.md

## Project rule

This repository is the standalone Reusable Process Engineering System. Do not reintroduce Kerno-specific coupling into the core.

## Architecture

- `core/` — reusable process-engineering machinery
- `contracts/` — normative interfaces and contracts
- `schemas/` — data-shape definitions
- `conformance/` — reusable conformance machinery
- `integrations/gpjk/` — GPJK-specific integration
- `profiles/` — reusable domain/process profiles
- `adapters/` — external-system boundaries
- `runtimes/` — runtime implementations
- `tests/` — project verification
- `docs/migration/` — extraction provenance and migration evidence

## Non-negotiable distinctions

`SCHEMA VALID != SEMANTICALLY CONFORMANT != EXECUTED != VERIFIED`

`OBSERVED != DERIVED != VERIFIED != EXECUTED`

Never claim execution from source inspection alone.

## Migration discipline

freeze -> formalize -> implement -> test -> release gate -> tag

Every extracted source artifact must have an explicit classification and destination in the extraction manifest.

## Boundary rule

GPJK names a process language/specification. It does not name this entire project.

Do not copy the Kerno `.agent` tree wholesale. Extract by responsibility.

# Extraction Mapping v0.1

**Status:** FROZEN_FOR_EXTRACTION

Source: Kerno `agent/reusable-verification-skills` @ `d1bf55e09de6a88e4a79e01084e1f0ac0cae9c99`.

## Rules

- Extract by responsibility, not directory.
- Core must not depend on Kerno identity or GPJK syntax/semantics.
- GPJK material belongs under `integrations/gpjk/`.
- Profiles remain optional domain workflows.
- Authority-specific integrations remain adapters.
- Extraction is not execution verification.

## Mapping

| Source | Target | Class | Action |
|---|---|---|---|
| `.agent/skills/process-*` | `core/skills/` | CORE | extract/rewrite |
| `.agent/skills/skill-creator` | `core/skills/skill-creator` | CORE | extract |
| `.agent/skills/evidence-*` | `core/evidence/` | CORE | extract/rewrite |
| `.agent/skills/execution-*` | `core/verification/` | CORE | extract/rewrite |
| `.agent/skills/gpjk-*` | `integrations/gpjk/skills/` | GPJK | isolate |
| `.agent/tools/gpjk-*` | `integrations/gpjk/schemas/` | GPJK | isolate |
| generic schemas | `schemas/` | CORE | extract/rewrite identifiers |
| GPJK fixtures/harness | `integrations/gpjk/conformance/` | GPJK | isolate |
| generic conformance machinery | `conformance/framework/` | CORE | extract/rewrite |
| repository audit | `profiles/repository-audit/` | PROFILE | extract |
| trust/protocol/federation/market | `profiles/` | PROFILE | extract |
| GitHub/repository adapters | `adapters/` | ADAPTER | extract/rewrite |
| `agent-runner.ts` | `runtimes/reference/` | RUNTIME | rewrite, not copy |

## Explicit non-actions

Do not create Kerno coupling in core. Do not rename the system to GPJK. Do not treat GPJK fixtures as generic process truth. Do not preserve `kerno.dev` schema identifiers. Do not claim extracted code is tested until execution evidence exists.

## M5 decision

**FROZEN_FOR_EXTRACTION**

M6 may begin controlled extraction. Remaining unresolved work is implementation-level dependency checking for the Python conformance scripts and final cross-reference validation.

# Core ↔ GPJK Integration Contract Audit

**Status:** PARTIALLY_VERIFIED

## Scope

This audit checks the extracted core skills and GPJK integration boundary for accidental coupling and verifies that GPJK-specific semantics are referenced through an explicit integration boundary.

## Findings

| Area | Finding | Status |
|---|---|---|
| Core process specification | Uses implementation-neutral language and explicitly delegates reference syntax/semantics to the selected process-language integration. | PROVISIONAL |
| Core process kernel | Defines generic process extraction/modeling and does not require GPJK. | PROVISIONAL |
| GPJK reference resolution | Isolated under `integrations/gpjk`; GPJK syntax and four resolution states remain integration-specific. | PARTIALLY_VERIFIED |
| GPJK expression evaluation | Isolated under `integrations/gpjk`; TRUE/FALSE/UNKNOWN and strict typing remain integration-specific. | PARTIALLY_VERIFIED |
| GPJK state machine | Isolated under `integrations/gpjk`. | PARTIALLY_VERIFIED |
| GPJK authorization | Isolated under `integrations/gpjk`. | PARTIALLY_VERIFIED |
| GPJK temporal verification | Isolated under `integrations/gpjk`. | PARTIALLY_VERIFIED |
| GPJK interchange | Isolated under `integrations/gpjk`. | PARTIALLY_VERIFIED |
| GPJK governance | Isolated under `integrations/gpjk`. | PARTIALLY_VERIFIED |
| GPJK schemas | Source contract fields/constraints reconciled; Kerno namespace removed. | PARTIALLY_VERIFIED |
| GPJK fixtures | Eight semantic fixture domains extracted under `conformance/integrations/gpjk`. | OBSERVED |
| Conformance framework | Generic suite/differential contracts separated under `schemas/conformance` and `conformance/framework`. | OBSERVED |

## Boundary rules

1. Core MUST NOT require GPJK syntax.
2. Core MUST NOT import or depend on Kerno-specific identifiers.
3. GPJK semantics MUST remain inside the GPJK integration.
4. A process specification MAY select GPJK as its process-language integration.
5. Schema validation MUST NOT be treated as semantic conformance.
6. Fixture presence MUST NOT be treated as execution evidence.
7. Differential agreement MUST be scoped to executed fixture cases.

## Remaining uncertainty

This is a static source/tree audit. It does not establish:
- runtime importability;
- executable conformance;
- CI execution authority;
- semantic equivalence of an independent GPJK implementation;
- correctness of the extracted reference runner beyond actual execution.

## Next gate

Execute the extracted GPJK fixture runner in a controlled environment, capture complete execution evidence, then audit the generic conformance runner against the integration-specific runner.


---
name: evidence-ledger
description: Maintain claim-level provenance and explicit verification states for a research directory. Use throughout the lifecycle and before any public-facing conclusion.
---

# Evidence Ledger

## Core rule
NO EVIDENCE -> NO VERIFIED CLAIM.

## Procedure
1. Give each evidence item a stable evidence_id.
2. Store source URL, source type, title/description, access date, publication date if known, and the method of observation.
3. State the exact claim supported; one source may support one claim and not another.
4. Label evidence as DIRECT, CORROBORATING, CONTEXTUAL, CONTRADICTORY, or INACCESSIBLE.
5. Distinguish OBSERVED facts, DERIVED interpretations, VERIFIED conclusions, and EXECUTED operations.
6. Track source independence and possible circular repetition.
7. Preserve counterevidence, corrections, source changes, and uncertainty.
8. Keep record status separate from claim-level status.
9. Never upgrade a claim merely because a search snippet repeats it.
10. Record retrieval dates for content that can change.

## Status vocabulary
Record status: VERIFIED, PARTIALLY_VERIFIED, UNVERIFIED, EXCLUDED.
Claim status: SUPPORTED, MOSTLY_SUPPORTED, PARTIALLY_SUPPORTED, CONTRADICTED, MISLEADING_CONTEXT, UNVERIFIED, NOT_ASSESSABLE.
Evidence type: DIRECT, CORROBORATING, CONTEXTUAL, CONTRADICTORY, INACCESSIBLE.

## Output
Evidence ledger with claim IDs, source references, provenance, limitations, and review history.

## Failure conditions
If the source cannot be opened, do not claim direct inspection. If sources conflict, retain the conflict and mark the claim unresolved until adjudicated.
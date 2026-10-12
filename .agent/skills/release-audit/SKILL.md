---
name: release-audit
description: Audit a research directory for identity, evidence, metrics, deduplication, coverage, and schema quality before publication. Use at the end of a batch and before final release.
---

# Release Audit

## Procedure
1. Freeze a dated snapshot of the candidate ledger and evidence log.
2. Run the deterministic directory validator.
3. Check stable IDs, duplicates, required fields, URL presence, status consistency, metric dates, and source-to-claim mapping.
4. Recount VERIFIED, PARTIALLY_VERIFIED, UNVERIFIED, and EXCLUDED records; reconcile counts with exports.
5. Check category/language/region coverage and document gaps without adding weak records to fill quotas.
6. Ensure only VERIFIED records appear in the verified publication list.
7. Confirm rankings are omitted unless the formula is reproducible and the data supports comparison.
8. Summarize contradictions, inaccessible sources, missing metrics, and open questions.
9. Record each gate as PASS, FAIL, or NOT_VERIFIABLE and attach evidence.
10. Choose READY_FOR_PUBLICATION, PARTIALLY_READY, or BLOCKED. Explain any gate that prevents release.
11. Update the continuation ledger with exact next action.

## Output
Directory snapshot, validator output, gate matrix, reconciled counts, release decision, limitations, and change log.

## Failure conditions
Do not claim CI passed without observing its run. A valid schema does not prove that factual claims are true. A target of 100 does not override evidence requirements.
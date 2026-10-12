---
name: creator-research-orchestrator
description: Orchestrate a continuing, evidence-based research project that discovers, verifies, analyzes, and publishes a directory of public content creators. Use at project start and every continuation request.
---

# Creator Research Orchestrator

## Trigger
Use when a user asks to build, continue, audit, or publish a directory of creators or public channels, including requests phrased as Continue, Next, or Next Prompt Instructions.

## Inputs
- Research scope and inclusion criteria.
- Existing creator ledger, source log, prior outputs, and continuation state.
- Accessible search/platform tools and their limitations.
- Required target count, languages, platforms, and output formats.

## Procedure
1. Read existing state before searching. Preserve stable IDs, completed phases, and unresolved issues.
2. Define what qualifies as a creator and what constitutes a relevant connection to the target geography.
3. Use `multilingual-discovery` to generate and execute query families.
4. Use `identity-resolution` to link creators to official channels and profiles.
5. Use `evidence-ledger` to attach sources to specific claims and assign record statuses.
6. Use `channel-metrics`, `content-audit`, `collaboration-mapping`, `credibility-audit`, and `audience-analysis` only where the evidence and scope justify them.
7. Batch work to manageable sizes; report per-batch counts and preserve cumulative counts.
8. Deduplicate by entity identity, not display-name equality alone.
9. Use `release-audit` and the deterministic directory validator before publishing.
10. Update continuation state with completed work, gaps, decisions, record changes, and one concrete next action.

## Output contract
- Current phase and scope.
- Cumulative directory and explicit record statuses.
- Sources tied to claims.
- Coverage and quality summary.
- Unresolved issues and limitations.
- Continuation ledger with exact next action.
- Release decision when publication is requested.

## Stop conditions
Stop short of a VERIFIED claim if identity, relevant scope connection, or claim-specific evidence is inadequate. Do not fabricate records to reach a target count. If prior state cannot be accessed, disclose that and establish a recovery point.
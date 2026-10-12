# Agent Operating Contract

## Before acting
1. Read this file, `.agent/README.md`, the applicable skill, and the profile workflow.
2. Inspect existing artifacts and continuation state before beginning discovery.
3. State the intended output, scope, source-access limits, and verification gates.
4. Do not claim to have searched, opened, tested, or verified a source unless the action actually occurred.

## Evidence
- Keep source observations separate from interpretations and conclusions.
- Every material claim must point to one or more evidence records.
- A source's existence does not prove every claim attributed to it.
- Prefer direct creator/platform pages for identity and channel association; use independent corroboration when available.
- Record retrieval/observation dates for changing metrics.
- Preserve contradictions and inaccessible sources as explicit unresolved items.

## Continuity
- Reuse stable IDs and prior work.
- Maintain completed phases, outstanding work, decisions, changed records, and the next action.
- Do not silently restart, repeat completed work, or skip unresolved topics.
- When prior state is unavailable, say so and create a recovery ledger rather than pretending continuity.

## Tool and skill authoring
- Follow `.agent/skills/skill-creator/SKILL.md`.
- Skills define when/why/how; tools perform deterministic, bounded operations.
- Keep tool input/output contracts explicit, errors actionable, and dependencies minimal.
- Add fixtures for both valid and invalid cases.
- Do not label a tool verified until tests are executed and their results are recorded.

## Safety and scope
Use public, relevant information. Do not infer private attributes, sensitive traits, intent, or audience demographics without direct, appropriate evidence. Do not expose private personal data. Do not treat criticism, controversy, or allegation as established fact without claim-specific evidence.
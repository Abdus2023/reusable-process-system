# .agent — Reusable Research Process Pack

**Pack:** Tunisian Creator Research Profile  
**Version:** 0.1.0  
**Status:** PROVISIONAL until repository CI and release gates execute  
**Branch:** `agent/tunisian-creator-research-processes`

This directory turns the creator-research workflow developed across the conversation into reusable skills, contracts, tools, fixtures, and a workflow profile. The profile is Tunisian-creator-focused; underlying skills are designed for reuse in other public-entity research directories.

## Governing rules
- NO EVIDENCE → NO VERIFIED CLAIM.
- OBSERVED ≠ DERIVED ≠ VERIFIED ≠ EXECUTED.
- A target count never justifies fabricated records or weaker evidence.
- Search snippets are leads, not final proof.
- Each material claim must point to evidence supporting that specific claim.
- Missing, inaccessible, contradictory, or stale evidence remains visible.
- Preserve stable IDs and continuity across successive requests.
- Local tests prove only what they execute; CI status remains unknown until observed.

## Contents
- `skills/`: 11 role-scoped skills, including a local `skill-creator` authoring method.
- `contracts/`: JSON Schemas for creator records, evidence records, and continuation state.
- `tools/validate_directory.py`: deterministic structural and consistency checks.
- `tools/summarize_directory.py`: deterministic status and coverage counts.
- `tests/`: positive/negative fixtures and unit tests.
- `profiles/tunisian-creator-research/`: profile and 10-phase prompt library.
- `workflows/`: machine-readable orchestration plan.
- `manifest.json`: pack inventory and status.

## Run locally
```sh
python .agent/tools/validate_directory.py .agent/tests/fixtures/creators.valid.json
python .agent/tools/summarize_directory.py .agent/tests/fixtures/creators.valid.json
python -m unittest discover -s .agent/tests -v
```

Input JSON must contain a top-level `creators` array. See `profiles/tunisian-creator-research/PROFILE.md`.

## Release vocabulary
- `PROVED`: follows from a defined formal rule or executed deterministic check.
- `ARGUMENT`: reasoned but not mechanically established.
- `CONJECTURE`: plausible and not yet established.
- `OPEN`: unresolved.
- `VERIFIED`, `PARTIALLY_VERIFIED`, `UNVERIFIED`, `EXCLUDED`: record statuses.
- `READY_FOR_PUBLICATION`, `PARTIALLY_READY`, `BLOCKED`: release decisions.

This pack does not claim that 100 creators have already been researched. It supplies a repeatable process to conduct and audit that research.
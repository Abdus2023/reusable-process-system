# .agent — Reusable Research Process Pack

**Pack:** Tunisian Creator Research Profile  
**Version:** 0.1.0  
**Status:** PROVISIONAL until repository CI and release gates execute  
**Branch:** `agent/tunisian-creator-research-processes`

This directory turns the creator-research workflow developed across the conversation into reusable skills, contracts, tools, fixtures, and a workflow profile. The profile is Tunisian-creator-focused; the underlying skills are designed to be reusable for other public-entity research directories.

## Governing rules

- NO EVIDENCE → NO VERIFIED CLAIM.
- OBSERVED ≠ DERIVED ≠ VERIFIED ≠ EXECUTED.
- A target count is not a license to fabricate or lower evidence standards.
- Search snippets are discovery leads, not final proof.
- A source must be tied to the specific claim it supports.
- Missing, inaccessible, contradictory, or stale evidence remains visible.
- Preserve prior work and stable IDs across continuation requests.
- Local tests prove only what they execute; CI status remains unknown until observed.

## Contents

- `skills/`: role-scoped instructions, including a local `skill-creator` authoring method.
- `contracts/`: JSON Schemas for creator records, evidence records, and continuation state.
- `tools/validate_directory.py`: deterministic standard-library directory validator.
- `tests/`: fixtures and validator tests.
- `profiles/tunisian-creator-research/`: profile, workflow, and prompt library for phases 01–10.
- `workflows/`: machine-readable orchestration plan.
- `manifest.json`: file and capability inventory.

## Run the local validator

```sh
python .agent/tools/validate_directory.py path/to/directory.json
python -m unittest discover -s .agent/tests -v
```

The input JSON must contain a top-level `creators` array. See `profiles/tunisian-creator-research/PROFILE.md` and the test fixtures.

## Release vocabulary

- `PROVED`: follows from a defined formal rule or executed deterministic check.
- `ARGUMENT`: reasoned but not mechanically established.
- `CONJECTURE`: plausible and not yet established.
- `OPEN`: unresolved.
- `VERIFIED`: evidence threshold for a research record is met.
- `PARTIALLY_VERIFIED`, `UNVERIFIED`, `EXCLUDED`: explicit non-verified states.
- `READY_FOR_PUBLICATION`, `PARTIALLY_READY`, `BLOCKED`: release-gate decisions.

This pack does not claim that a list of 100 creators has already been researched. It provides the repeatable process for doing so.
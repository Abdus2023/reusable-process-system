---
name: skill-creator
description: Create, refine, and audit reusable agent skills and bounded tools in this repository. Use whenever a process must be extracted from conversation or project work and converted into a maintainable skill/tool pack.
---

# Skill Creator

## Purpose
Turn a repeated or clearly specified process into a reusable, testable skill without silently converting assumptions into requirements or claims into facts.

## Required inputs
- Process objective and intended users.
- Available source conversation/artifacts and their provenance.
- Expected outputs and consumers.
- Constraints, failure states, and non-goals.
- Runtime/tooling constraints.
If any required input is unavailable, record the gap and proceed only with a clearly marked provisional design where safe.

## Procedure
1. **Acquire**: collect the source instructions, examples, decisions, exceptions, and corrections. Preserve provenance; do not treat prior assistant text as execution evidence.
2. **Label**: classify each item as requirement, preference, observed fact, derived interpretation, open question, or rejected approach.
3. **Extract**: identify stable reusable actions and isolate domain-specific policy.
4. **Model**: define actors, inputs, outputs, state transitions, dependencies, and failure modes.
5. **Specify**: write a concise SKILL.md with purpose, trigger, prerequisites, ordered procedure, outputs, and explicit stop conditions.
6. **Decompose**: split large workflows into single-responsibility skills. Avoid duplicating shared rules; link to common contracts.
7. **Contract**: define schemas or command interfaces for machine-consumed artifacts. Specify required fields, status enums, and error behavior.
8. **Implement**: write deterministic tools only for operations that benefit from mechanical enforcement. Prefer standard library and no network access by default.
9. **Test**: create positive, negative, edge, and regression fixtures. Include duplicate, missing-field, malformed-input, and contradictory-status cases as appropriate.
10. **Verify**: run the tests when an execution environment is available. Record exact command, result, environment, and timestamp. If not run, mark NOT_EXECUTED.
11. **Package**: update README, manifest, references, and workflow links; check for dangling paths and inconsistent names.
12. **Release gate**: report PASS/FAIL/NOT_OBSERVED per gate. Do not claim repository CI ran unless its result was observed.
13. **Continuity**: record what was reused, created, changed, deferred, and the exact next action.

## Skill authoring requirements
Every skill should include:
- YAML frontmatter with a stable kebab-case name and useful description.
- A clear trigger and non-goals.
- Inputs/prerequisites.
- Numbered procedure.
- Output contract.
- Failure/stop conditions.
- Evidence and continuity requirements.
- Links to related skills/contracts when relevant.

## Tool authoring requirements
Every tool should:
- Have one bounded responsibility.
- Validate inputs before mutation or output.
- Use stable status codes and actionable diagnostics.
- Avoid hidden network calls and nondeterministic dependencies unless explicitly specified.
- Be safe to rerun or clearly document non-idempotent effects.
- Have tests for expected and rejected inputs.
- Never claim that its own output proves an external fact unless it actually checks that fact.

## Completion report
Return a manifest diff, files created/changed, tests actually run, observed results, unresolved risks, release decision, and next action.

## Governing invariant
NO EVIDENCE -> NO VERIFIED CLAIM. A generated skill is not a tested skill; a passing local test is not proof of CI or release conformance.
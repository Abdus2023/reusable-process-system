# Reusable Process Engineering System — Agent Workspace

This `.agent/` workspace expresses the generic process-engineering lifecycle as composable skills. It is deliberately separate from Kerno and GPJK. GPJK remains one optional integration boundary, not the identity of the system.

## Skills
- [skill-creator](skills/skill-creator/SKILL.md)
- [process-discovery-and-extraction](skills/process-discovery-and-extraction/SKILL.md)
- [process-specification-and-decomposition](skills/process-specification-and-decomposition/SKILL.md)
- [process-contract-and-composition](skills/process-contract-and-composition/SKILL.md)
- [process-evidence-conformance-release](skills/process-evidence-conformance-release/SKILL.md)

## Workflow
- [Reusable process engineering lifecycle](workflows/reusable-process-engineering-lifecycle.md).

## Computational support
- [validate_skill.py](tools/validate_skill.py) — structural skill lint only.
- [test_validate_skill.py](tests/test_validate_skill.py) — validator tests.

## Source authority and limits
The generic system specification is [process-system.md](../specification/process-system.md). Migration source classification is governed by [EXTRACTION-MANIFEST.md](../docs/migration/EXTRACTION-MANIFEST.md) and [EXTRACTION-MAPPING.md](../docs/migration/EXTRACTION-MAPPING.md). Do not mechanically copy Kerno's `.agent` tree. The current migration audits are PARTIALLY_VERIFIED and the standalone system remains PROVISIONAL.

Run:
```sh
python3 .agent/tools/validate_skill.py .agent/skills
python3 -m unittest discover -s .agent/tests -v
```

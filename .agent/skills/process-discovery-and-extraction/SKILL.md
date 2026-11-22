---
name: process-discovery-and-extraction
description: Discover and extract repeatable process knowledge with pinned provenance, explicit classification, and controlled source-to-target mapping.
---

# Process Discovery and Extraction

## Purpose
Convert source material, conversations, repositories and observed workflows into traceable process evidence without conflating proposals, implementation, or verification.

## Activation
Use when acquiring a process source, freezing a source snapshot, extracting process steps, classifying source artifacts, or preparing a controlled migration.

Do not use this skill to mechanically copy a source directory or to infer rights, completeness, or execution from repository presence.

## Inputs
- Source repository/ref/commit or explicitly supplied filesystem root.
- Scope and exclusions.
- Source manifest and byte/object identities.
- Provenance and licensing evidence.
- Extraction classification vocabulary and target architecture.
- Existing extraction records and mapping manifest.

## Procedure
1. ACQUIRE the source from an exact repository/ref or declared filesystem boundary.
2. LABEL the source with immutable commit/tree/blob or file digest/size identities where available.
3. Freeze the source manifest before extraction; never edit the frozen source snapshot.
4. Enumerate artifacts and record inaccessible paths, exclusions, file types and limits.
5. Classify every artifact with exactly one primary disposition: CORE, integration-specific, PROFILE, ADAPTER, RUNTIME, source-project-specific, or UNRESOLVED. Use project-defined classes where they are more precise.
6. EXTRACT by responsibility, not directory layout. Preserve source path, target path, dependencies, coupling, rewrite action and verification status.
7. Separate performed actions, explicit decisions, proposals, derived interpretations and open questions.
8. Preserve exact source anchors and provenance; do not infer license or permission from public visibility.
9. Identify Kerno-specific or GPJK-specific semantics before migration. Keep GPJK-specific syntax/semantics behind the integration boundary and Kerno-specific policy in Kerno.
10. Compare each candidate with existing target artifacts to avoid duplicates and preserve canonical ownership.
11. Record unresolved dependencies and stop extraction where source identity, rights, or semantic authority is unclear.

## Outputs
- Frozen source manifest.
- Artifact inventory and provenance ledger.
- Classification and source-to-target extraction mapping.
- Extraction records with dependencies and rewrite requirements.
- Open issue and blocked-gate list.

## Failure handling
Stop when the source anchor is ambiguous, the frozen snapshot cannot be reproduced, a file's classification is unresolved, or rights/security constraints block migration. Do not claim extraction completeness from path enumeration alone.

## Acceptance criteria
- Source identity is pinned.
- Source files remain unchanged.
- Every migrated artifact has a primary classification and target.
- Dependencies and Kerno/GPJK coupling are explicit.
- Proposals and implementation are distinguished.
- Provenance and rights remain evidence-based.
- Unresolved artifacts remain UNRESOLVED rather than being copied by default.

## Source references
- `README.md`
- `AGENTS.md`
- `docs/migration/EXTRACTION-MANIFEST.md`
- `docs/migration/EXTRACTION-MAPPING.md`

## Validation status
The repository's migration manifest is PROVISIONAL; this skill does not assert that the Kerno extraction is complete.

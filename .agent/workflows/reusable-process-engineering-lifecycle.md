# Reusable Process Engineering Lifecycle

**Status:** PROPOSED / OPERATOR-RUN  
**Source:** `specification/process-system.md`, `AGENTS.md`, `docs/migration/*`

## Lifecycle
`ACQUIRE → LABEL → EXTRACT → MODEL → SPECIFY → DECOMPOSE → CONTRACT → TEST → VERIFY → PACKAGE → RELEASE`

## Procedure
1. **ACQUIRE:** pin source repository/ref/commit or filesystem boundary.
2. **LABEL:** record provenance, authority, evidence class and classification.
3. **EXTRACT:** classify each artifact CORE, GPJK, PROFILE, ADAPTER, KERNO-SPECIFIC or UNRESOLVED; map source to target by responsibility.
4. **MODEL:** define process identity, actors, inputs, outputs, states, dependencies, gates and artifacts.
5. **SPECIFY:** formalize process semantics and constraints; keep representation-specific rules behind explicit integrations.
6. **DECOMPOSE:** create bounded operations, judgments, deterministic tools, human approvals and sub-processes.
7. **CONTRACT:** define versioned skill/tool/adapter/runtime interfaces, errors, permissions, resource limits and authority.
8. **TEST:** execute positive, negative, boundary and failure fixtures against pinned implementations.
9. **VERIFY:** bind results to exact commits, artifacts, environment and evidence; CI is execution authority where declared.
10. **PACKAGE:** validate dependencies, schemas, references, provenance and composition edges.
11. **RELEASE:** pass release gates, create immutable tag and record package manifest.

## Mandatory migration gates
- M1 Identity: standalone system is neither Kerno nor GPJK.
- M2 Classification: every source artifact has explicit disposition.
- M3 Dependency audit: imports, schemas, paths, runtime assumptions and hidden coupling inspected.
- M4 Semantic boundary: GPJK semantics isolated; generic core remains representation-independent.
- M5 Standalone bootstrap/conformance: bootstrap, validate, test and conformance without Kerno present.

## Stop conditions
Stop if a source artifact is UNRESOLVED, dependency coupling is not understood, a GPJK semantic rule leaks into generic core, evidence authority is unclear, or the standalone target cannot bootstrap independently.

## Outputs
Frozen source manifest, extraction mapping, process model, contracts, test fixtures, evidence ledger, conformance report, package manifest and release-gate record.

## Current gate
The repository baseline and migration mapping are PROVISIONAL / PARTIALLY_VERIFIED. This workflow is an authoring contract; it is not evidence that any gate has passed.

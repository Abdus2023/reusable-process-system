# Extraction Boundary

The standalone project is extracted from Kerno but does not inherit Kerno ownership or namespace.

## Four-way classification

- **Core:** generic process engineering, lifecycle, evidence, verification, conformance, release.
- **GPJK integration:** GPJK schemas, semantics, fixtures, and GPJK-specific reference checks.
- **Profile/adapter:** repository, GitHub, agent-runtime, and other environment-specific capabilities.
- **Kerno-specific:** material whose semantics depend on Kerno itself; it must not enter the standalone core.

Historical provenance is retained in migration documentation rather than runtime dependencies.

## Non-goals

The extraction is not a rename of Kerno's .agent directory. It is a reconstruction under explicit dependency boundaries.

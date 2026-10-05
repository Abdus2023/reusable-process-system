# M8 Runtime and Conformance Audit

**Status:** PARTIALLY_VERIFIED

> M8 execution evidence is now recorded in `docs/migration/M8-EXECUTION-EVIDENCE.md`. The scoped CI execution sub-gate is VERIFIED; the overall gate remains PARTIALLY_VERIFIED.

## Findings

The extracted GPJK reference runner is dependency-free Python and can be invoked directly from the repository. Its repository paths were rewritten for the standalone layout and its historical Kerno implementation identity was removed.

The fixture-shape validator now excludes the harness manifest because that manifest is a runner contract, not a fixture suite.

A GitHub Actions workflow has been added with two jobs:
- fixture-shape validation;
- GPJK reference conformance execution with an uploaded execution report.

## Critical semantic limitation

The reference runner contains compact fixture adapters rather than a complete normative GPJK implementation. Several checks are deliberately fixture-shaped, including temporal and evidence checks. Therefore a green runner result would establish execution of the registered reference checks, not complete GPJK semantic conformance.

## Execution boundary

The workflow has now been observed executing under GitHub Actions. Run `37351749239` completed successfully for commit `16bed636374c24093c90eb7c38443342d3beaa8d` and tree `aa98ecdaa3903d95af2deb630e816560ce0fa6f9`.

The scoped execution results were:
- reference-runtime: SUCCESS
- GPJK fixture-shape: SUCCESS
- GPJK reference conformance: SUCCESS
- registered GPJK cases: 28 PASS / 0 FAIL / 0 ERROR

This establishes execution evidence for the recorded workflow and exact snapshot. It does not establish complete semantic conformance because the reference runner contains compact fixture adapters.

## Next gate

1. Preserve the recorded execution evidence.
2. Expand semantic conformance beyond fixture-shaped adapters.
3. Add contract tests for runtime/adapters and evidence binding.
4. Complete runtime extraction and dependency audits.
5. Re-run CI after each normative change and bind the result to the exact commit/tree.

M8 therefore remains PARTIALLY_VERIFIED.

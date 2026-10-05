# M8 Runtime and Conformance Audit

**Status:** PARTIALLY_VERIFIED

## Findings

The extracted GPJK reference runner is dependency-free Python and can be invoked directly from the repository. Its repository paths were rewritten for the standalone layout and its historical Kerno implementation identity was removed.

The fixture-shape validator now excludes the harness manifest because that manifest is a runner contract, not a fixture suite.

A GitHub Actions workflow has been added with two jobs:
- fixture-shape validation;
- GPJK reference conformance execution with an uploaded execution report.

## Critical semantic limitation

The reference runner contains compact fixture adapters rather than a complete normative GPJK implementation. Several checks are deliberately fixture-shaped, including temporal and evidence checks. Therefore a green runner result would establish execution of the registered reference checks, not complete GPJK semantic conformance.

## Execution boundary

The workflow defines a future execution authority. No workflow result is claimed by this audit because the branch has not been observed executing the workflow.

## Next gate

Run the workflow, inspect every registered case, verify the generated report against the fixture inventory, and bind the execution evidence to the exact commit and tree.

Only then can M8 execution be classified beyond PARTIALLY_VERIFIED.

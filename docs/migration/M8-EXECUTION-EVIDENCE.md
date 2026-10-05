# M8 Execution Evidence

**Overall M8 status:** PARTIALLY_VERIFIED

## Verified execution

GitHub Actions executed the standalone branch workflow.

- repository: `Abdus2023/reusable-process-system`
- branch: `extract/core-foundation`
- commit: `16bed636374c24093c90eb7c38443342d3beaa8d`
- tree: `aa98ecdaa3903d95af2deb630e816560ce0fa6f9`
- workflow run: `37351749239`
- workflow: `.github/workflows/conformance.yml`
- event: push
- execution authority: GitHub Actions

Run jobs:

| Job | Result |
|---|---|
| reference-runtime | success |
| gpjk-fixture-shape | success |
| gpjk-reference-conformance | success |

The reference-runtime job successfully compiled `runtimes/reference/process_runner.py` and executed the runtime unit-test suite.

The GPJK reference job executed the registered conformance runner and produced:

- PASS: 28
- FAIL: 0
- ERROR: 0
- implementation identity: `gpjk-reference-runner`
- Python: 3.12.14

The generated execution report was uploaded as artifact `11363156063` with artifact SHA-256:

`sha256:358e843aef0dfca3521479c2d1b50bf4d95b27a58e65c9367b172dbd80cb0df6`

## Earlier observed failure

Run `37351640880` at commit `28d98866b55eeb69be56012f52198c90fd9896a6` executed the workflow but failed the GPJK reference job:

- PASS: 27
- FAIL: 1
- ERROR: 0
- failing case: `gpjk-authorization/a-permit`

The failure was corrected in subsequent commits and the next completed run passed all 28 registered cases.

## Claim boundary

The execution evidence proves that the registered reference runtime tests and registered GPJK fixture checks executed successfully for the exact commit/tree above.

It does **not** prove complete GPJK semantic conformance. The runner remains a compact fixture adapter, and the fixture set is not a complete normative test suite.

It also does not prove that every future implementation of GPJK conforms.

## M8 decision

M8 execution authority is now **VERIFIED for the recorded workflow run and scoped checks**.

M8 as a whole remains **PARTIALLY_VERIFIED** because semantic completeness and broader runtime extraction/release gates remain open.

**Rule:** successful execution is evidence of execution; it is not automatically evidence of semantic completeness.

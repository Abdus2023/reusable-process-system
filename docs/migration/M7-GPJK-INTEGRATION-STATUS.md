# M7 GPJK Integration Boundary — Status

**Status:** PARTIALLY_VERIFIED

## Completed

- Seven GPJK semantic skills are isolated under integrations/gpjk/skills/.
- Seven GPJK contract schemas are isolated under integrations/gpjk/schemas/.
- GPJK-specific conformance fixtures are isolated under conformance/integrations/gpjk/.
- Generic conformance suite and differential-result schemas are isolated under schemas/conformance/.
- Generic conformance framework documentation is under conformance/framework/.
- Core process specification explicitly delegates process-language syntax and semantics to a selected integration.
- Static inspection found no gpjk:, kerno.dev, Kerno, or .agent references in the inspected extracted core skill files.

## Important distinction

The GPJK fixtures and reference adapters describe the GPJK integration's fixture semantics. They are not generic process truth.

The extracted reference runner is an implementation artifact. Its presence is not execution evidence.

## Not yet proved

- runner execution on this branch;
- complete fixture-suite PASS;
- independent implementation differential conformance;
- CI execution authority;
- semantic equivalence beyond the registered fixture cases.

## Gate decision

M7 boundary work: PARTIALLY_VERIFIED

Proceed to runtime/reference-runner audit and controlled execution infrastructure. Do not promote this integration to VERIFIED until execution evidence exists.

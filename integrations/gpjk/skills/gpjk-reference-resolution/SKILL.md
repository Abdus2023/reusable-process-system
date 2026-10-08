---
name: gpjk-reference-resolution
description: Resolve GPJK references deterministically while preserving VALUE, NULL, MISSING, and UNRESOLVED outcomes.
---

# GPJK Reference Resolution

This integration adapts the reusable process system to GPJK reference syntax and semantics.

## Procedure
1. Parse `gpjk:<scope>:<path>`.
2. Validate syntax and scope.
3. Locate the target.
4. Return VALUE, NULL, MISSING, or UNRESOLVED without silent fallback.
5. Emit a resolution trace.

## Boundary
Resolution interprets a GPJK reference; it does not establish truth of the referenced external fact.

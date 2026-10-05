---
name: gpjk-expression-evaluation
description: Evaluate GPJK expressions with strict typing and TRUE/FALSE/UNKNOWN semantics.
---

# GPJK Expression Evaluation

Evaluate declarative GPJK conditions without implicit coercion or arbitrary host execution.

## Procedure
1. Parse and validate grammar.
2. Resolve GPJK references.
3. Apply strict type rules.
4. Evaluate permitted pure functions and logical operators.
5. Propagate UNKNOWN according to GPJK semantics.
6. Distinguish invalid expressions from UNKNOWN.
7. Emit an evaluation trace.

## Boundary
This is GPJK semantic integration; the generic process system supplies the surrounding process, evidence, verification, and release machinery.

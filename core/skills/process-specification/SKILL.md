---
name: process-specification
description: Convert an extracted workflow into a schema-first process specification with requirements, inputs, outputs, steps, control flow, evidence, constraints, and verification.
---

# Process Specification

## Purpose
Produce an implementation-neutral process definition suitable for JSON serialization and independent interpretation.

## Inputs
- extracted process
- requirements
- inputs and outputs
- constraints
- evidence requirements
- verification rules

## Outputs
- process artifact
- semantic rule inventory
- reference map
- verification plan

## Procedure
1. Define stable process identity and version.
2. Declare requirements and inputs.
3. Declare expected outputs.
4. Model each step with stable ID and action.
5. Make dependencies explicit; array order alone does not imply dependency.
6. Separate conditions from constraints.
7. Define preconditions and postconditions.
8. Declare required evidence.
9. Bind references through the selected process-language integration; GPJK reference syntax belongs to the GPJK integration.
10. Define verification assertions.
11. Apply the selected process-language semantics for reference resolution and evaluation.
12. Preserve explicit language semantics without assuming a particular process language.
13. Check composition and exact dependency versions.
14. Produce canonical JSON.

## Gates
PS1 identity/version bound
PS2 inputs/outputs explicit
PS3 dependencies explicit
PS4 constraints and conditions separated
PS5 evidence traceability present
PS6 verification rules independently evaluable

## Failure modes
Ambiguous action binding, missing dependency, silent version substitution, implicit coercion, unresolved reference, required evidence without verification use.

## Evidence policy
A process specification is a definition. It does not prove execution.

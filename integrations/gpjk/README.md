# GPJK Integration

This directory contains the integration boundary between the reusable process system and the General Process JSON Kernel (GPJK).

## Boundary

- The reusable process system provides generic process engineering, evidence, verification, conformance, and release machinery.
- GPJK provides one process representation and semantic contract integrated through this directory.
- Kerno is the historical source from which this integration was extracted; it is not a runtime dependency of this repository.

## Contents

- `skills/`: GPJK-specific semantic skills.
- `schemas/`: GPJK contract schemas with standalone repository identifiers.
- `conformance/`: GPJK fixtures and reference conformance material.

## Claim boundary

Schema validity does not establish semantic conformance. Fixture presence does not establish execution. A conformance claim requires complete execution evidence and sufficient scope.

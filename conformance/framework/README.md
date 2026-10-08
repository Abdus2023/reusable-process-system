# Conformance Framework

The reusable process system conformance framework defines implementation-neutral fixtures, runner contracts, result normalization, and evidence boundaries.

## Contract

A conformance suite contains a suite identifier, version, and registered cases. A runner consumes a fixture and an implementation and emits complete per-case results.

Required result statuses are explicit. A case that was not executed is not a pass.

## Evidence boundary

Fixture presence is observation. A runner result is execution evidence only when the run records implementation identity, fixture suite/version, invocation, timestamp, complete case results, exit status, and environment/toolchain identity.

CI is execution authority for release claims.

## Differential conformance

Differential comparison establishes agreement between identified implementations for the executed fixture scope. It does not establish correctness outside that scope.

## Separation

Domain semantics belong to integrations or profiles. The framework does not define GPJK semantics.

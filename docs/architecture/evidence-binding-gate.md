# Evidence Binding Gate

## Purpose

The execution-evidence schema establishes the shape of a record. The binding gate establishes whether that record is sufficient to verify a particular immutable repository target.

This is deliberately a pure contract layer:

- it does not execute an adapter;
- it does not discover CI runs;
- it does not fabricate evidence;
- it does not upgrade missing or unobservable execution into verification.

## Verification predicate

For a repository target T and evidence record E, E may establish VERIFIED only when:

1. E has repository, commit, and tree scope;
2. T has repository, commit, and tree scope;
3. E.status == PASS;
4. E.authority == required_authority (CI by default);
5. E.kind == EXECUTION (by default);
6. E.scope.repository == T.repository;
7. E.scope.commit == T.commit;
8. E.scope.tree == T.tree.

ref is contextual metadata. It cannot substitute for commit/tree identity.

## Explicit rejection cases

The gate rejects:

- branch-only evidence;
- missing commit or tree;
- NOT_OBSERVABLE evidence;
- local evidence when CI authority is required;
- evidence for a different commit;
- evidence for the same commit with a different tree;
- targets that lack immutable commit/tree identity.

These are negative contracts, not implementation preferences.

## Boundary

The gate answers only:

"Is this already-produced evidence sufficient to verify this exact target?"

It does not answer:

"Did CI actually execute?"

That second question belongs to an execution adapter and its authority-specific evidence source.

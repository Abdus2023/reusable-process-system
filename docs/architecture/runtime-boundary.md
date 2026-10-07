# Runtime Boundary

The runtime is divided into three authorities:

1. **Core planner** — pure lifecycle/state decision logic. It must not acquire repositories, execute external commands, or manufacture evidence.
2. **Adapters** — perform external operations such as GitHub acquisition, repository inspection, and CI observation. Each adapter returns typed evidence or an explicit blocked/not-observable result.
3. **Verification** — evaluates evidence against a contract and returns a scoped decision. Verification never upgrades missing execution evidence into a pass.

Dependency direction:

`core -> contracts`
`adapters -> contracts`
`verification -> contracts`
`profiles -> adapters + contracts`
`GPJK integration -> contracts + GPJK semantics`

Core must not depend on GitHub, Kerno, .agent, or a particular process language.

## Snapshot binding

Repository evidence is valid only when the evidence identifies the repository, ref, commit, and tree snapshot. A mutable branch name alone is insufficient.

## Execution binding

Execution evidence must identify authority, execution kind, status, observed time, exact commit/tree where applicable, and limitations.

## Authority rule

Local inspection may diagnose. CI execution may establish CI execution evidence. Neither authority may silently substitute for the other.

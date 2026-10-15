# ADR-0004: Governed Project Scopes Within a Repository

Status: Proposed
Owner: Catylist
Date: 2026-10-15

## Context

[ADR-001](ADR-001-repository-taxonomy.md) and the
[repository taxonomy](../architecture/repository-taxonomy.md) assign one
primary class to each project-owned repository. The repository's primary class
determines its authority and expected evidence. AES-SEC-001 adoption, AEMS
scanning, and the review-disposition ledger likewise treat the repository root
as the governed unit.

`dlworrell/code-noodling` is classified Experimental by
[ADR-0001](ADR-0001-catalyst-repository-tree.md). It now contains several
independent projects, for example a crypto pipeline, a prime-number suite, dice
simulation, and election analysis. Each has its own build system, tests, and
risk profile. Each needs its own CI. Each needs its own AES-SEC-001 scan,
review-disposition ledger, and waiver log, so that one project's findings,
waivers, or file moves do not churn another project's evidence. Today all of
them share a single repository-wide ledger, and file moves in one project
invalidate path-keyed findings for the whole repository.

GitHub runs workflows only from the repository root's `.github/workflows/`, so
per-project automation needs a defined model. Without one, projects either
accumulate root-level workflows with no recorded ownership, or rely on
undocumented conventions that automation cannot verify.

### Relationship to CAT-003

[CAT-003](../architecture/CAT-003-PSZ-Triangle-and-Recursive-Engineering-State.md)
already models nesting:

- §8 states that a PSZ Triangle may contain, depend on, compose, or govern other
  PSZ Triangles, and lists both "a project" and "a repository" as examples.
- §10 states that repositories are possible Implementations or containers of
  PSZ state and are not the universal architectural center.

CAT-003 therefore already allows a repository PSZ to contain project PSZs.
What it does not define is how a repository declares those child PSZs, who has
decision rights over them, or how standards adoption, automation, and evidence
attach to them. Formal composition operators and closure propagation rules
remain open, non-normative work (CAT-003 §13). This ADR does not define them.

This ADR therefore defines governed project scopes in CAT-003 terms. It adds
only the declaration, authority, and coverage rules that CAT-003 leaves open.

## Decision

### 1. Declaration

A repository MAY declare **governed project scopes**. A governed project scope
is a top-level directory listed in the repository manifest.

A repository that declares no scopes behaves exactly as it does today. The
repository root remains the single governed unit, and no existing repository
needs to change.

Scopes are top-level directories only. Nested scopes, meaning a scope inside a
scope, are not permitted by this ADR and would require a further ADR.

In CAT-003 terms, each scope is a child PSZ of the repository PSZ:

- its manifest entry declares the child boundary;
- its documentation and specifications are its Specification;
- its source and automation logic are its Implementation;
- its tests, CI results, and adoption evidence are its Evidence.

The CAT-003 §8 parent rule applies. The repository is not closed for a claim
merely because each of its scopes is closed for that claim. Parent closure still
requires evidence about the repository-level remainder, the root automation,
and the declared relationships between scopes.

### 2. Required scope declarations

Each scope declares:

| Field | Meaning |
|---|---|
| path | The top-level directory the scope owns |
| owner | The accountable owner of the scope |
| primary class | The scope's class, constrained by the repository's class (see below) |
| lifecycle state | One of the [repository taxonomy](../architecture/repository-taxonomy.md) lifecycle states, applied to the scope |
| governing standards | Each applicable standard, with its scope-local evidence paths, or an explicit not-applicable declaration (rule 8) |

A scope's primary class must not grant authority beyond its repository's
primary class. Scopes in an Experimental repository are experimental, and they
remain excluded from production claims, unless a Catylist ADR reclassifies
them. For an experimental scope, the expected route to a production class is
extraction into its own repository under rule 7, not reclassification in place.

The class and lifecycle vocabularies used for scopes are the same vocabularies
used for repositories. When the canonical vocabularies proposed in
[CAT-REV-001](../reviews/CAT-REV-001-Repository-Role-and-Lifecycle-Taxonomy-Assessment.md)
(`CAT-PL-0002`, `CAT-PL-0004`) are adopted, scopes adopt them too.

### 3. Self-contained scopes

Each scope is self-contained. What it must contain depends on its lifecycle
state:

| Content | `proposed` or `bootstrap` | `active` or later |
|---|---|---|
| `README.md` | REQUIRED | REQUIRED |
| `ci/`, holding the scope's automation logic | REQUIRED | REQUIRED |
| `docs/` | RECOMMENDED | REQUIRED |
| `tests/` | RECOMMENDED | REQUIRED |
| Adoption evidence under `<scope>/docs/engineering/` for each applicable standard | REQUIRED | REQUIRED |

For AES-SEC-001, adoption evidence means the secure-coding profile, the waiver
log, and the review-disposition ledger. Adoption evidence is required from the
moment a standard applies, whatever the scope's lifecycle state.

Scaling the other requirements to lifecycle keeps the overhead of starting an
experimental scope low. That overhead is the reason separate repositories per
project were rejected below.

A scope must not depend on another scope unless the dependency is declared in
the manifest. Declared dependencies must not be cyclic, and they go through the
other scope's documented interfaces rather than its internal files.

### 4. Repository-level obligations

These remain at the repository root and are owned at repository level:

- the repository manifest;
- the root `README.md`, which serves as an index of the scopes;
- `.github/workflows/`, containing thin caller workflows;
- any repository-wide policy or configuration that a governing standard requires
  at the root, such as the analysis configuration that the AEMS reusable
  workflow currently checks for.

A root workflow for a scope only selects triggers and path filters and then
invokes logic that lives in `<scope>/ci/`. It may do that through scripts or
through local composite actions. Build, test, and scan logic lives in the scope.

A root caller workflow that invokes scope-local logic MUST NOT run on
`pull_request_target`, or on any other trigger that has secrets or write tokens
while handling untrusted pull-request code, unless it checks out and executes
only the base-branch version of that logic. See "Security and trust-boundary
impact" below.

### 5. Coverage

Every governed file, as defined under [Terminology](#terminology), belongs to
exactly one scope or to the repository-level remainder. No file may belong to
two scopes, and none may be left out.

- A scope-level scan covers exactly that scope's path.
- A repository-level scan covers the remainder and excludes every declared
  scope.

CAT-003 permits PSZs to overlap or depend on one another in general. For
standards adoption and enforcement, this ADR is deliberately stricter and
requires disjoint, exhaustive coverage. That way every finding has exactly one
responsible ledger.

### 6. Exceptions and waivers

An exception or waiver belongs to the scope that owns the affected
implementation, and it is recorded in that scope's waiver log or ledger. This
applies the existing [governance model](../architecture/governance-model.md)
rule that a decision belongs in the narrowest repository with complete
authority, extended to the narrowest governed unit.

A waiver recorded in one scope never covers files in another scope or in the
repository-level remainder.

### 7. Promotion by extraction

A scope MAY be extracted into its own repository, with its history preserved.
Extraction requires:

- registering the new repository under
  [ADR-0001](ADR-0001-catalyst-repository-tree.md) and the
  [repository taxonomy](../architecture/repository-taxonomy.md), with its own
  primary class;
- moving the scope's adoption evidence with it, re-keyed to the new paths;
- retiring the scope from the source repository's manifest, with a record that
  points to the successor repository (CAT-003 §11 lineage).

### 8. Explicit non-applicability

A standard that does not apply to a scope, such as AES-SEC-001 for a scope with
no C or C++ surface, is declared not applicable in the manifest, together with
the reason. It is never silently skipped.

A not-applicable declaration is reviewable evidence. It must be revisited when
the scope's languages or surfaces change.

## Terminology

A **governed file** is any file within the purview of an applicable standard's
scanner or inspection, after that scanner's documented default exclusions, such
as version-control metadata, build outputs, and declared fixtures. Rule 5
applies to governed files.

Generated artifacts committed by automation, such as published reports, belong
to the scope whose automation generates them, wherever that automation is
triggered from.

"Governed project scope", or "scope" where unambiguous, means a directory-level
governance unit declared by this ADR. It is distinct from the `scope` field of a
closure unit in
[CAT-CON-001](../contracts/CAT-CON-001-Engineering-Closure-Metadata-Contract.md),
which states the boundary of a closure claim. A closure unit may declare a claim
whose scope is a governed project scope, but the two terms are not
interchangeable.

## Illustrative manifest shape (non-normative)

The manifest format is owned by AES (AES-003). The shape below only illustrates
the information this ADR requires. The normative field names and schema are
follow-up work for AES.

```yaml
scopes:
  - path: crypto_pipeline/
    owner: dlworrell
    class: experimental
    lifecycle: active
    standards:
      AES-DEV-001:
        profile: crypto_pipeline/docs/engineering/AES-DEV-001-development-principles.md
      AES-SEC-001:
        profile: crypto_pipeline/docs/engineering/SECURE-C-CXX.md
        waiver_log: crypto_pipeline/docs/engineering/AES-SEC-001-waivers.md
        review_dispositions: crypto_pipeline/docs/engineering/AES-SEC-001-review-dispositions.json
  - path: election-analysis/
    owner: dlworrell
    class: experimental
    lifecycle: active
    standards:
      AES-SEC-001:
        applicability: not-applicable
        reason: Python-only scope with no C or C++ surface.
```

## Alternatives considered

### Separate repositories per project

Every project gets its own repository. This fits the current taxonomy natively:
one repository, one primary class, one governed unit, and no new concepts.

Rejected for an experimental sandbox because of the overhead. Each small
exploratory project would need its own repository registration, manifest,
templates, adoption evidence, and CI before any exploration could start.
Extraction under rule 7 keeps this path available for any scope that matures.

### Status quo: a single repository-wide scope

Keep the repository root as the only governed unit.

Rejected because unrelated projects share one ledger and one waiver log, file
moves in one project invalidate findings repository-wide, and per-project CI
has no recorded ownership. Repositories that need nothing more remain on the
status quo by default (rule 1).

## Consequences

- A repository can host several self-contained projects that each own their
  automation and AES-SEC-001 evidence, without new repositories.
- Repositories that declare no scopes are unaffected.
- Automation needs scope-aware behavior before a repository can rely on scopes.
  Until AEMS supports scoped scanning, a repository that declares scopes keeps
  its current repository-wide scan, and the scope declarations are
  documentation-only.
- Classification remains anchored to the repository. A scope cannot be used to
  give an experimental repository production authority.
- Path-keyed evidence, such as AES-SEC-001 finding identities, must be re-keyed
  when files move into or between scopes. The existing review history is
  preserved, not discarded.

### Security and trust-boundary impact

- The root `.github/workflows/` directory remains a repository-level trust
  boundary. Workflow triggers, permissions, secrets, and runner selection are
  reviewed at repository level, and a scope cannot grant itself broader CI
  permissions.
- A root caller workflow that invokes scope-local logic, whether `<scope>/ci/`
  scripts or local composite actions, MUST NOT run on `pull_request_target`, or
  on any other trigger that has secrets or write tokens while handling untrusted
  pull-request code, unless it checks out and executes only the base-branch
  version of that logic. A local action or script is resolved from the
  checked-out tree, so checking out the pull-request head would run the PR
  author's code with the workflow's elevated permissions and secrets.
- Workflows that grant write permissions or target self-hosted runners must not
  run scope logic from unreviewed forks.
- A scope's waivers cannot weaken obligations outside that scope (rule 6).

### Recovery and migration impact

- Adoption is incremental: one scope per change, with the remainder unchanged
  until each move is complete.
- Every migration must preserve file history, for example by using `git mv`,
  and must carry review dispositions forward under their new paths.
- If scoped governance is withdrawn, removing a scope's manifest entry returns
  its files to the repository-level remainder. That remainder then needs one
  consolidated ledger again.

## Follow-up work in owning repositories

This ADR records program governance only. It contains no enforcement code. The
following work belongs to the owning repositories and is listed, not
implemented, here:

- **AES**
  - Confirm or adjust the AES-SEC-001 adoption wording, which currently binds
    obligations to "each repository" (local profile, waivers), so that a
    declared scope can satisfy them.
  - Add the `scopes` declaration, and the not-applicable form, to the AES-003
    repository manifest standard and its field reference.
- **AEMS**
  - Scoped scanning: a scan root per scope, exclusion of declared scopes from
    repository-level scans, per-scope profile, waiver, and ledger paths, and
    annotation paths reported relative to the repository root.
  - Ledger re-keying for moved files, since finding identities include the path.
  - Enforcement of the coverage rule.
  - Scope-aware handling of the root analysis-configuration check in the
    distributed governance workflow.
- **repo_templates**: a project-scope template providing `README.md`, `docs/`,
  `tests/`, `ci/`, `docs/engineering/` adoption files, and a root caller
  workflow example.
- **P0**: scope-aware inspection and readiness assessment, so readiness is
  reported per scope and for the repository-level remainder.
- **code-noodling**: add a manifest with declared scopes, then migrate one scope
  per pull request. Each migration moves the scope's files under one top-level
  directory. Today election analysis spans `election_reporting/`,
  `election-data/`, `reports/`, and `tests/`, and dice simulation sits inside
  `prime-number-suite/`. Each migration also adds the scope's `ci/` and root
  caller workflow, and splits and re-keys its AES-SEC-001 evidence. Dice
  simulation's optional prime-seed input, a primes JSON file, is a data
  dependency on the prime-number-suite scope and must be declared in the
  manifest under rule 3.

## Affected repositories

- `dlworrell/Catylist`
- `dlworrell/AES`
- `dlworrell/AEMS`
- `dlworrell/repo_templates`
- `dlworrell/P0`
- `dlworrell/code-noodling`

## Related documents

- [ADR-0001 — Catalyst Repository Tree](ADR-0001-catalyst-repository-tree.md)
- [ADR-001 — Repository Taxonomy](ADR-001-repository-taxonomy.md)
- [ADR-002 — Standards Hierarchy](ADR-002-standards-hierarchy.md)
- [ADR-003 — Authority Chain](ADR-003-authority-chain.md)
- [CAT-003 — PSZ Triangle and Recursive Engineering State](../architecture/CAT-003-PSZ-Triangle-and-Recursive-Engineering-State.md)
- [CAT-CON-001 — Engineering Closure Metadata Contract](../contracts/CAT-CON-001-Engineering-Closure-Metadata-Contract.md)
- [Repository taxonomy](../architecture/repository-taxonomy.md)
- [Governance model](../architecture/governance-model.md)
- [ADR-0005 — Agent Instruction Files](ADR-0005-agent-instruction-files.md)

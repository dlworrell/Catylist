# CAT-DISP-002 — Classification of Previously Unclassified Repositories

Status: Approved disposition
Owner: Catylist
Date: 2026-10-16
Applies to: `dlworrell/openCUDA`, `dlworrell/Rocket_demo`,
`dlworrell/audiblebooks`, `dlworrell/rea`,
`dlworrell/pythonista-tools-installer`
Originating issue: `dlworrell/Catylist#16`

## Context

The [repository inventory](../../inventory/repositories.json) introduced by
[ADR-0006](../adr/ADR-0006-default-branch-protection-and-signed-commits.md)
recorded five repositories as `unclassified`, because no Catylist record
classified them. Under ADR-0006 an unclassified repository has
`default_branch_policy: pending-classification` and stays out of scope until
Catylist records its classification.

## Decision

The maintainer, as repository owner, has stated:

- `openCUDA`, `Rocket_demo` and `audiblebooks` are the maintainer's own work and
  belong under Catylist management;
- `rea` and `pythonista-tools-installer` are external.

Catylist therefore records:

| Repository | Ownership | Class | Default-branch policy |
|---|---|---|---|
| `dlworrell/openCUDA` | project-owned | experimental | protected |
| `dlworrell/Rocket_demo` | project-owned | experimental | protected |
| `dlworrell/audiblebooks` | project-owned | experimental | protected |
| `dlworrell/rea` | external-reference | external-reference | excluded |
| `dlworrell/pythonista-tools-installer` | external-reference | external-reference | excluded |

### Why `experimental`

No Catylist record yet describes the architecture, product boundary, or
stability of the three project-owned repositories. The
[repository taxonomy](../architecture/repository-taxonomy.md) defines
`experimental` as exploratory work that is not yet stable architecture or
product behavior. That is the most conservative class: it grants no authority
beyond the repository itself and claims no production readiness.

A repository can later be reclassified, for example to `governed-product`, by
a project-specific disposition such as
[CAT-DISP-001](CAT-DISP-001-EVO-repository-classification.md). The inventory
changes in the same change series.

### External references

`rea` and `pythonista-tools-installer` are forks of upstream projects. As
external references, they are not rewritten to satisfy Catalyst governance
([ADR-0001](../adr/ADR-0001-catalyst-repository-tree.md),
[ADR-001](../adr/ADR-001-repository-taxonomy.md)), and ADR-0006 does not apply to
them.

## Consequences

- The three project-owned repositories enter ADR-0006 scope. Rulesets are
  applied to each one only after its P0 remediation (`dlworrell/Catylist#27`),
  following the ADR-0006 rollout ratchet.
- Each project-owned repository is expected to adopt an `aes-manifest.yaml`
  that names Catylist as its governance authority and cites this disposition,
  as P0 remediation and the inventory desired-state work
  (`dlworrell/Catylist#18`) define.
- `audiblebooks` is private. Repository rulesets on private repositories in a
  personal account require a paid GitHub plan, which the account has.
- No inventory entry remains `unclassified`.

## Authority

This disposition records repository ownership and class only. It does not
transfer standards authority from AES or enforcement authority from AEMS, and it
grants no waiver.

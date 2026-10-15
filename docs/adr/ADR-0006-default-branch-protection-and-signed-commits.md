# ADR-0006: Default-Branch Protection and Signed Commits

Status: Proposed
Owner: Catylist
Date: 2026-10-15

## Context

Catalyst depends on repository history as evidence. CAT-003 §11 requires that
superseded state remain addressable. [ADR-0004](ADR-0004-governed-project-scopes.md)
requires history to be preserved when files move between scopes or out of a
repository. AES-SEC-001 review dispositions and other evidence are keyed to
committed content.

None of these properties is currently protected by the hosting platform.
Default branches in Catalyst repositories can be:

- force-pushed, which rewrites history;
- deleted;
- updated by squash or rebase merges, which replace the reviewed commits with
  new ones.

They also accept unsigned commits. A review of recent activity on 2026-10-15
found the following:

| Commits | Authored by | Signed |
|---|---|---|
| Agent-authored commits in `Catylist` and `code-noodling` | AI coding agent | Yes; GitHub reports `verified: true` |
| GitHub-created merge commits | GitHub | Yes; GitHub reports `verified: true` |
| Direct pushes to `code-noodling` `main` from a mobile Git client | Maintainer | No; GitHub reports `reason: unsigned` |
| Election-report commits | `github-actions[bot]` | No; pushed directly to `main` by the Election Result Reports workflow |

The program intends to move to signed commits for all work on default
branches, whoever or whatever authors it.

Repository identity and ownership are recorded in
[ADR-0001](ADR-0001-catalyst-repository-tree.md), the
[ecosystem architecture](../architecture/catalyst-ecosystem.md), and the
[CAT-REV-001 inventory census](../reviews/CAT-REV-001-Repository-Inventory-and-Identity-Census.md).
All of these are prose. Automation that applies policy across repositories
needs one machine-readable source, a gap the census itself records
(`CAT-PL-0005`, `CAT-ID-002`).

## Decision

### 1. Scope

This decision applies to every repository recorded in the
[repository inventory](../../inventory/repositories.json) with ownership
`project-owned` or `organizational`. Those repositories have
`default_branch_policy: protected`.

The following are outside this decision:

- **External-reference repositories** (`default_branch_policy: excluded`). They
  are not rewritten to satisfy Catalyst governance (ADR-0001, ADR-001).
- **Unclassified repositories** (`default_branch_policy:
  pending-classification`). Each of these enters scope once Catylist records
  its classification.

### 2. Default-branch rules

On the default branch of every in-scope repository:

1. **No deletion.** The default branch cannot be deleted.
2. **No history rewriting.** Non-fast-forward updates, such as force pushes,
   are rejected.
3. **Changes arrive by pull request.** Direct pushes are rejected. No approving
   review is required while the program has a single maintainer. That
   threshold is revisited when a second maintainer joins.
4. **Merge commits only.** Squash and rebase merges are disabled, so the
   reviewed commits, their authorship, and their signatures reach the default
   branch unchanged. Linear-history enforcement is therefore not used, because
   it conflicts with merge commits.
5. **Signed commits.** Every commit that lands on the default branch must be
   reported as verified by GitHub. This applies equally to maintainers,
   AI coding agents, and automation.
6. **No bypass.** No user, team, or application is exempt from these rules.

Repository merge settings match rule 4: merge commits are allowed, and squash
and rebase merging are disallowed.

Head branches are deleted automatically when their pull request merges. Merged
work stays addressable through the merge commit and the pull request, so the
branch is no longer needed. Deleting it also makes GitHub retarget any pull
request stacked on it to the base branch. Without that, a stacked pull request
merges into the stale branch instead of the default branch, as Catylist #13 did
on 2026-10-15.

### 3. Release tags

Tags matching `v*` cannot be deleted, moved, or force-updated once created.

### 4. Required status checks

Required status checks are per repository and are not part of this baseline.
A check name that does not match a real job blocks every merge. Each
repository's checks are therefore proposed from its latest successful default
branch run, and enabled separately once their names are confirmed. The same applies to code scanning
requirements: the sandbox test showed that requiring code scanning results in a
repository where code scanning is not configured blocks every merge, including
fully signed ones.

### 5. Automation and signing

- Automation must not push to a default branch. Workflows that produce commits
  open a pull request instead.
- Commits that automation produces must themselves be verified. For example,
  commits created through the GitHub API with the workflow token are signed by
  GitHub, whereas a plain `git push` from a runner is unsigned.
- AI coding agents sign their commits with a platform-managed key and keep their
  co-authorship trailer, so that agent and maintainer contributions remain
  distinguishable.
- Maintainers configure commit signing in every Git client they use to commit,
  including mobile clients, and register the corresponding signing key on
  GitHub.

### 6. The inventory is authoritative

[`inventory/repositories.json`](../../inventory/repositories.json) is the
authoritative machine-readable list of Catalyst repositories, their ownership,
their Catylist class, and the evidence for each classification.

- Each `default_branch_policy` value is derived from ownership by rule 1, and
  `scripts/validate_repository.py` rejects any entry that contradicts this.
- Automation that applies repository policy reads the inventory at a pinned
  revision rather than parsing prose documents.
- The `class` values follow the CAT-REV-001 census vocabulary, plus
  `experimental` from the [repository taxonomy](../architecture/repository-taxonomy.md),
  plus `unclassified`. When the canonical vocabulary (`CAT-PL-0002`) is
  adopted, the inventory migrates to it.
- Adding, reclassifying, or removing a repository changes this file in the same
  change series as the decision that justifies it.

### 7. Existing history

These rules apply to new changes. Existing unsigned commits are not rewritten,
because rewriting them would violate rule 2 and the history-preservation
obligations above.

## Authority and implementation

Work flows in the authority order of [ADR-003](ADR-003-authority-chain.md),
followed by templating and remediation:

```text
Catylist -> AES -> AEMS -> repo_templates
                     |
                     +--> P0 remediates existing repositories and brings them
                          under Catylist management
```

| Order | Concern | Owner |
|---|---|---|
| 1 | This decision, its scope, and the inventory | Catylist |
| 2 | The engineering obligations (signed commits, no history rewriting, pull-request-only default branches) | AES, recorded in AES-DEV-001 check-in discipline |
| 3 | Applying rulesets and merge settings, and reporting drift | AEMS |
| 4 | Ruleset definitions, merge-setting documentation, and scaffolding for new repositories | `repo_templates` |
| 5 | Remediating each existing repository (workflows that push to default branches, unsigned automation, manifests) so it can be brought under these rules | P0 |
| — | Each repository's required status checks, and the implementation work that supports Catylist management | The owning repository |

Rulesets are applied by AEMS automation using a credential scoped to repository
administration. Neither Catylist nor AEMS gains authority over repository
contents from this decision.

## Alternatives considered

### Classic branch protection

Per-branch protection settings, configured individually in each repository.
Rejected in favor of repository rulesets. Rulesets can be defined once as
versioned JSON, applied identically by automation, and can target the default
branch and tags regardless of their names.

### Allow squash merges

Squash merges are signed by GitHub and keep the default branch simple.
Rejected because they replace the reviewed commits, along with their individual
authorship and signatures, with a single new commit. That loses the distinction
between agent and maintainer work and weakens the history ADR-0004 relies on.

### An administrator bypass

Rejected as a standing exception. When an urgent change cannot wait, the
[decision process](../architecture/decision-process.md) emergency path applies.
Temporarily relaxing a ruleset is an audited administrative action, and it must
be recorded and reversed afterwards.

### Signatures optional, history protection only

Rejected. The program intends all default-branch work to be attributable to a
verified key, and protecting history alone does not establish who produced it.

## Consequences

- Default-branch history in every in-scope repository becomes append-only and
  attributable.
- The maintainer's current practice of pushing directly to `main` from a mobile
  Git client stops working. Work moves to branches and pull requests with signed
  commits.
- Workflows that commit to default branches must be changed before their
  repository is protected. The `code-noodling` Election Result Reports workflow
  is one known example.
- Automation that opens pull requests with unsigned commits will produce pull
  requests that cannot be merged until it signs its commits. The P0
  project-zero remediation workflow in `repo_templates` is one known example.
- Merges proceed only through pull requests, so the existing CI on pull requests
  becomes the gate for every change.

### Security and trust-boundary impact

- The credential that applies rulesets has repository-administration rights. It
  is stored only as an AEMS Actions secret, limited to the in-scope repositories,
  and used only by a manually dispatched workflow.
- Requiring verified signatures makes a stolen push credential insufficient to
  land commits without also holding a registered signing key.
- Agent signing keys are managed by the agent platform. They are never stored in
  repositories, setup scripts, or plain environment configuration.

### Recovery and migration impact

Rollout follows the [standards lifecycle](../architecture/standards-lifecycle.md)
ratchet:

1. Report current settings and drift without changing anything.
2. Validate each ruleset version in the `ruleset-sandbox` repository first. A
   2026-10-15 test there confirmed that the baseline blocks an unsigned commit,
   squash and rebase merges, direct pushes, and force pushes, while a fully
   signed agent pull request merges with a GitHub-signed merge commit.
3. Apply the rules to one repository (`code-noodling`) once P0 remediation for
   it is complete, and confirm that an agent-authored pull request still merges
   with a merge commit.
4. Apply the rules to the remaining in-scope repositories, each after its P0
   remediation.

If signing cannot be met in a repository, every rule except signed commits may
be applied first. The exception is recorded as a waiver in that repository with
an expiry date.

Rulesets can be disabled by an administrator if they block urgent recovery.
Doing so is recorded under the emergency path and reversed afterwards.

## Follow-up work in owning repositories

Listed in the order above. Each item is tracked in the Catylist issue tracker
under [#14](https://github.com/dlworrell/Catylist/issues/14).

1. **Catylist**: classify the repositories marked `unclassified` in the
   inventory, so they enter or leave scope deliberately ([#16](https://github.com/dlworrell/Catylist/issues/16)).
2. **AES**: record the obligations in AES-DEV-001 check-in discipline: signed
   commits on default branches, no history rewriting, pull-request-only
   changes, and merge-commit-only integration ([#20](https://github.com/dlworrell/Catylist/issues/20)).
3. **AEMS**:
   - a manually dispatched workflow that reads this inventory at a pinned
     revision and applies the rulesets and merge settings, with a dry-run
     drift report ([#22](https://github.com/dlworrell/Catylist/issues/22));
   - later, a scheduled read-only drift audit ([#23](https://github.com/dlworrell/Catylist/issues/23)).
4. **repo_templates**: add `rulesets/protect-default-branch.json` and
   `rulesets/protect-release-tags.json`, document the matching merge settings,
   and propose required status checks per repository ([#25](https://github.com/dlworrell/Catylist/issues/25)).
5. **P0**: remediate existing repositories before each one is protected
   ([#27](https://github.com/dlworrell/Catylist/issues/27)):
   - change the project-zero remediation workflow so that it produces signed
     commits;
   - move workflows that push to default branches onto pull requests or
     API-created verified commits. The `code-noodling` Election Result
     Reports workflow is the first known case.
6. **Maintainer**: enable commit signing in every Git client used to commit,
   including mobile, and register the signing key on GitHub as a signing key
   ([#29](https://github.com/dlworrell/Catylist/issues/29)).

## Affected repositories

Every repository in the inventory with `default_branch_policy: protected`, plus
`dlworrell/AES`, `dlworrell/AEMS`, `dlworrell/repo_templates`, and
`dlworrell/P0` for the follow-up work.

## Related documents

- [ADR-0001 — Catalyst Repository Tree](ADR-0001-catalyst-repository-tree.md)
- [ADR-002 — Standards Hierarchy](ADR-002-standards-hierarchy.md)
- [ADR-003 — Authority Chain](ADR-003-authority-chain.md)
- [ADR-0004 — Governed Project Scopes](ADR-0004-governed-project-scopes.md)
- [CAT-003 — PSZ Triangle and Recursive Engineering State](../architecture/CAT-003-PSZ-Triangle-and-Recursive-Engineering-State.md)
- [CAT-REV-001 — Repository Inventory and Identity Census](../reviews/CAT-REV-001-Repository-Inventory-and-Identity-Census.md)
- [Repository inventory](../../inventory/repositories.json)

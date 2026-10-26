# ADR-0000: Catylist Code of Conduct (Ring 0)

Status: Accepted
Owner: Catylist
Date: 2026-10-26
Decision authority: Donovan Worrell
Ring: 0
Code version: 1.0.0
Applies to: every repository whose ownership is `project-owned` or
`organizational` in the [repository inventory](../../inventory/repositories.json),
and every contributor to them, human or automated
Builds on: [ADR-000](ADR-000-governance-authority.md),
[ADR-003](ADR-003-authority-chain.md),
[ADR-0004](ADR-0004-governed-project-scopes.md),
[ADR-0005](ADR-0005-agent-instruction-files.md),
[ADR-0006](ADR-0006-default-branch-protection-and-signed-commits.md),
[ADR-0007](ADR-0007-governed-check-in-and-shared-automation.md)

## Context

The program's rules are spread across many records. Catylist ADRs set program
policy, AES sets engineering standards, AEMS enforces them, and each project
keeps its own decisions, some in an ADR log and some nowhere. Of the 17
governed repositories at the time of this decision:

- 9 keep an ADR log, in four different locations (`docs/adr/`, `adr/`,
  `docs/architecture/`, and a governed scope's `docs/engineering/`);
- 8 keep none.

Nothing states, in one place, which rules bind everyone, in what order rules
win when they conflict, or that people and AI agents are bound the same way.
A new contributor, or an agent starting a session, has to reconstruct this
from several ADRs. Pull requests rarely say which decision they implement,
even though they are the public record of what the program intends and how
mature it is.

## Decision

### 1. Adopt the Catylist Code of Conduct as ring 0

The [Catylist Code of Conduct](../../CODE_OF_CONDUCT.md), version 1.0.0, is
adopted. It ranks above every other document in the program, including the
other Catylist ADRs. Its precedence order is:

1. the Code;
2. Catylist ADRs and program governance;
3. AES standards;
4. a repository's own ADRs;
5. any other documentation, configuration or code comment.

### 2. Every governed repository adopts it as its own ADR-0000

Each governed repository records the adoption as `ADR-0000` in its ADR log,
using the standard text in the [appendix](#appendix-standard-local-adr-0000).
A repository without an ADR log creates one. The number `ADR-0000` is
reserved for this purpose in every repository.

A local ADR-0000 is never renumbered, amended or superseded locally. Its only
change is the "Code version" line, updated by the amendment process in
section 5.

### 3. Conflicting ADRs move down

When an existing ADR conflicts with the Code or occupies the number
`ADR-0000`, that ADR moves down to make room:

- **Numbering:** an existing record numbered `ADR-0000` is renumbered to the
  next free number, and every reference to it is updated in the same pull
  request.
- **Content:** an ADR whose decision conflicts with the Code is amended or
  marked superseded in part, with a link to the law it conflicts with.

At the date of this decision, no governed repository has a record numbered
`ADR-0000`, so no renumbering is needed.

Catylist's own [ADR-000](ADR-000-governance-authority.md) (three digits) is a
different record. It establishes Catylist as the program-governance authority,
which is consistent with the Code, and keeps its number because the validator
and other records cite it. ADR-0000 ranks above it.

### 4. Pull requests and conformance

Every pull request in a governed repository names the ADR it implements or
changes, or states `ADR: n/a` with a reason (Code, Law 1). There are no exempt
pull requests. Automated pull requests cite a standing ADR for their class of
change.

Conformance with the Code is mandatory. A conformance check becomes a
**required status check** in every governed repository's ruleset. This
records the decision authority's explicit choice to require this check. It
replaces, for this check only, ADR-0006's deferral of required status checks.

The check reaches required status by the route
[ADR-0007](ADR-0007-governed-check-in-and-shared-automation.md) already sets
for any blocking rule:

1. **AES** adopts the normative rules for local ADR logs (location, template,
   front matter, what needs an ADR, and the waiver format).
2. **AEMS** implements the check. It cites the AES rule and this ADR for every
   finding, and it fails closed on `violation` and `indeterminate`.
3. The check runs in report-only mode on `ruleset-sandbox`, then on each
   repository as it adopts ADR-0000.
4. Once the check passes in a repository, the check is added to that
   repository's ruleset as required.

### 5. Amendment

The Code changes only through a Catylist ADR accepted by the decision
authority. Each change gets a new semantic version, is trialled on
`ruleset-sandbox` first, and reaches each repository as a pull request that
updates the "Code version" line of its ADR-0000.

## Authority and implementation

| Owner | Responsibility |
|---|---|
| Catylist | The Code, this ADR, and the inventory of governed repositories |
| AES | The normative rules for local ADR logs, PR ADR references and waivers |
| AEMS | The conformance check and its required-check rollout |
| `repo_templates` | The local ADR-0000 file, an ADR template, a `CODE_OF_CONDUCT.md` pointer, the pull request template's `ADR:` field, and agent instruction file pointers (ADR-0005) |
| P0 | Adopting ADR-0000 in each existing repository, including any renumbering |
| Each governed repository | Its ADR log, its ADR-0000, and its own decisions below ring 0 |

Agent instruction files point to the Code rather than restating it, as
ADR-0005 requires.

## Alternatives considered

- **Keep the rules spread across existing ADRs.** Rejected: contributors and
  agents have to reassemble the rules, and nothing states precedence.
- **Put the Code in AES.** Rejected: binding people and agents across the
  program is program governance, which ADR-000 assigns to Catylist. AES still
  owns the engineering rules that implement it.
- **Require ADRs only for pull requests that touch flagged areas.** Rejected
  by the decision authority: every pull request is part of the program's
  public record, and a rule with exemptions is easier to get around.
- **Make conformance advisory.** Rejected by the decision authority: an
  advisory check does not bind anyone.
- **Renumber Catylist's ADR-000 to make room.** Rejected: its content does not
  conflict with the Code, and renaming it would break the validator and
  existing citations. Precedence, not the file name, makes ADR-0000 ring 0.

## Consequences

- Every governed repository gains an ADR log and an ADR-0000.
- Every pull request, including small fixes, carries an `ADR:` line. This adds
  a little friction to every change.
- Dependency-update bots cannot write an `ADR:` line, so each repository needs
  a standing ADR for routine updates, and the check must recognise it.
- Until the conformance check is required in a repository, Laws 1, 2 and 6 are
  upheld there by review only.
- With one maintainer, review is self-review (ADR-0007 §2.6). The Code does
  not change that.
- Law 8 cannot be checked by machine. It is upheld by review and by reports.
- The owner can still relax a ruleset. Under Law 5 and ADR-0006 that is an
  audited emergency action, recorded and reversed.

## Follow-up work in owning repositories

1. **AES:** a standard for local ADR logs, PR ADR references and waivers, from
   which the conformance check's rules are cited.
2. **AEMS:** the conformance check, its report-only trial on
   `ruleset-sandbox`, and the per-repository change that makes it required.
3. **`repo_templates`:** the local ADR-0000, the ADR template,
   `CODE_OF_CONDUCT.md`, the pull request template's `ADR:` field, and agent
   instruction file pointers.
4. **P0 and each governed repository:** one adoption pull request per
   repository, following [ADR-0007 §5.3](ADR-0007-governed-check-in-and-shared-automation.md)
   rollout and recovery.
5. **Owner:** optionally, create a `dlworrell/.github` repository holding a
   default `CODE_OF_CONDUCT.md` that points to this Code. GitHub then shows it
   for every repository without its own file.

## Affected repositories

The 17 governed repositories in the inventory at this decision:

| Class | Repositories |
|---|---|
| Authority | Catylist, AES |
| Control plane | AEMS, P0, `repo_templates` |
| Shared service | `engineering-docs-toolkit`, EWT |
| Governed product | evo, atarix, `herkules-1934-english`, JAG, MayaUSD2017Bridge |
| Experimental | `code-noodling`, openCUDA, Rocket_demo, audiblebooks |
| Organizational | Just-a-Geek-LLC |

The inventory, not this table, determines scope. A repository classified as
`project-owned` or `organizational` later is bound from that point.

## Related documents

- [Catylist Code of Conduct](../../CODE_OF_CONDUCT.md)
- [Decision process](../architecture/decision-process.md)
- [Governance model](../architecture/governance-model.md)
- [Repository inventory](../../inventory/repositories.json)

## Appendix: standard local ADR-0000

Each governed repository adds this file as `ADR-0000-catylist-code-of-conduct.md`
in its ADR log. Fill in the adoption date and the Catylist commit the links
are pinned to, and change nothing else.

```markdown
# ADR-0000: Catylist Code of Conduct (Ring 0)

Status: Accepted
Ring: 0
Code version: 1.0.0
Adopted: YYYY-MM-DD
Authority: Catylist ADR-0000
Code: https://github.com/dlworrell/Catylist/blob/<commit>/CODE_OF_CONDUCT.md
Decision: https://github.com/dlworrell/Catylist/blob/<commit>/docs/adr/ADR-0000-catylist-code-of-conduct.md

## Decision

This repository is bound by the Catylist Code of Conduct at the version above.
The Code ranks above every other record and document in this repository.
Everyone and everything that works on this repository, people, bots and AI
agents alike, is bound by it.

This record is ring 0. It is never renumbered, amended or superseded here. Any
ADR in this repository that conflicts with the Code moves down: it is amended,
superseded or renumbered to make room. Only the "Code version" line changes,
through a pull request that follows a Catylist amendment.

## Consequences

- Every pull request names the ADR it implements or changes, or states
  `ADR: n/a` with a reason.
- Conformance with the Code is a required check on this repository.
- Don't be a dick.
```

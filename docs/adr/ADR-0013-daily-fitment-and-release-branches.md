# ADR-0013: Daily, Fitment and Release Branches

Status: Accepted
Owner: Catylist
Date: 2026-10-26
Decision authority: Donovan Worrell
Extends: [ADR-0006](ADR-0006-default-branch-protection-and-signed-commits.md)
(rules beyond the default branch)
Builds on: [ADR-0000](ADR-0000-catylist-code-of-conduct.md),
[ADR-0007](ADR-0007-governed-check-in-and-shared-automation.md),
[ADR-0010](ADR-0010-ring-0-input-gate-and-trust.md),
[ADR-0012](ADR-0012-ring-0-opens-verified-automation-pull-requests.md)

## Context

ADR-0006 protects only the default branch. Contributors have no shared place
to check in daily fixes, nothing gives agents a stable place to document and
test promoted work before release, and no path sends a problem back to the
person whose change caused it. Repositories release by tagging `main` ad hoc.

The decision authority asked for three things: a daily merge scope for bug
fixes and current issues; a space where daily work is promoted and AEMS's
agents run their documentation and test cycles to check it for fitment; and
a way for the people who checked code in to fix the problems found. Then a
first release.

## Decision

### 1. Branches

| Branch | Purpose | Arrives by |
|---|---|---|
| Topic branches: `fix/<issue>-<slug>`, `feat/<slug>`, `docs/<slug>` and the other prefixes of the AEMS Git workflow prompt | One change, by one author | Cut from `dev-daily` |
| **`dev-daily`** | The daily merge scope: bug fixes and current issues | Pull request from a topic branch |
| **`fitment`** | Promoted daily work, held while AEMS's agents document and test it | Pull request whose head is `dev-daily` |
| **`main`** (default) | Released work only | Pull request whose head is `fitment` |
| `automation/*` | Workflow-generated output (ADR-0012) | Workflows; once a repository adopts this ADR they target `dev-daily` |

`dev-daily` and `fitment` get the same six rules as the default branch
(ADR-0006 §2) through the ruleset `protect-integration-branches`: no deletion,
no force push, pull requests only, merge commits only, signed commits, no
bypass. Because neither branch can be deleted, merging a promotion never
removes it.

### 2. The daily cycle

- Contributors and agents cut topic branches from `dev-daily`, check in at
  least daily, and open pull requests into `dev-daily`. CI and ring-0 run on
  each one.
- Once a day, when `dev-daily` holds work that `fitment` does not and its CI
  is green, AEMS opens the promotion pull request `dev-daily` → `fitment`.
  The owner merges it.

### 3. The fitment cycle

When `fitment` moves, AEMS reviews the commits it has not reviewed yet:

1. **Tests:** the repository's own CI runs on the `fitment` head. Every check
   on that commit must pass.
2. **Agents:** the AEMS fitment reviewer reads the changed files and judges
   documentation (is the change described where readers will look) and tests
   (is the changed behaviour exercised, including refusal and edge cases). It
   treats code as data and never runs it. Each finding has a file, a kind
   (`documentation`, `test` or `defect`), a severity (`blocker`, `major` or
   `minor`) and a remedy.
3. **Findings go to their authors:** each finding becomes an issue labelled
   `fitment` and its severity, assigned to the person who last changed that
   file on `fitment` (named in the body if GitHub cannot assign them), and
   linked to the reviewed commit. The same finding is not filed twice while
   an issue for it is open.
4. **The `fitment` check** on the `fitment` head fails while any test check
   fails, while a `blocker` or `major` fitment issue is open, or while the
   review could not run. `minor` findings do not block.

### 4. Fixing what fitment finds

- The author fixes the issue on `fix/<issue>-<slug>` into `dev-daily`, with
  `Fixes #<issue>` in the fix commit's message.
- When that commit reaches `fitment`, AEMS closes the issue with a link to the
  commit, and the next review covers the fix itself.
- Anyone may take an issue whose author is unavailable; the owner reassigns it.

### 5. Release

- When the `fitment` check passes, AEMS opens the release candidate pull
  request `fitment` → `main`. The owner merges it.
- The repository's release workflow, dispatched with a version, builds and
  tests `main`, then **parks** at the `release` environment until the owner
  approves. Only then does it create the `v<version>` tag (immutable under
  ADR-0006 §3) and the GitHub release.
- A repository's first release through this cycle is `v0.1.0`.

### 6. Source rules

The check `fitment/source` fails a pull request into `fitment` whose head is
not `dev-daily`, and a pull request into `main` whose head is not `fitment`.
An urgent fix takes the same path, promoted immediately. There is no
exception branch.

### 7. Identity and permissions

The cycle runs centrally in AEMS every 30 minutes as the `catylist-ring-0` App,
with its existing permissions (ADR-0010 §4). It opens promotion pull requests,
files and closes `fitment` issues and posts the `fitment` and `fitment/source`
checks. It never approves, merges, pushes or runs repository code, and the
model key stays only in AEMS. A repository joins the cycle through AEMS
`config/fitment.json`.

### 8. Rollout

1. `ruleset-sandbox` first: create `dev-daily` and `fitment` from `main`,
   apply the ruleset, run a full cycle with a planted documentation gap and a
   planted untested change, and release `v0.1.0`.
2. Each governed repository then adopts it in its ADR-0000 adoption pull
   request. `fitment` and `fitment/source` become required checks on `main`
   only after the repository's first clean cycle (ADR-0006 §4).

## Alternatives considered

- **Trunk only (topic branches into `main`, release by tag).** Rejected: it
  gives agents no stable place to review promoted work, and a finding would
  arrive after the code was already in the release line.
- **Per-person daily branches (`dev/<login>/*`).** Not needed: topic branches
  already give each author a place to check in daily, and `dev-daily` is
  where their work meets.
- **Release branches (`release/<version>`).** Deferred: with one maintainer,
  `fitment` already holds the candidate. Revisit when releases need to be
  supported in parallel.
- **Run the agents in each repository's own workflow.** Rejected: every
  repository would need the model key.

## Consequences

- Work reaches `main` only after it has passed CI on `dev-daily`, CI on
  `fitment` and an agent review, and after its blocking findings are fixed by
  their authors.
- The release line moves in reviewed batches, and every release is a tagged,
  owner-approved build.
- Contributors branch from `dev-daily`, not `main`, and AEMS's Git workflow
  prompt and `dev-setup.sh` say so.
- A finding can be wrong. Its author says so on the issue, and the owner
  closes it as not planned; the review is evidence, not a verdict.

## Related documents

- [ADR-0006: Default-Branch Protection and Signed Commits](ADR-0006-default-branch-protection-and-signed-commits.md)
- [ADR-0012: Ring 0 Opens Verified Automation Pull Requests](ADR-0012-ring-0-opens-verified-automation-pull-requests.md)
- AEMS `scripts/fitment_cycle.py`, `prompts/fitment-reviewer.md` and
  `config/fitment.json`
- repo_templates `rulesets/protect-integration-branches.json` and
  `templates/workflows/release.yml`

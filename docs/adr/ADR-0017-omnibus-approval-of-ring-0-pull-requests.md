# ADR-0017: Omnibus Approval of Ring 0 Pull Requests

Status: Proposed
Owner: Catylist
Date: 2026-10-29
Decision authority: Donovan Worrell
Amends: [Catylist Code of Conduct](../../CODE_OF_CONDUCT.md) 1.1.0 → 1.2.0
(Law 4, through Law 7);
[ADR-0016](ADR-0016-owner-approved-omnibus-merges.md) rule 3 (last bullet)
and rule 5
Builds on: [ADR-0000](ADR-0000-catylist-code-of-conduct.md),
[ADR-0006](ADR-0006-default-branch-protection-and-signed-commits.md),
[ADR-0012](ADR-0012-ring-0-opens-verified-automation-pull-requests.md),
[ADR-0013](ADR-0013-daily-fitment-and-release-branches.md)

## Context

ADR-0013 has `catylist-ring-0` open a promotion pull request
(`dev-daily` → `fitment`) and later a release candidate (`fitment` → `main`)
in every repository in the fitment cycle. ADR-0012 also has it open
automation pull requests for verified workflow output. On 29 October that was
16 open pull requests across 14 repositories after one cycle, each needing the
owner to open it and press merge, usually from a phone.

ADR-0016 lets the owner approve a batch of pull requests with one omnibus
merge, but its rule 5 refuses pull requests that ring-0 authored, because
Law 4 says an agent may not "approve or merge its own work". So the pull
requests that recur most often are the ones the omnibus cannot carry.

The work in these pull requests is not ring-0's. A promotion or release
candidate carries commits that people and agents already merged into
`dev-daily` through reviewed pull requests; an automation pull request carries
a GitHub-verified workflow commit (ADR-0012). ring-0 only opened the pull
request. What Law 4 protects is that no agent decides on its own that its work
lands. An omnibus keeps that decision with the owner.

## Decision

1. **Law 4 gains one narrow exception (Code 1.2.0).** `catylist-ring-0` may
   merge a pull request it opened when the owner has approved that exact head
   commit through an omnibus. The owner's approval is the decision; the merge
   only carries it out. No other agent, and no other route, gains this.
2. **Only three classes qualify.** The executor accepts a ring-0-authored
   entry only when it is one of:
   - a **promotion**: base `fitment`, head branch `dev-daily` in the same
     repository;
   - a **release candidate**: base `main` (the default branch), head branch
     `fitment` in the same repository;
   - an **automation pull request**: head branch under `automation/` that
     ring-0 opened under ADR-0012.

   Any other ring-0-authored pull request is refused, as before.
3. **The usual gates still apply, on the approved commit.** Every check
   ADR-0016 rule 3 lists still applies: open, not a draft, on the listed base,
   at the approved head, mergeable, every check passed and nothing blocked by
   the rulesets. For a promotion and a release candidate that includes
   `fitment/source`. For a release candidate it also includes the `fitment`
   check, so a candidate with an open blocker or major finding cannot land.
4. **Releases are still the owner's alone (Law 5).** Merging a release
   candidate puts work on `main`; it publishes nothing. Tags and GitHub
   releases are created only after the owner approves the `release`
   environment, as ADR-0013 §5 requires.
5. **ADR-0016 rule 5 is replaced** by this decision, and the last bullet of
   its rule 3 ("was not authored by `catylist-ring-0[bot]`") now reads "was
   not authored by `catylist-ring-0[bot]`, unless it is in a class
   ADR-0017 allows". Every other ADR-0016 rule stands: immutable manifests,
   approval only by a listed approver's verified merge into AEMS `dev-daily`,
   merge at the approved commit, stop at the first refusal, and the ledger.
6. **Everything ring-0 merges this way is marked.** Its merge comment and the
   ledger record the class and the omnibus that approved it, so a self-opened
   pull request merged by ring-0 is always traceable to the owner's approval.

## Rollout (Law 7)

1. **AEMS** changes the omnibus executor to accept the three classes, with
   tests for each class and for refusals: an unlisted class, a promotion whose
   head is not `dev-daily`, a release candidate whose `fitment` check fails,
   and a moved head. The executor runs from AEMS `main`, so the change takes
   effect after its own promotion and release.
2. **Trial on `ruleset-sandbox`.** One omnibus lists a ring-0-authored pull
   request there and is merged; a second lists one that must be refused. Both
   results are recorded in the ledger.
3. **Each governed repository** receives a pull request that updates the
   "Code version" line of its ADR-0000 to 1.2.0. These are approved together
   as one omnibus.

Until step 1 is released, ring-0-authored pull requests are still refused and
the owner merges them by hand.

## Alternatives considered

- **Keep merging ring-0 pull requests by hand.** Safe, but it is the largest
  recurring cost of ADR-0013: one action per repository per cycle.
- **A second App that merges ring-0's pull requests.** Satisfies the letter of
  Law 4 while defeating its purpose, and adds an App and a key.
- **Let ring-0 merge promotions without an omnibus once checks pass.** Removes
  the owner from the decision. Rejected: the owner approves every landing.
- **Allow every ring-0-authored pull request in an omnibus.** Broader than
  needed. Limiting it to the three classes keeps anything new ring-0 might
  open in the future under the old rule until an ADR says otherwise.

## Consequences

- A whole cycle's promotions, release candidates and automation pull requests
  can be approved with one omnibus merge.
- Law 4's "approve or merge its own work" now has one stated exception. The
  approval half is unchanged: no agent approves anything.
- A push to `dev-daily` or `fitment` after approval moves the head of the
  open promotion or candidate, so that entry is refused and the run stops
  there. The next omnibus picks it up.
- Each governed repository needs one more ADR-0000 pull request for the Code
  version line.

## Related documents

- [Catylist Code of Conduct](../../CODE_OF_CONDUCT.md), version 1.2.0
- [ADR-0016: Owner-Approved Omnibus Merges](ADR-0016-owner-approved-omnibus-merges.md)
- AEMS `scripts/omnibus_merge.py` and `docs/engineering/omnibus-merge.md`

# ADR-0016: Owner-Approved Omnibus Merges

Status: Accepted
Owner: Catylist
Date: 2026-10-29
Decision authority: Donovan Worrell
Amends: [ADR-0012](ADR-0012-ring-0-opens-verified-automation-pull-requests.md)
rule 3 (ring-0 never merges)
Builds on: [ADR-0000](ADR-0000-catylist-code-of-conduct.md),
[ADR-0006](ADR-0006-default-branch-protection-and-signed-commits.md),
[ADR-0010](ADR-0010-ring-0-input-gate-and-trust.md),
[ADR-0013](ADR-0013-daily-fitment-and-release-branches.md)

## Context

Rolling ADR-0000 and ADR-0013 out to every governed repository produces about
50 pull requests: a few per repository, in an order that matters (rulesets
before branch models, branch models before workflows). Each one waits for the
owner to open it, check it, and press merge, often from a phone. The checks
already decide whether a pull request is sound; what the owner adds is the
decision that it should land, and in what order.

The `catylist-ring-0` App already opens pull requests (ADR-0012) and holds
Pull requests write on every repository it is installed on. ADR-0012 rule 3
says it never merges.

## Decision

1. **The owner approves a batch with one pull request.** An *omnibus* pull
   request adds one manifest, `omnibus/<id>.json`, to AEMS. The manifest lists
   pull requests in merge order. Each entry names the repository, the pull
   request number, its base branch and the exact head commit being approved.
   The omnibus pull request body repeats the list.
2. **Merging the omnibus is the approval.** It counts only when the omnibus
   pull request was merged by an approver listed in AEMS
   `config/omnibus.json`, into an approval branch listed there (AEMS's
   `dev-daily`), its merge commit is verified as signed, and it changed
   nothing but manifests, so a manifest cannot ride along in an unrelated
   change. That merge is the owner's explicit approval of every listed pull
   request at its listed commit, recorded in a pull request (Code, Law 4).
3. **ring-0 then merges the listed pull requests, in order,** by merge commit
   and with the approved commit as the expected head, so GitHub refuses the
   merge if the head has moved. Before each merge it confirms that the pull
   request:
   - is open, not a draft, and targets the listed base;
   - still has the approved head commit;
   - is mergeable with every check on that commit passed (Law 6), and nothing
     else blocks it under the branch's rulesets; and
   - was not authored by `catylist-ring-0[bot]` (rule 5).

   It stops at the first pull request that fails and reports which one and
   why. It does not retry, update branches, or skip ahead.
4. **Every merge is recorded.** ring-0 comments on each merged pull request
   with a link to the omnibus pull request and the approver, and on the
   omnibus pull request with the result of every entry. Results are kept in
   AEMS's `ring0/ledger` branch at `omnibus/<id>.json`.
5. **ring-0 never merges its own work.** Pull requests it authored, such as
   fitment promotions and automation pull requests, are refused even when
   listed; the owner merges those directly. This keeps Law 4 intact without
   amending the Code.
6. **Manifests are immutable once approved.** Changing the list needs a new
   omnibus pull request with a new id. A manifest edited after its approval is
   refused. Re-running a manifest merges only entries that are still open at
   their approved commit; entries already merged at that commit are reported
   as done.
7. **No new bypass and no new key.** ring-0 merges through the same rulesets
   as everyone else: required checks, signed history (GitHub signs the merge
   commits it creates) and merge commits only (ADR-0006). The App needs
   Contents write and Pull requests write in the target repositories; the
   private key stays only in AEMS's `ring-0` environment. Releases are still
   cut by the owner (Law 5); an omnibus never publishes one.

## Alternatives considered

- **Keep merging every pull request by hand.** Safe but slow, and the order is
  easy to get wrong across 17 repositories.
- **GitHub auto-merge on each pull request.** Still needs one action per pull
  request, has no cross-repository order, and merges whatever the head is when
  checks pass rather than the commit the owner looked at.
- **Let ring-0 merge its own pull requests too.** Would cover fitment
  promotions, but conflicts with Law 4. It would need a Code amendment under
  Law 7, not this ADR.
- **A separate merge App.** Keeps duties apart but adds an App and a key, as
  ADR-0012 also concluded.

## Consequences

- A batch of pull requests lands after one owner action, in a stated order,
  and only at the commits the owner approved. A push after approval removes
  that pull request from the batch and stops the run there.
- ring-0 now merges pull requests. The decision stays with the owner: it acts
  only on an approver's signed merge of a manifest, never on its own judgement.
- A failed entry leaves later entries open. The owner fixes the cause, then
  approves the remainder with a new omnibus.
- The merge executor runs from AEMS's default branch, so its code has passed
  fitment before it holds merge power. Omnibus merges therefore start only
  after this ADR's implementation has been released to AEMS `main`.

## Related documents

- AEMS `scripts/omnibus_merge.py`, `config/omnibus.json` and
  `docs/engineering/omnibus-merge.md`
- [ADR-0012: Ring 0 Opens Verified Automation Pull Requests](ADR-0012-ring-0-opens-verified-automation-pull-requests.md)

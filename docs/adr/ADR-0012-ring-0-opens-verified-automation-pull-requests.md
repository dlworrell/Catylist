# ADR-0012: Ring 0 Opens Verified Automation Pull Requests

Status: Accepted
Owner: Catylist
Date: 2026-10-26
Decision authority: Donovan Worrell
Amends: [ADR-0010](ADR-0010-ring-0-input-gate-and-trust.md) §4 (what the
`catylist-ring-0` App does)
Builds on: [ADR-0000](ADR-0000-catylist-code-of-conduct.md),
[ADR-0006](ADR-0006-default-branch-protection-and-signed-commits.md),
[ADR-0007](ADR-0007-governed-check-in-and-shared-automation.md)

## Context

Some workflows publish generated reports through GitHub-signed commits on a
workflow-owned `automation/` branch, then open a pull request. GitHub refuses
that last step when the repository setting "Allow GitHub Actions to create
and approve pull requests" is off, even though the workflow token has
`pull-requests: write`. Turning the setting on also lets workflows approve
pull requests, which conflicts with the Code's Law 4.

The `catylist-ring-0` App already holds Pull requests write in every
repository it is installed on. Under ADR-0010 it only checks and reports.

## Decision

1. **ring-0 may open the pull request** for an `automation/` branch that is
   listed for that repository in AEMS `config/ring0.json`
   (`automation_publishing`). Nothing else is opened.
2. **It opens one only for verified workflow output:** the branch is exactly
   one commit ahead of the default branch; that commit was created and signed
   by GitHub (committer `web-flow`, verified, reason `valid`); its author is a
   workflow bot listed for the branch; it changes only the listed paths; and
   no pull request for the branch is open. Anything else is recorded in the
   ledger as a violation and reported in Catylist; nothing is opened.
3. **It never approves, merges or edits** these pull requests, and it pushes
   nothing. The pull request body names this ADR, the commit, and the owner
   who reviews and merges. Its required checks and the owner's approval apply
   as for any other pull request.
4. **No new access.** It uses the App's existing permissions. The private key
   stays only in AEMS; repositories do not hold it, and their workflows may
   drop `pull-requests: write`.

## Alternatives considered

- **Turn the repository setting on.** Rejected: it also lets workflows
  approve pull requests.
- **A separate publisher App per repository.** Workable and keeps duties
  apart, but adds an App and a key to manage. The owner chose to widen
  ring-0's tasking instead, with the limits above.
- **Put the ring-0 key in each repository.** Rejected: any workflow there
  could then mint a token that writes ring-0's check results.

## Consequences

- Generated-report pull requests open within one sweep interval (30 minutes)
  of the workflow run, authored by `catylist-ring-0[bot]`.
- ring-0 now opens pull requests it may later check. It authors none of their
  content, its checks stay deterministic, and the owner still merges, so it
  never passes its own work.
- A branch that does not meet rule 2 stays unopened and is reported, so a
  tampered or unsigned branch never reaches review through ring-0.

## Related documents

- [ADR-0010: Ring 0 Input Gate and Trust](ADR-0010-ring-0-input-gate-and-trust.md)
- AEMS `scripts/ring0_sweep.py` and `config/ring0.json`

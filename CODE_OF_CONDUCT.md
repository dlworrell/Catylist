# Catylist Code of Conduct

Version: 1.2.0
Status: Accepted
Adopted by: [ADR-0000](docs/adr/ADR-0000-catylist-code-of-conduct.md); amended by [ADR-0010](docs/adr/ADR-0010-ring-0-input-gate-and-trust.md) and [ADR-0017](docs/adr/ADR-0017-omnibus-approval-of-ring-0-pull-requests.md)
Decision authority: Donovan Worrell
Date: 2026-10-29

This Code is the ring 0 rule for the Catalyst program. It binds every
Catylist-governed repository and everyone and everything that works on them.
It is short on purpose. Each law names how it is enforced, so it is always
clear which laws a machine enforces and which depend on review.

## Who and what is bound

- **Governed repositories:** every repository whose ownership is
  `project-owned` or `organizational` in the
  [repository inventory](inventory/repositories.json). A repository enters
  scope as soon as Catylist classifies it that way. External-reference
  repositories are other people's projects and are not bound.
- **Contributors:** every person, bot, workflow and AI agent that proposes,
  reviews, merges or automates a change to a governed repository.

## The laws

The laws are in order of precedence. A lower law never overrides a higher one.
Law 8 applies throughout, and no other law justifies breaking it.

### Law 0: Ring 0 supremacy

This Code ranks above every other document in the program. When two rules
conflict, the higher one wins:

1. this Code;
2. Catylist ADRs and program governance;
3. AES standards;
4. a repository's own ADRs;
5. any other documentation, configuration or code comment.

Every governed repository adopts this Code as its own **ADR-0000**. That
number is reserved for this purpose in every repository. ADR-0000 is never
renumbered, amended or superseded locally. When an existing ADR conflicts with
it, that ADR moves down: it is amended, superseded or renumbered to make room.
Ring 0 never moves.

### Law 1: Recorded decisions

Every governed repository keeps an ADR log, and its first record is ADR-0000.

Every pull request names the ADR or ADRs it implements or changes, or states
`ADR: n/a` with a reason. No pull request is exempt, because pull requests
show the public our intent and our maturity.

A change to any of the following needs an ADR that is Accepted before the
change merges, or in the same pull request:

- architecture or module boundaries;
- a security or trust boundary;
- a public interface or file format;
- dependencies, including adding, removing or replacing one;
- the handling of data, credentials or personal information;
- licensing;
- governance, including this Code, rulesets and enforcing workflows.

Automated pull requests, such as dependency updates, satisfy this law by
citing a standing ADR that covers their class of change.

### Law 2: Conform upward

A repository's ADRs may not contradict a higher authority, and each one names
the authority it implements. An exception exists only as a waiver ADR that
records its owner, its reason and an expiry date. An expired waiver is a
conformance failure.

### Law 3: Integrity of history

Default branches change only through pull requests, by merge commit, with
signed commits. History is never rewritten. Nobody, human or automation, has
a standing bypass. The detailed rules are in
[ADR-0006](docs/adr/ADR-0006-default-branch-protection-and-signed-commits.md).

### Law 4: Humans and agents alike

Every law binds people, bots and AI agents equally.

Before changing a repository, an agent reads this Code, the repository's ADR
log and its agent instruction file. An agent may author changes. It may not:

- approve or merge its own work. One exception: `catylist-ring-0` may merge
  a promotion, release candidate or automation pull request it opened once
  the owner has approved that exact commit in an omnibus
  ([ADR-0017](docs/adr/ADR-0017-omnibus-approval-of-ring-0-pull-requests.md));
- grant a licence or sign as a human;
- change governance files (this Code, ADRs, rulesets or enforcing workflows)
  without the owner's explicit approval, recorded in the pull request.

AI-authored work is attributed as such.

Every contributor, person, bot or agent, is **untrusted until trust is
verified** and recorded by the maintainer in Catylist's trusted-contributor
list. Trust never exempts anyone from the required checks; it only affects how
an inconclusive result on a conversation post is handled (Law 6).

### Law 5: Secrets and irreversible actions

Never commit, print or log a secret, private key or token.

Destructive or irreversible actions need the owner's explicit approval each
time. These include deleting anything, rewriting history, relaxing a ruleset
and publishing a release.

### Law 6: Evidence, not assertion

Required checks must pass on the exact commit being merged. Conformance with
this Code is a required check in every governed repository.

**Every input is checked.** That covers pushes, pull requests, reviews,
comments, issues, discussions, wiki edits, tags and releases, from every
contributor, at least every 30 minutes, and every result is recorded in an
append-only ledger:

- Code waits in its pull request until it conforms; nothing reaches a default
  branch before then.
- A conversation post that fails is hidden, which can be undone, and
  reported. An untrusted contributor's post is also hidden while its result is
  inconclusive, and shown again once it passes.
- A wiki edit that fails is reported, and the maintainer reverts it.

Nobody skips, disables or weakens a test or check to get a green result. A
claim of compliance cites its evidence, and a failure is reported as a
failure.

### Law 7: Amendment

This Code changes only through a Catylist ADR accepted by the decision
authority. Each change gets a new version number, is trialled on
`ruleset-sandbox` first, and reaches each repository as a reviewable pull
request that updates its ADR-0000. It never changes silently. A repository
may propose a change by opening an issue in Catylist; it may not amend the
Code locally.

### Law 8: Wheaton's Law

> Don't be a dick.
>
> — Wil Wheaton

Treat everyone who works on or uses these projects with respect, whether they
are a person or an agent. This applies to code, reviews, issues, commit
messages and anything an agent writes. No other law justifies breaking this
one.

## Enforcement

| Law | Enforced by |
|---|---|
| 0 | The repository inventory and the conformance check (ADR-0000 present and pinned to the current Code version) |
| 1 | The conformance check: the ADR log exists, and every pull request names an ADR or gives a reason that the AI enforcer accepts |
| 2 | The conformance check (citations and waiver expiry dates) and review |
| 3 | Repository rulesets (ADR-0006) |
| 4 | Rulesets, agent instruction files (ADR-0005), the conformance check for changes to governance files, the trusted-contributor list, and the omnibus executor's class and approval checks (ADR-0017) |
| 5 | Secret scanning, push protection and review |
| 6 | Required status checks, the ring 0 input sweep (ADR-0010) and its ledger, and review |
| 7 | A pinned conformance workflow, updated only by reviewable pull requests |
| 8 | The AEMS AI enforcer (organizational psychologist prompt), review, and reports to the maintainer |

Laws 3 and 6 are enforced by the hosting platform. No instruction file can
enforce anything on its own; it only tells contributors what the checks
expect.

## Raising a concern

Open an issue in [Catylist](https://github.com/dlworrell/Catylist/issues), or
contact the maintainer privately through their GitHub profile if the concern
is about a person. Reports are handled under Law 8, and nobody is penalised
for raising one in good faith.

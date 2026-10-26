# ADR-0010: Ring 0 Input Gate and Trust

Status: Accepted
Owner: Catylist
Date: 2026-10-26
Decision authority: Donovan Worrell
Amends: [Catylist Code of Conduct](../../CODE_OF_CONDUCT.md) 1.0.0 → 1.1.0
(Law 7)
Builds on: [ADR-0000](ADR-0000-catylist-code-of-conduct.md),
[ADR-0006](ADR-0006-default-branch-protection-and-signed-commits.md),
[ADR-0007](ADR-0007-governed-check-in-and-shared-automation.md)

## Context

[ADR-0000](ADR-0000-catylist-code-of-conduct.md) made conformance with the
Code a required check on pull requests. Pull requests are only one way content
enters a repository. Issues, comments, reviews, discussions, wiki pages, tags
and releases also carry the program's public voice, and none of them passes
through a pull request check.

The decision authority requires that every input method be checked, that
content be held until it conforms where the platform allows it, and that this
apply to every contributor until their trust is verified.

GitHub constrains how this can work:

- Code can be held: a pull request cannot merge until its required checks
  pass.
- Conversation cannot be held. GitHub publishes an issue, comment, review or
  discussion post as soon as it is submitted. The nearest equivalent is to
  check it promptly and hide it if it fails. Hiding ("minimizing") can be
  undone.
- Wiki edits are published immediately, and a GitHub App cannot edit a wiki.
  A failing wiki edit can only be reported and reverted by the maintainer.
- A scheduled workflow can run as often as every few minutes, but GitHub may
  start it late under load.

## Decision

### 1. Every input is checked

| Input | How it is gated | Held until it conforms? |
|---|---|---|
| Pushes to a default branch | Rulesets: pull request only, signed, no bypass (ADR-0006) | Yes |
| Pull requests: opened, new commits, edited | Required checks `ring-0` (deterministic) and `ring-0/conduct` (AI enforcer) | Yes: no merge until both pass |
| Pull requests from bots and agents | The same required checks | Yes |
| Pushes to other branches | Recorded by the sweep; checked for secrets and signatures | Cannot reach a default branch without a pull request |
| Tags and releases | `v*` tag protection (ADR-0006); releases need owner approval (Code, Law 5); recorded by the sweep | Yes |
| Issues, issue and pull request comments, reviews, review comments, commit comments, discussions and discussion comments | The sweep checks every new or edited post and hides one that fails | Hidden within one sweep interval |
| Wiki edits | The sweep checks every changed page and reports one that fails | Reported; the maintainer reverts |
| Repository settings and rulesets | The sweep compares them with the inventory and reports drift | Reported |

### 2. The sweep

AEMS runs a central sweep **every 30 minutes** across every governed
repository, in the same structure as its existing ecosystem scans. Because
GitHub can start scheduled runs late, the guarantee is "at least every 30
minutes, as scheduled", not an exact interval.

For every new or edited input since the previous sweep, it:

1. runs the deterministic checks and the AI enforcer
   (`prompts/organizational-psychologist-code-enforcer.md` in AEMS);
2. appends one record to an append-only ledger in AEMS: repository, input
   type, link, author, trust tier, timestamps, a SHA-256 hash of the content
   (never the content itself, so a pasted secret is not copied), the verdict
   and the findings;
3. acts on the verdict:
   - on a pull request, it posts the `ring-0/conduct` check on the head
     commit;
   - on a failing conversation post, it hides the post and opens or updates
     one violation issue in Catylist citing the law;
   - on a failing wiki edit, it opens or updates a violation issue for the
     maintainer to revert;
   - it never deletes anything (Code, Law 5).

An edit to a post that has already passed is checked again.

### 3. Untrusted until verified

Every contributor, including the maintainer, bots and AI agents, is untrusted
until the maintainer records them in Catylist's **trusted-contributor list**.

- Trust never exempts anyone from the required checks.
- For an untrusted contributor, a conversation post with an `indeterminate`
  result is hidden until it passes. For a trusted contributor, it stays
  visible and goes to the maintainer.
- A `violation` is hidden for everyone.

**The list's location is not yet decided.** It must be readable by the AEMS
sweep and writable only by the maintainer. A GitHub Actions secret in
Catylist cannot be read by a workflow in AEMS, so the choice is between an
AEMS secret and a maintainer-only file. Until the list exists, it is empty and
**every contributor is untrusted**.

### 4. Identity and permissions

The sweep acts as the GitHub App **`catylist-ring-0`** (App ID `5474337`),
owned by the maintainer and installed only on the governed repositories and
`ruleset-sandbox`. It requests no webhooks.

| Permission | Level |
|---|---|
| Checks, Commit statuses | Read and write |
| Issues, Pull requests, Discussions | Read and write |
| Contents, Metadata | Read-only |
| Administration, Actions, Workflows, Secrets, and everything else | No access |

- The App cannot push, merge or change settings or rulesets. Its actions never
  count as the maintainer's approval.
- Its private key is held only as the AEMS secret `RING0_APP_PRIVATE_KEY`.
  Each sweep exchanges it for an installation token that expires within an
  hour.
- The AI enforcer's model key is held only as the AEMS secret
  `ANTHROPIC_API_KEY`. Without it, `ring-0/conduct` reports `indeterminate`,
  which fails closed.
- Each governed repository's ruleset requires `ring-0` and `ring-0/conduct`
  from this App only, so no other app or token can satisfy them.

### 5. Wikis and discussions stay on

- **Wikis** hold each repository's software architecture plan and the current
  state of the work. Wiki editing should be restricted to collaborators in
  each repository's settings.
- **Discussions** are where contributors talk to each other and track
  codebase questions for a specific repository.

Both are inputs under section 1.

### 6. Rollout

The sweep runs on `ruleset-sandbox` first (Code, Law 7), with conforming and
failing examples of each input type. It then covers each governed repository
as that repository adopts ADR-0000, and `ring-0` and `ring-0/conduct` become
required in its ruleset.

## Alternatives considered

- **Interaction limits instead of a trusted list** (only prior contributors
  may post). Rejected by the decision authority in favour of an explicit list.
  Interaction limits would also block the discussions this decision keeps.
- **Turn wikis off.** Rejected by the decision authority: wikis carry each
  repository's architecture plan and status.
- **Personal access tokens for posting and hiding.** Rejected: a token acts as
  the maintainer, could approve pull requests, and lets anything holding a
  status token spoof the check. The App avoids all three.
- **Check every 10 minutes.** Not chosen: 30 minutes is the decision
  authority's minimum, and it keeps model costs low.

## Consequences

- A conversation post that fails can be visible for up to one sweep interval
  before it is hidden. GitHub offers no way to hold it.
- A pull request's `ring-0/conduct` result can take up to one sweep interval
  to appear, and the pull request cannot merge until it does.
- Wiki violations depend on the maintainer to revert them.
- Until the trusted-contributor list exists, every inconclusive conversation
  post is hidden until it passes.
- The ledger grows with every input. It stores hashes, not content.
- Model usage is billed to the maintainer. A spend limit on the model key is
  the safeguard against runaway cost.

## Follow-up work

1. **AEMS:** the `ring-0` reusable workflow, the 30-minute sweep acting as
   `catylist-ring-0`, the ledger, and tests; then the `ruleset-sandbox` trial.
2. **AEMS:** add `ring-0` and `ring-0/conduct`, pinned to App ID `5474337`, to
   each governed repository's ruleset as it adopts ADR-0000.
3. **Maintainer:** decide where the trusted-contributor list lives; add the
   `ANTHROPIC_API_KEY` secret to AEMS with a spend limit; restrict wiki
   editing to collaborators in each governed repository.

## Related documents

- [Catylist Code of Conduct](../../CODE_OF_CONDUCT.md), version 1.1.0
- [ADR-0000](ADR-0000-catylist-code-of-conduct.md)
- [Repository inventory](../../inventory/repositories.json)

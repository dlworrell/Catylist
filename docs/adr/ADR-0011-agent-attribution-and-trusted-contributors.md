# ADR-0011: Agent Attribution and Trusted Contributors

Status: Accepted
Owner: Catylist
Date: 2026-10-26
Decision authority: Donovan Worrell
Builds on: [ADR-0000](ADR-0000-catylist-code-of-conduct.md) (Code, Law 4),
[ADR-0010](ADR-0010-ring-0-input-gate-and-trust.md) (section 3, trust)

## Context

The Code requires AI-authored work to be attributed (Law 4), and ADR-0010
makes every contributor untrusted until verified. Two facts make both hard to
enforce:

- **Agents post from the prompting user's account.** A review of the governed
  repositories on 2026-10-26 found that Claude commits under its own GitHub
  identity, `claude`, but ChatGPT and Notion have no separate identity: their
  connectors post as the user who prompted them. Claude's comments and pull
  requests made through connectors also appear as that user.
- **Nothing tells an agent's post from the user's.** A check cannot
  distinguish them, so an agent could post the owner's approval phrase, and a
  reader cannot tell who actually wrote a comment.

ADR-0010 also left open where the trusted-contributor list lives.

## Decision

### 1. Agents post as "<Agent> for @<user>"

An AI agent acting under a person's prompt posts from that person's account,
and starts every post, pull request body, review and comment it writes with a
title line naming itself and the prompting user:

```text
**Claude for @dlworrell**
```

The same form applies to `ChatGPT for @…`, `Notion for @…` and any other
agent. Commits keep their existing attribution (a `Co-Authored-By:` trailer
or the agent's own identity).

ring-0 enforces this under Law 4:

- A title naming a user other than the posting account is a violation.
- Agent-written text without a title line is a violation. Agent-written text
  is recognised by the agent's own markers, such as the Claude Code footer or
  a `Co-Authored-By: Claude` line.
- An agent-written comment never counts as the owner's approval, whatever it
  says.

### 2. The trusted-contributor list is a file in Catylist

The list lives in [`inventory/trusted-contributors.json`](../../inventory/trusted-contributors.json).
Only the maintainer changes it, through a pull request that ring-0 treats as
a governance change. The `catylist-ring-0` App reads it at Catylist's default
branch. This settles the open question in ADR-0010 section 3; the list names
GitHub logins and agent names, which are not secret.

The first entries, verified by the decision authority on 2026-10-26:

| Entry | Kind |
|---|---|
| `dlworrell` (Donovan Worrell) | Person, maintainer |
| `claude` | Agent (also its GitHub login) |
| `chatgpt` | Agent |
| `notion` | Agent |

An agent-titled post is trusted only when the agent and the prompting user
are both listed and the post comes from that user's account. Trust never
exempts anyone from the required checks.

## Alternatives considered

- **Give each agent its own GitHub account or App.** The strongest
  separation, and still the long-term fix. It is not available today for
  ChatGPT and Notion connectors, which act as the user.
- **Keep the list as an AEMS secret.** Logins are not secret, a secret cannot
  be reviewed, and a Catylist secret cannot be read by AEMS workflows.
- **Attribute in a footer instead of a title.** A footer is easy to miss and
  easy to forge further down; a fixed first line is unambiguous for people
  and for the checks.

## Consequences

- Every agent session that posts to a governed repository must start its
  posts with the title line. Agent instruction files (ADR-0005) should say so.
- Existing agent posts without a title are not rewritten; the rule applies to
  new and edited posts.
- A person can still forge an agent title on their own account, or remove it.
  Law 4 forbids both, and the posting account remains accountable.
- ChatGPT and Notion are trusted as agents, but they cannot act independently
  of a listed person: their posts are trusted only from that person's
  account.

## Follow-up work

1. **AEMS:** read `inventory/trusted-contributors.json` in the ring-0 sweep,
   and check agent titles, in [dlworrell/AEMS#39](https://github.com/dlworrell/AEMS/pull/39).
2. **`repo_templates`:** add the title-line rule to the agent instruction
   file templates.
3. **Agents:** use the title line from now on.

## Related documents

- [Catylist Code of Conduct](../../CODE_OF_CONDUCT.md)
- [ADR-0005: Agent Instruction Files](ADR-0005-agent-instruction-files.md)
- [ADR-0010: Ring 0 Input Gate and Trust](ADR-0010-ring-0-input-gate-and-trust.md)

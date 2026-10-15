# ADR-0005: Agent Instruction Files

Status: Accepted
Owner: Catylist
Date: 2026-10-15

## Context

AI coding agents read repository-local instruction files, such as `CLAUDE.md`
and a `.claude/` settings directory, to learn how to work in a repository.
Catalyst repositories have started to use these agents for governed work,
including AES-SEC-001 review-disposition updates and CI changes.

No Catalyst repository currently defines what these files may contain, where
their canonical form lives, or how they relate to authoritative policy. Without
a convention, instruction files tend to restate rules from AES, AEMS, and local
ADRs in condensed form. They then drift from the authoritative text and become a
second, unreviewed source of policy that agents follow in preference to the real
one. That would contradict the
[governance model](../architecture/governance-model.md) rule that automation may
report and enforce declared policy but may not invent policy, and the
[ADR-002](ADR-002-standards-hierarchy.md) rejection of automation-defined policy.

Instruction and settings files are also committed configuration. A machine path,
token, or credential placed in them is published with the repository.

## Decision

### 1. Scaffolding, with the template in repo_templates

Agent instruction files are repository scaffolding. Their canonical template is
owned by `dlworrell/repo_templates`, consistent with its authority over
reusable repository structure (see the
[repository taxonomy](../architecture/repository-taxonomy.md)).

Adopting them is optional. A repository that has no agent instruction files is
fully conformant.

### 2. Permitted files

A repository MAY contain:

- `CLAUDE.md` at the repository root;
- at most a minimal `.claude/` directory holding shared, committed agent tool
  settings, such as a permissions allowlist for routine read-only and build
  commands.

Per-user or machine-local agent settings, such as `.claude/settings.local.json`,
must not be committed.

### 3. Pointers, not policy

Agent instruction files are not authoritative policy. They point to the
authoritative documents and do not restate them. Those documents are:

- Catylist governance and ADRs, for program structure and authority;
- AES standards, for engineering obligations;
- AEMS, for enforcement mechanics;
- the repository's own manifest, local profiles, ADRs, and documentation.

An instruction file may contain navigation and working context that is not
policy. Examples are where things live, how to build and test, which documents
to read before which kinds of change, and repository-specific conventions that
are already recorded elsewhere.

When an instruction file conflicts with an authoritative document, the
authoritative document wins. The conflict is a defect in the instruction file
and must be corrected there.

Agent tool settings, such as permission allowlists, configure what an agent may
run without prompting. They do not change what governance requires. Settings
must not be used to waive, skip, or redefine a governing standard's obligations.

### 4. Scoped repositories

A repository that declares governed project scopes
([ADR-0004](ADR-0004-governed-project-scopes.md)) MAY add `<scope>/CLAUDE.md`
for scope-local context, under the same pointers-not-restatement rule. A scope's
instruction file may point to the scope's own profiles, ledgers, and ADRs. It
must not contradict repository-level instructions or governance.

### 5. No secrets or machine-specific content

Agent instruction and settings files must not contain secrets, credentials,
tokens, private endpoints, or machine-specific absolute paths. They are subject
to the same secret-handling obligations as any other committed file.

## Alternatives considered

### Instruction files as a policy summary

Let `CLAUDE.md` summarize the rules agents must follow. This is convenient for
agents, but it creates a second, drifting policy source that is not reviewed
under the standards lifecycle. Rejected.

### No convention

Leave each repository to decide. This produces inconsistent files with no
canonical template and no rule against restating or contradicting policy.
Rejected.

### Policy authority in AES or AEMS

Make agent instructions an AES standard or an AEMS-generated artifact. AES owns
engineering obligations, not repository scaffolding. AEMS must implement policy,
not author agent-facing policy text. Rejected, although AEMS MAY later check
these files against the rules in this ADR.

## Consequences

- Agents are directed to authoritative documents, so updating policy in its
  owning repository updates what agents follow, with no second copy to keep in
  sync.
- Instruction files stay short and low-maintenance.
- Repositories without agent files are unaffected.

### Security and trust-boundary impact

Instruction files influence what automated agents do inside a repository, so
changes to them are reviewed like other repository configuration. Committed
agent settings must not broaden an agent's permissions beyond what the
repository's governance allows, and must never carry secrets (rule 5).

### Recovery and migration impact

Existing instruction files that restate policy should be reduced to pointers
when next touched. No repository is required to add instruction files.

## Follow-up work in owning repositories

- **repo_templates**: add canonical `CLAUDE.md` and minimal `.claude/` templates
  that follow this ADR, plus a scope-level `CLAUDE.md` variant for ADR-0004
  scopes. Ensure `.claude/settings.local.json` is ignored by version control.
- **AEMS** (optional, later): a check that agent instruction files contain no
  secrets or absolute machine paths and that their links resolve.

## Affected repositories

- `dlworrell/Catylist`
- `dlworrell/repo_templates`
- `dlworrell/AEMS`
- every Catalyst project-owned repository that chooses to add agent instruction
  files

## Related documents

- [ADR-002 — Standards Hierarchy](ADR-002-standards-hierarchy.md)
- [ADR-003 — Authority Chain](ADR-003-authority-chain.md)
- [ADR-0004 — Governed Project Scopes](ADR-0004-governed-project-scopes.md)
- [Governance model](../architecture/governance-model.md)

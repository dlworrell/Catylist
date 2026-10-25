# Catylist Architecture Decision Records

Status: Active
Owner: Catylist
Repository: `dlworrell/Catylist`

## Purpose

This directory records program-governance decisions for the Catalyst umbrella and managing organization.

Catylist ADRs are for decisions that affect Catalyst-wide structure, repository ownership, governance boundaries, program policy, or cross-repository coordination.

## Scope

Use Catylist ADRs for decisions such as:

- defining or changing the Catalyst repository tree;
- classifying repositories as Catalyst project-owned, external/reference, or third-party mirrors/forks;
- establishing cross-repository governance boundaries;
- changing program-level documentation authority;
- adopting or retiring project-management conventions;
- resolving ambiguity between Catalyst, AES, AEMS, Atarix, EDT, and repo template responsibilities.

Do not use Catylist ADRs for:

- engineering standards owned by `dlworrell/AES`;
- enforcement implementation details owned by `dlworrell/AEMS`;
- Atarix OS or target-hardware integration decisions owned by `dlworrell/atarix`;
- template implementation details owned by `dlworrell/repo_templates`;
- EDT implementation details owned by `dlworrell/engineering-docs-toolkit`;
- external/reference repository internals.

## Format

ADR files should use a stable numeric prefix and a short descriptive slug:

```text
ADR-0001-short-title.md
ADR-0002-short-title.md
```

Each ADR should record:

- status;
- context;
- decision;
- consequences;
- affected repositories;
- related standards or reports.

## Current Index

| ADR | Title | Status | Date |
|---|---|---|---|
| [ADR-000](ADR-000-governance-authority.md) | Establish Catylist as the Program-Governance Authority | Accepted | 2026-07-12 |
| [ADR-0001](ADR-0001-catalyst-repository-tree.md) | Catalyst Repository Tree | Accepted | 2026-07-06 |
| [ADR-001](ADR-001-repository-taxonomy.md) | Adopt an Explicit Catalyst Repository Taxonomy | Accepted | 2026-07-12 |
| [ADR-002](ADR-002-standards-hierarchy.md) | Separate Governance, Standards, and Enforcement Authority | Accepted | 2026-07-12 |
| [ADR-003](ADR-003-authority-chain.md) | Catalyst Authority Chain | Accepted | 2026-07-12 |
| [ADR-0004](ADR-0004-governed-project-scopes.md) | Governed Project Scopes Within a Repository | Accepted | 2026-10-15 |
| [ADR-0005](ADR-0005-agent-instruction-files.md) | Agent Instruction Files | Accepted | 2026-10-15 |
| [ADR-0006](ADR-0006-default-branch-protection-and-signed-commits.md) | Default-Branch Protection and Signed Commits | Accepted | 2026-10-15 |
| [ADR-0007](ADR-0007-governed-check-in-and-shared-automation.md) | Governed Check-In and Shared Automation | Accepted | 2026-10-25 |

| [ADR-0009](ADR-0009-codeql-assisted-security-review.md) | CodeQL-assisted Security Review and Evidence-Based Gate Promotion | Proposed | 2026-10-25 |

ADR-0008 is historical proposal lineage superseded within ADR-0007; the distinct CodeQL proposal uses ADR-0009 without reusing that identity.

This index previously stated that no Catylist ADRs had been adopted, even
though the ADRs listed above had already been accepted. The table above
replaces that stale statement.

### Historical numbering

The existing ADRs do not follow the four-digit format above consistently:

- `ADR-000` uses three digits;
- `ADR-001`, `ADR-002`, and `ADR-003` use three digits;
- `ADR-0001` uses four digits, so `ADR-0001` and `ADR-001` are different
  records with the same numeric value.

These files are preserved under their original names as lineage. Other
documents reference them by path, including:

- this repository's `scripts/validate_repository.py`, which requires
  `ADR-000` through `ADR-002`;
- AES's `aes-manifest.yaml` and AES-BLD-001, which cite
  `docs/adr/ADR-003-authority-chain.md`;
- AEMS ownership-inventory reports, which cite
  `docs/adr/ADR-0001-catalyst-repository-tree.md`.

Renaming them would break those references.

New ADRs use the four-digit format and take the next number that collides with
neither naming form. The first such number is `ADR-0004`. Always cite ADRs by
their full file name or link, because a bare number such as "ADR-001" is
ambiguous between `ADR-001` and `ADR-0001`.

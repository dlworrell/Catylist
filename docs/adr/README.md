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

No Catylist ADRs have been adopted yet.

The first expected ADR should record the Catalyst repository tree and repository ownership classifications.

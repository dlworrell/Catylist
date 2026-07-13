# ADR-003: Catalyst Authority Chain

Status: Accepted
Date: 2026-07-12
Owner: Catylist

## Context

Catalyst uses separate repositories for program governance, engineering standards, project management and compliance enforcement, and implementation work. Earlier transitional documents sometimes assigned overlapping responsibilities to AEMS, AES, Atarix, or Just-a-Geek-LLC.

That ambiguity creates circular ownership, duplicated policy, and uncertainty about where authoritative changes belong.

## Decision

The Catalyst authority chain is:

```text
Catylist
    defines program governance, repository relationships, and authority boundaries

        ↓

AES
    defines engineering obligations, standards, and required evidence

        ↓

AEMS
    manages the Catalyst project, evaluates repositories, and verifies/enforces AES

        ↓

Project repositories
    implement systems and maintain project-specific specifications, ADRs, and evidence
```

The responsibilities are therefore:

- **Catylist** owns what the Catalyst program is and how its repositories relate.
- **AES** owns how engineering must be performed across the program.
- **AEMS** owns project-management automation, assessment, reporting, evidence packaging, and enforcement of AES requirements.
- **Project repositories** own their implementation and project-specific architecture, specifications, ADRs, tests, and operational evidence.
- **Just-a-Geek-LLC** owns company and public-facing organizational material, not Catalyst engineering governance.

## Dependency Direction

The intended policy dependency direction is:

```text
Catylist → AES → AEMS → governed repositories
```

Implementation repositories may consume AEMS tooling and reference AES and Catylist documents. AEMS may read Catylist and AES metadata, but it must not redefine their authority. AES may reference Catylist governance, but it must not take ownership of program governance.

## Consequences

- New governance policy belongs in Catylist.
- New engineering requirements belong in AES.
- New compliance scanners, reports, and project-management automation belong in AEMS.
- Project-specific design remains local to the relevant implementation repository.
- Transitional documents that conflict with this chain must be marked superseded, migrated, or rewritten.
- Circular policy dependencies are prohibited.

## Alternatives Considered

### AEMS owns standards and enforcement

Rejected. Combining engineering authority and enforcement weakens separation of concerns and makes it difficult to distinguish policy from implementation.

### AES owns program governance

Rejected. Engineering standards are subordinate to program governance and should not define the repository authority structure that gives AES its mandate.

### Just-a-Geek-LLC owns Catalyst governance

Rejected. The company/public repository has a different purpose and should not be the canonical engineering governance authority.

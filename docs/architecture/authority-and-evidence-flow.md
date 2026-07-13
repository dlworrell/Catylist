# Authority and Evidence Flow

Status: Adopted
Owner: Catylist
Scope: Catalyst program repositories

## Purpose

This document defines the governing direction of authority and evidence across the Catalyst ecosystem.

## Authority Chain

```text
Catylist -> AES -> AEMS -> governed repositories
```

The layers have distinct responsibilities:

- **Catylist** defines program governance, repository authority, taxonomy, lifecycle, and cross-repository relationships.
- **AES** defines normative engineering obligations and standards authorized by Catylist.
- **AEMS** implements, measures, reports, and enforces Catylist governance and AES standards.
- **Governed repositories** implement projects and produce evidence of conformance.

## Governing Principle

> Authority flows downward. Evidence flows upward.

Authority flows from Catylist through AES and AEMS to governed repositories. Evidence flows from governed repositories through AEMS to AES and Catylist.

## Dependency Direction

The dependency graph shall remain acyclic:

- Catylist shall not depend on AES or AEMS.
- AES may depend on Catylist governance but shall not depend on AEMS implementation.
- AEMS may depend on Catylist governance and AES standards.
- Governed repositories may consume Catylist, AES, and AEMS contracts.
- Downstream implementation repositories shall not redefine upstream governance or standards.

## Separation of Concerns

### Catylist

Catylist answers: **What is governed, by whom, and under what authority?**

### AES

AES answers: **What engineering obligations apply?**

### AEMS

AEMS answers: **How is compliance detected, measured, evidenced, and enforced?**

### Governed repositories

Project repositories answer: **What is being built, and what evidence proves it meets its obligations?**

## Evidence Flow

AEMS shall collect and normalize evidence such as:

- architecture and specification records;
- ADRs;
- test and verification results;
- static-analysis and sanitizer results;
- document-authority records;
- traceability graphs;
- compliance reports;
- waivers and exceptions.

Evidence shall identify the repository, commit, applicable standard revision, scanner revision, timestamp, and result.

## Enforcement Boundary

AEMS is not itself the source of engineering authority. It executes authority granted by Catylist and expressed normatively by AES. AEMS shall not invent new engineering obligations without a corresponding Catylist governance decision or AES standard.

## Consequences

- Governance, standards, enforcement, and implementation remain independently reviewable.
- Repository migrations have a deterministic canonical destination.
- AEMS rules can be traced to AES requirements and Catylist authority.
- Project repositories remain focused on project-specific implementation and evidence.

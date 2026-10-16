# Catalyst Ecosystem Architecture

Status: Active draft
Owner: Catylist

## Purpose

This document provides a concise overview of the Catalyst engineering ecosystem. The normative system architecture is [CAT-001 — Catalyst System Architecture](CAT-001-Catalyst-System-Architecture.md).

## Architectural model

Catalyst separates program governance, engineering standards, project management, repository lifecycle execution, templates, document engineering, shared infrastructure, and product implementation.

| Repository | Primary authority |
|---|---|
| `Catylist` | Program governance, ecosystem architecture, repository relationships |
| `AES` | Engineering standards and evidence obligations |
| `AEMS` | Engineering project management, planning, dependencies, and remediation tracking |
| `P0` | Repository initiation, inspection, remediation, verification, and readiness assessment |
| `repo_templates` | Reusable repository scaffolding, profiles, and baseline workflows |
| `engineering-docs-toolkit` | Semantic document engineering, transformation, and report rendering |
| `evo` | Evolutionary optimization infrastructure |
| `atarix` | Reference operating-system architecture and implementation |
| `JAG` | Application-specific architecture and implementation |
| `MayaUSD2017Bridge` | Maya 2017/OpenUSD compatibility product and RenderMan-preserving bridge |
| `code-noodling` | Experimental and exploratory engineering work; scoped repository under [ADR-0004](../adr/ADR-0004-governed-project-scopes.md); scopes not yet declared |
| `openCUDA` | Experimental; classified by [CAT-DISP-002](../reviews/CAT-DISP-002-unclassified-repository-classification.md) |
| `Rocket_demo` | Experimental; classified by [CAT-DISP-002](../reviews/CAT-DISP-002-unclassified-repository-classification.md) |
| `audiblebooks` | Experimental (private); classified by [CAT-DISP-002](../reviews/CAT-DISP-002-unclassified-repository-classification.md) |

`code-noodling` hosts several independent experimental projects. Under [ADR-0004](../adr/ADR-0004-governed-project-scopes.md), it is to
declare them as governed project scopes. Each scope will own its automation
and AES-SEC-001 evidence, while the repository keeps its single Experimental
classification. Until its manifest declares scopes and each migration lands,
`code-noodling` remains governed as a single repository-wide unit.

The machine-readable counterpart of this table, including external-reference
repositories, is the [repository inventory](../../inventory/repositories.json),
authoritative under [ADR-0006](../adr/ADR-0006-default-branch-protection-and-signed-commits.md).

## Authority boundaries

Catylist defines how repositories relate; it does not absorb their local authority.

- AES standards are authoritative in AES.
- AEMS project-management behavior is authoritative in AEMS.
- P0 repository-lifecycle behavior is authoritative in P0.
- EDT document-processing behavior is authoritative in `engineering-docs-toolkit`.
- Project architecture and implementation are authoritative in the owning project repository.
- Templates are authoritative only for new or deliberately synchronized scaffolding.
- `MayaUSD2017Bridge` owns its wrapper, adapters, protocol, tests, and evidence; OpenUSD, MayaUSD, Maya, and RenderMan remain external dependencies governed by their respective upstream owners.
- External references are not governed as Catalyst-owned repositories and must not be rewritten merely to satisfy Catalyst policy.

## Dependency direction

The authority and work flow follows [ADR-003](../adr/ADR-003-authority-chain.md):

```text
Catylist governance
        |
        v
AES standards and obligations
        |
        v
AEMS project management, assessment, and enforcement
        |
        +----> repo_templates scaffolding for new repositories
        |
        +----> P0 remediation of existing repositories, bringing them
        |      under Catylist management
        |
        v
project implementation and evidence
        |
        +----> EDT-rendered reports
```

Each layer consumes the authority of the layers above it and must not redefine
it. `repo_templates` turns that authority into scaffolding for new
repositories. P0 inspects, remediates, verifies, and assesses the readiness of
existing repositories against the same authority, so that each one can be
brought under Catylist management. Shared libraries such as EVO may be consumed
by project repositories, but they must not redefine program governance or
engineering standards.

[CAT-001 — Catalyst Engineering Ecosystem](../governance/CAT-001-catalyst-engineering-ecosystem.md)
records the same direction, with CAT-SCHEMA between AES and AEMS.

An earlier version of this section placed P0 between AES and AEMS, with
`repo_templates` supplying structures to P0. It contradicted ADR-003 and was
corrected in `dlworrell/Catylist#17`. The earlier text remains in this file's
history.

## Evidence model

A repository claim is accepted only when supported by repository evidence such as:

- an authoritative document;
- a manifest declaration;
- an ADR;
- a test or workflow result;
- an inspection report;
- a waiver record;
- a commit or release artifact.

Conversation, intent, or undocumented convention is not authoritative evidence.

## Failure and recovery

Program governance can fail through ambiguity, contradictory authority, stale inventories, disconnected project work, unenforced requirements, or undocumented exceptions.

Recovery requires:

1. identify the conflicting or missing authority;
2. preserve the current state as evidence;
3. record the decision or finding needed to resolve it;
4. update the authoritative repository;
5. create or update AEMS-managed remediation work;
6. run P0 or project-local verification;
7. regenerate affected EDT reports and documentation;
8. document any temporary waiver or migration state.

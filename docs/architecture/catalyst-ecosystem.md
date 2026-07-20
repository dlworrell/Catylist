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
| `code-noodling` | Experimental and exploratory engineering work |

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

The intended authority and work flow is:

```text
Catylist governance
        |
        v
AES standards and obligations
        |
        v
P0 inspection and verification
        |
        +----> AEMS-managed work
        |
        +----> EDT-rendered reports
        |
        v
project implementation and evidence
```

`repo_templates` supplies initial and selected target structures to P0. Shared libraries such as EVO may be consumed by project repositories, but they must not redefine program governance or engineering standards.

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

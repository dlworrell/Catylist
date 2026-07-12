# Catalyst Ecosystem Architecture

Status: Active draft
Owner: Catylist

## Purpose

This document defines the program-level architecture of the Catalyst engineering ecosystem. It identifies the authoritative repositories, their responsibilities, and the permitted direction of governance and engineering dependencies.

## Architectural model

Catalyst separates program governance, standards, enforcement, templates, bootstrap execution, shared engineering infrastructure, and product implementation.

| Repository | Primary authority |
|---|---|
| `Catylist` | Program governance, ecosystem architecture, repository relationships |
| `AES` | Engineering standards |
| `AEMS` | Assessment, reporting, and standards enforcement automation |
| `repo_templates` | Reusable repository scaffolding and policy templates |
| `P0` | Bootstrap execution and early project formation |
| `evo` | Evolutionary optimization infrastructure |
| `atarix` | Reference operating-system architecture and implementation |
| `JAG` | Application-specific architecture and implementation |
| `engineering-docs-toolkit` | Engineering-document tooling |
| `code-noodling` | Experimental and exploratory engineering work |

## Authority boundaries

Catylist defines how repositories relate; it does not absorb their local authority.

- AES standards are authoritative in AES.
- AEMS enforcement behavior is authoritative in AEMS.
- Project architecture and implementation are authoritative in the owning project repository.
- Templates are authoritative only for new or deliberately synchronized scaffolding.
- External references are not governed as Catalyst-owned repositories and must not be rewritten merely to satisfy Catalyst policy.

## Dependency direction

The intended governance dependency direction is:

```text
Catylist governance
        |
        v
AES standards
        |
        v
AEMS assessment and enforcement
        |
        v
repo_templates and project-local adoption
        |
        v
project implementation and evidence
```

Shared libraries such as EVO may be consumed by project repositories, but they must not redefine program governance or standards.

## Evidence model

A repository claim is accepted only when supported by repository evidence such as:

- an authoritative document;
- a manifest declaration;
- an ADR;
- a test or workflow result;
- a scanner report;
- a waiver record;
- a commit or release artifact.

Conversation, intent, or undocumented convention is not authoritative evidence.

## Failure and recovery

Program governance can fail through ambiguity, contradictory authority, stale inventories, unenforced standards, or undocumented exceptions.

Recovery requires:

1. identify the conflicting or missing authority;
2. preserve the current state as evidence;
3. record the decision needed to resolve it;
4. update the authoritative repository;
5. update AEMS inventories and checks;
6. verify downstream repositories;
7. document any temporary waiver or migration state.

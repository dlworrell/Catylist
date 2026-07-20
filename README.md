# Catylist

Catylist is the program umbrella and governing body for the Catalyst engineering ecosystem.

It defines the program-level architecture, project and repository relationships, governance boundaries, decision process, lifecycle rules, and bounded engineering-state model that connect Catalyst projects. Project-specific implementation, standards, automation, and product authority remain in their owning repositories.

## Responsibilities

Catylist owns:

- the Catalyst ecosystem architecture;
- the program governance model;
- PSZ boundaries, relationships, lifecycle, and lineage;
- repository taxonomy and relationship definitions;
- standards hierarchy and lifecycle integration;
- program-level architectural decision records;
- authoritative descriptions of governed projects and repositories.

Catylist does not replace project-local authority. AES manages and preserves engineering knowledge, AEMS manages and assesses PSZ state and closure, P0 owns repository initiation, inspection, remediation, and readiness assessment, `repo_templates` owns reusable repository scaffolding, EDT owns semantic document import, validation, transformation, and publication with provenance preservation, EVO optimizes within currently bounded PSZs, EWT is the public window, doorway, and administrator control centre for Catylist, and Atarix owns its operating-system architecture and implementation.

## Governance entry points

- [CAT-001 — Catalyst System Architecture](docs/architecture/CAT-001-Catalyst-System-Architecture.md)
- [CAT-002 — Engineering Representation, Closure, and Recovery](docs/architecture/CAT-002-Engineering-Representation-Closure-and-Recovery.md)
- [CAT-003 — PSZ Triangle and Recursive Engineering State](docs/architecture/CAT-003-PSZ-Triangle-and-Recursive-Engineering-State.md)
- [CAT-REV-002 — PSZ Architecture Update](docs/reviews/CAT-REV-002-PSZ-Architecture-Update.md)
- [Catalyst ecosystem architecture](docs/architecture/catalyst-ecosystem.md)
- [Governance model](docs/architecture/governance-model.md)
- [Repository taxonomy](docs/architecture/repository-taxonomy.md)
- [Standards lifecycle](docs/architecture/standards-lifecycle.md)
- [Decision process](docs/architecture/decision-process.md)
- [Architecture decision records](docs/adr/)
- [Engineering profiles and reports](docs/engineering/)
- [Architecture and production reviews](docs/reviews/)

## Engineering standards

This repository inherits:

- `AES-DEV-001: Development Principles and Check-In Discipline`;
- `AES-SEC-001: Secure C and C++ Coding Rules` for any present or future native-code surface.

Major governance changes require architecture or specification evidence before implementation, documentation in the same change series, and an ADR when the decision changes program authority, project or repository classification, standards hierarchy, or compatibility expectations.

## Repository manifest

`aes-manifest.yaml` declares this repository's role, authority paths, governing standards, and relationships to the rest of Catalyst.

## Current maturity

Catylist is active and is being developed from a minimal umbrella repository into the authoritative program-level governance specification for Catalyst. CAT-003 is currently proposed; CAT-002 and all prior review artifacts remain preserved and addressable as lineage rather than being rewritten out of history.

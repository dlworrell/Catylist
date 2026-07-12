# Catylist

Catylist is the program umbrella and managing-governance repository for the Catalyst engineering ecosystem.

It defines the program-level architecture, repository relationships, governance boundaries, decision process, and lifecycle rules that connect Catalyst projects. Project-specific implementation, standards, automation, and product authority remain in their owning repositories.

## Responsibilities

Catylist owns:

- the Catalyst ecosystem architecture;
- the program governance model;
- repository taxonomy and relationship definitions;
- standards hierarchy and lifecycle integration;
- program-level architectural decision records;
- authoritative descriptions of governed repositories.

Catylist does not replace project-local authority. AES owns engineering standards, AEMS owns assessment and enforcement automation, `repo_templates` owns reusable repository scaffolding, P0 owns bootstrap execution, EVO owns evolutionary optimization infrastructure, and Atarix owns its operating-system architecture and implementation.

## Governance entry points

- [Catalyst ecosystem architecture](docs/architecture/catalyst-ecosystem.md)
- [Governance model](docs/architecture/governance-model.md)
- [Repository taxonomy](docs/architecture/repository-taxonomy.md)
- [Standards lifecycle](docs/architecture/standards-lifecycle.md)
- [Decision process](docs/architecture/decision-process.md)
- [Architecture decision records](docs/adr/)
- [Engineering profiles and reports](docs/engineering/)

## Engineering standards

This repository inherits:

- `AES-DEV-001: Development Principles and Check-In Discipline`;
- `AES-SEC-001: Secure C and C++ Coding Rules` for any present or future native-code surface.

Major governance changes require architecture or specification evidence before implementation, documentation in the same change series, and an ADR when the decision changes program authority, repository classification, standards hierarchy, or compatibility expectations.

## Repository manifest

`aes-manifest.yaml` declares this repository's role, authority paths, governing standards, and relationships to the rest of Catalyst.

## Current maturity

Catylist is active and is being developed from a minimal umbrella repository into the authoritative program-level governance specification for Catalyst.

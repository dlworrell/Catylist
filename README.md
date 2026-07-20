# Catylist

Catylist is the program umbrella and program-governance repository for the
Catalyst engineering ecosystem.

It defines the program-level architecture, project and repository
relationships, governance boundaries, decision process, lifecycle rules, and
bounded engineering-state model that connect Catalyst projects.
Project-specific implementation, standards, automation, and product authority
remain in their owning repositories.

## Responsibilities

Catylist owns:

- the Catalyst ecosystem architecture;
- the program governance model;
- PSZ boundaries, relationships, lifecycle, and lineage;
- repository taxonomy and relationship definitions;
- standards hierarchy and lifecycle integration;
- program-level architectural decision records;
- authoritative descriptions of governed projects and repositories;
- common cross-repository engineering contracts and schema namespaces.

Catylist does not replace project-local authority. The accepted authority chain
is:

```text
Catylist -> AES -> AEMS -> governed repositories
```

AES owns engineering obligations and required evidence. AEMS owns
project-management automation, assessment, reporting, evidence packaging, and
enforcement. Project repositories own their implementations and local
architecture, specifications, ADRs, tests, and operational evidence. The
current repository roles and authority boundaries are maintained in the
[Catalyst ecosystem architecture](docs/architecture/catalyst-ecosystem.md).

EWT remains an intended public, visualization, and administrative surface for
Catylist. Adoption of the common closure contract by EWT and other downstream
repositories is not yet complete.

## Governance entry points

- [CAT-001 — Catalyst System Architecture](docs/architecture/CAT-001-Catalyst-System-Architecture.md)
- [CAT-002 — Engineering Representation, Closure, and Recovery](docs/architecture/CAT-002-Engineering-Representation-Closure-and-Recovery.md)
- [CAT-003 — PSZ Triangle and Recursive Engineering State](docs/architecture/CAT-003-PSZ-Triangle-and-Recursive-Engineering-State.md)
- [CAT-CON-001 — Engineering Closure Metadata Contract](docs/contracts/CAT-CON-001-Engineering-Closure-Metadata-Contract.md)
- [Engineering closure JSON Schema v1](schemas/catalyst/engineering-closure-v1.schema.json)
- [CAT-REV-002 — PSZ Architecture Update](docs/reviews/CAT-REV-002-PSZ-Architecture-Update.md)
- [Catalyst ecosystem architecture](docs/architecture/catalyst-ecosystem.md)
- [Governance model](docs/architecture/governance-model.md)
- [Repository taxonomy](docs/architecture/repository-taxonomy.md)
- [Standards lifecycle](docs/architecture/standards-lifecycle.md)
- [Decision process](docs/architecture/decision-process.md)
- [Architecture decision records](docs/adr/)
- [Engineering profiles and reports](docs/engineering/)
- [Architecture and production reviews](docs/reviews/)

## Current closure-contract implementation

The repository contains the first reviewable CAT-CON-001 increment:

- the draft `0.1.0` semantic contract;
- a Draft 2020-12 JSON Schema;
- positive and negative closure fixtures;
- a deterministic Python validator; and
- a dedicated validation workflow.

This is structural `E0` evidence. Schema conformance does not prove engineering
closure or production readiness. The contract's workstream remains
`VERIFYING`, and adoption by AES, AEMS, P0, templates, tools, and governed
projects requires separately reviewed changes in those repositories.

## Engineering standards

This repository inherits:

- `AES-DEV-001: Development Principles and Check-In Discipline`;
- `AES-SEC-001: Secure C and C++ Coding Rules` for any present or future
  native-code surface.

Major governance changes require architecture or specification evidence before
implementation, documentation in the same change series, and an ADR when the
decision changes program authority, project or repository classification,
standards hierarchy, or compatibility expectations.

## Repository manifest

`aes-manifest.yaml` declares this repository's role, authority paths, governing
standards, and relationships to the rest of Catalyst.

## Current maturity

Catylist is active and is evolving from a minimal umbrella repository into the
authoritative program-level governance specification for Catalyst. CAT-001,
CAT-002, and CAT-003 remain proposed architecture. CAT-CON-001 is a merged draft
implementation increment with downstream adoption and production-baseline
qualification still open. Prior review artifacts remain preserved and
addressable as lineage rather than being rewritten out of history.

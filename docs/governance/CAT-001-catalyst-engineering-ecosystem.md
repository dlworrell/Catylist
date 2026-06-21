# CAT-001 Catalyst Engineering Ecosystem

Status: Draft
Owner: catylist
Version: 0.1.0

## Purpose

Define the Catalyst engineering ecosystem, repository relationships, and governance boundaries.

CAT-001 describes how Catalyst repositories work together to produce standards, automation, templates, execution workflows, and reference implementations.

## Ecosystem Repositories

Catalyst is organized around the following core repositories:

| Repository | Responsibility |
|---|---|
| catylist | Ecosystem governance and program architecture. |
| AES | Engineering standards. |
| CAT-SCHEMA | Machine-readable schemas and controlled vocabularies. |
| AEMS | Engineering automation and assessment. |
| repo_template | Repository bootstrap. |
| P0 | Project Zero execution and readiness tracking. |
| Project repositories | Product engineering and reference implementation evidence. |

## Dependency Direction

Repository dependencies should flow from governance toward implementation:

```text
catylist -> AES -> CAT-SCHEMA -> AEMS -> repo_template -> P0 -> project repositories
```

Lower layers consume higher-layer authority. Lower layers should not redefine concepts owned by higher layers.

## Repository Ownership Rule

Each reusable engineering concept should have one authoritative repository.

Examples:

- Governance belongs in catylist.
- Engineering standards belong in AES.
- Machine-readable schemas belong in CAT-SCHEMA.
- Automation belongs in AEMS.
- Repository bootstrap belongs in repo_template.
- Project Zero execution belongs in P0.
- Product-specific engineering belongs in project repositories.

## Reference Implementations

Reference implementations demonstrate that standards are usable in real repositories.

Atarix is the primary reference implementation for Project Zero, repository manifests, documentation organization, traceability, and engineering evidence.

AEMS is the reference implementation for automated repository discovery, inspection, validation, reporting, and certification.

## Governance Expectations

Catalyst repositories should:

- declare ownership,
- declare lifecycle state,
- preserve evidence,
- maintain traceability,
- avoid duplicate authority,
- and consume upstream standards rather than redefining them.

## Related Documents

- CAT-000 Catalyst Meta-Architecture
- CAT-002 Repository Taxonomy
- CAT-003 Governance Model
- AES-001 Repository Lifecycle Standard
- AES-002 Project Zero Standard
- AES-003 Repository Manifest Standard

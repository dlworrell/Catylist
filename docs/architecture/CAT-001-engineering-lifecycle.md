# CAT-001 Supporting Document: Engineering Lifecycle

Status: Draft
Owner: catylist
Parent: CAT-001 Catalyst Engineering Ecosystem

## Purpose

Define the program-level engineering lifecycle used by Catalyst repositories.

## Lifecycle

Catalyst repositories move through a common lifecycle:

1. Idea
2. Program Planning
3. Project Creation
4. Project Zero
5. Engineering Ready
6. Implementation
7. Verification
8. Release
9. Maintenance
10. Archive

## State Meanings

| State | Meaning |
|---|---|
| Idea | A concept exists, but no repository commitment is required yet. |
| Program Planning | catylist evaluates scope, ownership, dependencies, and roadmap fit. |
| Project Creation | A repository is created or identified and baseline structure is established. |
| Project Zero | The repository is inventoried, organized, configured, and prepared for sustained engineering work. |
| Engineering Ready | The repository has enough structure, evidence, metadata, and automation to support implementation. |
| Implementation | Product, standard, automation, template, or governance work proceeds under engineering control. |
| Verification | Claims are checked against requirements, evidence, tests, reviews, or certification criteria. |
| Release | A versioned artifact, standard, template, report, or product baseline is published. |
| Maintenance | The repository is supported and evolved while preserving traceability. |
| Archive | The repository or artifact is preserved for historical record and no longer treated as active. |

## Ownership

- catylist owns ecosystem-level lifecycle visibility.
- AES defines normative lifecycle requirements.
- AEMS implements lifecycle inspection and reporting.
- repo_templates supports repository creation and Project Zero bootstrap.
- Project repositories provide lifecycle evidence.

## Rule

A repository should not enter normal implementation work until it is Engineering Ready or has explicitly documented accepted deferrals.

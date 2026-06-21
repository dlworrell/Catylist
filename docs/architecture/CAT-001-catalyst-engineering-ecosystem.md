# CAT-001 Catalyst Engineering Ecosystem

## Purpose

Define the Catalyst engineering ecosystem and the responsibilities of each repository.

## Repository Roles

- catylist: program governance and roadmap.
- AES: engineering standards.
- AEMS: engineering automation.
- repo_templates: repository bootstrap.
- Atarix: reference implementation.
- JAG: engineering assistant.

## Dependency Model

catylist -> AES -> AEMS -> repo_templates -> project repositories.

## Guiding Principles

- Observe before modifying.
- Standards before automation.
- Automation before repetition.
- One authoritative owner per artifact.
- Repository state is engineering evidence.
- Generated artifacts are reproducible.
- Every repository has one primary responsibility.
- Project Zero precedes implementation.

## PI-0 Objective

Establish a self-hosting engineering ecosystem capable of bringing repositories to an Engineering Ready state through Project Zero.
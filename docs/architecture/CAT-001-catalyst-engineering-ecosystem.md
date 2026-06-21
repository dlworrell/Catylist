# CAT-001 Catalyst Engineering Ecosystem

Status: Draft
Owner: catylist

## Purpose

Define the Catalyst engineering ecosystem, its governing repositories, and the responsibilities of each repository.

CAT-001 is the program-level entry point for understanding how Catalyst repositories relate to each other. It does not replace the detailed standards in AES, the automation in AEMS, the bootstrap assets in repo_templates, or the project-specific documentation in Atarix and JAG.

## Vision

Catalyst is an engineering ecosystem for building long-lived software, hardware, firmware, FPGA, documentation, and verification projects under a common evidence-based engineering discipline.

The ecosystem exists so that complex projects can be initialized, organized, reviewed, automated, and brought to an Engineering Ready state without inventing a new process for each repository.

## Mission

The mission of Catalyst PI-0 is to establish a self-hosting engineering foundation where:

- engineering standards are defined once,
- automation implements those standards,
- repository templates bootstrap new projects,
- Project Zero prepares repositories before implementation,
- evidence is reproducible from repository state,
- and each repository has one clear authoritative responsibility.

## Scope

CAT-001 covers:

- the Catalyst repository map,
- repository responsibilities,
- cross-repository dependency direction,
- Project Zero positioning,
- Program Increment 0 objectives,
- artifact ownership,
- repository interface contracts,
- and guiding engineering principles.

CAT-001 does not define detailed AES requirements, AEMS implementation internals, repository template file contents, or Atarix operating-system architecture.

## Repository Roles

- catylist: program governance, ecosystem roadmap, and cross-repository coordination.
- AES: engineering standards, governance rules, lifecycle definitions, and normative specifications.
- AEMS: engineering automation, repository inspection, inventory, traceability, issue graph generation, reports, and certification.
- repo_templates: repository bootstrap, standard directory layout, baseline manifests, workflows, labels, and issue templates.
- Atarix: operating-system, hardware, firmware, FPGA, and architecture validation project.
- JAG: engineering assistant and future consumer of AES and AEMS repository state.

## Repository Map

```text
catylist
  ├── AES
  ├── AEMS
  ├── repo_templates
  ├── Atarix
  └── JAG
```

## Dependency Model

The intended dependency direction is:

```text
catylist -> AES -> AEMS -> repo_templates -> project repositories
```

This diagram represents governance and consumption, not source-code linkage.

The dependency direction should remain acyclic. Reusable standards belong in AES. Reusable automation belongs in AEMS. Reusable bootstrap assets belong in repo_templates. Project-specific artifacts remain in their project repositories.

## Dependency Semantics

The dependency model has three meanings:

1. Governance dependency: lower layers should conform to the expectations set by higher layers.
2. Artifact dependency: lower layers may consume artifacts owned by higher layers.
3. Feedback dependency: lower layers may expose problems that require changes in higher layers, but they do not redefine higher-layer artifacts locally.

A project may discover that an AES standard is incomplete, that AEMS automation is missing, or that repo_templates lacks a bootstrap asset. In those cases, the project should create feedback in the owning repository rather than permanently solving the general problem locally.

## Repository Interface Contracts

Each repository has a simple ecosystem contract:

1. Own only the artifacts for which it is authoritative.
2. Declare what it consumes from other repositories.
3. Export reusable artifacts only from the proper ownership layer.
4. Keep project-specific material out of shared layers.
5. Provide evidence for any Project Zero or Engineering Ready claim.

### catylist Interface

catylist consumes status and evidence from every repository.

catylist exports:

- ecosystem vision,
- program roadmap,
- Program Increment definitions,
- cross-repository dependency maps,
- risk registers,
- and cross-repository governance decisions.

catylist must not redefine AES standards, AEMS implementation, repo_templates bootstrap assets, or product-specific architecture.

### AES Interface

AES consumes governance direction from catylist.

AES exports:

- engineering standards,
- lifecycle definitions,
- Project Zero definitions,
- manifest standards,
- metadata standards,
- traceability standards,
- and certification standards.

AES must not contain automation implementation or project-specific design.

### AEMS Interface

AEMS consumes AES standards and catylist program context.

AEMS exports:

- automation tools,
- repository inspection results,
- inventory generation,
- traceability generation,
- issue graph generation,
- validation reports,
- and certification reports.

AEMS must not define engineering rules independently of AES.

### repo_templates Interface

repo_templates consumes AES standards and AEMS automation expectations.

repo_templates exports:

- baseline repository structure,
- default manifests,
- Project Zero scaffolding,
- baseline workflows,
- issue templates,
- pull request templates,
- labels,
- and repository bootstrap assets.

repo_templates must not contain product-specific architecture.

### Project Repository Interface

Project repositories consume catylist governance, AES standards, AEMS automation, and repo_templates bootstrap assets.

Project repositories export:

- product-specific architecture,
- implementation,
- verification evidence,
- Project Zero evidence,
- and feedback to shared layers.

Project repositories should validate the ecosystem but should not become owners of reusable standards, automation, or templates.

## Ownership Matrix

Each engineering artifact should have exactly one authoritative owner. Other repositories may consume, validate, or provide feedback on that artifact, but they should not redefine it.

| Artifact class | Authoritative owner | Consumers |
|---|---|---|
| Ecosystem vision | catylist | all repositories |
| Program roadmap | catylist | all repositories |
| Program increments | catylist | all repositories |
| Cross-repository dependency graph | catylist | AES, AEMS, repo_templates, project repositories |
| Engineering standards | AES | AEMS, repo_templates, project repositories |
| Engineering lifecycle definitions | AES | AEMS, repo_templates, project repositories |
| Project Zero standard | AES | AEMS, repo_templates, project repositories |
| Repository manifest standard | AES | AEMS, repo_templates, project repositories |
| Automation implementation | AEMS | repo_templates, project repositories |
| Inventory generation | AEMS | all repositories |
| Traceability automation | AEMS | all repositories |
| Issue graph automation | AEMS | all repositories |
| Certification automation | AEMS | all repositories |
| Repository bootstrap layout | repo_templates | all new repositories |
| Baseline workflows | repo_templates | all new repositories |
| Baseline issue templates | repo_templates | all new repositories |
| Operating-system architecture | Atarix | Atarix contributors, AEMS, JAG |
| Engineering assistant behavior | JAG | engineers and project repositories |

## Ownership Rules

1. A project repository may validate a reusable concept, but should not become the long-term owner of that concept.
2. If a rule applies to every repository, it belongs in AES.
3. If a repeatable task can be automated for every repository, it belongs in AEMS.
4. If a structure should exist in every new repository, it belongs in repo_templates.
5. If a decision affects the ecosystem roadmap or cross-repository priorities, it belongs in catylist.
6. If an artifact is specific to one product, it belongs in that product repository.

## Guiding Principles

- Observe before modifying.
- Standards before automation.
- Automation before repetition.
- One authoritative owner per artifact.
- Repository state is engineering evidence.
- Generated artifacts are reproducible.
- Every repository has one primary responsibility.
- Capabilities belong at the highest reusable layer.
- Project Zero precedes implementation.
- Feedback from projects improves the standards, automation, and templates.

## PI-0 Objective

Establish a self-hosting engineering ecosystem capable of bringing repositories to an Engineering Ready state through Project Zero.

PI-0 succeeds when Catalyst can initialize repositories from repo_templates, inspect them with AEMS, validate them against AES, and track the program from catylist.

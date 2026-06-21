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

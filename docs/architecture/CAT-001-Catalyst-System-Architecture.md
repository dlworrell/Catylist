# CAT-001 — Catalyst System Architecture

Status: Draft
Owner: Catylist
Type: Program architecture
Lifecycle: Proposed

## 1. Purpose

This document defines the system architecture of the Catalyst engineering ecosystem. It establishes the responsibilities, authority boundaries, canonical information flows, shared engineering objects, service contracts, and lifecycle workflows that connect Catalyst repositories.

CAT-001 governs relationships between systems. It does not replace the project-local architecture, standards, implementation, or evidence owned by individual repositories.

## 2. Architectural objectives

Catalyst shall:

1. preserve clear authority and ownership;
2. separate governance, standards, project management, repository inspection, documentation transformation, and product implementation;
3. exchange durable engineering objects rather than undocumented conventions;
4. preserve evidence and provenance across every transformation;
5. support deterministic and reproducible automation;
6. make all consequential changes reviewable through version control;
7. permit operation from GitHub Actions and mobile clients without weakening controls;
8. avoid forcing one repository to redefine another repository's authority.

## 3. Governing principle

The architectural discipline is:

> First, Observe. Then, Understand. Then, Improve.

Observation produces evidence. Understanding produces findings, decisions, and plans. Improvement produces reviewed changes and verification evidence.

## 4. System context

```text
                              Catylist
                 program governance and architecture
                                  |
                 +----------------+----------------+
                 |                                 |
                AES                               AEMS
       engineering standards             engineering project management
                 |                                 |
                 +----------------+----------------+
                                  |
                                  P0
              repository initiation, inspection, remediation,
                       verification, and readiness
                                  |
                    canonical engineering objects
                 +----------------+----------------+
                 |                |                |
                EDT        governed repositories  portfolio views
       document engineering    implementation       and metrics
```

This diagram expresses responsibility, not a mandatory runtime topology.

## 5. Authoritative systems

### 5.1 Catylist

Catylist owns:

- Catalyst program governance;
- ecosystem and repository architecture;
- repository taxonomy and relationships;
- authority boundaries;
- program lifecycle rules;
- program-level architectural decisions;
- portfolio-level definitions and views.

Catylist does not own project-local engineering standards, implementation, tests, or product architecture.

### 5.2 AES

AES owns:

- engineering doctrine and standards;
- evidence obligations;
- secure engineering requirements;
- development, documentation, verification, release, and maintenance standards;
- canonical cross-ecosystem semantics for reports, findings, evidence, and related engineering records;
- permitted waivers and standard-level exceptions.

AES defines obligations. It does not schedule or execute project work.

### 5.3 AEMS

AEMS is the engineering project-management and orchestration system.

AEMS owns:

- projects, workstreams, epics, tasks, and milestones;
- owners, assignments, priorities, dependencies, and blockers;
- planning and remediation campaigns;
- acceptance criteria and completion tracking;
- coordination of reviews and lifecycle transitions;
- import and management of findings produced by P0 or other authorized assessors;
- portfolio progress and project-management reporting.

AEMS does not define AES requirements, reinterpret Catylist authority, or independently invent certification criteria. It manages work needed to satisfy governing requirements.

### 5.4 Project Zero (P0)

P0 owns the repository lifecycle for initiation and remediation.

P0 provides:

- repository discovery and inventory;
- profile selection and desired-state comparison;
- inspection and assessment;
- finding and evidence production;
- remediation planning;
- safe automatic remediation through reviewed pull requests;
- verification of the resulting repository state;
- readiness assessment against declared profiles and AES requirements;
- report-model production for EDT rendering.

P0 does not own project schedules, portfolio governance, or document-rendering semantics.

### 5.5 Engineering Documents Toolkit (EDT)

EDT owns semantic document engineering.

EDT provides:

- extraction and import;
- semantic normalization into EDOM;
- validation and reference analysis;
- provenance-preserving transformation;
- report and documentation rendering;
- publication into Markdown, HTML, PDF, EPUB, and other approved formats;
- historical document comparison and regeneration.

EDT does not decide whether a repository complies with a standard or qualifies for certification. It renders durable knowledge products from authoritative evidence and decisions.

### 5.6 repo_templates

`repo_templates` owns reusable repository scaffolding, profiles, baseline workflows, and installation manifests. Templates define an initial state or an explicitly selected synchronization target; they do not override project-local authority after adoption.

### 5.7 Governed project repositories

Each project repository owns:

- project-specific purpose and scope;
- architecture and specifications;
- implementation;
- tests and verification assets;
- build and release behavior;
- project-local decisions and waivers;
- operational evidence and history.

## 6. Authority and dependency direction

The normative authority direction is:

```text
Catylist program governance
          |
          v
AES engineering obligations
          |
          v
repository profiles and project-local requirements
          |
          v
P0 assessment and verification
          |
          +----> AEMS-managed work
          |
          +----> EDT-rendered reports
          |
          v
governed repository changes and evidence
```

No downstream system may silently weaken an upstream requirement. Conflicts require an authoritative change, ADR, or permitted waiver.

## 7. Canonical Engineering Object Model

Catalyst systems shall converge on shared engineering objects rather than tool-specific interpretations.

The initial object set is:

- Repository;
- Project;
- Profile;
- Standard;
- Requirement;
- Finding;
- Evidence;
- Remediation;
- Task;
- Milestone;
- Decision;
- Artifact;
- Verification;
- Report;
- Certificate;
- Metric.

Each canonical object shall eventually define:

- a stable identifier;
- object type and schema version;
- lifecycle state;
- owning authority;
- creation and modification provenance;
- relationships to other objects;
- serialization rules;
- compatibility and migration behavior.

AES owns the cross-ecosystem semantic standards. A dedicated schema registry may be separated later when the model is stable and consumed by multiple implementations.

## 8. Core object relationships

```text
Standard -> Requirement
Requirement -> Finding
Finding -> Evidence
Finding -> Remediation
Remediation -> Task
Task -> Artifact
Artifact -> Verification
Verification -> Evidence
Evidence -> Report
Report -> Certificate
Project -> Milestone
Repository -> Project
Repository -> Profile
Metric -> any versioned engineering object
```

Relationships shall be explicit and traceable. A report is a view over engineering objects; it is not a substitute for the underlying evidence.

## 9. Service contracts

Catalyst defines logical services independently of the repositories that implement them.

### 9.1 Repository lifecycle service

Creates or imports a repository, selects a profile, initializes required controls, and records repository identity.

Primary implementation: P0 with `repo_templates`.

### 9.2 Inspection service

Observes repository state and emits findings supported by evidence.

Primary implementation: P0 and authorized project-specific inspectors.

### 9.3 Remediation service

Produces a remediation plan and applies approved safe changes through a dedicated branch and pull request.

Primary implementation: P0, with work coordinated by AEMS.

### 9.4 Verification service

Tests whether requirements and remediation acceptance criteria are satisfied and emits verification evidence.

Primary implementation: P0 and project-local CI.

### 9.5 Project-management service

Converts findings and program objectives into planned work, dependencies, assignments, milestones, and tracked outcomes.

Primary implementation: AEMS.

### 9.6 Documentation service

Extracts, normalizes, validates, transforms, and publishes engineering documentation and reports.

Primary implementation: EDT.

### 9.7 Evidence service

Records immutable evidence identity, provenance, integrity, custody, and relationships.

Semantic authority: AES. Producers include P0, CI systems, repositories, and EDT extraction pipelines.

### 9.8 Portfolio service

Aggregates repository, project, finding, remediation, verification, report, and metric objects into ecosystem views.

Program authority: Catylist. Project-management data provider: AEMS.

## 10. Normative workflows

### 10.1 New repository initiation

```text
Program intent
    -> repository classification
    -> profile and template selection
    -> repository creation
    -> identity initialization
    -> P0 inspection
    -> safe remediation
    -> verification
    -> EDT report generation
    -> readiness decision
    -> AEMS project tracking as needed
```

A new repository shall not begin as an ungoverned empty container when an approved template and profile are available.

### 10.2 Existing repository remediation

```text
Repository import
    -> preserve current state
    -> inventory and evidence capture
    -> desired-state assessment
    -> findings
    -> AEMS remediation campaign
    -> reviewed implementation
    -> P0 re-verification
    -> EDT report and historical comparison
```

Existing history shall be preserved. Obsolete material should be archived, superseded, redirected, or otherwise reconciled rather than casually discarded.

### 10.3 Continuous inspection

```text
Repository change or scheduled trigger
    -> P0 inspection
    -> new, changed, resolved, or recurring findings
    -> AEMS work updates
    -> remediation
    -> verification
    -> report and metric update
```

Continuous inspection shall not directly mutate the default branch.

### 10.4 Documentation and reporting

```text
Sources and evidence
    -> EDT extraction
    -> canonical semantic model
    -> validation and provenance checks
    -> P0/AEMS/Catylist decision objects
    -> canonical report model
    -> EDT rendering
    -> archived human and machine outputs
```

The facts shall be represented once in canonical objects and may be rendered into multiple formats.

## 11. Engineering reports

Engineering reports are point-in-time, evidence-backed views of repository or program state. They may include:

- repository identity and profile;
- inventory;
- applicable requirements;
- findings and severities;
- remediation state;
- verification results;
- evidence references;
- health and trend metrics;
- readiness or certification decisions;
- provenance and generation metadata.

AES defines report semantics. P0 and other authorized systems produce report data. EDT renders and publishes the report. AEMS manages any resulting work. Catylist may aggregate reports into portfolio views.

## 12. Profiles

Profiles declare the desired state appropriate to a repository class. Initial profile families may include:

- default;
- operating system;
- compiler or toolchain;
- C or C++ library;
- FPGA or HDL;
- embedded firmware;
- hardware or PCB;
- mechanical engineering;
- documentation;
- book;
- research;
- web service or API;
- dataset.

Profiles may extend AES obligations but may not weaken them without an approved waiver.

## 13. Client model

GitHub Actions, command-line tools, web interfaces, mobile applications, desktop applications, and AI engineering agents are clients of the same governed services and objects.

An AI agent shall not bypass the platform's authority, evidence, review, or traceability requirements. AI-produced changes must be represented through the same branches, pull requests, findings, tasks, verification records, and evidence as human-produced changes.

## 14. Mobile-operability requirement

Core repository lifecycle operations shall be invocable through GitHub Actions or another governed remote interface so they can be initiated from an iOS device. Mobile operation does not relax review or safety controls.

At minimum, authorized users should be able to trigger:

- inspection;
- planning;
- safe remediation pull-request creation;
- verification;
- report generation;
- readiness assessment.

## 15. Failure and recovery

Architectural failures include:

- conflicting authority claims;
- undocumented repository relationships;
- incompatible object schemas;
- orphaned findings or evidence;
- reports that cannot be regenerated;
- project work disconnected from requirements;
- automatic mutation of protected branches;
- certification without supporting evidence.

Recovery shall:

1. preserve the observed state;
2. identify the authoritative source of conflict;
3. record a finding or decision;
4. create managed remediation work;
5. apply reviewed changes;
6. re-run verification;
7. regenerate affected reports;
8. retain historical evidence.

## 16. Conformance

A Catalyst repository or service conforms to CAT-001 when it:

- declares its purpose and owning authority;
- respects the boundaries in this document;
- uses or maps to canonical engineering objects;
- preserves evidence and provenance;
- performs consequential changes through reviewable version-control operations;
- supports reproducible assessment and reporting;
- records deviations through an approved ADR or waiver.

## 17. Planned subordinate specifications

CAT-001 establishes the architecture but does not fully define every schema or protocol. Follow-on work may include:

- Canonical Engineering Object Model;
- Engineering Finding Model;
- Remediation Model;
- Repository Health Model;
- Verification and Certification Model;
- repository lifecycle service contract;
- portfolio aggregation model;
- client API conventions.

These specifications shall preserve the ownership boundaries established here.

# CAT-REV-001 — End-to-End Workflow Assessment

Status: Active review artifact  
Owner: Catylist  
Parent review: `CAT-REV-001`  
Date: 2026-07-19

## 1. Purpose

This assessment evaluates whether Catalyst can carry a governed change from initial intent through implementation, evidence, merge, release, ecosystem assessment, and recovery without relying on undocumented human memory.

The review uses the accepted authority chain:

```text
Catylist → AES → AEMS → governed repositories
```

The question is not whether individual repositories contain useful pieces. The question is whether the pieces form one deterministic operating system for engineering work.

## 2. Required production workflow

A production-capable Catalyst workflow must support the following sequence:

1. classify the repository and production profile;
2. identify applicable governance and AES standards;
3. establish intent and acceptance criteria;
4. record architecture or specification where required;
5. record an ADR for authority-changing, irreversible, or major decisions;
6. implement one logical change;
7. execute local verification;
8. package evidence with provenance;
9. run repository conformance checks;
10. perform review under explicit decision rights;
11. merge only when required checks pass;
12. qualify a release candidate;
13. retain release evidence and provenance;
14. reassess ecosystem compatibility;
15. publish or deploy only after qualification;
16. preserve rollback, reconstruction, and recovery information.

A workflow is incomplete if any required transition is merely implied, manually remembered, or represented differently in each repository.

## 3. Current observed workflow surfaces

### 3.1 Catylist

Catylist defines the authority chain, governance layers, change lifecycle, repository taxonomy, and ratcheting posture. These documents are coherent enough to guide a human reviewer.

However, Catylist does not yet provide an executable workflow contract that names every state, transition, required input, produced artifact, responsible authority, failure mode, and closure condition.

### 3.2 AES

AES identifies reusable engineering obligations and evidence expectations. Its current manifest declares required profiles and supported evidence formats.

However, the ecosystem does not yet demonstrate deterministic standard resolution by revision, profile, repository class, lifecycle state, and production participation.

### 3.3 AEMS

AEMS contains working local and aggregate scanners for AES-DEV-001 and AES-SEC-001. It can emit JSON and Markdown reports and upload workflow artifacts.

However, current automation is principally scan-oriented. It does not yet operate as a complete workflow coordinator that can prove every transition from intent through release and ecosystem closure.

### 3.4 P0

P0 is assigned the bootstrap, inspection, remediation, and readiness role, but its README still identifies the repository as AES and assigns obsolete authority. No trustworthy production workflow can begin from a repository whose bootstrap authority is itself contradictory.

### 3.5 repo_templates

`repo_templates` correctly aims to provide repeatable structure, documentation, CI scaffolding, and project metadata. Its README still describes the production template baseline as a planned milestone and the repository layout as proposed.

The template source therefore cannot yet serve as proven workflow realization.

### 3.6 Governed repositories

Atarix demonstrates the strongest local closure discipline currently observed: specification, implementation, tests, retained evidence, and explicit refusal to fabricate unavailable hardware evidence.

That discipline is not yet proven as a reusable ecosystem workflow. It remains a strong project-local example rather than a system-wide contract.

## 4. Findings

### CAT-WF-001 — No canonical workflow state machine

- Recovery state: Observed
- Confidence: High
- Claim: Catalyst documents lifecycle concepts but does not define one machine-readable engineering workflow state machine.
- Consequence: Repositories can use the same words while advancing work under different closure rules.
- Corrective action: Define a versioned workflow schema with states, transitions, actors, required inputs, produced outputs, guards, failure states, and evidence requirements.
- Punch-list linkage: `CAT-PL-0501`

### CAT-WF-002 — Intent is not a required machine-verifiable input

- Recovery state: Observed
- Confidence: High
- Claim: The engineering model requires intent, realization, and evidence, but no canonical artifact proves the intent and acceptance criteria attached to every governed change.
- Consequence: Implementation and test results can exist without proving that the intended problem was solved.
- Corrective action: Require a change record or equivalent PR-bound artifact containing claim, scope, assumptions, acceptance criteria, authority, and applicable standards.
- Punch-list linkage: `CAT-PL-0502`

### CAT-WF-003 — Architecture and ADR triggers are prose-only

- Recovery state: Observed
- Confidence: High
- Claim: Catylist states when architecture and ADRs are expected, but automation cannot determine whether a given change triggered either obligation or whether the required artifact exists.
- Consequence: Major changes can bypass durable rationale without deterministic failure.
- Corrective action: Define trigger declarations and validation rules, including an explicit `not_required` rationale where no architecture or ADR is produced.
- Punch-list linkage: `CAT-PL-0503`

### CAT-WF-004 — Bootstrap cannot yet produce a trusted repository

- Recovery state: Observed
- Confidence: High
- Claim: P0 is contradictory and `repo_templates` is not yet demonstrated as a versioned production baseline.
- Consequence: WF-002 repository bootstrap has no authoritative, reproducible implementation.
- Corrective action: Normalize P0, freeze template classes, generate deterministic fixtures, and require AEMS conformance before accepting generated repositories.
- Punch-list linkage: `CAT-PL-0001`, `CAT-PL-0201`, `CAT-PL-0504`

### CAT-WF-005 — Remediation workflow is not distinct from bootstrap

- Recovery state: Inferred from current role descriptions
- Confidence: Medium
- Claim: Catalyst assigns P0 both initial formation and remediation responsibilities, but no contract distinguishes greenfield generation from brownfield inspection and repair.
- Consequence: Remediation may overwrite project-specific authority, history, or intentional deviations.
- Corrective action: Define separate bootstrap and remediation modes, with dry-run plans, migration records, conflict handling, preservation rules, waivers, and rollback.
- Punch-list linkage: `CAT-PL-0505`

### CAT-WF-006 — Evidence packaging is not a first-class workflow transition

- Recovery state: Observed
- Confidence: High
- Claim: Scanners emit reports and workflows upload artifacts, but evidence packaging is not uniformly required before merge or release.
- Consequence: A successful job can be mistaken for durable engineering evidence.
- Corrective action: Make evidence assembly a named transition producing a provenance envelope, hashes, subject revision, tool versions, claims tested, results, limitations, and retention location.
- Punch-list linkage: `CAT-PL-0308`, `CAT-PL-0506`

### CAT-WF-007 — Review authority and approval semantics are unresolved

- Recovery state: Indeterminate
- Confidence: Medium
- Claim: Governance documents assign decision domains, but the review did not establish a common CODEOWNERS model, required reviewer mapping, segregation of duties, or authority-sensitive approval rule across repositories.
- Consequence: A change may be technically reviewed without approval from the authority that owns the affected decision.
- Corrective action: Map changed artifact classes to required authorities and verify repository protection settings against that mapping.
- Punch-list linkage: `CAT-PL-0310`, `CAT-PL-0507`

### CAT-WF-008 — Merge closure is not defined as a portable contract

- Recovery state: Observed
- Confidence: High
- Claim: Individual workflows can fail or pass, but Catalyst lacks a common merge verdict schema combining required checks, evidence, waivers, review authority, and unresolved findings.
- Consequence: “Green CI” may not mean “engineering closed.”
- Corrective action: Define a deterministic merge-qualification result with fail-closed semantics for mandatory repositories.
- Punch-list linkage: `CAT-PL-0508`

### CAT-WF-009 — Release qualification is not demonstrated end to end

- Recovery state: Observed
- Confidence: High
- Claim: The reviewed surfaces do not prove a reusable release process from tagged source through built artifacts, tests, evidence, provenance, compatibility assessment, publication, and post-release verification.
- Consequence: Repository maturity and feature completion cannot be translated into a trustworthy release claim.
- Corrective action: Define and implement WF-005 Product Release as a reusable AEMS-orchestrated workflow.
- Punch-list linkage: `CAT-PL-0309`, `CAT-PL-0509`

### CAT-WF-010 — Ecosystem reassessment is detached from repository change

- Recovery state: Observed
- Confidence: High
- Claim: Aggregate scans are manually dispatched and use scanner-specific repository lists.
- Consequence: A merged change can invalidate ecosystem assumptions without triggering a consolidated assessment.
- Corrective action: Trigger impact-scoped ecosystem assessment from canonical graph changes, standards changes, template releases, AEMS releases, and production repository releases.
- Punch-list linkage: `CAT-PL-0302`, `CAT-PL-0312`, `CAT-PL-0510`

### CAT-WF-011 — Waivers lack a common lifecycle

- Recovery state: Observed from policy references; implementation remains incomplete
- Confidence: High
- Claim: Waivers are acknowledged, but no common workflow proves request, authority, scope, rationale, compensating controls, expiration, review, and retirement.
- Consequence: Temporary exceptions can become permanent invisible policy forks.
- Corrective action: Define a versioned waiver record and make active waivers part of merge, release, and ecosystem verdicts.
- Punch-list linkage: `CAT-PL-0511`

### CAT-WF-012 — Recovery is not connected to ordinary delivery

- Recovery state: Inferred
- Confidence: Medium
- Claim: Recovery metadata is well defined conceptually, but release and change workflows do not yet require reconstruction inputs, rollback procedure, or recovery evidence.
- Consequence: A system may be deliverable but not reproducibly recoverable.
- Corrective action: Require recovery-classification, rebuild instructions, artifact integrity, rollback boundaries, and indeterminate-state reporting for production releases.
- Punch-list linkage: `CAT-PL-0512`

### CAT-WF-013 — Human and machine workflow views can diverge

- Recovery state: Observed
- Confidence: High
- Claim: README, ADR, manifests, scanner configuration, workflow YAML, and release claims are not generated from or checked against one workflow model.
- Consequence: Documentation can remain plausible while automation implements a different process.
- Corrective action: Generate human-readable workflow documentation and validation fixtures from the canonical machine model, or validate both against a shared schema.
- Punch-list linkage: `CAT-PL-0513`

## 5. Proposed canonical workflow model

The workflow should be represented independently of GitHub Actions so that GitHub is an execution environment rather than the definition of engineering policy.

Minimum structure:

```yaml
workflow:
  schema: catalyst.workflow.v1
  id: governed-change
  revision: 1.0.0
  authority: dlworrell/Catylist
  applies_to:
    classes:
      - authority
      - control-plane
      - shared-service
      - governed-product
    production_profiles:
      - mandatory
      - optional
  states:
    - id: proposed
    - id: specified
    - id: implementing
    - id: verified-local
    - id: evidence-packaged
    - id: review-approved
    - id: merge-qualified
    - id: merged
    - id: release-qualified
    - id: released
    - id: ecosystem-verified
    - id: closed
    - id: blocked
    - id: waived
  transitions:
    - id: propose-to-specify
      from: proposed
      to: specified
      authority: repository-owner
      requires:
        - change-intent
        - acceptance-criteria
        - applicable-standards-resolution
      produces:
        - specification-or-rationale
    - id: evidence-to-review
      from: evidence-packaged
      to: review-approved
      authority: mapped-review-authority
      requires:
        - evidence-envelope
        - zero-unresolved-mandatory-findings
        - valid-waivers
  failure_policy: fail-closed
```

The final design may use a different serialization, but it must preserve these semantics.

## 6. Required workflow records

A complete governed change should produce or reference:

- repository identity and production profile;
- change intent;
- claim and assumptions;
- acceptance criteria;
- applicable standards and exact revisions;
- architecture/specification decision;
- ADR decision or explicit non-applicability rationale;
- implementation revision;
- local verification results;
- evidence envelope;
- review authority and approvals;
- waiver records;
- merge qualification verdict;
- release qualification verdict where applicable;
- ecosystem impact assessment;
- rollback and recovery information;
- final closure record.

These records need not all be separate files, but each semantic field must be machine-resolvable and reviewable.

## 7. Workflow responsibility allocation

### Catylist

- owns workflow semantics, repository classes, authority mapping, and cross-repository transitions;
- defines which workflow profiles exist and when they apply;
- owns the canonical ecosystem graph.

### AES

- owns reusable engineering requirements applied at workflow transitions;
- defines evidence sufficiency requirements and verification obligations;
- defines standard-specific waiver constraints.

### AEMS

- resolves the applicable workflow and standards;
- evaluates transition guards;
- invokes scanners and project-native tests;
- packages evidence;
- emits merge, release, and ecosystem verdicts;
- never invents policy.

### P0

- implements bootstrap and remediation entry workflows;
- preserves project history and local authority during remediation;
- produces a repository that AEMS can assess independently.

### repo_templates

- provides versioned realizations of approved repository profiles;
- records source template identity and revision;
- includes required workflow integration surfaces.

### Governed repositories

- own project-specific intent, architecture, implementation, tests, operational evidence, and releases;
- may extend but not weaken mandatory workflow requirements without an approved waiver.

## 8. Priority remediation order

### Wave 0 — Authority correction

1. Correct P0 identity and obsolete authority statements.
2. Approve the canonical repository taxonomy and lifecycle model.
3. Approve the canonical ecosystem graph semantics.

### Wave 1 — Workflow specification

1. Define `catalyst.workflow.v1`.
2. Define the governed-change, bootstrap, remediation, standards-propagation, release, and external-intake profiles.
3. Define change, waiver, merge-verdict, release-verdict, and closure records.

### Wave 2 — Realization

1. Freeze and version `repo_templates` baseline classes.
2. Implement P0 bootstrap and remediation modes.
3. Implement AEMS workflow resolution and transition evaluation.
4. Reuse existing AEMS scanners as subordinate verification steps.

### Wave 3 — Qualification

1. Generate clean repository fixtures from each template class.
2. Run bootstrap and remediation fixtures deterministically.
3. Execute governed changes through merge and release.
4. Retain evidence and independently decode all verdicts.

### Wave 4 — Ecosystem adoption

1. Normalize mandatory repositories.
2. Enable required checks and authority-aware review.
3. Trigger impact-scoped ecosystem reassessment automatically.
4. Report zero contradictory or indeterminate mandatory workflow states.

## 9. Closure criteria

The workflow portion of CAT-REV-001 may close only when:

1. one versioned workflow schema is accepted;
2. all mandatory workflow profiles are defined;
3. every transition identifies authority, guards, inputs, outputs, failure behavior, and evidence;
4. P0 can generate a clean repository from a pinned template revision;
5. P0 can remediate a legacy fixture without destroying intentional local content;
6. AEMS independently assesses both outputs;
7. a governed change proceeds from intent through merge qualification with retained evidence;
8. a release proceeds from tagged source through publication and post-release verification;
9. active waivers are visible in all relevant verdicts and expire deterministically;
10. ecosystem-impact reassessment runs from the canonical graph;
11. rollback and recovery information is verified for production releases;
12. the complete workflow is reproducible from a clean environment;
13. all mandatory verdicts are machine-readable and independently decodable;
14. human documentation and machine behavior are proven consistent;
15. the retained final report contains no contradictory or indeterminate mandatory workflow state.

## 10. Current conclusion

Catalyst has the beginnings of a strong engineering operating model, but today it is still a collection of aligned intentions, project-local discipline, and partially connected automation.

The most important missing production capability is a canonical workflow state machine enforced by AEMS and realized through P0, `repo_templates`, and governed repositories.

Until that exists, the ecosystem can demonstrate good engineering work, but it cannot yet prove that every governed change follows the same complete path from intent to durable closure.

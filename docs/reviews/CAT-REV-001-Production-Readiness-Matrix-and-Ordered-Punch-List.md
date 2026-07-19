# CAT-REV-001 — Production Readiness Matrix and Ordered Punch List

Status: Active review artifact  
Owner: Catylist  
Review: CAT-REV-001  
Date: 2026-07-19

## 1. Purpose

This document converts the CAT-REV-001 findings into a single execution baseline. It does not assert that every repository has been exhaustively qualified. It records the strongest maturity claim currently supportable, the evidence still missing, and the ordered work required to establish a production-capable Catalyst ecosystem.

No maturity score in this document is a substitute for repository-local verification. Scores may increase only when intent, realization, and retained evidence agree.

## 2. Scoring method

Each repository or workflow is assessed across ten production dimensions:

1. identity and authority;
2. machine-readable contract;
3. architecture and specification;
4. implementation completeness;
5. build and execution reproducibility;
6. CI and policy enforcement;
7. tests and retained evidence;
8. security and dependency control;
9. release, rollback, and recovery;
10. lifecycle and maintenance ownership.

Dimension values are:

- `0` — absent, contradictory, or unverifiable;
- `1` — declared in prose;
- `2` — partially realized;
- `3` — functional with local evidence;
- `4` — production candidate with complete repository-level evidence;
- `5` — continuously enforced and qualified as part of the ecosystem.

The repository maturity level is not the arithmetic average. It is the highest level for which all mandatory claims at that level are supported. A zero in identity, authority, or a mandatory trust boundary caps the repository at Level 0 or Level 1 regardless of strengths elsewhere.

## 3. Minimum production profile

The first Catalyst production baseline requires the following repositories:

- Catylist;
- AES;
- AEMS;
- P0;
- repo_templates;
- one governed reference implementation, initially Atarix;
- engineering-docs-toolkit only for the semantic-publication profile.

EWT, EVO, HERKULES, JAG, company/public repositories, experiments, demos, and external references must be inventoried and correctly classified, but they do not block the minimum baseline unless Catylist explicitly marks them mandatory for a selected release profile.

## 4. Repository readiness matrix

| Repository | Current level | Target for baseline | Confidence | Binding blockers | Disposition |
|---|---:|---:|---|---|---|
| Catylist | 2 — Bootstrapped | 5 | High | Canonical graph, schema validation, profile definition, consolidated verdict, release governance | Mandatory |
| AES | 2 — Bootstrapped | 5 | Medium | Authority text drift, standard schema, machine index, compatibility and waiver semantics | Mandatory |
| AEMS | 2 — Bootstrapped | 5 | Medium | Executable contract, canonical inventory consumption, qualification suite, durable evidence, deterministic ecosystem verdict | Mandatory |
| P0 | 0 — Undefined | 4 | High | Incorrect identity and authority; no proven bootstrap or remediation contract | Mandatory |
| repo_templates | 2 — Bootstrapped | 4 | Medium | Template classes not frozen; generation, upgrades, and AEMS conformance not proven | Mandatory |
| Atarix | 3 — Functional | 4 | Medium | Ecosystem-contract adoption, release qualification, physical hardware evidence for hardware-bound claims | Mandatory reference system |
| engineering-docs-toolkit | 3 — Functional | 4 | Medium | Release-class ambiguity, normative documentation alignment, reproducibility corpus, recovery evidence | Conditional profile |
| EWT | 2 — Bootstrapped | 2 or deferred | Medium | Role, interfaces, and production-profile status not frozen | Optional/deferred candidate |
| EVO | 2 — Bootstrapped | 2 or deferred | Medium | Role and production-profile status not frozen; production service claims unproven | Optional/deferred candidate |
| HERKULES | Indeterminate | 3 if publication profile selected | Low | Repository and publication workflow not fully inspected | Conditional exemplar |
| JAG | Indeterminate | Profile-specific | Low | Role, implementation boundary, build, release, and governance adoption not inspected | Governed but not baseline-blocking until classified |
| Just-a-Geek-LLC | 1 — Declared | 2 | Medium | Organizational/public boundary and publication authority need explicit contract | Non-technical boundary |
| code-noodling | 1 — Declared | 1 | Medium | Must be classified experimental and excluded from production conformance claims | Experimental |
| Rocket_demo | 1 — Declared | 1 | Low | Must be classified demo and excluded from production conformance claims | Demo |
| External references | 1 — Declared | 2 inventory control | Medium | Provenance, license, version pinning, integrity, update policy, governed wrapper boundary | External/reference |

## 5. Mandatory workflow readiness matrix

| Workflow | Current level | Target | Primary blockers |
|---|---:|---:|---|
| WF-001 Governance-to-enforcement | 2 | 5 | Authority graph and standard-resolution contracts are not continuously validated |
| WF-002 New repository bootstrap | 1 | 4 | P0 identity invalid; template generation and independent AEMS pass not demonstrated |
| WF-003 Existing repository remediation | 1 | 4 | No canonical remediation plan, change record, reassessment, and closure sequence |
| WF-004 Standards revision propagation | 1 | 5 | No versioned compatibility, affected-repository calculation, migration, or waiver lifecycle |
| WF-005 Product release | 2 | 4 | No common release record, provenance package, rollback evidence, or ecosystem reassessment |
| WF-006 Semantic document publication | 3 | 4 | Release-class and reproducibility evidence require normalization |
| WF-007 Atarix qualification | 3 | 4 | Emulator evidence exists; physical hardware evidence remains open for hardware-bound closure |
| WF-008 External dependency intake | 1 | 4 | No common provenance, license, integrity, update, and wrapper contract |

## 6. Production gate

Catalyst may claim a first production baseline only when all of the following are true:

1. Catylist publishes and validates the canonical ecosystem inventory, graph, repository taxonomy, lifecycle vocabulary, and production profiles.
2. AES publishes a machine-readable standards index with stable identifiers, revisions, applicability, evidence requirements, compatibility rules, and waiver hooks.
3. AEMS consumes Catylist and AES contracts without repository-specific inventory duplication and emits one deterministic ecosystem verdict.
4. P0 has correct identity and proves both a clean bootstrap and an existing-repository remediation cycle.
5. repo_templates produces versioned golden fixtures for every mandatory class, and every fixture passes independent AEMS assessment without local exceptions.
6. Required repository checks, release checks, and evidence records are reproducible and retained outside transient job summaries.
7. At least one governed implementation reaches Level 4 under the common contracts.
8. Every mandatory workflow reaches its target level.
9. Open P0 findings are zero.
10. Any remaining P1 finding has an explicit owner, approved waiver, expiry, compensating evidence, and migration plan.

## 7. Ordered punch list

### Wave 0 — Normalize authority and identity

#### CAT-PL-0001 — Correct and specify P0 identity and authority

- Priority: P0
- Owner: P0
- Dependencies: none
- Required state: P0 has a repository-local charter and manifest consistent with Catylist authority decisions.
- Corrective action: Replace copied or obsolete AES identity material; define P0 inputs, outputs, authority limits, bootstrap mode, remediation mode, and failure semantics.
- Verification: P0 self-check passes, Catylist graph validation passes, and no P0 document claims standards or program-governance authority.

#### CAT-PL-0002 — Freeze repository taxonomy

- Priority: P0
- Owner: Catylist
- Dependencies: none
- Required state: One canonical primary-class vocabulary exists; secondary capabilities cannot absorb another repository's authority.
- Verification: Every project-owned repository has exactly one valid primary class.

#### CAT-PL-0003 — Publish the canonical ecosystem graph contract

- Priority: P0
- Owner: Catylist
- Dependencies: CAT-PL-0002
- Required state: Versioned inventory and typed relationship graph with uniqueness, cardinality, direction, compatibility, and external-reference rules.
- Verification: Schema validation detects missing repositories, duplicate authorities, illegal cycles, unresolved edges, and incompatible versions.

#### CAT-PL-0004 — Freeze lifecycle and maturity vocabularies

- Priority: P0
- Owner: Catylist
- Dependencies: CAT-PL-0002
- Required state: Repository class, lifecycle, maturity, and production-profile participation are independent fields with defined transitions.
- Verification: No governed manifest relies on ambiguous values such as `foundation`, `stable`, or `feature-complete` without a mapped canonical state.

#### CAT-PL-0005 — Complete repository identity census

- Priority: P0
- Owner: Catylist
- Dependencies: CAT-PL-0002, CAT-PL-0003, CAT-PL-0004
- Required state: Every governed, optional, experimental, demo, organizational, and external/reference repository is inventoried.
- Verification: The machine inventory and accessible repository population reconcile with no unexplained omissions.

### Wave 1 — Make standards consumable

#### CAT-PL-0101 — Correct AES authority-facing documentation

- Priority: P0
- Owner: AES
- Dependencies: CAT-PL-0003
- Required state: AES consistently identifies Catylist as program authority and itself as engineering-standards authority.
- Verification: README, manifest, ADRs, standards index, and generated documentation contain no contradictory authority chain.

#### CAT-PL-0102 — Publish the AES standard schema and index

- Priority: P0
- Owner: AES
- Dependencies: CAT-PL-0101
- Required state: Stable machine-readable records include ID, revision, status, applicability, normative source, required evidence, enforcement mode, compatibility, supersession, and waiver policy.
- Verification: AEMS resolves every mandatory standard from the index without hard-coded paths or repository-specific exceptions.

#### CAT-PL-0103 — Define common waiver contract

- Priority: P0
- Owner: AES with Catylist governance
- Dependencies: CAT-PL-0102
- Required state: Waivers contain authority, scope, rationale, risk, compensating control, affected versions, issue date, expiry, renewal rules, and closure evidence.
- Verification: Expired, unauthorized, overly broad, or orphaned waivers fail assessment.

#### CAT-PL-0104 — Define standards revision propagation

- Priority: P0
- Owner: AES and AEMS
- Dependencies: CAT-PL-0102, CAT-PL-0103
- Required state: Every revision is classified as compatible, migration-required, or breaking, and affected repositories can be calculated.
- Verification: A fixture revision produces the expected impact set, migration tasks, waivers, and final closure report.

### Wave 2 — Establish executable enforcement

#### CAT-PL-0201 — Freeze the AEMS assessment contract

- Priority: P0
- Owner: AEMS
- Dependencies: CAT-PL-0003, CAT-PL-0102
- Required state: Versioned input, output, finding, evidence, exit-code, failure, and compatibility semantics.
- Verification: Golden fixtures prove deterministic JSON and human-readable output.

#### CAT-PL-0202 — Remove duplicated repository inventories

- Priority: P0
- Owner: AEMS
- Dependencies: CAT-PL-0003, CAT-PL-0201
- Required state: AEMS consumes the Catylist graph and profile selections instead of maintaining separate per-standard repository lists.
- Verification: Adding or reclassifying a repository in Catylist changes all applicable AEMS assessments without editing scanner-specific inventories.

#### CAT-PL-0203 — Qualify AEMS itself

- Priority: P0
- Owner: AEMS
- Dependencies: CAT-PL-0201
- Required state: Scanner unit tests, malformed-input tests, golden vectors, version-compatibility tests, deterministic ordering, and fail-closed trust-boundary behavior.
- Verification: AEMS qualification suite passes in a pinned, reproducible environment.

#### CAT-PL-0204 — Implement a consolidated ecosystem verdict

- Priority: P0
- Owner: AEMS
- Dependencies: CAT-PL-0202, CAT-PL-0203
- Required state: One command or workflow evaluates the selected production profile and emits repository results, workflow results, open findings, waivers, provenance, and final verdict.
- Verification: Repeated runs at the same source revisions produce byte-stable normalized output except explicitly nondeterministic timestamps or run identifiers.

#### CAT-PL-0205 — Establish durable evidence custody

- Priority: P0
- Owner: AEMS and Catylist
- Dependencies: CAT-PL-0201
- Required state: Evidence records include repository, commit, workflow, tool revision, policy revision, environment, inputs, hashes, results, and retention location.
- Verification: A reviewer can independently retrieve and validate evidence after transient workflow artifacts expire.

#### CAT-PL-0206 — Harden CI execution dependencies

- Priority: P1
- Owner: AEMS and repo_templates
- Dependencies: CAT-PL-0203
- Required state: Actions, toolchains, runners where possible, and third-party dependencies are pinned or otherwise integrity-controlled.
- Verification: Supply-chain policy detects mutable or unapproved workflow dependencies.

### Wave 3 — Prove repository creation and remediation

#### CAT-PL-0301 — Freeze mandatory template classes and version 1

- Priority: P0
- Owner: repo_templates
- Dependencies: CAT-PL-0002, CAT-PL-0102
- Required state: Mandatory classes and their required files, workflows, manifests, profiles, and ownership metadata are fixed for v1.
- Verification: Template release manifest and compatibility policy are complete.

#### CAT-PL-0302 — Add template golden-generation fixtures

- Priority: P0
- Owner: repo_templates
- Dependencies: CAT-PL-0301
- Required state: Each mandatory template can be generated non-interactively from fixed inputs.
- Verification: Generated trees and normalized contents match reviewed golden fixtures.

#### CAT-PL-0303 — Require independent AEMS conformance of generated fixtures

- Priority: P0
- Owner: repo_templates and AEMS
- Dependencies: CAT-PL-0204, CAT-PL-0302
- Required state: Every generated fixture passes the selected baseline profile without local exceptions.
- Verification: CI generates and assesses every mandatory class from a clean environment.

#### CAT-PL-0304 — Implement P0 clean-bootstrap workflow

- Priority: P0
- Owner: P0
- Dependencies: CAT-PL-0001, CAT-PL-0303
- Required state: Request -> classification -> template selection -> generation -> manifest resolution -> AEMS assessment -> closure record.
- Verification: One retained end-to-end fixture proves the complete path.

#### CAT-PL-0305 — Implement P0 remediation workflow

- Priority: P0
- Owner: P0 and AEMS
- Dependencies: CAT-PL-0001, CAT-PL-0204
- Required state: Finding -> remediation plan -> approved change -> reassessment -> closure or waiver.
- Verification: One intentionally nonconforming repository is corrected with retained before-and-after evidence.

#### CAT-PL-0306 — Define template drift and upgrade policy

- Priority: P1
- Owner: repo_templates and AEMS
- Dependencies: CAT-PL-0303
- Required state: Generated repositories record template provenance; drift is distinguished from legitimate local extension; upgrade paths are versioned.
- Verification: A fixture repository can be compared, upgraded, and reassessed without overwriting project-owned decisions.

### Wave 4 — Normalize governed repositories

#### CAT-PL-0401 — Adopt canonical manifests

- Priority: P0
- Owner: Each governed repository
- Dependencies: CAT-PL-0003, CAT-PL-0102
- Required state: Valid identity, authority, class, lifecycle, maturity, profiles, standards, interfaces, dependencies, evidence paths, release policy, and ownership.
- Verification: AEMS manifest assessment passes across the selected profile.

#### CAT-PL-0402 — Normalize required repository contracts

- Priority: P1
- Owner: Each governed repository
- Dependencies: CAT-PL-0301, CAT-PL-0401
- Required state: Required README, license, contribution, security, code ownership, architecture, specification, ADR, evidence, release, and recovery records exist according to repository class.
- Verification: No required element is satisfied solely by an undocumented convention.

#### CAT-PL-0403 — Prove required branch and merge protections

- Priority: P1
- Owner: Repository owners and AEMS
- Dependencies: CAT-PL-0204
- Required state: Required checks, review rules, bypass authority, force-push policy, and release-branch policy are declared and assessed.
- Verification: AEMS or an approved administrative audit produces evidence of configured protections.

#### CAT-PL-0404 — Establish external dependency intake records

- Priority: P1
- Owner: Consuming repository
- Dependencies: CAT-PL-0005
- Required state: Dependency purpose, provenance, license, version, integrity, update policy, vulnerability handling, wrapper/fork boundary, and removal plan are explicit.
- Verification: WF-008 passes for every mandatory external dependency.

### Wave 5 — Release and recovery qualification

#### CAT-PL-0501 — Define common release record

- Priority: P0
- Owner: Catylist and AES
- Dependencies: CAT-PL-0205
- Required state: Release intent, source revision, specifications, artifacts, toolchain, tests, security result, provenance, compatibility, migration, rollback, recovery, approvals, and ecosystem verdict are recorded.
- Verification: Schema and golden release package pass independent validation.

#### CAT-PL-0502 — Implement product release qualification

- Priority: P0
- Owner: AEMS and governed product repository
- Dependencies: CAT-PL-0204, CAT-PL-0501
- Required state: Release candidates cannot be called qualified without complete repository and ecosystem evidence.
- Verification: A governed reference release is built, assessed, packaged, and independently reproduced.

#### CAT-PL-0503 — Qualify Atarix as the first reference system

- Priority: P0
- Owner: Atarix
- Dependencies: CAT-PL-0401, CAT-PL-0502
- Required state: Existing emulator evidence is integrated into the common evidence contract; all hardware-bound claims are either supported by physical evidence or explicitly remain open.
- Verification: Atarix reaches Level 4 with no fabricated hardware closure.

#### CAT-PL-0504 — Qualify semantic publication profile

- Priority: P1 unless selected for baseline
- Owner: engineering-docs-toolkit and HERKULES
- Dependencies: CAT-PL-0401, CAT-PL-0502
- Required state: Corpus import, semantic model, validation, generation, reproducibility, quality report, provenance, rollback, and recovery are evidenced.
- Verification: WF-006 reaches Level 4 using a retained HERKULES fixture or approved equivalent.

#### CAT-PL-0505 — Run full system recovery exercise

- Priority: P1
- Owner: Catylist, AEMS, and profile owners
- Dependencies: CAT-PL-0502
- Required state: A release and its engineering rationale can be reconstructed from authoritative repositories and retained evidence after loss of transient CI state.
- Verification: Independent recovery drill produces the expected source, artifacts, assessment, and decision record.

### Wave 6 — Production declaration and continuous control

#### CAT-PL-0601 — Execute baseline qualification

- Priority: P0
- Owner: Catylist and AEMS
- Dependencies: all baseline-blocking items
- Required state: Selected production profile completes all mandatory workflows with zero unwaived P0 findings.
- Verification: Signed or otherwise integrity-protected consolidated qualification package.

#### CAT-PL-0602 — Publish production declaration

- Priority: P0
- Owner: Catylist
- Dependencies: CAT-PL-0601
- Required state: Scope, included repository revisions, supported profiles, known limitations, waivers, maintenance owners, and requalification triggers are public and unambiguous.
- Verification: Declaration references retrievable evidence and does not exceed the qualified scope.

#### CAT-PL-0603 — Enable continuous ecosystem reassessment

- Priority: P1
- Owner: AEMS
- Dependencies: CAT-PL-0601
- Required state: Relevant changes to governance, standards, enforcement, templates, manifests, dependencies, or releases trigger impact-aware reassessment.
- Verification: Controlled changes demonstrate expected selective and full requalification behavior.

## 8. Critical path

The shortest credible path to a first production baseline is:

`0001 -> 0002 -> 0003 -> 0004 -> 0005 -> 0101 -> 0102 -> 0103 -> 0201 -> 0202 -> 0203 -> 0204 -> 0301 -> 0302 -> 0303 -> 0304 -> 0305 -> 0401 -> 0501 -> 0502 -> 0503 -> 0601 -> 0602`

Work outside that path may proceed in parallel only when it does not introduce new authority, schema, template, or enforcement assumptions.

## 9. Atarix resume gate

Atarix feature development may resume before the entire ecosystem reaches production only after the following minimum controls exist:

1. CAT-PL-0002 through CAT-PL-0005 are approved;
2. CAT-PL-0101 and CAT-PL-0102 are complete enough to provide stable standards references;
3. CAT-PL-0201 defines the AEMS contract and CAT-PL-0204 has a working baseline verdict;
4. Atarix has adopted the canonical manifest and selected profiles;
5. new Atarix work can produce evidence in the common envelope;
6. resumption does not claim physical hardware closure where none exists.

Until these conditions are met, continued Atarix feature work risks embedding unstable ecosystem contracts and creating avoidable rework.

## 10. Review conclusion

Catalyst has substantial engineering content and several functional local mechanisms. Its principal production deficiency is not lack of implementation effort; it is the absence of one authoritative, machine-verifiable chain connecting governance, standards, enforcement, repository creation, delivery, release, evidence custody, and recovery.

The production program should therefore execute the punch list in dependency order rather than polishing individual repositories independently. The first objective is a trustworthy control plane. Repository-level maturity can then be raised against stable contracts instead of moving targets.

# CAT-REV-001 — Ecosystem Manifest and Relationship Contract Assessment

Status: Active review artifact  
Owner: Catylist  
Parent review: `CAT-REV-001`  
Date: 2026-07-19

## 1. Purpose

This assessment evaluates whether Catylist presently defines a complete, versioned and executable contract for the Catalyst repository graph.

The question is not whether repository relationships are understandable to a human reader. The question is whether one deterministic consumer can discover the supported repository population, resolve every authority and dependency edge, reject contradictions, calculate production-profile membership and emit retained evidence without repository-specific interpretation.

## 2. Evidence inspected

The assessment inspected:

- `aes-manifest.yaml` in Catylist;
- `docs/adr/ADR-003-authority-chain.md`;
- the repository inventory and identity census;
- the manifest and authority census;
- the role and lifecycle taxonomy assessment.

## 3. Current realization

Catylist currently has two useful but incomplete authority surfaces.

### 3.1 ADR-003

ADR-003 establishes the normative policy chain:

```text
Catylist -> AES -> AEMS -> governed repositories
```

It also separates company/public organizational authority from Catalyst engineering governance and prohibits circular policy dependencies.

This is a sound human-readable authority decision.

### 3.2 Catylist manifest

The Catylist root manifest records named relationship slots for standards, enforcement, templates, bootstrap, optimization and the reference system.

This is a useful bootstrap representation, but it is not yet a complete ecosystem graph contract.

It contains one Catylist-local record and several special-purpose relationship keys. It does not define the full supported repository population, edge semantics, cardinality, reciprocity, compatibility, production-profile membership, integrity, evidence, or validation outcomes.

## 4. Findings

### CAT-GRAPH-001 — The authority chain is normative prose, not an executable graph

- Recovery state: Observed
- Priority: P0
- Confidence: High
- Claim: ADR-003 establishes correct authority direction, but no machine-readable system graph proves that all repository-local declarations conform to it.
- Risk: A repository may declare a circular, reversed or obsolete authority relationship without deterministic ecosystem failure.
- Punch-list linkage: `CAT-PL-0003`, `CAT-PL-0105`

### CAT-GRAPH-002 — Relationship keys encode repository names rather than reusable semantics

- Recovery state: Observed
- Priority: P0
- Confidence: High
- Claim: Keys such as `standards_repository`, `enforcement_repository`, `template_repository`, `bootstrap_repository`, `optimization_repository` and `reference_system_repository` combine role, cardinality and edge meaning in field names.
- Risk: The schema cannot cleanly represent multiple implementations, optional services, migrations, alternates, profile-specific relationships or future repository classes.
- Required state: Relationship records use stable edge identifiers and explicit source, target, direction, requiredness, cardinality and compatibility semantics.
- Punch-list linkage: `CAT-PL-0002`, `CAT-PL-0003`

### CAT-GRAPH-003 — The manifest does not enumerate the supported ecosystem population

- Recovery state: Observed
- Priority: P0
- Confidence: High
- Claim: The root manifest names selected relationships but does not contain or reference one complete repository inventory.
- Risk: Repositories may exist in an ambiguous state: governed, optional, experimental, external, abandoned or simply forgotten.
- Punch-list linkage: `CAT-PL-0005`

### CAT-GRAPH-004 — No edge cardinality or uniqueness constraints are defined

- Recovery state: Observed
- Priority: P0
- Confidence: High
- Claim: The current representation does not state which roles must have exactly one authority, which may have several providers and which are optional by production profile.
- Risk: Multiple repositories can claim the same exclusive authority, or a required role can be absent, without a well-defined validation result.
- Punch-list linkage: `CAT-PL-0002`, `CAT-PL-0003`

### CAT-GRAPH-005 — Relationship reciprocity and local-declaration reconciliation are undefined

- Recovery state: Observed
- Priority: P0
- Confidence: High
- Claim: There is no normative rule stating how Catylist-owned graph declarations reconcile with repository-local manifests.
- Risk: One side may declare a dependency or authority edge that the other side omits or contradicts.
- Required state: Catylist owns the canonical graph; repository-local manifests declare their local view; AEMS verifies agreement and reports unilateral, missing and contradictory edges.
- Punch-list linkage: `CAT-PL-0003`, `CAT-PL-0103`

### CAT-GRAPH-006 — Production profiles cannot be calculated

- Recovery state: Observed
- Priority: P0
- Confidence: High
- Claim: The current manifest has no versioned production-profile definitions and no rule for mandatory, optional, deferred or excluded participation.
- Risk: EWT, EVO, EDT, Atarix and other repositories cannot be objectively classified as blockers or non-blockers for a Catalyst release.
- Punch-list linkage: `CAT-PL-0003`, `CAT-PL-0307`

### CAT-GRAPH-007 — Version compatibility and migration semantics are absent

- Recovery state: Observed
- Priority: P1
- Confidence: High
- Claim: Relationship entries do not state required versions, compatibility ranges, migration obligations or replacement policy.
- Risk: A repository graph may be structurally complete but operationally incompatible.
- Punch-list linkage: `CAT-PL-0003`, `CAT-PL-0404`

### CAT-GRAPH-008 — External dependencies are outside the executable graph

- Recovery state: Observed
- Priority: P1
- Confidence: High
- Claim: External and reference repositories are not represented with provenance, licensing, integrity, pinning, maintenance and replacement fields.
- Risk: Unsupported or unverified upstream material can silently enter a production path.
- Punch-list linkage: `CAT-PL-0005`, `WF-008`

### CAT-GRAPH-009 — No deterministic consolidated result contract exists

- Recovery state: Observed
- Priority: P0
- Confidence: High
- Claim: There is no specified command, report schema, exit status or retained evidence artifact for whole-ecosystem conformance.
- Risk: System readiness remains a manual interpretation rather than a reproducible engineering result.
- Punch-list linkage: `CAT-PL-0102`, `CAT-PL-0105`

## 5. Required contract separation

The production design should separate three machine-readable artifacts.

### 5.1 Repository manifest

Owned by each repository. It declares local identity, role, lifecycle, maturity, standards adoption, local evidence and the repository's view of relationships.

### 5.2 Ecosystem inventory and graph

Owned by Catylist. It declares the supported repository population, canonical authority assignments, relationship edges, production profiles and external dependency intake records.

### 5.3 Assessment report

Produced by AEMS. It records input revisions, schema versions, resolved graph, findings, waivers, evidence references, exit semantics and deterministic result identity.

Combining these into one mutable file would blur authority. Separating them allows independent comparison of declared intent, local realization and observed evidence.

## 6. Proposed ecosystem graph skeleton

```yaml
schema:
  id: catalyst.ecosystem-graph
  version: 1.0.0

program:
  id: catalyst
  authority_repository: dlworrell/Catylist
  authority_decision: docs/adr/ADR-003-authority-chain.md

profiles:
  - id: catalyst-production-v1
    status: draft
    target_maturity: 5
    required_roles:
      - governance-authority
      - engineering-standards-authority
      - assessment-enforcement
      - repository-bootstrap
      - repository-template-provider

repositories:
  - full_name: dlworrell/Catylist
    class: authority
    role_id: governance-authority
    lifecycle: active
    participation:
      catalyst-production-v1: mandatory
    manifest: aes-manifest.yaml

relationships:
  - id: catalyst-governed-by
    source: dlworrell/AES
    target: dlworrell/Catylist
    kind: governance-authority
    required: true
    cardinality:
      source: one
      target: many
    compatibility:
      policy: explicit
    evidence:
      authority: docs/adr/ADR-003-authority-chain.md

external_dependencies:
  - id: upstream-example
    consumer: owner/repository
    upstream: upstream-owner/repository
    revision: immutable-reference
    license: SPDX-expression
    integrity: sha256:value
    update_policy: path-or-policy-id
    replacement_policy: path-or-policy-id
```

This skeleton is illustrative. The approved schema must be formally specified and validated before use as an enforcement gate.

## 7. Required graph invariants

A conforming graph validator must fail closed when any mandatory invariant is violated.

1. Every repository identifier is unique.
2. Every project-owned repository has exactly one primary class and one primary role.
3. Every relationship source and target resolves to a declared repository or approved external dependency.
4. The governance authority is exactly one repository.
5. The engineering standards authority is exactly one repository for a production profile.
6. Enforcement implementations may consume policy but may not own or redefine it.
7. Circular policy-authority paths are prohibited.
8. Every mandatory profile role resolves to at least one compatible active repository.
9. Exclusive roles resolve to exactly one repository.
10. Repository-local identity and relationship declarations agree with the Catylist graph.
11. Every required external dependency has provenance, license, immutable revision, integrity and maintenance policy.
12. Every graph and assessment result records exact input revisions.
13. Unknown schema major versions are rejected.
14. Unsupported relationship kinds are rejected rather than ignored.
15. Waived violations remain visible, scoped, owned and time-bounded.

## 8. Consolidated assessment contract

The eventual ecosystem assessment should support a command equivalent to:

```text
aems assess ecosystem --graph path/to/catalyst-ecosystem.yaml --profile catalyst-production-v1
```

The exact interface belongs to AEMS, but the result must provide:

- deterministic exit codes;
- graph schema and profile versions;
- exact repository revisions inspected;
- resolved repository population;
- resolved authority and dependency edges;
- missing, unilateral, contradictory and circular relationships;
- profile participation and blocking status;
- standards resolution outcomes;
- waiver application and expiration state;
- external dependency intake outcomes;
- evidence references;
- a reproducible machine-readable report;
- an operator-readable summary;
- a content or result digest.

## 9. Remediation order

1. Approve stable repository classes, lifecycle states and maturity semantics.
2. Specify `catalyst.repository-manifest` and `catalyst.ecosystem-graph` as separate versioned contracts.
3. Convert the current Catylist manifest into a conforming repository-local manifest.
4. Create the Catylist-owned canonical ecosystem graph.
5. Migrate core repositories and reconcile local declarations.
6. Implement fail-closed graph validation in AEMS.
7. Define `catalyst-production-v1` and classify every repository's participation.
8. Retain a deterministic consolidated assessment as closure evidence.

## 10. Closure criteria

`CAT-PL-0003` may close only when:

1. the repository-manifest and ecosystem-graph schemas are approved and versioned;
2. Catylist owns one complete supported-population graph;
3. all mandatory repositories have conforming local manifests;
4. every relationship resolves and satisfies cardinality, authority and compatibility rules;
5. local declarations agree with the canonical graph;
6. circular authority paths are rejected by test;
7. missing, duplicate, unilateral and incompatible edges are covered by negative fixtures;
8. production-profile membership is explicit and machine calculable;
9. external dependencies are represented by complete intake records;
10. AEMS emits a deterministic retained consolidated report.

## 11. Current state

The ecosystem manifest and relationship contract is **OPEN**.

Catylist has a sound accepted authority decision and a useful bootstrap manifest, but realization and evidence are incomplete. The current state is human-interpretable rather than production-executable.
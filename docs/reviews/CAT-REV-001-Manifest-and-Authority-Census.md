# CAT-REV-001 — Manifest and Authority Census

Status: Active review artifact  
Owner: Catylist  
Parent review: `CAT-REV-001`  
Date: 2026-07-19

## 1. Purpose

This census evaluates whether Catalyst repository manifests provide a trustworthy, machine-readable representation of repository identity, authority, lifecycle, standards, relationships, and evidence obligations.

The census distinguishes three conditions:

1. **present** — a manifest exists at the expected repository root path;
2. **correct** — the manifest identifies the repository and its role accurately;
3. **conformant** — the manifest follows the approved ecosystem schema and can be consumed without repository-specific interpretation.

Presence alone is not evidence of correctness or conformance.

## 2. Expected authority model

The current intended policy direction is:

```text
Catylist -> AES -> AEMS -> governed repositories
```

Supporting control-plane and shared-service relationships include:

```text
Catylist
  |- AES               normative standards
  |- AEMS              assessment and enforcement
  |- P0                bootstrap and remediation
  |- repo_templates    reusable repository scaffolding
  |- EWT               engineer-facing workbench
  |- EDT               semantic document engineering
  |- EVO               optimization service/library
  `- governed products and organizational repositories
```

A repository manifest must describe its own place in this system. It must not silently duplicate another repository's identity or redefine upstream authority.

## 3. Observed manifest population

The expected root manifest path for this census is `aes-manifest.yaml`, because that path is already used by Catylist and AES and is referenced by current repository documentation. This path remains provisional until `CAT-PL-0003` approves the canonical schema and filename.

| Repository | Root manifest observed | Identity correct | Schema family | Current disposition |
|---|---:|---:|---|---|
| `dlworrell/Catylist` | yes | yes | `schema_version: 1` / Catylist profile | provisional |
| `dlworrell/AES` | yes | yes | `schema_version: 1` / AES profile | provisional |
| `dlworrell/AEMS` | no | n/a | none observed | nonconformant |
| `dlworrell/P0` | no | n/a | none observed | nonconformant |
| `dlworrell/repo_templates` | no | n/a | none observed | nonconformant |
| `dlworrell/EWT` | yes | **no** | copied AES manifest | contradictory |
| `dlworrell/engineering-docs-toolkit` | no | n/a | none observed | nonconformant |
| `dlworrell/evo` | yes | yes at repository identity level | `manifest_version: 0.1` / EVO-local profile | schema-incompatible |
| `dlworrell/atarix` | no | n/a | none observed at expected path | nonconformant |

A missing file means only that no manifest was found at the expected path during this census. It does not prove that no manifest-like metadata exists elsewhere. However, metadata hidden at repository-specific paths cannot satisfy a uniform ecosystem contract without an approved discovery mechanism.

## 4. Structural comparison

### 4.1 Catylist manifest

Catylist uses:

- `schema_version: 1`;
- repository identity, role, ownership, lifecycle, and default branch;
- authority paths divided by architecture, specification, ADR, and engineering functions;
- named standards profiles;
- explicit relationships to AES, AEMS, repo_templates, P0, EVO, and Atarix;
- acceptance requirements.

Strengths:

- correct local identity;
- explicit relationship targets;
- explicit authority paths;
- explicit acceptance obligations.

Open problems:

- no declared maturity value;
- role and relationship values have no published normative vocabulary;
- no schema identifier or compatibility policy beyond integer `schema_version`;
- profile paths point to local engineering documents rather than version-pinned upstream AES authority;
- no evidence or last-assessment record;
- no declaration of production-profile participation.

### 4.2 AES manifest

AES also uses `schema_version: 1`, but its structure differs materially from Catylist:

- `documentation_authority` and `authoritative_paths` are nested under `repository` rather than a shared `authority` section;
- governance relationships use `authority_repository`, `managed_by`, and upstream/downstream arrays;
- standards are represented as a repository-local `core` list;
- compliance requirements are represented separately.

Strengths:

- correct identity;
- correct Catylist authority declaration;
- standards and compliance concepts are represented;
- maturity is explicitly declared as `foundation`.

Open problems:

- the same `schema_version: 1` label describes a different document shape from Catylist;
- standard statuses use unnormalized values such as `foundation`, `draft`, and `adopted`;
- the manifest declares downstream repositories but does not encode relationship types or reciprocal constraints;
- standards are listed without revisions or compatibility ranges;
- evidence and assessment state are absent.

### 4.3 EWT manifest

EWT's root `aes-manifest.yaml` is byte-identical to the inspected AES manifest and declares:

- repository name `AES`;
- full name `dlworrell/AES`;
- role `engineering-standards-authority`;
- AES authoritative paths and standards;
- AES dependency relationships.

This is not a minor metadata omission. It is a complete machine-readable identity substitution.

Any scanner trusting repository-local manifest data would classify EWT as AES, assign it standards authority it does not possess, and fail to represent EWT's actual workbench role.

### 4.4 EVO manifest

EVO contains a legitimate local manifest, but it uses a different model:

- `manifest_version: "0.1"` rather than `schema_version: 1`;
- repository identity split across `id`, `name`, and `owner`;
- lifecycle and Project Zero state in separate sections;
- standards as plain string identifiers;
- dependencies by short repository names rather than canonical `owner/name` identities;
- source, testing, benchmarks, and documentation paths.

Strengths:

- correct local identity;
- useful implementation and testing paths;
- explicit lifecycle and dependency intent.

Open problems:

- incompatible schema and naming conventions;
- no Catylist authority declaration;
- no AEMS management or assessment contract;
- standards identifiers appear to include `AES-001`, `AES-002`, and `AES-003`, while the inspected AES manifest identifies `AES-000`, `AES-DEV-001`, and `AES-SEC-001`; resolution is therefore unproven;
- dependency names are not globally canonical;
- no relationship types, evidence, waivers, or compatibility rules.

## 5. Findings

### CAT-MAN-001 — The same schema version does not identify the same schema

- Priority: P0
- Recovery state: Observed
- Confidence: High
- Claim: Catylist and AES both declare `schema_version: 1` while using materially different top-level and nested structures.
- Effect: AEMS cannot safely select one parser or validation schema from the version value alone.
- Required correction: Publish one canonical schema identifier, semantic version, compatibility policy, and validation artifact.
- Punch-list linkage: `CAT-PL-0003`, `CAT-PL-0102`, `CAT-PL-0103`

### CAT-MAN-002 — EWT contains a copied AES identity manifest

- Priority: P0
- Recovery state: Observed
- Confidence: High
- Claim: EWT's root manifest identifies the repository as `dlworrell/AES` and assigns it engineering-standards authority.
- Effect: Machine inventory, authority resolution, dependency analysis, and compliance assessment become actively incorrect.
- Required correction: Replace the copied manifest with an EWT-specific manifest and add a repository-self-identity validation rule.
- Closure evidence: EWT manifest agrees with repository metadata and Catylist inventory; deliberate identity substitution fails CI.
- Punch-list linkage: `CAT-PL-0003`, `CAT-PL-0307`

### CAT-MAN-003 — Mandatory repositories lack manifests at the expected path

- Priority: P0
- Recovery state: Observed
- Confidence: High
- Affected repositories: AEMS, P0, repo_templates, EDT, Atarix
- Claim: No `aes-manifest.yaml` was found at the expected root path.
- Effect: These repositories cannot participate uniformly in machine inventory, authority verification, standards resolution, or consolidated assessment.
- Required correction: After schema approval, add conformant manifests and validation to every mandatory repository.
- Punch-list linkage: `CAT-PL-0003`, `CAT-PL-0005`, `CAT-PL-0301` through `CAT-PL-0309`

### CAT-MAN-004 — EVO uses an incompatible local manifest dialect

- Priority: P1
- Recovery state: Observed
- Confidence: High
- Claim: EVO's manifest describes useful local information but does not conform to the Catylist/AES manifest family.
- Effect: AEMS would require repository-specific parsing and identity normalization.
- Required correction: Migrate EVO to the canonical schema or publish an approved, versioned adapter with lossless conversion evidence.
- Punch-list linkage: `CAT-PL-0003`, `CAT-PL-0307`

### CAT-MAN-005 — Standards references are not reliably resolvable

- Priority: P0
- Recovery state: Observed
- Confidence: Medium to high
- Claim: Standards are represented using different shapes and apparently inconsistent identifiers, without explicit revisions or compatibility ranges.
- Effect: A repository may claim compliance with a standard that AEMS cannot locate, version, or interpret deterministically.
- Required correction: AES must publish a machine-readable standards index; manifests must reference canonical standard IDs and compatible revisions.
- Punch-list linkage: `CAT-PL-0101`, `CAT-PL-0103`

### CAT-MAN-006 — Relationship semantics are prose-dependent

- Priority: P0
- Recovery state: Observed
- Confidence: High
- Claim: Existing manifests use named singleton relationships, upstream/downstream arrays, and short dependency lists without one relationship vocabulary or reciprocal-validation rule.
- Effect: Dependency direction, authority, management, consumption, optionality, and release coupling cannot be inferred safely.
- Required correction: Define typed relationship records with canonical targets, required/optional status, version policy, and reciprocal constraints where applicable.
- Punch-list linkage: `CAT-PL-0002`, `CAT-PL-0003`

### CAT-MAN-007 — Manifest claims are not continuously reconciled with repository reality

- Priority: P0
- Recovery state: Inferred from the EWT substitution and missing manifests
- Confidence: High
- Claim: Current CI does not universally prove that manifest identity matches repository identity or that relationship targets and authority claims are valid.
- Effect: Incorrect metadata can persist while appearing structurally valid YAML.
- Required correction: Add deterministic validation covering repository full name, allowed role, authority owner, relationship targets, standards resolution, path existence, and schema conformance.
- Punch-list linkage: `CAT-PL-0103`, `CAT-PL-0105`

## 6. Required canonical schema properties

The approved ecosystem manifest must provide at least:

```yaml
schema:
  id: catalyst.repository-manifest
  version: 1.0.0

repository:
  full_name: owner/name
  canonical_name: string
  class: authority | control-plane | shared-service | governed-product | organizational | external-reference
  role_id: stable-role-id
  ownership: project-owned | organization-owned | external
  lifecycle: stable-lifecycle-value
  maturity:
    current: 0
    target: 5
  default_branch: main
  production_profile: mandatory | optional | deferred | excluded

authority:
  owner: owner/name
  documentation: local | external-reference
  paths:
    architecture: []
    specifications: []
    decisions: []
    engineering: []

relationships:
  - target: owner/name
    type: governed-by | standards-from | assessed-by | bootstrapped-by | templated-by | consumes | provides-to | publishes-for | external-upstream
    required: true
    version_policy: string

standards:
  - id: AES-...
    revision: compatible-range
    profile: optional-profile-id
    waiver: optional-waiver-record

interfaces:
  manifests: []
  commands: []
  reports: []
  artifacts: []

evidence:
  identity: path-or-uri
  architecture: path-or-uri
  assessment: path-or-uri
  release: path-or-uri

verification:
  state: verified | provisional | contradictory | indeterminate
  assessed_at: ISO-8601
  assessor: tool-and-version
```

The normative schema must define:

- required and optional fields by repository class;
- allowed values and extension rules;
- canonical repository identity format;
- semantic-version compatibility;
- unknown-field handling;
- relationship cardinality and reciprocal constraints;
- standards resolution and waiver behavior;
- path normalization and existence checks;
- deterministic serialization or canonicalization for evidence hashing;
- migration from all existing dialects.

## 7. Minimum validation rules

A conforming validator must reject or report at least:

1. repository `full_name` different from the GitHub repository being assessed;
2. role or class inconsistent with the Catylist inventory;
3. unsupported schema identifier or incompatible version;
4. missing mandatory authority owner;
5. nonexistent relationship targets;
6. invalid relationship direction or cardinality;
7. unresolved standard identifiers or revisions;
8. missing required authority paths;
9. declared paths that do not exist;
10. unsupported lifecycle or maturity values;
11. missing external dependency provenance where applicable;
12. contradictory local and central inventory claims.

Validation must fail closed for identity, authority, standards, and required relationship errors. Informational extensions may be preserved without granting authority.

## 8. Remediation order

1. Freeze repository classes, role IDs, lifecycle values, and relationship types.
2. Approve the canonical manifest schema and compatibility policy.
3. Publish a schema validator with malformed and adversarial fixtures.
4. Correct EWT's substituted identity immediately.
5. Migrate Catylist and AES without losing current semantics.
6. Migrate EVO from its local dialect.
7. Add manifests to AEMS, P0, repo_templates, EDT, Atarix, and remaining governed repositories.
8. Add cross-repository reconciliation and consolidated reporting.
9. Retain a deterministic manifest census as closure evidence.

## 9. Closure criteria

The manifest and authority census may close only when:

1. one normative schema and compatibility policy are approved;
2. every mandatory repository has a conforming manifest at a discoverable canonical path;
3. all repository identities agree with GitHub metadata and the Catylist inventory;
4. no repository claims authority assigned to another repository;
5. every relationship target and required reciprocal constraint validates;
6. every mandatory standard reference resolves to an AES index entry and compatible revision;
7. all required paths exist and match their declared authority function;
8. malformed, contradictory, stale, and cross-repository substitution fixtures fail deterministically;
9. AEMS produces a consolidated manifest and authority report;
10. the retained report contains zero P0 manifest findings.

## 10. Current state

The manifest and authority census is **OPEN**.

The present manifest population cannot support a trustworthy production control plane. The most severe observed defect is the complete AES identity substitution in EWT. More broadly, existing manifests are absent, structurally incompatible, or insufficiently versioned. `CAT-PL-0003` must therefore be completed before repository-wide normalization can be measured reliably.
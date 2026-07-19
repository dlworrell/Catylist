# CAT-REV-001 — Repository Inventory and Identity Census

Status: Active review artifact  
Owner: Catylist  
Parent review: `CAT-REV-001`  
Date: 2026-07-19

## 1. Purpose

This census records the current known Catalyst repository population, the role claimed for each repository, the role assigned by Catylist, and the minimum evidence still required before identity and authority can be considered verified.

This is an evidence ledger, not a maturity award. A repository remains unverified where its README, manifest, implementation, and governing authority have not all been reconciled.

## 2. Classification

Each repository is assigned one review class:

- **authority** — defines governance or normative engineering obligations;
- **control-plane** — assesses, creates, repairs, or coordinates governed repositories;
- **shared service** — provides reusable engineering capability without owning policy;
- **governed product** — implements a product or reference system;
- **organizational** — owns company or public organizational material;
- **external/reference** — imported, forked, vendored, or consumed without Catalyst authority over the upstream project.

Identity state:

- **verified** — Catylist assignment, repository declaration, and machine-readable metadata agree;
- **provisional** — assignment is plausible but one or more evidence surfaces remain incomplete;
- **contradictory** — declarations disagree materially;
- **indeterminate** — insufficient evidence has been inspected.

## 3. Core ecosystem inventory

| Repository | Catylist class | Assigned role | Observed declaration | Identity state | Required verification |
|---|---|---|---|---|---|
| `dlworrell/Catylist` | authority | Program umbrella, ecosystem architecture, governance, repository relationships and authority boundaries | README and manifest agree on the program-governance role | provisional | Validate every declared relationship against the target repository; publish the executable ecosystem contract |
| `dlworrell/AES` | authority | Normative engineering standards, evidence obligations, terminology and standard-level templates | README declares canonical standards authority | provisional | Freeze standard metadata schema; prove machine resolution of mandatory standards and profiles |
| `dlworrell/AEMS` | control-plane | Assessment, enforcement, orchestration, reporting and remediation | README expresses evidence philosophy but not a complete operational role contract | provisional | Establish architecture, CLI/API contract, rule resolution, report schema, exit semantics and retained evidence |
| `dlworrell/P0` | control-plane | Repository initiation, inspection, bootstrap, remediation and readiness | README identifies the repository as AES and uses obsolete authority relationships | contradictory | Correct charter, README and manifest; demonstrate clean bootstrap and remediation cycles |
| `dlworrell/repo_templates` | control-plane | Canonical reusable repository scaffolding | README declares template authority but describes the production baseline as planned/proposed | provisional | Freeze template classes and version; retain generation fixtures; require independent AEMS pass |
| `dlworrell/EWT` | shared service | Engineer-facing workspace, toolchain, debugging, packaging and UX | README agrees with the shared-workbench role and disclaims policy authority | provisional | Approve architecture and interfaces; classify participation in the minimum production profile |
| `dlworrell/engineering-docs-toolkit` | shared service | Semantic document engineering, validation, transformation and publication | README declares EDT role and substantial implemented capability | provisional | Reconcile 1.0 claims with normative specifications, release evidence and HERKULES workflow |
| `dlworrell/evo` | shared service | Reproducible evolutionary optimization infrastructure | README declares Project Zero/bootstrap status | provisional | Define supported API and evidence baseline or explicitly defer from the first production profile |

## 4. Governed products and integration exemplars

| Repository | Catylist class | Assigned role | Observed declaration | Identity state | Required verification |
|---|---|---|---|---|---|
| `dlworrell/atarix` | governed product | Reference governed systems project and primary cross-system qualification target | Repository contains architecture, implementation, tests and retained evidence under active closure engineering | provisional | Complete ecosystem normalization and remaining hardware evidence; verify full governance-to-release workflow |
| `dlworrell/herkules-1934-english` | governed product | EDT flagship corpus, translation and reproducible publication exemplar | Repository exists and is named by EDT as a flagship workflow | indeterminate | Inspect charter, manifest, source provenance, build, generated outputs and reproducibility evidence |
| `dlworrell/JAG` | governed product | Product/project exemplar within Catalyst | Repository exists but inspected evidence is insufficient to establish its production role | indeterminate | Establish charter, manifest, architecture, delivery model and relationship to Just-a-Geek-LLC |
| `dlworrell/Just-a-Geek-LLC` | organizational | Company and public-facing organizational authority | Repository exists; role is referenced by ecosystem documents | indeterminate | Inspect organizational charter, publication authority, legal boundaries and relationship to JAG |

## 5. External and reference repositories

| Repository | Current disposition | Catalyst obligation before production use |
|---|---|---|
| `dlworrell/65x02` | external/reference | Record upstream origin, fork intent, license, pinned revision, integrity and update policy |
| `dlworrell/CLK` | external/reference | Record upstream origin, fork intent, license, pinned revision, integrity and update policy |
| `dlworrell/ulx3s` | external/reference | Record upstream origin, hardware/toolchain dependency, license, pinned revision and update policy |
| `dlworrell/cglm` | external/reference | Record upstream origin, license, pinned revision, integrity and vulnerability/update policy |
| `dlworrell/Vega816` | external/reference or governed dependency, pending classification | Determine whether Catalyst owns modifications, merely studies the design, or consumes artifacts |
| `dlworrell/BB816-MATX-PCIE` | external/reference or governed dependency, pending classification | Determine design authority, provenance, license, manufacturing status and supported dependency relationship |

No external/reference repository may silently become part of a production release path. Entry into a supported profile requires an explicit intake record covering provenance, license, version pinning, integrity, maintenance and replacement strategy.

## 6. Identity findings

### CAT-ID-001 — P0 is materially misidentified

- Recovery state: Observed
- Confidence: High
- Claim: P0's primary declaration identifies it as AES rather than the repository bootstrap and readiness control-plane.
- Effect: Human readers and automation cannot rely on repository-local identity.
- Punch-list linkage: `CAT-PL-0001`

### CAT-ID-002 — Repository roles are mostly prose-only

- Recovery state: Observed
- Confidence: High
- Claim: Several roles are described consistently in README documents, but no single versioned schema currently proves that the same vocabulary, cardinality and dependency rules are enforced everywhere.
- Effect: Role drift can occur without a deterministic conformance failure.
- Punch-list linkage: `CAT-PL-0002`, `CAT-PL-0003`

### CAT-ID-003 — Lifecycle language cannot be compared

- Recovery state: Observed
- Confidence: High
- Claim: Repositories use terms including active, foundation, bootstrap, stable, mature, complete and feature-complete without a common normative mapping.
- Effect: Portfolio status and release readiness cannot be calculated consistently.
- Punch-list linkage: `CAT-PL-0004`

### CAT-ID-004 — External dependency ownership is unresolved

- Recovery state: Inferred from repository population; individual dependency edges remain indeterminate
- Confidence: Medium
- Claim: Multiple imported or reference repositories exist, but their exact production dependency relationships and support obligations are not yet centrally recorded.
- Effect: Licensing, provenance, integrity, update and maintenance risk may remain invisible.
- Punch-list linkage: `CAT-PL-0005`, `CAT-PL-0401` / `WF-008`

## 7. Minimum canonical inventory record

The future machine-readable ecosystem inventory must contain at least:

```yaml
repository:
  id: catalyst.repository.v1
  full_name: owner/name
  canonical_name: string
  class: authority | control-plane | shared-service | governed-product | organizational | external-reference
  role_id: stable-role-identifier
  lifecycle: defined-lifecycle-value
  maturity:
    current: 0..5
    target: 0..5
  authority_owner: owner/name
  documentation_authority: local | external-reference
  production_profile: mandatory | optional | deferred | excluded
  dependencies:
    - repository: owner/name
      relationship: stable-relationship-identifier
      required: true
      version_policy: string
  standards:
    - id: stable-standard-id
      revision: string
      profile: string
  evidence:
    identity: path-or-uri
    architecture: path-or-uri
    assessment: path-or-uri
  verification:
    state: verified | provisional | contradictory | indeterminate
    assessed_at: ISO-8601 timestamp
    assessor_version: string
```

The final schema may extend this record but must not omit its semantics without an approved replacement.

## 8. Census closure criteria

`CAT-PL-0005` may close only when:

1. every repository in the supported Catalyst population has one canonical inventory record;
2. repository-local manifests agree with the Catylist-owned system inventory;
3. all relationship targets exist and reciprocal constraints are validated where required;
4. every external/reference dependency has provenance, license, pinning, integrity and update policy;
5. lifecycle and maturity values use the approved shared vocabulary;
6. an automated census reports zero contradictory or indeterminate mandatory repositories;
7. the resulting report is deterministic and retained as evidence.

## 9. Current state

The inventory is **OPEN**.

The repository population and initial roles are now recorded, but identity verification remains blocked by the absence of the canonical role taxonomy, ecosystem schema, normalized lifecycle vocabulary and automated cross-repository census.
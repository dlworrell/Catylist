# CAT-REV-001 — Repository Role and Lifecycle Taxonomy Assessment

Status: Active review artifact  
Owner: Catylist  
Parent review: `CAT-REV-001`  
Date: 2026-07-19

## 1. Purpose

This assessment determines whether Catalyst has one sufficiently precise repository-role taxonomy and one lifecycle vocabulary that can be consumed consistently by humans, manifests, templates, AEMS, P0, and governed repositories.

The assessment distinguishes three concepts that are currently at risk of being conflated:

1. **repository class** — what kind of authority or engineering function the repository primarily owns;
2. **lifecycle state** — where the repository is in its existence and support lifecycle;
3. **production maturity** — how completely its declared obligations are realized and evidenced.

These dimensions must remain independent. A repository may be `active` while only maturity level 2, or `maintenance` while remaining maturity level 5 for its supported scope.

## 2. Existing taxonomy

The current Catylist taxonomy defines these primary classes:

- governance;
- standards;
- enforcement and automation;
- template;
- bootstrap and execution;
- shared infrastructure;
- product or reference implementation;
- experimental;
- external reference.

The taxonomy also states that each project-owned repository must declare one primary class and may declare secondary capabilities. This is a sound authority-preservation rule.

The current recommended lifecycle values are:

- proposed;
- bootstrap;
- active;
- maintenance;
- deprecated;
- archived;
- external-reference.

## 3. Findings

### CAT-TAX-001 — Review artifacts and architecture use competing class vocabularies

- Priority: P0
- Recovery state: Observed
- Confidence: High
- Claim: The architecture taxonomy uses `governance`, `standards`, `enforcement-and-automation`, `template`, `bootstrap-and-execution`, `shared-infrastructure`, `product-or-reference-implementation`, `experimental`, and `external-reference`, while the identity census uses `authority`, `control-plane`, `shared-service`, `governed-product`, `organizational`, and `external-reference`.
- Effect: The same repository can receive different class values depending on which Catylist document or future schema is consulted.
- Required correction: Select one canonical machine vocabulary and define any human-facing labels as aliases, not parallel taxonomies.
- Punch-list linkage: `CAT-PL-0002`.

### CAT-TAX-002 — Organizational authority is not represented in the current architecture taxonomy

- Priority: P1
- Recovery state: Observed
- Confidence: High
- Claim: `Just-a-Geek-LLC` is treated elsewhere as organizational and public-facing authority, but the current taxonomy has no organizational class.
- Effect: Company governance may be misclassified as program governance, product work, or external material.
- Required correction: Add an explicit organizational class or establish a justified mapping that preserves the boundary between company authority and Catalyst engineering authority.
- Punch-list linkage: `CAT-PL-0002`, `CAT-PL-0309`.

### CAT-TAX-003 — Control-plane responsibilities are split into overlapping classes without cardinality rules

- Priority: P0
- Recovery state: Observed
- Confidence: High
- Claim: Enforcement, templates, and bootstrap are separate classes, but AEMS, P0, and `repo_templates` collaborate as one repository-management control plane. The taxonomy does not define which relationships are mandatory or prohibited among them.
- Effect: P0, AEMS, and templates may duplicate policy, generation, assessment, or remediation authority.
- Required correction: Preserve their separate primary classes while defining explicit control-plane relationship semantics and prohibited authority transfers.
- Punch-list linkage: `CAT-PL-0002`, `CAT-PL-0003`.

### CAT-TAX-004 — `external-reference` is incorrectly used as both a class and lifecycle state

- Priority: P0
- Recovery state: Observed
- Confidence: High
- Claim: `external-reference` appears in the class list and again in the lifecycle list.
- Effect: A repository's ownership/provenance category becomes entangled with its support state. An external reference may itself be active, pinned, deprecated, or archived from Catalyst's perspective.
- Required correction: Remove `external-reference` from lifecycle. Represent external ownership as class or provenance, and represent Catalyst support disposition independently.
- Punch-list linkage: `CAT-PL-0004`, `CAT-PL-0005`.

### CAT-TAX-005 — `bootstrap` is overloaded as both repository purpose and lifecycle state

- Priority: P1
- Recovery state: Observed
- Confidence: High
- Claim: P0 owns bootstrap as a persistent system function, while `bootstrap` is also proposed as a transient lifecycle state.
- Effect: A repository such as P0 can be permanently bootstrap-classed but no longer in lifecycle bootstrap, creating ambiguous statements such as “P0 is bootstrap.”
- Required correction: Use distinct identifiers such as `bootstrap-control` for role and `initializing` for lifecycle.
- Punch-list linkage: `CAT-PL-0002`, `CAT-PL-0004`.

### CAT-TAX-006 — Lifecycle states lack entry, exit, and support obligations

- Priority: P0
- Recovery state: Observed
- Confidence: High
- Claim: Lifecycle values are listed but not normatively defined with allowed transitions, required evidence, release obligations, or dependency treatment.
- Effect: Repositories may self-label as active, maintenance, deprecated, or archived without consistent operational consequences.
- Required correction: Define a state machine with transition evidence and downstream notification requirements.
- Punch-list linkage: `CAT-PL-0004`.

### CAT-TAX-007 — Maturity language remains separate and unbound

- Priority: P0
- Recovery state: Observed
- Confidence: High
- Claim: Manifests and READMEs use `foundation`, `project-zero`, `stable`, `mature`, `complete`, and `feature-complete`, while CAT-REV-001 defines numeric production maturity levels 0 through 5.
- Effect: Portfolio status cannot be calculated or compared deterministically.
- Required correction: Adopt a canonical numeric maturity value and permit descriptive labels only as non-normative summaries or versioned aliases.
- Punch-list linkage: `CAT-PL-0004`.

## 4. Proposed canonical dimensions

### 4.1 Repository class

A repository must declare exactly one primary class from the following proposed vocabulary:

| Identifier | Meaning | Typical repository |
|---|---|---|
| `program-governance` | Ecosystem architecture, authority boundaries, repository relationships, program decisions | Catylist |
| `engineering-standards` | Reusable normative engineering requirements and standard evidence obligations | AES |
| `assessment-enforcement` | Deterministic assessment, reporting, evidence evaluation and policy enforcement | AEMS |
| `repository-bootstrap` | Repository initiation, inspection, migration, remediation orchestration and readiness workflows | P0 |
| `repository-template` | Versioned reusable repository scaffolding and generation inputs | repo_templates |
| `shared-service` | Reusable engineering library, tool or service without policy authority | EDT, EWT, EVO |
| `governed-product` | Product, platform, operating system, application or reference implementation | Atarix, JAG, HERKULES |
| `organizational-authority` | Company, legal, public identity and organizational publication authority | Just-a-Geek-LLC |
| `experimental` | Exploratory work excluded from production claims unless promoted | code-noodling |
| `external-reference` | Upstream, imported, forked or reference material not governed as Catalyst-owned authority | 65x02, CLK, ulx3s, cglm pending exact intake records |

Secondary capabilities may be declared, but they do not transfer authority. A shared service that contains templates does not become the repository-template authority. A product that contains local standards does not become the engineering-standards authority.

### 4.2 Lifecycle state

A repository must declare exactly one lifecycle state:

| State | Meaning | Minimum transition evidence |
|---|---|---|
| `proposed` | Approved concept; repository may not yet contain a supported realization | charter or accepted initiating decision |
| `initializing` | Identity, manifest, authority, baseline structure and initial contracts are being established | bootstrap plan and named owner |
| `active` | Supported work and compatible change are expected | current owner, supported branch, assessment path |
| `maintenance` | Supported scope is stable; changes are primarily fixes, security work and compatibility maintenance | maintenance policy and supported versions |
| `deprecated` | New use is discouraged and migration is required | deprecation decision, migration path, deadline or review date |
| `retired` | No supported production use remains, but historical evidence and migration records are retained | retirement evidence and dependency census showing no unsupported consumers |
| `archived` | Repository is immutable or administratively archived after retirement or external preservation | integrity record and archival location |

Allowed normal transitions:

```text
proposed -> initializing -> active -> maintenance -> deprecated -> retired -> archived
```

Exceptional transitions require an ADR or recovery record. Reactivation from `maintenance`, `deprecated`, or `retired` requires reassessment and explicit compatibility treatment.

### 4.3 Production maturity

Production maturity is independent of lifecycle and uses CAT-REV-001 levels:

- 0 — Undefined
- 1 — Declared
- 2 — Bootstrapped
- 3 — Functional
- 4 — Production candidate
- 5 — Production

A maturity value must be accompanied by:

- target maturity;
- assessed maturity;
- assessment revision;
- evidence reference;
- assessment timestamp;
- assessor identity/version.

A repository must not self-award maturity solely through README language.

### 4.4 Production-profile participation

Each repository must declare one profile disposition:

- `mandatory` — required for the profile to function;
- `optional` — supported but not required;
- `deferred` — intentionally excluded until a later profile revision;
- `experimental` — available without production guarantees;
- `excluded` — outside the profile and must not appear in its release path.

This field determines whether an immature repository blocks a specific Catalyst production profile.

## 5. Authority invariants

A canonical schema and AEMS validator must enforce these invariants:

1. exactly one primary repository class is declared;
2. secondary capabilities cannot grant authority owned by another primary class;
3. `program-governance` is the only class that may define ecosystem-wide repository relationships;
4. `engineering-standards` is the only class that may define reusable normative engineering requirements;
5. `assessment-enforcement` may evaluate declared policy but may not invent or redefine policy;
6. `repository-template` may encode adopted policy but may not become the policy authority;
7. `repository-bootstrap` may coordinate change but may not silently modify authority or waive standards;
8. `shared-service` and `governed-product` repositories own their local architecture but not program-wide governance;
9. `external-reference` repositories must not be rewritten merely to appear Catalyst-conformant;
10. organizational authority and engineering authority remain explicitly separated.

## 6. Proposed manifest representation

```yaml
repository:
  class: governed-product
  secondary_capabilities:
    - reference-implementation

lifecycle:
  state: active
  since: 2026-07-01
  owner: dlworrell
  policy: docs/lifecycle.md

maturity:
  current: 3
  target: 5
  assessed_by: aems/0.1.0
  assessed_at: 2026-07-19T00:00:00Z
  evidence: evidence/aems/latest.json

production_profiles:
  catalyst-v1:
    disposition: mandatory
```

## 7. Required remediation order

1. Approve or revise the canonical class vocabulary.
2. Approve lifecycle states and transition semantics.
3. Approve maturity levels and evidence requirements.
4. Encode all three dimensions in the ecosystem manifest schema.
5. Update the Catylist inventory and all repository-local manifests.
6. Implement fail-closed AEMS validation for unknown or contradictory values.
7. Generate a deterministic portfolio report showing class, lifecycle, maturity and production-profile participation separately.

## 8. Closure criteria

`CAT-PL-0002` and `CAT-PL-0004` may close only when:

1. one normative Catylist document owns the class, lifecycle and maturity vocabularies;
2. each term has machine identifier, definition and authority consequences;
3. lifecycle transitions have entry and exit evidence;
4. class, lifecycle and maturity are represented as independent manifest fields;
5. every mandatory repository uses only approved values;
6. AEMS rejects unknown, contradictory and authority-invalid combinations;
7. the consolidated inventory contains no prose-only status claims used as release gates;
8. retained tests cover valid values, invalid values, illegal transitions and authority violations.

## 9. Current state

The taxonomy and lifecycle normalization work is **OPEN**.

The current Catylist draft contains a useful foundation, but competing class vocabulary, overloaded lifecycle terms, missing organizational authority, and undefined transition semantics prevent deterministic ecosystem enforcement.
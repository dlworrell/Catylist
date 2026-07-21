# CAT-CON-001 — Engineering Closure Metadata Contract

Status: Draft  
Owner: Catylist  
Type: Program contract  
Version: 0.1.0

## 1. Purpose

This contract defines the minimum machine-readable record required to describe a Catalyst engineering closure unit under CAT-002.

It does not replace project specifications, tests, implementation records, architecture decisions, or review judgment. It provides a common exchange format through which Catylist, AES, AEMS, P0, repo_templates, EDT, EVO, EWT, and governed projects can identify the same engineering claim and its supporting representations and transformations.

Production readiness remains a derived conclusion. A record conforming to this contract does not by itself establish closure.

## 2. Governing architecture

This contract is subordinate to:

- CAT-001 — Catalyst System Architecture;
- CAT-002 — Engineering Representation, Closure, and Recovery;
- CAT-REV-001 — Catalyst Functional 360° Production Readiness Review.

Where this contract conflicts with CAT-002, CAT-002 governs and the contract shall be revised.

## 3. Contract boundary

The contract describes one claim-relative closure unit. A closure unit shall identify:

- its stable identity and scope;
- authoritative Intent;
- applicable Realization;
- required and retained Evidence;
- consequential transformations among representations;
- closure state;
- recovery classification where reconstruction occurred;
- assumptions, exclusions, unresolved gaps, authority, confidence, and provenance.

The contract does not require every representation to be stored in the same repository. It requires identities and relationships to be explicit and resolvable.

## 4. Canonical vocabulary

### 4.1 Representation classes

The representation class shall be one of:

- `intent`
- `realization`
- `evidence`

### 4.2 Closure states

The closure state shall be one of:

- `PROPOSED`
- `OPEN`
- `VERIFYING`
- `DIVERGENT`
- `CLOSED`
- `SUPERSEDED`
- `INDETERMINATE`

`CLOSED` is permitted only when the declared claim and scope have sufficient Intent, all required Realizations are identified and applicable, required Evidence meets its declared obligations, required transformations are traceable, and no unresolved mandatory divergence invalidates the claim.

### 4.3 Recovery classes

Recovery classification shall be one of:

- `R0_OBSERVED`
- `R1_CORRECTED`
- `R2_RECONSTRUCTED`
- `R3_INFERRED`
- `RX_INDETERMINATE`

Recovery classification describes how the record or represented artifact was obtained. It does not confer normative authority.

### 4.4 Evidence levels

Evidence level shall be one of:

- `E0` — structural checks;
- `E1` — component evidence;
- `E2` — emulator, model, or reference evidence;
- `E3` — realization evidence such as simulation, synthesis, integration, or deployed execution;
- `E4` — differential or independent implementation evidence;
- `E5` — physical or operational evidence;
- `E6` — representative end-to-end system evidence.

Evidence levels are claim-relative. A numerically higher level does not automatically satisfy lower-level diagnostic or structural obligations.

### 4.5 Authority classes

Authority shall be one of:

- `normative`
- `delegated`
- `descriptive`
- `recovered`
- `generated`
- `unknown`

A recovered or generated representation shall not silently acquire normative authority.

### 4.6 Requirement disposition

A representation or evidence obligation shall declare one of:

- `required`
- `deferred`
- `not_applicable`
- `optional`

`deferred` and `not_applicable` are not interchangeable. Deferred work leaves the associated claim open unless the declared scope explicitly excludes it.

## 5. Record structure

The canonical serialized record is JSON and shall validate against `schemas/catalyst/engineering-closure-v1.schema.json`.

YAML may be used as an authoring representation only when it round-trips without semantic loss to the canonical JSON data model.

The top-level record contains:

- `schema`
- `closure_unit`

The closure unit contains:

- `id`
- `claim`
- `scope`
- `owner`
- `state`
- `representations`
- `transformations`
- `assumptions`
- `exclusions`
- `gaps`
- `provenance`

## 6. Stable identity

A closure-unit identifier shall be stable within its governing authority and shall not be reused for a materially different claim.

Artifact references should use immutable identities where practical, including:

- repository and path;
- commit, tag, release, digest, or immutable object identifier;
- schema or format version;
- external authority identifier where the artifact is not repository-owned.

A mutable branch name or web location may be included for navigation but shall not be the sole identity used for closure evidence.

## 7. Representations

Each representation record shall declare:

- a stable local identifier;
- representation class;
- title or concise description;
- authority;
- requirement disposition;
- one or more artifact references when an artifact exists;
- recovery classification when recovered, reconstructed, or inferred;
- confidence when uncertainty is material;
- limitations.

A descriptive Intent representation recovered from Realization shall remain `descriptive` or `recovered` unless a competent authority explicitly adopts it as normative.

## 8. Transformations

Each consequential transformation record shall declare:

- stable local identifier;
- input representation identities;
- output representation identities;
- method;
- tool identities and versions where applicable;
- assumptions and configuration;
- authority of the output;
- determinism;
- reversibility;
- known information loss;
- provenance references;
- verification status.

Transformation direction is not restricted to forward development. Recovery and reconstruction transformations are first-class records.

## 9. Evidence obligations

Evidence representations shall declare:

- the claim or representation relationship supported;
- required evidence level;
- achieved evidence level, if any;
- method;
- result;
- retained artifact references;
- environment and configuration sufficient for reproduction;
- limitations and validity window where applicable.

Allowed result values are:

- `not_run`
- `passed`
- `failed`
- `inconclusive`
- `not_applicable`

A passing result is not sufficient where the evidence method, provenance, environment, or supported claim is absent.

## 10. Closure decision

A closure decision shall identify:

- the resulting closure state;
- decision authority;
- decision timestamp;
- reviewed record revision;
- rationale;
- unresolved gaps;
- evidence limitations;
- superseding closure unit, where applicable.

Automation may recommend or validate a closure state. It shall not silently assume authority to make a normative closure decision.

## 11. Confidence

Confidence is distinct from authority.

Where used, confidence shall be represented as:

- `high`
- `medium`
- `low`
- `unknown`

A highly confident descriptive or inferred statement remains non-normative. A normative statement may have high authority while still being incomplete or ambiguous.

## 12. Minimum conformance profiles

### 12.1 Draft profile

A draft closure record shall include:

- stable identity;
- claim;
- scope;
- owner;
- state;
- at least one Intent representation;
- declared Evidence obligations;
- assumptions and known gaps.

### 12.2 Verification profile

A record in `VERIFYING` shall additionally include:

- required Realization identities;
- evidence methods and required levels;
- transformation records sufficient to relate Intent, Realization, and Evidence;
- reproduction information for retained evidence.

### 12.3 Closed profile

A record in `CLOSED` shall additionally include:

- all required representations;
- fulfilled required evidence obligations;
- retained evidence artifacts;
- no unresolved mandatory divergence;
- a closure decision with identifiable authority;
- immutable provenance sufficient to audit the decision.

## 13. Validation responsibilities

The current allocation of structural checks, semantic validation, and review
authority is recorded in
[CAT-CON-001 — Enforcement Boundary](CAT-CON-001-Enforcement-Boundary.md).
That profile may document enforcement without assigning new normative meaning
to this contract or CAT-002.

Catylist owns the common semantic contract and schema namespace.

AES may define profile-specific obligations and minimum evidence requirements.

AEMS shall validate records, resolve applicable profiles, report missing relationships, and refuse unsupported closure.

P0 shall create or recover records during repository bootstrap and remediation while preserving uncertainty.

repo_templates shall instantiate valid draft records for supported repository classes.

EDT may emit and publish typed representation metadata without changing authority.

EVO may navigate declared transformations while preserving provenance, assumptions, and human decision boundaries.

EWT may visualize records and gaps but shall not substitute presentation for retained evidence.

Governed projects own project-local claims, artifacts, and closure decisions within delegated authority.

## 14. Compatibility and evolution

The schema identifier is versioned. Additive optional fields may be introduced within a compatible minor revision. Removing fields, changing field meaning, tightening an existing accepted value without migration, or changing closure semantics requires a new major schema version.

Consumers shall reject unknown major versions unless an explicit compatibility adapter is available and evidenced.

## 15. Initial acceptance criteria

CAT-CON-001 reaches its first reviewable increment when:

1. the JSON Schema validates a complete closed example and rejects unsupported closure examples;
2. the schema distinguishes required, deferred, and not-applicable obligations;
3. recovery class and authority are independently represented;
4. transformation provenance and information loss are representable;
5. evidence obligations and achieved evidence are independently represented;
6. an ATARIX closure unit can be represented without project-specific changes to the common schema;
7. AEMS and P0 owners can implement against the contract without relying on conversational context.

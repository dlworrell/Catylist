# CAT-002 — Engineering Representation, Closure, and Recovery

Status: Draft
Owner: Catylist
Type: Program architecture
Lifecycle: Proposed

## 1. Purpose

This document defines the Catalyst engineering representation model. It establishes how intent, realization, and evidence are represented, related, reviewed, recovered, and declared complete across governed repositories.

CAT-002 supplements CAT-001. CAT-001 defines the Catalyst system architecture and authority boundaries. CAT-002 defines the representation and closure model used within that architecture.

## 2. Scope

CAT-002 applies to architecture, specifications, source code, firmware, HDL, hardware designs, data formats, tests, proofs, measurements, reports, recovery work, and other governed engineering artifacts.

It does not require every artifact to contain all representations in one file. It requires the representations and their relationships to be explicit, traceable, and reviewable.

## 3. Engineering representation model

A governed engineering capability shall be understood through three representation classes:

```text
                         Intent
             requirements, semantics, doctrine
                    /                   \
                   /                     \
          Realization ---------------- Evidence
       code, hardware, data       tests, proofs, traces,
          and operations          measurements and records
```

### 3.1 Intent

Intent states what is required, permitted, prohibited, expected, or claimed. Intent may include:

- architecture and doctrine;
- requirements and specifications;
- behavioral contracts;
- security and safety constraints;
- compatibility commitments;
- resource and error budgets;
- acceptance criteria.

Intent may be normative or descriptive. A descriptive specification recovered from an implementation shall not silently acquire normative authority.

### 3.2 Realization

Realization is the concrete system that attempts to satisfy intent. It may include:

- software and firmware;
- HDL and physical hardware;
- generated code and public headers;
- schemas, data layouts, and persistent formats;
- deployed services and operational procedures;
- compiler, synthesis, and transformation outputs.

A realization is not authoritative merely because it exists or executes.

### 3.3 Evidence

Evidence supports or falsifies claims about intent and realization. It may include:

- unit, integration, system, and conformance tests;
- formal proofs and static analysis;
- simulation, emulation, and reference-model comparison;
- benchmarks and measurements;
- logic-analyzer captures, traces, logs, and fault records;
- checksums, signatures, journals, parity, ECC syndromes, and replicas;
- review records and reproducible build outputs.

Evidence shall identify the claim it supports, the method used, its provenance, and its limitations.

## 4. Closure

A capability is closed only with respect to a declared claim and scope.

Closure requires:

1. sufficient intent to state the claim;
2. identified realizations that are required to satisfy it;
3. evidence appropriate to the claim;
4. traceable agreement between the three representations;
5. no unresolved divergence that invalidates the claim.

Closure shall not mean that the entire system is completely known, perfectly observed, or permanently correct.

### 4.1 Closure states

The standard closure states are:

- **PROPOSED** — intent is under consideration;
- **OPEN** — one or more required representations or relationships are missing;
- **VERIFYING** — required realizations exist and evidence is being produced;
- **DIVERGENT** — intent, realization, or evidence disagree;
- **CLOSED** — the declared claim is supported within its stated scope;
- **SUPERSEDED** — a later closure unit replaces the claim;
- **INDETERMINATE** — available information cannot support a defensible decision.

A failing test shall not automatically be classified as an implementation defect. It may expose defective evidence, incomplete intent, an invalid assumption, or a defective realization.

## 5. Closure units

Engineering work should be divided into closure units small enough to review coherently.

A closure unit shall identify:

- a stable identifier;
- the claim or capability being advanced;
- authoritative intent sources;
- applicable realizations;
- evidence obligations;
- assumptions and exclusions;
- security, compatibility, persistence, and recovery impact;
- current closure state;
- unresolved gaps.

Example:

```yaml
closure_unit:
  id: ATX-MBX-PING-001
  claim: A valid mailbox PING returns PONG and preserves the transaction identifier.
  intent:
    authority: normative
    sources:
      - docs/mailbox-protocol-v1.md
  realizations:
    public_header: required
    firmware: required
    emulator: required
    rtl: required
    physical_hardware: deferred
  evidence:
    encoding_vectors: required
    emulator_tests: required
    rtl_simulation: required
    differential_test: required
    hardware_capture: deferred
  state: OPEN
```

`deferred` and `not_applicable` are distinct. Deferred work leaves the relevant claim open unless the declared scope explicitly excludes it.

## 6. Transformations and edge records

The relationships between representations are first-class engineering artifacts.

Common transformations include:

```text
Intent -> Realization      design, refinement, compilation, synthesis
Intent -> Evidence         test derivation, proof obligations, acceptance criteria
Realization -> Evidence    execution, simulation, measurement, verification
Realization -> Intent      reverse engineering, behavioral extraction
Evidence -> Intent         requirement discovery, validation, revision
Evidence -> Realization    diagnosis, reconstruction, system identification
```

Each consequential transformation should record:

- input identities and versions;
- output identities and versions;
- method and tool versions;
- assumptions and configuration;
- determinism or nondeterminism;
- authority of the result;
- provenance and integrity information;
- known information loss;
- reversibility and recovery limits.

Recoverability is determined primarily by the information preserved across these transformations, not by the mere survival of isolated artifacts.

## 7. Development-cycle requirements

A governed development cycle shall use closure units as the default unit of consequential work.

Before implementation begins, the work item shall identify intent and evidence obligations sufficiently to make the proposed behavior reviewable.

A substantive pull request shall state:

- the closure unit or units advanced;
- the intent changed or implemented;
- realizations changed;
- evidence added or updated;
- unresolved gaps;
- resulting closure state.

A realization change shall normally include new or updated evidence. When evidence is unaffected, the pull request shall explain why.

A closure unit shall not be marked CLOSED solely because:

- documentation exists;
- code compiles;
- one test passes;
- one hardware demonstration succeeds;
- a generated report claims success.

## 8. Evidence levels

Projects may refine evidence levels, but the following general ladder is recommended:

- **E0 — Structural evidence:** parsing, linting, schema, link, and source checks;
- **E1 — Component evidence:** unit tests and local proofs;
- **E2 — Reference evidence:** emulator, model, or known-good comparison;
- **E3 — Realization evidence:** simulation, synthesis, integration, or deployed execution;
- **E4 — Differential evidence:** independent implementations tested against common vectors;
- **E5 — Physical or operational evidence:** measurements from the target platform;
- **E6 — System evidence:** end-to-end behavior under representative operating conditions.

The required level depends on the claim. Higher evidence levels do not automatically replace lower-level diagnostic evidence.

## 9. Recovery model

Recovery is an inverse engineering process. Missing representations may be recovered only to the degree supported by surviving constraints.

### 9.1 Recovery classes

- **R0 — Observed:** surviving material is acquired without reconstruction;
- **R1 — Corrected:** redundancy uniquely corrects a bounded error, such as ECC or parity recovery;
- **R2 — Reconstructed:** metadata, journals, mappings, or other transformation records support a unique or near-unique reconstruction;
- **R3 — Inferred:** multiple valid candidates remain and a candidate is selected using context, heuristics, or probability;
- **RX — Indeterminate:** available constraints do not support a defensible reconstruction.

Recovered artifacts shall state whether they are normative, descriptive, inferred, or unknown in authority.

### 9.2 Recovery record

A recovery record shall preserve:

- source artifacts and acquisition method;
- recovery classification;
- transformation method;
- assumptions;
- integrity checks;
- confidence or error bounds;
- alternative candidates;
- unresolved identity or chronology;
- destructive actions, if any.

Original evidence shall not be overwritten by a recovered result.

## 10. Persistent data and memory systems

Systems intended to support recovery should preserve sufficient independent constraints, including as appropriate:

- stable object identities;
- format and schema versions;
- lengths and bounds;
- checksums and cryptographic hashes;
- generation counters;
- transaction identifiers and commit markers;
- journals and audit records;
- ECC, parity, replicas, or erasure coding;
- logical-to-physical mapping provenance;
- migration and compatibility behavior.

A recovery percentage shall not collapse unlike claims. Content recovery, identity recovery, placement recovery, chronology recovery, and integrity verification should be reported separately.

## 11. Probabilistic and quantum systems

CAT-002 applies to probabilistic and quantum systems with additional qualifications.

### 11.1 Claim-relative probabilistic closure

For probabilistic systems, closure shall identify:

- the supported claim;
- accepted assumptions;
- confidence or credible interval;
- error or failure bound;
- sample count and statistical method;
- verification resource cost;
- excluded claims.

Evidence need not reconstruct the complete internal state. It must be sufficient to support the declared claim within stated bounds.

### 11.2 Layered realization

A scalable quantum realization may include:

```text
application intent
    -> quantum algorithm
    -> logical circuit
    -> fault-tolerant circuit
    -> error-correction schedule
    -> native-gate circuit
    -> pulse and control realization
    -> physical device
```

Each transformation shall preserve traceability and have evidence appropriate to its layer.

### 11.3 Quantum recovery

Quantum recovery generally targets logical information rather than an exact physical trajectory.

Quantum recovery classes may refine the general model as:

- **Q0 — Classical outcome observed;**
- **Q1 — Error or constraint violation detected;**
- **Q2 — Error corrected within a declared code guarantee;**
- **Q3 — Error class decoded probabilistically;**
- **Q4 — Logical result certified within a stated failure bound;**
- **QX — Evidence insufficient to distinguish logical success from failure.**

No-cloning, measurement disturbance, probabilistic outcomes, and syndrome degeneracy prevent CAT-002 from requiring complete physical-state reconstruction.

### 11.4 Verification cost

Verification cost is part of the evidence model. A theoretically valid verification method that requires impractical or exponential resources shall not be treated as an operational closure mechanism without explicit qualification.

A probabilistic or quantum closure record should include applicable quantities such as:

- physical and logical resource counts;
- circuit depth or execution duration;
- code distance and syndrome rounds;
- shot count;
- calibration identity and validity window;
- classical decoding cost;
- statistical confidence;
- accepted logical failure rate.

## 12. Metrics

Closure metrics are views over engineering objects, not substitutes for review.

A project may report intent coverage, realization coverage, evidence coverage, and edge traceability separately. An aggregate number shall not conceal a missing critical representation.

A useful conservative rule is:

```text
closure capability cannot exceed its least-supported required representation
```

This rule is a gate, not a universal mathematical scoring formula.

## 13. AI and automated engineering agents

AI and automation shall participate through the same closure units, branches, pull requests, evidence records, and authority controls as human contributors.

Generated intent, realizations, tests, recovered specifications, or closure claims shall identify their provenance and shall not silently acquire authority through automation.

## 14. Conformance

A governed repository conforms to CAT-002 when it:

1. can identify intent, realization, and evidence for consequential capabilities;
2. records traceable relationships between those representations;
3. uses claim-relative closure states;
4. distinguishes normative specification from recovered descriptive behavior;
5. records recovery classification, assumptions, and uncertainty;
6. requires evidence appropriate to the declared claim;
7. preserves provenance across transformations;
8. treats probabilistic confidence and verification cost as first-class when applicable;
9. performs closure decisions through reviewable version-control operations.

## 15. Adoption

Adoption should proceed incrementally:

1. add closure-unit declarations to substantive pull requests;
2. apply the model to one project subsystem;
3. record missing representation and traceability gaps;
4. add validation tooling after the metadata stabilizes;
5. extend AEMS, P0, EDT, EVO, and EWT integrations through their owning repositories.

ATARIX is the initial product-level proving ground for this model because it already couples architecture, public interfaces, firmware, emulator behavior, FPGA realization, hardware bring-up, and layered verification.
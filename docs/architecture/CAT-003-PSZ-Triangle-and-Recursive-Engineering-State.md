# CAT-003 — PSZ Triangle and Recursive Engineering State

Status: Draft  
Owner: Catylist  
Type: Program architecture  
Lifecycle: Proposed  
Depends on: CAT-001, CAT-002  
Preserves: CAT-002 intent/realization/evidence model as a prior PSZ representation

## 1. Purpose

This document defines the PSZ Triangle as the recursively composable representation of bounded engineering state within Catalyst.

The Catylist use of **PSZ Triangle** is inspired by the Pasterski–Strominger–Zhiboedov infrared triangle in theoretical physics. The physics framework relates asymptotic symmetries, soft theorems, and memory effects as connected descriptions of infrared structure in gauge theory and gravity. Catylist does not claim that its engineering model is mathematically equivalent to that physical theory. It adopts the architectural insight that distinct representations of one bounded system can be mutually constraining, mutually informative, and partially translatable.

## 2. Intellectual lineage

Primary physics references include:

- Sabrina Pasterski, Andrew Strominger, and Alexander Zhiboedov, *New Gravitational Memories*, arXiv:1502.06120.
- Andrew Strominger and Alexander Zhiboedov, *Gravitational Memory, BMS Supertranslations and Soft Theorems*, arXiv:1411.5745.
- Sabrina Pasterski, *Asymptotic Symmetries and Electromagnetic Memory*, arXiv:1505.00716.
- Andrew Strominger, *Lectures on the Infrared Structure of Gravity and Gauge Theory*, arXiv:1703.05448.

These references establish the source of the name and conceptual inspiration. The Specification–Implementation–Evidence interpretation below is a Catylist engineering construct.

## 3. Definition

A bounded engineering system is represented by a PSZ Triangle:

```text
                         Specification
                    constraints and intent
                         /           \
                        /             \
                       /               \
          Implementation ------------- Evidence
        realized system or process     observations, tests,
                                       proofs and records
```

The vertices are:

- **Specification (S):** governing intent, requirements, invariants, constraints, permitted transformations, acceptance criteria, and declared boundaries.
- **Implementation (I):** the concrete realization, operation, artifact, process, system, or state that purports to satisfy the Specification.
- **Evidence (E):** observations, tests, proofs, measurements, traces, records, and retained artifacts that support or falsify claims about Specification and Implementation.

A PSZ Triangle is denoted:

```text
P = (S, I, E)
```

This notation is descriptive. It does not imply that the three components are simple sets, complete, uniquely recoverable, or formally equivalent.

## 4. Relationship to CAT-002

CAT-002 introduced the representation classes **Intent**, **Realization**, and **Evidence**. CAT-003 preserves that work as a prior PSZ representation and establishes the following canonical correspondence:

| CAT-002 term | CAT-003 term | Disposition |
|---|---|---|
| Intent | Specification | Preserved as a broader historical and explanatory term |
| Realization | Implementation | Preserved as a broader historical and explanatory term |
| Evidence | Evidence | Unchanged |

The earlier terminology remains valid when discussing CAT-002, recovery history, and documents written under that model. New normative work should use Specification, Implementation, and Evidence unless a more precise domain term is required.

No CAT-002 content is deleted or silently rewritten. CAT-002 remains addressable as the prior state from which CAT-003 was derived.

## 5. Mutual constraint

No vertex is independently authoritative for all questions.

- Specification constrains permissible Implementation.
- Implementation exposes ambiguities, omissions, and infeasible assumptions in Specification.
- Evidence evaluates claims about both Specification and Implementation.
- Evidence may require Specification revision rather than Implementation correction.
- Existing Implementation does not silently become normative Specification.
- A passing test does not prove an incomplete or incorrectly scoped Specification.

A consequential change at one vertex SHALL identify its effects and obligations at the other two vertices.

## 6. Translation edges

Relationships between vertices are first-class engineering objects.

```text
Specification -> Implementation   realization, design, refinement
Specification -> Evidence         acceptance criteria, test and proof obligations
Implementation -> Evidence        execution, measurement, simulation, verification
Implementation -> Specification   reverse engineering, behavioral extraction
Evidence -> Specification         validation, requirement discovery, revision
Evidence -> Implementation        diagnosis, reconstruction, correction
```

Each consequential edge SHOULD preserve:

- source and destination identities and versions;
- method, tool, and operator or agent identity;
- assumptions and configuration;
- authority and provenance;
- known information loss;
- reversibility and recovery limits;
- resulting closure state.

## 7. Bounded closure

Closure is claim-relative and boundary-relative.

A PSZ Triangle is closed for a declared claim only when:

1. the Specification states the claim and its boundary sufficiently;
2. the applicable Implementation is identified;
3. Evidence is appropriate to the claim;
4. required translation edges are traceable;
5. no unresolved divergence invalidates the claim.

Closure does not imply complete knowledge, permanent correctness, or closure of every child or neighboring PSZ.

A useful consistency cycle is:

```text
Specification -> Implementation -> Evidence -> validated Specification
```

The final Specification need not be textually identical to the initial Specification. It must remain consistent with the accepted claim, or the cycle exposes a revision, divergence, or indeterminate state.

## 8. Recursion

A PSZ Triangle may contain, depend on, compose, or govern other PSZ Triangles.

Examples include:

- an ecosystem;
- a project;
- a repository;
- a document transformation;
- a recovery operation;
- a hardware subsystem;
- a compiler pass;
- an algorithm;
- a function;
- a quantum circuit or verification claim.

A parent PSZ SHALL NOT be declared closed merely because selected child PSZs are closed. Parent closure requires evidence that composition, interfaces, boundaries, and required child obligations are themselves satisfied.

Likewise, an open child PSZ need not block a parent when the parent Specification explicitly excludes or defers that child and the exclusion is supported by appropriate Evidence.

## 9. Scale independence

The PSZ representation is intended to remain structurally stable across scale. Scope changes; the three representation classes and their obligations do not.

Scale independence is an architectural requirement, not a claim that verification cost, observability, or recoverability remains constant. Large, probabilistic, distributed, physical, and quantum systems may require bounded claims, statistical evidence, layered implementations, and explicit verification budgets.

## 10. Governance

Catylist governs bounded engineering systems represented by PSZ Triangles. Repositories, documents, databases, workflows, deployed services, and physical artifacts are possible Implementations or containers of PSZ state; none is the universal architectural center.

Subsystem responsibilities are:

| Authority or subsystem | PSZ responsibility |
|---|---|
| Catylist | governs PSZ boundaries, authority, lifecycle, and ecosystem relationships |
| AES | preserves and serves knowledge relevant to PSZs |
| AEMS | manages and assesses PSZ state, relationships, divergence, and closure |
| EDT | imports, validates, transforms, and publishes technical representations while preserving provenance |
| EVO | searches for improved solutions within a currently bounded PSZ and its invariants |
| EWT | provides the human-facing window, doorway, and administrative control surface for Catylist |

Owning repositories retain authority for their own implementations. This table does not transfer project-local authority to Catylist.

## 11. PSZ lineage and supersession

A superseded PSZ SHALL remain addressable.

A successor SHALL record:

- the prior PSZ identifier or document;
- the precise claim, terminology, boundary, or relationship superseded;
- the reason for change;
- the Evidence or analysis supporting the change;
- migration or compatibility consequences;
- the authoritative successor.

A superseded record SHALL be marked non-current without destroying its original content, provenance, or chronology.

The lineage for this specification begins:

```text
CAT-002 Intent / Realization / Evidence
                 |
                 v
CAT-003 Specification / Implementation / Evidence
```

CAT-002 is not rejected. It is preserved as the prior representation and remains informative for recovery, rationale, and historical comparison.

## 12. Conformance

A governed system conforms to CAT-003 when it:

1. identifies a bounded PSZ and the claim under review;
2. identifies Specification, Implementation, and Evidence appropriate to that claim;
3. records consequential translation edges;
4. treats divergence and uncertainty explicitly;
5. applies closure only within the declared boundary;
6. preserves parent, child, and dependency relationships where recursion matters;
7. preserves superseded PSZs and links them to successors;
8. avoids claims of equivalence to the physics PSZ triangle beyond the documented intellectual inspiration.

## 13. Open work

The following remain non-normative research directions:

- formal composition operators for PSZs;
- closure propagation rules;
- graph invariants and dependency semantics;
- optimization over bounded PSZ graphs;
- information-loss measures for translation edges;
- fixed-point and category-theoretic formulations.

These topics require separate evidence and review before becoming normative.

## 14. Revision history

- 2026-07-19 — Initial draft defining the Catylist PSZ Triangle, physics lineage, recursive composition, bounded closure, and preservation of prior PSZs.

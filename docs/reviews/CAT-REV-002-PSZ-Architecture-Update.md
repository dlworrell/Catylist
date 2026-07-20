# CAT-REV-002 — PSZ Architecture Update

Status: Active review addendum  
Owner: Catylist  
Governing specifications: CAT-002, CAT-003  
Related review: CAT-REV-002 — Post-P0 Functional Closure Review Plan  
Date: 2026-07-19

## 1. Purpose

This addendum updates the overall Catylist architectural review after formal identification of the Pasterski–Strominger–Zhiboedov intellectual lineage and adoption of the Catylist PSZ Triangle as the recursively composable representation of bounded engineering state.

It does not erase CAT-REV-001 or the original CAT-002 model. Those records remain authoritative descriptions of the understanding and evidence available when they were written. This addendum identifies the successor model and the required lineage links.

## 2. Review conclusion

The strongest currently supportable architectural statement is:

> Catylist is a governance ecosystem for recursively composable bounded engineering systems represented by PSZ Triangles. Each PSZ relates Specification, Implementation, and Evidence through traceable, mutually constraining transformations. Repositories are important implementation and persistence mechanisms, but they are not the universal governed object.

This conclusion supersedes repository-centric descriptions that treat repository state as the primary object of governance.

## 3. Intellectual lineage finding

### CAT-FND-013 — PSZ intellectual lineage identified

- Priority: P1
- State: Observed
- Claim: The name and organizing concept of the PSZ Triangle derive from the Pasterski–Strominger–Zhiboedov infrared triangle connecting asymptotic symmetries, soft theorems, and memory effects.
- Evidence: Primary literature identified in CAT-003, including arXiv:1411.5745, arXiv:1502.06120, arXiv:1505.00716, and arXiv:1703.05448.
- Consequence: Catylist must distinguish established physics from its own Specification–Implementation–Evidence engineering abstraction.
- Required correction: Preserve the source lineage explicitly and prohibit unsupported claims of mathematical equivalence.
- Closure evidence: CAT-003 remains linked from Catylist governance entry points and future normative uses cite it.

## 4. Fundamental object finding

### CAT-FND-014 — Bounded PSZ identified as the governed engineering object

- Priority: P0
- State: Observed
- Claim: The common object across Catylist, AES, AEMS, EDT, EVO, and EWT is not the repository but the bounded PSZ Triangle.
- Evidence: CAT-002 already applies Intent, Realization, and Evidence to software, hardware, data, recovery, probabilistic systems, and quantum systems. CAT-003 makes the recursive and scale-independent structure explicit.
- Consequence: Repository-only schemas and workflows will be too narrow for document transformations, recovery operations, physical systems, and layered computational systems.
- Required correction: Define subsystem interfaces in terms of PSZ identities, boundaries, representations, edges, provenance, and closure rather than Git repository identity alone.
- Closure evidence: AEMS can assess at least one non-repository PSZ and one recursively composed parent/child PSZ without special-case semantics.

## 5. Representation terminology finding

### CAT-FND-015 — Representation vocabulary requires controlled migration

- Priority: P1
- State: Observed
- Claim: CAT-002 uses Intent, Realization, and Evidence; CAT-003 adopts Specification, Implementation, and Evidence as the canonical PSZ vertex names.
- Consequence: Silent replacement would destroy architectural lineage and could make older closure records ambiguous.
- Required correction: Preserve CAT-002 unchanged as the prior representation, publish an explicit correspondence table, and require new normative work to use the CAT-003 terminology unless a domain-specific reason is recorded.
- Closure evidence: Existing records remain readable; new records identify their governing vocabulary revision; automated tooling accepts declared versioned mappings.

## 6. Supersession and lineage finding

### CAT-FND-016 — Prior PSZs must remain recoverable

- Priority: P0
- State: Observed
- Claim: Architectural evolution requires an explicit trail from each superseded PSZ to its successor.
- Consequence: Rewriting documents in place would remove assumptions, rationale, chronology, and evidence needed to understand later decisions.
- Required correction: Treat supersession as a typed relationship rather than deletion. Preserve original content and record the changed claim, reason, supporting evidence, successor, and compatibility impact.
- Closure evidence: CAT-002 remains addressable; CAT-003 identifies it as the prior PSZ representation; CAT-REV-001 remains available and is linked from successor review material.

## 7. Subsystem reconciliation

The review adopts the following architectural responsibilities:

| Authority or subsystem | Current reviewed responsibility |
|---|---|
| Catylist | governing body and umbrella for projects, PSZ boundaries, authority, and lifecycle |
| AES | management and preservation of knowledge across Catylist |
| AEMS | management and assessment of PSZ state, hierarchy, relationships, divergence, and closure |
| EDT | import, validation, transformation, and publication of complex technical documents with provenance preservation |
| EVO | optimization of the best evolutionary answer within the currently bounded PSZ |
| EWT | public window and doorway into Catylist and administrator control centre |

Earlier review statements that assign materially different primary missions SHALL be treated as prior review findings and linked to this reconciliation rather than silently edited out of history.

## 8. Effect on CAT-REV-002 execution

The Post-P0 Functional Closure Review Plan remains valid, with these additions:

1. Review fixtures SHALL identify their governing PSZ vocabulary version.
2. At least one fixture SHALL demonstrate recursive parent/child PSZ composition.
3. At least one fixture SHALL demonstrate a PSZ whose primary implementation is not a Git repository.
4. The review SHALL test supersession lineage and recovery of a prior PSZ.
5. AEMS SHALL distinguish repository identity from PSZ identity.
6. Review outputs SHALL identify which prior claims were superseded and why.

## 9. Required migration sequence

1. Publish CAT-003 without rewriting CAT-002.
2. Link CAT-003 from the Catylist README and architecture index.
3. Add vocabulary versioning to future closure and PSZ records.
4. Update AEMS schemas to represent recursive PSZ identities and typed edges.
5. Update subsystem documentation in their owning repositories.
6. Execute CAT-REV-002 against the revised model.
7. Mark findings closed only when evidence exists; do not close them by documentation alone.

## 10. Disposition of prior material

The following rules apply:

- CAT-002 remains a preserved prior PSZ representation and continues to govern existing records until migrated.
- CAT-003 is the proposed successor for PSZ terminology, recursion, scale independence, and lineage requirements.
- CAT-REV-001 remains retained as the historical production-readiness review.
- CAT-REV-002 remains the planned independent functional-closure review.
- This document is an architectural addendum to CAT-REV-002, not a declaration that Project Zero is complete.

## 11. Review status

This architectural update is documented but not yet operationally closed.

Closure requires:

- approval of CAT-003;
- adoption by the relevant subsystem specifications;
- machine-readable PSZ identity and lineage schemas;
- evidence from recursive and non-repository fixtures;
- independent reproduction during CAT-REV-002.

Until those conditions are met, the architecture is **documented and proposed**, not fully qualified.

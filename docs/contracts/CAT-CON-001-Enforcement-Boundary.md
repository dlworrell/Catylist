# CAT-CON-001 — Enforcement Boundary

Status: Reviewable baseline
Owner: Catylist
Type: Contract enforcement profile
Version: 0.1.0

## 1. Purpose

This document identifies which CAT-CON-001 obligations are enforced by the
common JSON Schema and fixture validator, which require semantic validation,
and which remain decisions for competent human or delegated project authority.

It prevents structural conformance from being reported as semantic closure,
downstream adoption, or production readiness. It does not add normative meaning
to [CAT-002](../architecture/CAT-002-Engineering-Representation-Closure-and-Recovery.md)
or replace the
[CAT-CON-001 contract](CAT-CON-001-Engineering-Closure-Metadata-Contract.md).

## 2. Enforcement layers

The common contract uses four enforcement layers:

1. **JSON Schema** — validates serialized structure, required fields, and
   bounded conditional constraints.
2. **Fixture validator** — validates the schema itself, applies JSON Schema
   format checking, accepts positive fixtures, and requires negative fixtures
   to be rejected.
3. **Semantic validator** — resolves identities and relationships, evaluates
   complete profile obligations, and refuses unsupported state transitions.
   This layer is assigned to AEMS and is not implemented by this increment.
4. **Review authority** — decides whether intent, realization, evidence,
   assumptions, exclusions, and residual gaps support the claim. Automation may
   provide evidence but does not silently acquire this authority.

## 3. Obligation matrix

| Obligation | Governing source | Current enforcement | Retained evidence | Remaining limitation |
|---|---|---|---|---|
| Top-level record and closure-unit shape | CAT-CON-001 sections 5 and 12 | JSON Schema | Positive and negative fixtures | Structural only |
| Canonical enumerations | CAT-CON-001 section 4 | JSON Schema | Schema-validation workflow | Does not prove the selected value is truthful |
| CLOSED requires a closure decision | CAT-CON-001 sections 10 and 12.3 | JSON Schema | Negative fixture without a decision | Decision authority remains review-controlled |
| CLOSED contains required Intent, Realization, and passed Evidence records | CAT-002 section 4; CAT-CON-001 section 12.3 | JSON Schema existence checks | Positive fixture and focused negative fixtures | Does not prove that every applicable representation is present |
| CLOSED rejects an open or blocked mandatory gap | CAT-002 section 4; CAT-CON-001 section 4.2 | JSON Schema | Mandatory-open-gap negative fixture | Gap classification and completeness remain semantic judgments |
| Date-time values conform to the declared JSON Schema format | CAT-CON-001 sections 9 and 10 | Fixture validator with `FormatChecker` | Invalid-decision-time negative fixture | Timestamp provenance remains a review concern |
| Representation, transformation, and gap identifiers are unique | CAT-002 sections 5 and 6 | Future AEMS semantic validation | None in this increment | Open |
| `supports`, transformation inputs, and transformation outputs resolve to declared identities | CAT-002 section 6; CAT-CON-001 sections 8 and 9 | Future AEMS semantic validation | None in this increment | Open |
| Every required evidence obligation is fulfilled at an appropriate level | CAT-002 sections 4 and 8; CAT-CON-001 sections 9 and 12.3 | AEMS profile validation plus review authority | One bounded E0 record | Evidence sufficiency is claim-relative and remains open outside the bounded claim |
| Artifact and decision provenance is immutable and auditable | CAT-CON-001 sections 6, 10, and 12.3 | Review authority; AEMS validation planned | Exact PR head, merge commit, and workflow-run references | General immutability classification is not derivable from an arbitrary string |
| Transformation method, loss, reversibility, and output authority are semantically sufficient | CAT-002 section 6; CAT-CON-001 section 8 | Review authority; AEMS validation planned | Bounded contract-to-schema transformation record | General semantic sufficiency remains open |
| Recovered material does not silently become normative | CAT-002 section 9; CAT-CON-001 sections 4.3 and 7 | JSON Schema records independent fields; review decides adoption | Field-level schema representation | Authority truth and adoption remain review-controlled |
| ATARIX can use the common schema without project-specific changes | CAT-CON-001 section 15.6 | Project-owned integration evidence | None in this increment | Open in `dlworrell/atarix` |
| AEMS and P0 can implement without conversational context | CAT-CON-001 section 15.7 | Repository-owned implementations and review | Common contract and this boundary document | Implementation evidence remains open |
| Ecosystem production readiness | CAT-REV-001 and CAT-002 | Derived multi-claim review | None from schema conformance alone | Explicitly open |

## 4. Bounded closure decision

`CAT-CON-001-SCHEMA-001` is CLOSED only for this claim:

> Catalyst has a reviewable common contract and validated JSON Schema for
> representing one claim-relative engineering closure unit.

The retained E0 evidence is tied to pull request 4, reviewed head commit
`60225ab9b931bb51edcd8328b695db3b581ab93b`, merge commit
`16a76bcbadd3a9808c6b803116f614d923bf4735`, and the successful documentation,
AES-compliance, and closure-schema workflow runs recorded in the
[CAT-IMP-001 continuity record](../workstreams/CAT-IMP-001-workstream-continuity.yaml).

This decision does not close CAT-IMP-001 as a whole. It does not establish
semantic completeness, adoption by another repository, ATARIX compatibility,
AEMS or P0 implementation, migration compatibility, or production readiness.

## 5. Fixture-validator behavior

The deterministic validator at
[`scripts/validate_closure_schema.py`](../../scripts/validate_closure_schema.py):

- checks that the common schema is a valid JSON Schema Draft 2020-12 schema;
- enables JSON Schema format validation;
- requires every positive fixture directly under `examples/closure` to pass;
- requires every fixture under `examples/closure/invalid` to fail;
- reports the rejecting instance path and reason.

Negative fixtures are evidence for named structural rules. Their rejection does
not prove that all invalid closure records are rejected. Semantic negative
coverage belongs to the future AEMS implementation.

## 6. Change control

Changes that alter this boundary shall state whether they:

- add or tighten a JSON Schema constraint;
- add semantic-validator behavior;
- change decision authority;
- change the claim or scope of an existing closure unit;
- require schema-version or migration work under CAT-CON-001 section 14.

No enforcement layer may silently claim authority assigned to another layer.

# Catalyst Governance Model

Status: Active draft
Owner: Catylist

## Principles

Catalyst governance is evidence-driven, repository-local where possible, explicit about authority, and designed to preserve reviewability and recovery.

## Governance layers

1. **Program governance** — Catylist defines ecosystem structure, repository roles, and cross-project authority.
2. **Engineering standards** — AES defines reusable engineering requirements.
3. **Assessment and enforcement** — AEMS inventories repositories, detects evidence, reports gaps, and ratchets enforcement.
4. **Repository adoption** — each project declares local profiles, documentation authority, waivers, and implementation-specific extensions.
5. **Project execution** — repositories implement, test, document, and release their owned systems.

## Decision rights

A decision belongs in the narrowest repository that has complete authority over it.

- Program-wide repository relationships belong in Catylist.
- Reusable engineering requirements belong in AES.
- Scanner and enforcement mechanics belong in AEMS.
- Project architecture belongs in the project repository.
- Exceptions belong in the repository that owns the affected implementation.

## Change lifecycle

A significant change proceeds through:

1. problem statement and scope;
2. architecture or specification;
3. ADR when the choice is major, irreversible, or authority-changing;
4. small implementation changes;
5. tests and evidence;
6. documentation updates;
7. review against AES-DEV-001 and AES-SEC-001;
8. merge and post-merge verification.

## Enforcement posture

Enforcement ratchets in stages:

1. detect;
2. report;
3. baseline;
4. require evidence for new work;
5. block repeated or unreviewed violations;
6. retire waivers over time.

Legacy gaps are not silently accepted, but new work must not expand them.

## Trust boundaries

Program-level trust boundaries include:

- who may alter governance documents;
- which repository is authoritative for a rule;
- what automation may block or modify;
- how templates propagate policy;
- how external-reference repositories are separated from project-owned repositories;
- how waivers are approved, reviewed, and expired.

Automation may report and enforce declared policy, but it may not invent policy or silently redefine repository authority.

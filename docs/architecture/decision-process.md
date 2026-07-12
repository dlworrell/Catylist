# Catalyst Governance Decision Process

Status: Active draft
Owner: Catylist

## Decision categories

### Routine repository-local decision

Handled in the owning repository through normal review, tests, and documentation.

### Major architectural decision

Requires an ADR in the owning repository when it changes architecture, interfaces, compatibility, security boundaries, recovery behavior, or build strategy.

### Program-governance decision

Requires a Catylist ADR when it changes repository authority, taxonomy, standards hierarchy, cross-repository dependency direction, or ecosystem lifecycle policy.

### Engineering-standard decision

Normative text is decided and versioned in AES. Catylist records only the program-level consequences when necessary.

### Enforcement decision

Scanner and workflow mechanics are decided in AEMS. Changes that alter policy rather than implementation must first be resolved in the authoritative governance or standards repository.

## Required record

A major decision record includes:

- context;
- decision;
- alternatives considered;
- consequences;
- authority and affected repositories;
- security and trust-boundary impact;
- recovery and migration impact;
- status and date.

## Disagreement and ambiguity

When authority is unclear:

1. stop irreversible implementation;
2. identify the candidate authoritative repositories;
3. preserve the conflicting evidence;
4. resolve the authority question in Catylist;
5. record the resulting decision;
6. update affected manifests and inventories;
7. resume implementation with traceable authority.

## Emergency changes

An urgent change may precede complete documentation only when delay would create greater operational or security harm. The change must be narrowly scoped, visibly marked, tested to the extent possible, and followed by the missing record and review without an open-ended deferral.

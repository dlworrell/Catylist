# ADR-000: Establish Catylist as the Program-Governance Authority

Status: Accepted
Date: 2026-07-12
Owner: Catylist

## Context

Catalyst spans multiple repositories with distinct responsibilities. Without an explicit program-governance authority, repository relationships and cross-project decisions can become duplicated, contradictory, or dependent on conversation history.

## Decision

Catylist is the authoritative repository for Catalyst program governance, ecosystem architecture, repository relationships, and cross-project authority boundaries.

Project-local architecture and implementation remain authoritative in their owning repositories. AES remains authoritative for engineering standards, and AEMS remains authoritative for enforcement implementation and evidence reporting.

## Alternatives considered

- Put all governance in AES. Rejected because program structure and engineering standards are different authorities.
- Put all governance in AEMS. Rejected because enforcement automation must implement policy rather than define it.
- Allow each repository to infer relationships independently. Rejected because it creates contradictory sources of truth.

## Consequences

- Program-wide governance changes require Catylist documentation or an ADR.
- Other repositories may reference Catylist rather than duplicate program-level policy.
- Catylist must maintain clear boundaries and avoid absorbing project-local authority.
- AEMS inventories should align with Catylist classifications.

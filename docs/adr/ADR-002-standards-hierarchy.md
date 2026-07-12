# ADR-002: Separate Governance, Standards, and Enforcement Authority

Status: Accepted
Date: 2026-07-12
Owner: Catylist

## Context

Catalyst needs program governance, normative engineering standards, and automated enforcement. Combining these responsibilities in one repository would make it difficult to distinguish policy decisions from implementation details.

## Decision

Catalyst uses a three-part authority hierarchy:

1. Catylist defines program governance and repository relationships.
2. AES defines normative engineering standards.
3. AEMS implements assessment, reporting, and enforcement against declared policy.

Project repositories adopt standards locally and retain authority over project-specific architecture and implementation.

## Alternatives considered

- A single governance repository for all policy and automation. Rejected because it conflates authority and mechanism.
- Project-local standards only. Rejected because reusable engineering requirements would diverge.
- Automation-defined policy. Rejected because scanners must not silently invent governance.

## Consequences

- Changes must be made in the repository with the correct authority.
- AEMS findings must trace to Catylist governance, AES standards, or an explicit project-local profile.
- Project-local extensions may strengthen standards but require a waiver or ADR to weaken them.
- Cross-repository changes may require coordinated commits while preserving distinct authority.

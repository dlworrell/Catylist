# Catalyst Standards Lifecycle

Status: Active draft
Owner: Catylist

## Purpose

This document defines how program governance interacts with engineering standards throughout their lifecycle.

## Lifecycle

A Catalyst standard normally progresses through:

1. proposal;
2. draft;
3. review;
4. adopted;
5. active enforcement;
6. revision or deprecation;
7. archival.

## Authority

AES owns normative engineering-standard text. Catylist owns the program-level relationship between AES, AEMS, templates, and project repositories. AEMS owns enforcement implementation and evidence reporting.

## Adoption

A project adopts a standard by recording:

- the inherited standard identifier;
- a local profile or explicit declaration of direct adoption;
- documentation authority;
- local extensions or stricter rules;
- applicable waiver records;
- evidence paths and workflows.

Local profiles may strengthen a standard but must not weaken it without an explicit waiver or ADR.

## Enforcement ratchet

New standards should not begin with indiscriminate hard failure. The expected sequence is:

1. inventory applicability;
2. detect evidence;
3. report missing or contradictory evidence;
4. preserve a baseline;
5. require evidence for new work;
6. block new violations;
7. remediate legacy findings;
8. retire waivers.

## Revision

A revision must state compatibility and migration consequences. Existing interfaces or obligations must not silently change. When a revision alters program authority or repository responsibilities, Catylist must also update its governance architecture or record an ADR.

## Deprecation

Deprecation requires:

- reason and replacement;
- affected repositories;
- migration path;
- enforcement transition;
- final review or removal date;
- preserved historical reference.

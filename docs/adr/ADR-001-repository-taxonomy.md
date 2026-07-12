# ADR-001: Adopt an Explicit Catalyst Repository Taxonomy

Status: Accepted
Date: 2026-07-12
Owner: Catylist

## Context

Catalyst repositories serve materially different purposes. Treating every repository alike creates incorrect enforcement, duplicated authority, and pressure to rewrite external references as though they were project-owned code.

## Decision

Catalyst repositories are classified by primary responsibility, including governance, standards, enforcement and automation, template, bootstrap and execution, shared infrastructure, product or reference implementation, experimental, and external reference.

Every project-owned repository should declare one primary class. External-reference repositories are inventoried but are not rewritten merely to satisfy Catalyst governance.

## Alternatives considered

- No taxonomy. Rejected because repository expectations become implicit and inconsistent.
- Classify only by programming language. Rejected because language does not determine authority or lifecycle.
- Apply identical policy to all repositories. Rejected because documentation, hardware, code, templates, and third-party references require different evidence.

## Consequences

- AEMS can apply role-aware checks.
- Templates can be selected by repository class.
- External references remain clearly separated from project-owned work.
- Classification changes require review because they alter expected authority and evidence.

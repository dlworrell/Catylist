# Catalyst Repository Taxonomy

Status: Active draft
Owner: Catylist

## Purpose

Repository taxonomy identifies the primary responsibility and governance treatment of each repository.

## Classes

### Governance

Defines program structure, ownership, repository relationships, and decision authority.

Example: `Catylist`.

### Standards

Defines reusable engineering requirements and normative policy.

Example: `AES`.

### Enforcement and automation

Implements assessment, reporting, evidence collection, and policy enforcement.

Example: `AEMS`.

### Template

Provides reusable repository structures, workflows, and policy-adoption scaffolding.

Example: `repo_templates`.

### Bootstrap and execution

Coordinates initial formation, migration, or staged execution of the ecosystem.

Example: `P0`.

### Shared infrastructure

Provides reusable libraries, tools, or services consumed by multiple projects.

Examples: `evo`, `engineering-docs-toolkit`.

### Product or reference implementation

Owns architecture and implementation of a product, platform, operating system, or application.

Examples: `atarix`, `JAG`.

### Experimental

Contains exploratory work that is not yet stable architecture or product behavior.

Example: `code-noodling`.

### External reference

Preserves third-party or upstream material for research, compatibility, or lineage. External references are not rewritten to satisfy Catalyst governance.

## Classification rule

Each project-owned repository must declare one primary class and may declare secondary capabilities. The primary class determines its authority and expected evidence.

A repository must not use a secondary capability to absorb authority belonging to another repository. For example, AEMS may contain documentation, but its primary authority remains enforcement automation rather than engineering standards.

## Governed project scopes

Status: Proposed, pending acceptance of [ADR-0004](../adr/ADR-0004-governed-project-scopes.md).

A repository may declare governed project scopes. A governed project scope is a
top-level directory listed in the repository manifest that contains a
self-contained project with its own automation and its own standards-adoption
evidence. In [CAT-003](CAT-003-PSZ-Triangle-and-Recursive-Engineering-State.md)
terms, each scope is a child PSZ of the repository PSZ.

The repository-level rules remain unchanged:

- the repository still declares exactly one primary class;
- a repository with no declared scopes is governed exactly as before.

Scopes relate to the repository's class as follows:

- each scope declares its own owner, primary class, lifecycle state, and
  governing standards;
- a scope's primary class is constrained by the repository's primary class and
  cannot grant authority beyond it. For example, scopes in an Experimental
  repository are experimental unless a Catylist ADR reclassifies them;
- the expected route from an experimental scope to a production class is
  extraction into its own repository, which is then classified under this
  taxonomy;
- every governed file belongs to exactly one scope or to the repository-level
  remainder.

ADR-0004 defines the full rules.

## Lifecycle states

Recommended states are:

- proposed;
- bootstrap;
- active;
- maintenance;
- deprecated;
- archived;
- external-reference.

Lifecycle changes must preserve migration and compatibility information where downstream repositories depend on the repository.

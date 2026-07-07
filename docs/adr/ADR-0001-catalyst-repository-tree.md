# ADR-0001: Catalyst Repository Tree

Status: Accepted
Owner: Catylist
Date: 2026-07-06

## Context

Catalyst needs a clear repository ownership model so AEMS can report engineering evidence without treating reference repositories as Catalyst-governed project repositories.

Earlier AES-DEV-001 scans treated several reference repositories as project-owned repositories. That produced misleading local-profile, specification, and ADR gaps.

## Decision

The Catalyst repository tree is organized as follows:

- `dlworrell/Catylist` is the Catalyst program umbrella and managing organization.
- `dlworrell/AES` is the engineering standards repository.
- `dlworrell/AEMS` is the project management, assessment, reporting, and enforcement repository for Catalyst.
- `dlworrell/atarix` is the operating system for the target hardware being built.
- `dlworrell/engineering-docs-toolkit` is the engineering document toolkit.
- `dlworrell/repo_templates` is the repository standard that Catalyst repositories default to or start with.
- `dlworrell/herkules-1934-english` is the EDT validation project.
- `dlworrell/code-noodling` is an experimentation and testing repository.

The following repositories are external/reference repositories and are not governed as Catalyst project repositories:

- `dlworrell/cglm`
- `dlworrell/CLK`
- `dlworrell/65x02`
- `dlworrell/BB816-MATX-PCIE`
- `dlworrell/ulx3s`
- `dlworrell/Vega816`

## Consequences

AEMS should report Catalyst project-owned repositories separately from external/reference repositories.

External/reference repositories may be listed for traceability, lineage, compatibility research, or borrowed implementation patterns, but they should not be rewritten to satisfy Catalyst policy.

Atarix may contain reference material about external repositories when that material supports Atarix design. Such material remains Atarix-local unless explicitly reclassified.

## Affected Repositories

- `dlworrell/Catylist`
- `dlworrell/AES`
- `dlworrell/AEMS`
- `dlworrell/atarix`
- `dlworrell/engineering-docs-toolkit`
- `dlworrell/repo_templates`
- `dlworrell/herkules-1934-english`
- `dlworrell/code-noodling`
- `dlworrell/cglm`
- `dlworrell/CLK`
- `dlworrell/65x02`
- `dlworrell/BB816-MATX-PCIE`
- `dlworrell/ulx3s`
- `dlworrell/Vega816`

## Related Evidence

- `dlworrell/AEMS/docs/engineering/reports/AES-DEV-001-catalyst-tree-baseline-2026-07-06.md`
- `dlworrell/AEMS/docs/engineering/reports/AES-DEV-001-local-profile-adoption-2026-07-06.md`
- `dlworrell/AEMS/docs/engineering/reports/AES-DEV-001-role-aware-baseline-2026-07-06.md`

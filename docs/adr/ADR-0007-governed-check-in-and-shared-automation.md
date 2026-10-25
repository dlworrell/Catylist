# ADR-0007: Governed Check-In and Shared Automation

Status: Accepted
Owner: Catylist
Date: 2026-10-25
Proposed: 2026-10-19
Decision authority: Donovan Worrell
Implementation qualification: Open; evidence is required per repository and scope

Destination: `docs/adr/ADR-0007-governed-check-in-and-shared-automation.md`
Applies to: Catylist, AES, AEMS, P0, `repo_templates`, EDT, and Catalyst-owned repositories and scopes
Supersedes (proposal lineage): v0.8 ADR-0007 *Shared Automation Architecture* and v0.8 ADR-0008 *IDE-Neutral Check-In Governance* (preserved in `v0.8-original/`)
Builds on: ADR-0003 (authority chain), ADR-0004 (governed project scopes), ADR-0005 (agent instruction files), ADR-0006 (default-branch protection and signed commits)

References as cited in the text below:

- "ADR-0003" means [ADR-003](ADR-003-authority-chain.md), the Catalyst authority chain; no `ADR-0003` file exists.
- [ADR-0004](ADR-0004-governed-project-scopes.md), [ADR-0005](ADR-0005-agent-instruction-files.md), [ADR-0006](ADR-0006-default-branch-protection-and-signed-commits.md).
- Not yet published: `ROADMAP-v0.9.md`, `v0.8-original/`, AEMS-ADR-001, AES-ADR-0002, P0-ADR-0002. Link them here when they land.

## 1. Context

Every repository and scope needs the same things: stable file identity, correct licensing, meaningful documentation, and evidence tied to exact revisions. Implementing these separately per repository, editor, agent, or workflow produces drift and inconsistent verdicts. Catylist already separates governance (Catylist), normative standards (AES), enforcement and evidence (AEMS), migration (P0), scaffolding (`repo_templates`), and publication (EDT). This ADR applies that chain to a single shared automation path.

## 2. Decision

### 2.0 Program-wide applicability

This decision applies to every repository whose ownership is `project-owned`
or `organizational` in the authoritative
[repository inventory](../../inventory/repositories.json), including all
declared governed scopes and the repository-level remainder. The inventory at
commit `703921c0d66bb46754804781274ac6075da0a656` contains 17 such
repositories. That count records the adoption baseline; the current inventory
determines scope. Newly classified governed repositories inherit this decision.

External-reference repositories are excluded. Unclassified repositories enter
scope only after Catylist records their classification. Repository-specific
implementation, standards, and evidence remain with their owning authorities.

### 2.1 Develop freely; govern at check-in

Contributors may use any editor, IDE, script, or AI agent. **No editor plugin, IDE integration, watcher, or on-save scanner is required or recognized as a control.** Governance begins when work enters the repository lifecycle:

| GitHub event | What happens | Evidence |
|---|---|---|
| Local work | Optional `aems check` / `aems fix` for fast feedback | None required |
| Signed commit (ADR-0006) | Commit identity and signer, verified by GitHub | GitHub verification status |
| Pull request + required checks | AEMS evaluates the exact head commit with pinned policy | Typed attestation per check, bound to that commit |
| Merge to default branch | Merge-commit-only, signed, required checks passed (ADR-0006) | Merge commit identity |
| Release / publication | Release workflow attests the exact artifacts | Provenance attestation per artifact |

State is carried by these GitHub-native events. No separate state store is maintained.

### 2.2 One authority, one engine

1. **Catylist** decides which repositories and scopes are governed, and their lifecycle.
2. **AES** defines normative requirements, profiles, and permitted exceptions.
3. **AEMS** implements one headless evaluator, distributed as the `aems` CLI and a reusable CI action. It MUST NOT invent obligations; every finding cites the rule's issuing standard and revision.
4. **`repo_templates`** provides repository-level wiring only (manifest skeleton, CI stub, REUSE configuration). It contains no policy text.
5. **P0** inventories and migrates existing repositories and proposes ratchet transitions.
6. **EDT** renders publications and may attach publication provenance; it does not judge rights or compliance.

Local runs, Claude Code, and CI all invoke the same pinned `aems` version. Workflow YAML and agent instruction files only pass arguments; they never restate policy (ADR-0005).

### 2.3 Trusted CI is the gate; local checks are convenience

- Hooks and local runs are bypassable and are never the trust boundary.
- The required check runs the AEMS version pinned by the repository manifest, never a validator supplied by the pull request under test.
- Signing of attestations happens only in trusted workflow contexts (no `pull_request_target` execution of PR code, per ADR-0004). Untrusted PRs get unsigned reports.
- Checks report three outcomes: `pass`, `violation`, `indeterminate`. Required gates fail closed on the last two.

### 2.4 Adopt standards before building

Shared automation SHALL prefer established, maintained standards and tools over Catalyst-specific designs:

| Need | Adopted mechanism |
|---|---|
| License and copyright declarations | SPDX expressions + REUSE Specification (headers, `.license` sidecars, `REUSE.toml`) |
| Evidence format | in-toto Statement v1 in a DSSE envelope |
| Signing, signer identity, time witness for automated evidence | GitHub Artifact Attestations (Sigstore keyless, transparency log) |
| Build provenance | SLSA provenance predicate |
| Human commit identity | Signed commits (ADR-0006) |
| Contributor rights for outside contributions | Developer Certificate of Origin (`Signed-off-by`) |

A Catalyst-specific mechanism requires a recorded reason why an existing one is unsuitable.

### 2.5 Evidence first, then normative text

A requirement may be piloted in **report-only** mode inside a scope whose lifecycle is `proposed`, `bootstrap`, or experimental (ADR-0004) **before** AES adopts it. Report-only results never block merges and never claim compliance. AES normative text is then written from pilot evidence, and only AES-adopted rules may become blocking.

### 2.6 Honest roles

- Machine attestations state what a workflow checked; they never imply human review.
- With a single maintainer, review is recorded as `self-reviewed` and is never presented as independent.
- AI agents may author changes; they may not grant licenses, approve their own work, or sign as a human.

## 3. Alternatives considered

| Alternative | Reason not selected |
|---|---|
| Per-editor or per-agent integrations | Duplicate policy, drift, unreviewable |
| Catylist runs scanners | Conflates governance with enforcement (ADR-0003) |
| Custom signed-evidence format and ledger | Rebuilds what in-toto/DSSE and Sigstore already provide |
| Hooks that rewrite staged content before signing | Fragile, bypassable, and not a trust boundary |
| Normative AES text before any pilot | Slow; specifications written without evidence |

## 4. Consequences

- AEMS gains an `aems` CLI and reusable action (AEMS-ADR-001).
- AES gains a file identity, licensing, and documentation standard (AES-ADR-0002), written from pilot results.
- P0 runs the first pilot on `code-noodling/crypto_pipeline/` (P0-ADR-0002).
- Public repositories get Sigstore-backed attestations; private repositories need the fallback in AEMS-ADR-001 §1.4 unless the plan supports attestations.

## 5. Adoption, verification, and migration

### 5.1 Acceptance record

On 2026-10-25, Donovan Worrell directed: "Then we should formally adopt
adr-0007 for all of Catylist repos." This records the maintainer's acceptance
of the shared-automation architecture for the full scope in section 2.0,
effective when this adoption change merges through the normal signed-commit
pull-request route. Preparation of the record is AI-assisted; it does not
assert independent review or grant an agent human approval authority.

The original proposal made ADR acceptance conditional on Slice 1 pilot
verification. This adoption amendment separates the maintainer's architecture
decision from implementation qualification. The original pilot criteria below
remain required evidence; they have not been waived or declared satisfied.

Acceptance of this ADR does not adopt unpublished AES requirements, accept
dependent ADRs in other repositories, or qualify an implementation for
production. AES continues to decide normative obligations, and AEMS continues
to implement and report them.

### 5.2 Implementation qualification

Slice 1 verification on `code-noodling/crypto_pipeline/` still requires:

1. identical findings from local and CI runs (RVW: same-rule behavior);
2. a PR-supplied validator being ignored in favor of the pinned evaluator; and
3. an attestation that verifies against the exact head commit and fails
   against any other commit.

Retain source and evaluator revisions, the applicable AES revision, actual
test outcomes, and all limitations with that evidence. Existing results remain
bound to their recorded subjects. Missing, failed, or unrun checks remain open;
adoption cannot convert them into passing evidence.

The crypto pilot and the EVO archive work retain separate scope and acceptance
records. Evidence from one does not close obligations owed by the other.
The referenced roadmap and owning-repository ADRs must be reconciled and linked
as they are published; absent documents remain explicit dependencies.

### 5.3 Rollout and recovery

Each governed repository records its applicable AES requirements, pinned AEMS
version, scope coverage, implementation gaps, waivers, and verification
evidence. Reuse existing tasks and evidence identities. Keep repository wiring
thin and route changes through the authority chain in section 2.2.

Report-only pilots continue under section 2.5. Blocking enforcement requires
adopted AES obligations, a reviewed repository-specific transition, verified
check names and behavior, and an explicit migration window where applicable.
This governance adoption does not itself change repository settings, rulesets,
required checks, secrets, runners, or workflow permissions.

Implementation changes use signed pull requests and retain their prior state
and recovery instructions. Any reversal of this governance decision requires
an attributable superseding decision; history and existing evidence remain
addressable.

## 6. Decision history

- 2026-10-19: shared-automation architecture proposed.
- 2026-10-25: maintainer directed adoption across all governed Catylist
  repositories. Applicability was tied to the authoritative inventory, and
  architecture acceptance was separated from implementation qualification
  while retaining the original pilot verification criteria.

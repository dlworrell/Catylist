# ADR-0015: REA Recovery Capability through EVO

Status: Proposed
Owner: Catylist
Date: 2026-10-26 (America/Los_Angeles)
Decision authority: Donovan Worrell; acceptance pending
Amends: [Catalyst Ecosystem Architecture](../architecture/catalyst-ecosystem.md), by adding the proposed relationship below
Builds on: [ADR-003](ADR-003-authority-chain.md), [ADR-0004](ADR-0004-governed-project-scopes.md), [ADR-0006](ADR-0006-default-branch-protection-and-signed-commits.md), [ADR-0007](ADR-0007-governed-check-in-and-shared-automation.md)
Tracking: [EVO #132](https://github.com/dlworrell/evo/issues/132)

## Context and observed baseline

On 2026-10-26 the owner directed REA-assisted recovery to become an EVO
capability in the Catylist-managed ecosystem. EVO #132 records that direction;
its checkbox state alone does not establish implementation or qualification.
[EVO PR #133](https://github.com/dlworrell/evo/pull/133) merged investigation
documents, not an installed recovery/optimization capability.

The authoritative [repository inventory](../../inventory/repositories.json)
classifies EVO as `project-owned` / `governed-product` with protected default
branch policy. REA is `external-reference` / `external-reference` with excluded
default branch policy. This amendment preserves those records and changes
neither classification nor policy.

[TASK-38](https://app.notion.com/p/402ae4dd715381bfa629f893f99e0543) remains In
progress for read-only REA source/history/CI mining. The retained
[REA outcome](https://app.notion.com/p/403ae4dd715381f2bc91d7974c2cc207) describes
partial source inspection and delivered ingestion materials, with execution
and hardware limits. This amendment consumes that evidence without replacing
the task or declaring its remaining criteria complete.

## Proposed relationship decision

1. **EVO owns the companion integration.** It owns interface/device packages,
   evidence-export mapping and companion metadata, compatible implementations,
   C source admission, optimization and replay. Its local ADR-0046 and EVO-004
   contract are separately reviewed proposals tracked by EVO #132. Their local
   serialization, module and execution mechanics remain EVO authority.
   Review the [EVO proposal PR #134](https://github.com/dlworrell/evo/pull/134)
   and [EVO-004 at its verified proposal head](https://github.com/dlworrell/evo/blob/197c5160632e7c160aae1dce474eca9898447061/docs/specs/EVO-004-rea-recovery-integration-contract.md);
   these are proposed contract sources, not adopted implementation evidence.
2. **REA remains an external reference.** The integration baseline is the fork
   at `9e22da845bf8b447f81539e0ba57d5deb59e9103`. Its public CLI/MCP/evidence
   contracts supply analysis; this relationship neither enrolls REA under
   Catalyst enforcement nor authorizes vendoring, combining histories or
   assuming upstream maintenance. Any classification change needs a separate
   Catylist decision and inventory amendment.
3. **Authority stays divided.** Catylist governs this relationship and its
   lifecycle. AES defines adopted requirements and permitted exceptions. AEMS
   assesses and indexes evidence. REA and other producers retain canonical
   observations; EVO retains its specifications, source and run evidence.
   Target owners retain access/rights and acceptance of downstream patches.
   Attributable reviewers/laboratories provide claim-specific verification.
4. **Source admission is explicit.** The boundary is REA analysis →
   evidence-linked interface/behavior specification → independently verified,
   buildable C baseline → EVO source optimization → retained comparison/replay
   evidence. Pseudocode/assembly alone is not admitted C. Initial other-language
   analysis remains recovery evidence outside that optimizer path.
5. **Evidence is linked, not reassigned.** Retain native REA bundles unchanged,
   including confidence, authority, limitations and unknown histories. Versioned
   companion metadata links exact input/spec/code/test/output identities and
   rights/access. Reuse AEMS's existing typed graph; unsupported mappings remain
   contract gaps. Neither a graph, a Notion record nor a green documentation
   check establishes engineering truth or closure.
6. **Use EVO's existing repository governance.** The planned companion modules
   are ordinary directories in EVO's repository-level remainder, not a new
   repository or a separately governed scope. A future formal scope must satisfy
   ADR-0004's ownership, standards, dependencies and exhaustive coverage rules,
   with actual scope-aware enforcement verified before reliance on it.

These are governance and ownership boundaries. This ADR creates no new AES
normative standard or AEMS enforcement mechanism. Accepted ADR-0007 applies to
EVO, while its repository/scope implementation qualification remains open.
Crypto and Gmail-archive pilot evidence does not transfer qualification here.

## Security and claim boundaries

Use bounded, actually isolated provider and project-command execution. Preserve
normal untrusted-PR isolation; public CI receives no lab device, network,
credential or private-capture access. Keep AI/MCP/cloud orchestration outside
deterministic control and protective interlocks. Future hardware work needs its
own authorized device/command/limit policy and accountable laboratory review.

The first implementation target is one offline record decoded to value, unit,
status and timestamp against independent expected cases. No actual instrument
or private acquisition capture is selected. Synthetic tests remain synthetic.
Compatibility, numerical correctness, performance, measurement fitness, timing
and machinery safety are distinct claims with distinct evidence obligations.
Historical driver matching supplies no automatic accuracy or safety acceptance.

Installed integration depends on open [EVO #93](https://github.com/dlworrell/evo/issues/93)
and [#68](https://github.com/dlworrell/evo/issues/68), retaining the separate
[#69](https://github.com/dlworrell/evo/issues/69) product-proof obligation.
Private/fake providers cannot establish installed-product qualification. A
no-improvement run may be valid evidence without proving improvement.

## Acceptance, implementation and recovery

Publication of this ADR is a **proposal**. Acceptance requires the owner's
explicit attributable decision recorded through the signed-PR process. The
Accepted status must be recorded before or in the same PR as governed changes
that rely on it, under the Code's Law 1. An agent does not approve its own work.

Acceptance of this relationship does not accept the EVO local contract on
EVO's behalf or complete intake, source admission, installed optimization,
hardware validation or any dependent issue. EVO must retain stage-specific
acceptance evidence and exact-head CI/artifact links under #132. Notion remains
coordination; TASK-38 retains its existing owner and scope.

No repository settings, manifests, workflows, runners, credentials or inventory
classification change in this proposal. New requirements proceed through AES;
assessment/graph extensions proceed through AEMS. Upstream pin updates need a
reviewed source/contract/provider/replay comparison in EVO. Retain old evidence.

Abandon an unaccepted proposal without affecting adopted governance. Reverse a
merged decision through a reviewed revert/superseding decision, preserving
history and existing evidence. Withdrawing the relationship does not delete
REA observations or transfer ownership of target source or private captures.

## Alternatives considered

- A new Catylist-owned recovery repository: rejected for this increment; the
  owner selected EVO and no separate lifecycle/ownership need is established.
- Govern/rewrite the REA fork as project-owned: rejected; the existing inventory
  deliberately excludes external references and the companion can own the
  integration without changing REA's status.
- Make AEMS or Notion the source of recovered behavior: rejected; indexing and
  coordination cannot replace native observations or project-local evidence.
- Delay governance until the installed optimizer is complete: rejected; clear
  ownership and admission contracts can be reviewed now while execution and
  hardware qualification remain gated by their own evidence.

## Affected repositories and source records

- `dlworrell/Catylist`: this relationship proposal and overview/index links.
- `dlworrell/evo`: the companion contract/implementation and #132, within
  existing [EVO classification](../reviews/CAT-DISP-001-EVO-repository-classification.md).
- `dlworrell/rea`: pinned external-reference input; no source/policy changes.
- `dlworrell/AES` and `dlworrell/AEMS`: existing requirements/assessment and
  traceability authority; no new adoption or implementation claimed.
- [REA intake source tree](https://github.com/dlworrell/rea/tree/9e22da845bf8b447f81539e0ba57d5deb59e9103) and the existing TASK-38/outcome records above.

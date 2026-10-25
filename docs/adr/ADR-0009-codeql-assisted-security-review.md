# ADR-0009: CodeQL-assisted Security Review and Evidence-Based Gate Promotion
Draft lineage: DRAFT-CAT-CODEQL-REVIEW
Date: 2026-10-25
AI-assisted drafting: ChatGPT; no independent review asserted.
Status: Proposed
Owner: Catylist
Decision authority: Donovan Worrell
Affected repositories: current and future project-owned/organizational inventory entries and governed scopes; external-reference repositories excluded.
Related decisions: accepted ADR-002 authority hierarchy, ADR-0004 scopes, ADR-0005 agent instructions, ADR-0006 branch protection, ADR-0007 shared automation.

## Context
Catylist needs a consistent security review processor for adopted AES-SEC-001/002 without equating source analysis with compliance. AEMS already delivers custom queries, pinned upstream suites, fixtures and reporting. Program-wide adoption, reviewer responsibility, limitations and promotion into required checks need an explicit decision. Repository enrollment and actual enforcement remain separate evidence claims.

The build used to create a CodeQL database can execute repository-controlled code. A pinned scanner alone therefore does not establish trustworthy extraction. Signed results also need verified producer identity, execution context and exact subject binding.

## Proposed decision
1. Adopt CodeQL, through the shared pinned AEMS evaluator, as a security-analysis input to code review. CodeQL does not approve a PR, certify a standard, prove cryptographic security or replace authorized review.
2. AES alone defines normative obligations, exception authority and applicability. AEMS maintains query implementations, tests, mappings and evidence. Repository owners maintain extraction/build profiles and complementary evidence. Catylist approves governance and promotion policy; P0 coordinates migration; templates provide wiring.
3. Start each applicable repository/language profile in report-only mode. Unsupported or unextracted surfaces are explicitly not assessed. A repository with no applicable supported-language surface records a reviewed applicability rationale rather than a synthetic successful scan.
4. Pin the AEMS revision, CodeQL CLI/archive digest, library/query pack versions, suite resolution, source selection, standard revisions and extraction/build profile. Changes to these inputs require review and refreshed qualification evidence. A PR cannot make its proposed evaluator authoritative for its own assessment.
5. Retain exact subject commit/tree, extraction provenance and logs, source coverage/exclusions, toolchain identity, query hashes, SARIF and operational outcome. A caller-supplied commit label alone cannot establish database provenance.
6. Separate analysis completion, security review disposition, AES obligation evidence and promotion authorization. Each finding receives an accountable disposition and source citation. Suppressions and baselines remain visible. Waivers cite the authority, scope, rationale and applicable expiry/review conditions supplied by AES; scanning does not grant one.
7. Use a three-outcome gate interpretation: pass, violation, indeterminate. Preserve underlying detector and operational outcomes. A timeout, missing language job, partial SARIF, provenance failure or unsupported required assessment is not a clean pass. Report-only runs remain nonblocking until an explicit promotion decision.
8. A required profile may be promoted only after its evidence package satisfies the criteria below and the authorized maintainer approves the repository/scope-specific transition and migration window. Name the actual observed check and its trusted producer; do not infer required-check integration from YAML.
9. Protect the analysis/build trust boundary. Untrusted PR builds receive isolated execution with minimal permissions and no signing, ruleset-administration, deployment or production secrets. PR-owned code must not execute in a privileged signing job. Never run untrusted fork code on the user's lab/self-hosted runner. Runner enrollment/reachability must be separately verified before qualification; current registration is unknown in this package.
10. Human/authorized review remains distinct from automated evidence. The implementing agent cannot attest independent human review of its own work. Follow current accepted maintainer rules; do not fabricate an independent reviewer where none exists.
11. Changing the PR head invalidates prior subject-bound gate/review evidence for the changed subject. Any merge candidate or merge-queue policy must define and verify which final subject is authorized. GitHub-native records remain the lifecycle source; reports/indexes are derived views.

## Initial implementation profile, not new AES requirements
AEMS currently documents CLI 2.27.2; cpp-all 12.2.0 / cpp-queries 1.9.1; swift-all 6.8.5 / swift-queries 1.3.12, with security-extended suites. These are the observed implementation baseline, not permanently mandated versions. Reviewed locks remain authoritative.

C/C++ and Swift require their actual supported extraction environments. Objective-C/Objective-C++, indirect and cross-language flows, CUDA surfaces, assembly and 65C816 targets need explicit coverage assessment and complementary methods. Secret-name heuristics are neither a secret inventory nor erasure proof.

Applicable complementary evidence includes warning/hardening builds, sanitizers, fuzzing, ownership/ABI and concurrency tests, key-store and erasure evidence, failure/integrity/restore tests, release inspection and threat-model review. Cryptographic experiments remain experimental unless their distinct acceptance process succeeds.

## Alternatives and trade-offs
| Option | Benefit | Cost / reason |
|---|---|---|
| Human review alone | Flexible interpretation | Inconsistent repeatability and avoidable review burden |
| CodeQL as automatic reviewer/compliance verdict | Simple merge signal | Unsupported completeness and authority claims; rejected |
| Independent scanners configured per repository | Local flexibility | Policy drift, duplicated engines and inconsistent evidence |
| Shared AEMS CodeQL plus accountable review | Reuse, traceability and bounded automation | Extraction complexity, macOS availability, false-positive disposition and ongoing qualification; proposed |

## Measurable promotion criteria
| ID | Required evidence |
|---|---|
| CQL-G01 | Exact inventory scope and AES applicability, with supported/excluded languages and complementary coverage matrix |
| CQL-G02 | Locked evaluator/tool/query inputs and reproducible suite resolution; positive and negative fixtures retained |
| CQL-G03 | Proven checkout-to-database lineage for the exact subject, build flags/toolchain, logs, coverage and exclusions |
| CQL-G04 | PR validator substitution cannot replace the trusted evaluator; a changed pin/profile invalidates prior qualification |
| CQL-G05 | Missing/failed/skipped required language, timeout and malformed/partial output yield indeterminate, never pass |
| CQL-G06 | Wrong commit, altered artifact, wrong producer workflow identity and wrong event/trigger are rejected as distinct negative cases |
| CQL-G07 | Real fork-PR execution demonstrates isolation and absence of privileged signing/administration credentials; report-only evidence remains untrusted for promotion |
| CQL-G08 | Findings, suppressions, baseline and valid scoped waivers have recorded dispositions; complementary obligations remain separately evaluated |
| CQL-G09 | Actual named check/producer is bound to the intended branch/scope and blocks an authorized controlled failing case; a corrected case succeeds |
| CQL-G10 | Maintainer records transition authority, migration/rollback plan and retained evidence. Qualification is recorded separately per repository/profile |

These are proposed acceptance criteria, not tests run by this document.

## Consequences, recovery and decisions needed
The proposal supports consistent review while retaining coverage limits and clear ownership. Costs include extraction runners, version maintenance, evidence retention and reviewer time. Do not require local desktop setup: use approved hosted workflows where feasible, including macOS for Swift.

Decisions needed: accept CodeQL's bounded review role; approve the promotion criteria; select the first repository/scope pilot and the authorized reviewing role. No assignee or deadline is implied.

If a promoted profile fails operationally, report indeterminate. Correct through a reviewed pinned update or an explicitly authorized temporary return to report-only mode; retain evidence and existing signature/history protections. No automatic bypass or settings change is authorized by this draft.


## Source and proposal lineage

Prepared with [Software Architect](https://www.dropbox.com/scl/fi/xb7j0gitfr1kojii9bzns) and [Security Architect](https://www.dropbox.com/scl/fi/wowzx81a51upq2yqwvq5d) analytical guidance. The [review package](https://chatgpt.com/library?file_id=libfile_bf517bbea7ec8191b5de98af02721c7f&account_id=personal) retains the original draft and ordered implementation queue.

- [Accepted shared-automation ADR-0007](ADR-0007-governed-check-in-and-shared-automation.md).
- [Governing repository inventory](../../inventory/repositories.json).
- [AEMS implementation and limits](https://github.com/dlworrell/AEMS/blob/dac93871987b3234743854cc39c8b3dc89009a4d/docs/engineering/AES-CodeQL.md).
- [AES-SEC-001](https://github.com/dlworrell/AES/blob/2a29348533bbc29f9e645c45316bcce33d75ae0c/standards/AES-SEC-001-secure-c-cpp-coding-rules.md) and [AES-SEC-002](https://github.com/dlworrell/AES/blob/2a29348533bbc29f9e645c45316bcce33d75ae0c/standards/AES-SEC-002-cross-language-secret-storage-boundaries.md).

Numbering: ADR-0008 is retained as historical proposal lineage superseded within ADR-0007; this distinct CodeQL proposal uses ADR-0009 to avoid reusing that identity. Publication as Proposed does not authorize implementation or accept this decision. Formal acceptance requires an explicit maintainer decision recorded in a reviewed change to this status and the index.


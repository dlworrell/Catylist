# CAT-REV-001 — CI/CD and Evidence Pipeline Assessment

Status: Active review artifact  
Owner: Catylist  
Parent review: `CAT-REV-001`  
Date: 2026-07-19

## 1. Purpose

This assessment determines whether Catalyst repositories currently possess a coherent, repeatable and production-grade continuous-integration, continuous-delivery and evidence-retention system.

The review distinguishes three separate concerns:

1. **repository CI** — validates a change within one repository;
2. **ecosystem assessment** — evaluates relationships and shared obligations across repositories;
3. **release evidence** — proves what artifact was released, from which source, under which policy and with which verification results.

Passing one of these concerns does not imply the others are satisfied.

## 2. Evidence inspected

The current pass inspected indexed GitHub workflow content across the core ecosystem and directly reviewed:

- `dlworrell/AEMS/.github/workflows/aes-dev-001-scan.yml`;
- `dlworrell/AEMS/.github/workflows/aes-sec-001-scan.yml`;
- `dlworrell/AEMS/config/aes-dev-001-repositories.json`;
- the current Catylist authority, taxonomy and ecosystem-manifest review artifacts.

Repository-wide indexed search found the two AEMS workflows above as the only core-ecosystem workflow files matching the common checkout and pull-request patterns used for this census. This is evidence of the indexed state inspected, not proof that no other workflow file exists under every historical branch or unindexed path. Any final census must use an authenticated repository tree walk rather than code-search presence alone.

## 3. Current implementation observed

### 3.1 AES-DEV-001 workflow

The AEMS development-principles workflow:

- runs a local scan on pull requests and selected pushes;
- produces JSON and Markdown reports;
- uploads both reports as workflow artifacts;
- can run an aggregate ecosystem scan only through manual dispatch;
- defaults aggregate strict enforcement to `false`;
- explicitly describes evidence gaps as reporting-only;
- performs the strict aggregate gate only when manually requested.

The local job therefore demonstrates useful scanner execution and report retention, but it does not yet establish a mandatory ecosystem conformance gate.

### 3.2 AES-SEC-001 workflow

The AEMS security workflow:

- runs on relevant source and build-system changes in pull requests;
- runs on all pushes to `main`;
- generates JSON and Markdown reports;
- uploads reports as workflow artifacts;
- performs a strict local gate by default;
- supports a manually dispatched ecosystem scan;
- performs ecosystem strict enforcement only when manually selected.

This is the strongest currently observed CI implementation. It provides a real repository-local gate and retained reports. It still does not prove cross-repository adoption, release qualification or long-term evidence custody.

### 3.3 Aggregate repository lists

AEMS contains a hand-maintained repository list for AES-DEV-001 assessment. That list mixes:

- authoritative repositories;
- control-plane repositories;
- products;
- shared services;
- organizational repositories;
- demos and experiments;
- external references.

The list duplicates repository identity, role, ownership, documentation authority and profile requirements that should instead derive from the canonical Catylist ecosystem inventory and repository-local manifests.

## 4. CI/CD findings

### CAT-CI-001 — CI implementation is centralized in AEMS but adoption is not proven

- Recovery state: Observed
- Confidence: High
- Claim: AEMS contains functioning scanners and workflows, but the reviewed evidence does not show that every mandatory repository runs equivalent required checks on its own changes.
- Expected: Every repository in a mandatory production profile executes its applicable local validation before merge, using centrally versioned AEMS capability or an approved equivalent.
- Consequence: A repository may merge changes that violate a shared standard even though AEMS itself passes its local checks.
- Corrective action: Publish reusable AEMS workflows or a versioned CLI package and require repository-local invocation through the canonical production profile.
- Evidence required for closure: One retained successful and one retained deliberately failing conformance run for each mandatory repository class.
- Priority: P0
- Verification cost: Medium
- Closure state: Open

### CAT-CI-002 — Ecosystem scans are manual rather than continuous

- Recovery state: Observed
- Confidence: High
- Claim: Both reviewed aggregate scans are gated behind `workflow_dispatch`.
- Expected: Changes to Catylist inventory, AES standards, AEMS rules, templates and mandatory repository manifests automatically trigger ecosystem assessment.
- Consequence: Cross-repository breakage can remain undetected until a person remembers to run the aggregate workflow.
- Corrective action: Add scheduled, change-triggered and release-triggered ecosystem assessment with deterministic repository revisions.
- Evidence required for closure: A retained run proving automatic detection of an intentionally introduced cross-repository contradiction.
- Priority: P0
- Verification cost: Medium
- Closure state: Open

### CAT-CI-003 — Development-process enforcement remains reporting-first without an approved ratchet state

- Recovery state: Observed
- Confidence: High
- Claim: AES-DEV-001 aggregate strict mode defaults to false, and evidence gaps are described as reporting-only.
- Expected: The ratchet stage for every rule and repository is explicit, versioned and time-bounded.
- Consequence: Reporting-only behavior can become permanent by inertia, with no objective point at which a known requirement becomes mandatory.
- Corrective action: Add rule-level enforcement states such as `detect`, `report`, `baseline`, `required-new-work`, `blocking`, plus owner, effective revision and waiver expiry.
- Evidence required for closure: Machine-readable ratchet configuration and tests proving each transition.
- Priority: P0
- Verification cost: Medium
- Closure state: Open

### CAT-CI-004 — Repository population is duplicated in scanner-specific configuration

- Recovery state: Observed
- Confidence: High
- Claim: `aes-dev-001-repositories.json` independently defines repository roles, ownership and applicability.
- Expected: Scanner targets and applicability derive from the Catylist-owned ecosystem graph and AES-owned profile definitions.
- Consequence: The scanner population can disagree with the canonical ecosystem population, producing false passes, omissions or contradictory classification.
- Corrective action: Replace scanner-owned repository censuses with generated assessment plans derived from canonical manifests.
- Evidence required for closure: A deterministic generation test showing that no repository can be added to the production profile without appearing in applicable assessments.
- Priority: P0
- Verification cost: Medium
- Closure state: Open

### CAT-CI-005 — Workflow actions are version-tag pinned, not immutable-revision pinned

- Recovery state: Observed
- Confidence: High
- Claim: The reviewed workflows use tags including `actions/checkout@v4`, `actions/setup-python@v5` and `actions/upload-artifact@v4`.
- Expected: Production workflows pin third-party actions to reviewed immutable commit SHAs, with an automated update process preserving provenance.
- Consequence: A moving tag can change the executed supply-chain component without a repository commit changing.
- Corrective action: Pin all external actions by commit SHA and retain the human-readable release tag in comments or dependency metadata.
- Evidence required for closure: Workflow linter and negative fixture rejecting mutable action references.
- Priority: P1
- Verification cost: Low
- Closure state: Open

### CAT-CI-006 — Runtime and toolchain versions are not fully reproducible

- Recovery state: Observed
- Confidence: High
- Claim: Workflows use `ubuntu-latest` and Python `3.x`.
- Expected: Qualification runs identify a supported runner image, language version and dependency lock state.
- Consequence: Identical source revisions may execute under different environments and produce different findings.
- Corrective action: Pin supported Python versions, record runner image identity, lock dependencies and include environment fingerprints in reports.
- Evidence required for closure: Repeated-run comparison demonstrating stable output under the declared qualification environment.
- Priority: P1
- Verification cost: Medium
- Closure state: Open

### CAT-CI-007 — Reports lack a common evidence envelope

- Recovery state: Inferred from reviewed workflow contracts
- Confidence: High
- Claim: JSON and Markdown outputs are retained, but no shared envelope has been demonstrated containing source revision, rule revision, tool revision, environment, invocation, timestamps, input inventory digest and result digest.
- Expected: Every retained assessment artifact can be independently attributed and replayed.
- Consequence: A report may be readable but cannot reliably prove what exact system state it assessed.
- Corrective action: Define `catalyst.evidence.v1` and require all scanners, tests, builds and release workflows to emit it.
- Evidence required for closure: Independent verifier accepts a valid bundle and rejects altered source, configuration or report data.
- Priority: P0
- Verification cost: High
- Closure state: Open

### CAT-CI-008 — Workflow artifact retention is not a complete evidence-custody policy

- Recovery state: Observed and inferred
- Confidence: High
- Claim: Reports are uploaded as GitHub Actions artifacts, but the reviewed workflows do not declare retention duration, immutable release attachment, evidence index registration or external archival policy.
- Expected: Evidence classes have explicit retention, immutability, indexing and disposal rules.
- Consequence: Qualification evidence can expire, become difficult to locate or lose its relationship to the released artifact.
- Corrective action: Define evidence custody classes and copy release-critical bundles to durable, content-addressed release or archival storage.
- Evidence required for closure: Retrieval test for an older qualified release using only the release identifier.
- Priority: P0
- Verification cost: Medium
- Closure state: Open

### CAT-CI-009 — No production release pipeline has yet been demonstrated

- Recovery state: Indeterminate after inspected evidence
- Confidence: Medium
- Claim: The reviewed evidence demonstrates scanning, not a full build-sign-attest-publish-verify release workflow.
- Expected: A release pipeline binds source, dependencies, build environment, tests, security assessment, produced artifacts, checksums, provenance, signatures and publication state.
- Consequence: Repositories may claim stable or production status without reproducible release evidence.
- Corrective action: Define a minimum release contract by repository class and implement it first in one representative product and one shared service.
- Evidence required for closure: Independent clean-room verification of a published release bundle.
- Priority: P0
- Verification cost: High
- Closure state: Open

### CAT-CI-010 — Branch-protection and required-check policy is not represented in the ecosystem contract

- Recovery state: Indeterminate
- Confidence: Medium
- Claim: Workflow existence alone does not prove that checks are required before merge.
- Expected: Required checks, review count, force-push restrictions, administrator bypass policy and protected release tags are declared and assessed.
- Consequence: A correctly implemented check may still be bypassed or remain advisory.
- Corrective action: Add repository protection expectations to the production profile and assess live GitHub settings through AEMS.
- Evidence required for closure: Machine assessment showing actual settings match policy for every mandatory repository.
- Priority: P0
- Verification cost: Medium
- Closure state: Open

### CAT-CI-011 — Scanner testing and version compatibility are not yet part of the observed workflow contract

- Recovery state: Inferred
- Confidence: Medium
- Claim: The workflows execute scanner help and scanner runs, but this pass has not observed dedicated unit, malformed-input, golden-vector, schema-compatibility and backwards-compatibility gates for the scanner/report contracts.
- Expected: Enforcement tooling is qualified as production software, not merely invoked as a script.
- Consequence: Scanner regressions can silently alter findings or output schema.
- Corrective action: Establish AEMS self-tests, golden fixtures, schema validation, semantic-version compatibility and mutation/negative tests.
- Evidence required for closure: Retained scanner qualification suite and independently verified golden outputs.
- Priority: P0
- Verification cost: High
- Closure state: Open

### CAT-CI-012 — No single ecosystem verdict exists

- Recovery state: Observed
- Confidence: High
- Claim: Separate scans produce separate reports, but no reviewed contract combines identity, graph, standards, source, security, tests, release and evidence-custody results into one fail-closed ecosystem verdict.
- Expected: AEMS emits one deterministic assessment bundle with repository-level and ecosystem-level status.
- Consequence: Decision-makers must manually reconcile partial reports and may overlook contradictory states.
- Corrective action: Implement a consolidated AEMS assessment model with stable finding identifiers, severity, applicability, waiver resolution and final verdict semantics.
- Evidence required for closure: One command assesses the declared ecosystem revision and emits a deterministic bundle whose verdict is independently reproduced.
- Priority: P0
- Verification cost: High
- Closure state: Open

## 5. Required pipeline architecture

The production target should use four coordinated layers.

### 5.1 Reusable local validation

AEMS owns reusable, versioned workflows or CLI entry points for:

- manifest and schema validation;
- repository contract checks;
- applicable AES profile checks;
- source and security checks;
- tests and coverage policy;
- evidence-envelope generation.

Each governed repository invokes the applicable version locally on every relevant pull request.

### 5.2 Ecosystem integration assessment

Catylist supplies the authoritative ecosystem graph. AEMS resolves immutable repository revisions and runs:

- identity reconciliation;
- authority and relationship validation;
- standards/profile resolution;
- compatibility assessment;
- cross-repository workflow tests;
- consolidated verdict generation.

### 5.3 Release qualification

A repository-class-specific release workflow must:

1. resolve the exact source revision;
2. resolve and lock dependencies;
3. run all mandatory validation;
4. build in a declared environment;
5. generate checksums and provenance;
6. sign or attest release artifacts where required;
7. publish artifacts and evidence together;
8. independently verify the published result.

### 5.4 Evidence custody

Every evidence item must be registered with:

- stable evidence identifier;
- repository and source revision;
- standard/rule revisions;
- tool and workflow revision;
- environment identity;
- input and output digests;
- result and finding set;
- retention class;
- publication or archive location;
- independent verification state.

## 6. Proposed common evidence envelope

```json
{
  "schema": "catalyst.evidence.v1",
  "evidence_id": "stable-id",
  "kind": "assessment|test|build|release|verification",
  "subject": {
    "repository": "owner/name",
    "revision": "immutable-commit",
    "tree_digest": "digest"
  },
  "policy": {
    "ecosystem_revision": "immutable-commit",
    "standards": [
      {"id": "AES-...", "revision": "immutable-revision", "profile": "profile-id"}
    ]
  },
  "producer": {
    "tool": "AEMS",
    "version": "semantic-version",
    "revision": "immutable-commit",
    "workflow": "workflow-id-and-revision"
  },
  "environment": {
    "runner": "declared-image",
    "runtime": "declared-runtime",
    "dependencies_digest": "digest"
  },
  "invocation": {
    "command": ["normalized", "arguments"],
    "started_at": "ISO-8601",
    "completed_at": "ISO-8601"
  },
  "result": {
    "verdict": "pass|fail|indeterminate",
    "findings_digest": "digest",
    "artifact_digests": []
  },
  "verification": {
    "state": "unverified|verified|rejected",
    "verifier": "tool-or-party",
    "verified_at": "ISO-8601"
  }
}
```

## 7. Remediation sequence

### CI Wave 0 — Establish authority and applicability

1. Complete the canonical ecosystem inventory and production profiles.
2. Remove scanner-specific repository identity duplication.
3. Define the applicability resolver for each standard and check.

### CI Wave 1 — Qualify AEMS as enforcement software

1. Freeze scanner CLI and report schemas.
2. Add unit, malformed-input, golden-vector and compatibility tests.
3. Define deterministic exit semantics.
4. Emit the common evidence envelope.

### CI Wave 2 — Propagate local gates

1. Publish reusable pinned workflows.
2. Apply them to Catylist, AES, AEMS, P0 and `repo_templates` first.
3. Apply them to shared services and governed products.
4. Assess actual branch-protection settings.

### CI Wave 3 — Automate ecosystem assessment

1. Trigger assessment from authority, standards, tool, template and manifest changes.
2. Add scheduled drift detection.
3. Resolve immutable repository revisions.
4. Produce the consolidated ecosystem verdict.

### CI Wave 4 — Implement release qualification

1. Define release profiles by repository class.
2. Qualify one shared service and Atarix as reference implementations.
3. Retain release evidence durably.
4. Perform independent clean-room verification.

## 8. Closure criteria

The CI/CD and evidence-pipeline work may be considered production-ready only when:

1. every mandatory repository runs applicable required checks before merge;
2. live branch-protection settings are assessed and conformant;
3. third-party workflow actions and toolchains are reproducibly pinned;
4. AEMS scanners have retained qualification evidence and stable schemas;
5. all assessment outputs use the common evidence envelope;
6. ecosystem scans run automatically on relevant changes and on a schedule;
7. scanner target population derives solely from canonical ecosystem data;
8. one consolidated command produces a deterministic ecosystem verdict;
9. release-critical evidence has durable, indexed custody;
10. representative product and shared-service releases can be independently reproduced and verified;
11. an intentionally introduced local violation and an intentionally introduced cross-repository violation both fail closed;
12. no mandatory result remains indeterminate.

## 9. Current conclusion

The CI/CD posture is **OPEN** and below a consistent production level.

AEMS already contains valuable working elements: local scanners, JSON and Markdown reporting, artifact upload, a strict local security gate and aggregate runners. Those are meaningful foundations. They do not yet form an ecosystem-wide production pipeline because adoption, automatic cross-repository execution, immutable inputs, evidence attribution, branch enforcement, release qualification and durable evidence custody are not proven.

The immediate engineering priority is not to add more independent workflows. It is to turn the existing AEMS scanner capability into one versioned, reusable and evidence-producing enforcement plane driven by the canonical Catylist graph and AES profiles.
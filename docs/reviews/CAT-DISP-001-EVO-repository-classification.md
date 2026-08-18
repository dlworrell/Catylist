# CAT-DISP-001 — EVO Repository Classification Disposition

Status: Approved project-specific disposition  
Owner: Catylist  
Date: 2026-08-17  
Applies to: `dlworrell/evo`  
Originating finding: `dlworrell/evo#112`

## Decision

Catylist classifies `dlworrell/evo` as a **`governed-product`** repository.

Its primary engineering role is **source-optimization-toolchain**: EVO is an engineering product that ingests governed C source projects, produces analysis and transformation evidence, evaluates isolated candidates, and is progressing toward an installed standalone source-optimization executable.

EVO may retain multiple locally meaningful component classes without changing the repository-level class:

- `catalyst_evo` is a `reusable-library` component that provides the deterministic C17 evolutionary-search core; and
- `evo-source-optimizer` is an `engineering-application` component that owns the source-to-source optimization product pipeline.

The reusable core is therefore a supported product component, not the repository's ecosystem-level primary class.

## Rationale

Catylist's active repository-role review separates a repository's one primary class from secondary/local capabilities and requires those capabilities not to transfer ecosystem authority. `governed-product` already expresses the appropriate primary responsibility; creating a new ecosystem class named `source-optimization-toolchain` would mix product role with authority taxonomy and unnecessarily expand the class vocabulary.

The earlier 2026-07-19 inventory described EVO as a `shared service` while its repository declaration and product boundary were still substantially earlier. That entry is superseded for EVO by this disposition. The implemented repository now has a reusable core plus a source-optimizer application boundary, executable-facing command contract, concrete production providers, release-readiness gates, and an explicit standalone-product roadmap. Its primary responsibility is consequently the governed engineering product, while reuse of its core remains an internal/component capability.

## Authority and applicability

This classification does not transfer governance, standards, or assessment authority into EVO.

The authority direction remains:

`Catylist -> AES -> AEMS -> governed EVO engineering`

Accordingly:

- Catylist remains repository-classification and ecosystem-relationship authority;
- AES remains reusable engineering-standard authority;
- AEMS remains assessment/enforcement authority;
- EVO owns product-specific architecture, implementation, tests, evidence, packaging, and releases;
- existing applicable AES and AEMS requirements remain active; and
- no waiver, standards exception, or release-readiness reduction follows from this classification.

## Lifecycle consequence

The classification is compatible with EVO's current engineering-ready/active development state. It resolves repository-role ambiguity before the standalone executable and 1.0 stabilization boundaries.

`dlworrell/evo#93` and `dlworrell/evo#56` may rely on this disposition once EVO's local `repo.yaml` and governance documentation reference it.

## Machine/local representation

The EVO repository should record the disposition as:

```yaml
repository:
  class: governed-product
  role: source-optimization-toolchain
  classification_status: approved-catylist
  classification_authority: docs/reviews/CAT-DISP-001-EVO-repository-classification.md
  components:
    - id: catalyst_evo
      class: reusable-library
    - id: evo-source-optimizer
      class: engineering-application
```

The `classification_authority` value in EVO may use the full Catylist repository/path reference rather than a local path.

## Supersession

For `dlworrell/evo` only, this project-specific disposition supersedes the provisional `shared service` assignment in `CAT-REV-001 — Repository Inventory and Identity Census` dated 2026-07-19. It does not resolve or amend the broader open CAT-REV-001 taxonomy review for other repositories.

## Closure evidence

EVO issue #112 is governance-ready to close after both of these records are on their respective default branches:

1. this Catylist disposition; and
2. EVO's local metadata/governance reconciliation naming `governed-product` and retaining the reusable-library/application component split.

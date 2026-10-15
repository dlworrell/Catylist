#!/usr/bin/env python3
"""Validate Catylist's required governance files, local Markdown links, and repository inventory."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "aes-manifest.yaml",
    "docs/architecture/catalyst-ecosystem.md",
    "docs/architecture/governance-model.md",
    "docs/architecture/repository-taxonomy.md",
    "docs/architecture/standards-lifecycle.md",
    "docs/architecture/decision-process.md",
    "docs/adr/ADR-000-governance-authority.md",
    "docs/adr/ADR-001-repository-taxonomy.md",
    "docs/adr/ADR-002-standards-hierarchy.md",
    "docs/engineering/AES-DEV-001-development-principles.md",
    "docs/engineering/SECURE-C-CXX.md",
    "docs/engineering/AES-SEC-001-waivers.md",
)
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

INVENTORY_PATH = "inventory/repositories.json"
INVENTORY_SCHEMA = "catylist.repository-inventory.v1"
# ADR-0006 rule 1: default_branch_policy is derived from ownership.
POLICY_BY_OWNERSHIP = {
    "project-owned": "protected",
    "organizational": "protected",
    "external-reference": "excluded",
    "unclassified": "pending-classification",
}
INVENTORY_CLASSES = {
    "authority",
    "control-plane",
    "shared-service",
    "governed-product",
    "organizational",
    "experimental",
    "external-reference",
    "unclassified",
}


def validate_required_files() -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED:
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing required file: {relative}")
        elif not path.read_text(encoding="utf-8").strip():
            errors.append(f"required file is empty: {relative}")
    return errors


def validate_manifest() -> list[str]:
    manifest = (ROOT / "aes-manifest.yaml").read_text(encoding="utf-8")
    required_tokens = (
        "schema_version:",
        "full_name: dlworrell/Catylist",
        "role: program-umbrella-and-managing-organization",
        "ownership: project-owned",
        "id: AES-DEV-001",
        "id: AES-SEC-001",
    )
    return [f"manifest missing declaration: {token}" for token in required_tokens if token not in manifest]


def validate_local_links() -> list[str]:
    errors: list[str] = []
    for markdown in sorted(ROOT.rglob("*.md")):
        if ".git" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        for target in LINK_PATTERN.findall(text):
            target = target.strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean_target = target.split("#", 1)[0]
            if not clean_target:
                continue
            destination = (markdown.parent / clean_target).resolve()
            try:
                destination.relative_to(ROOT)
            except ValueError:
                errors.append(f"{markdown.relative_to(ROOT)}: link escapes repository: {target}")
                continue
            if not destination.exists():
                errors.append(f"{markdown.relative_to(ROOT)}: missing link target: {target}")
    return errors


def validate_inventory() -> list[str]:
    path = ROOT / INVENTORY_PATH
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{INVENTORY_PATH}: cannot read inventory: {exc}"]

    errors: list[str] = []
    if document.get("schema") != INVENTORY_SCHEMA:
        errors.append(f"{INVENTORY_PATH}: schema must be {INVENTORY_SCHEMA}")
    authority = document.get("authority")
    if not isinstance(authority, str) or not (ROOT / authority).is_file():
        errors.append(f"{INVENTORY_PATH}: authority must name an existing file")

    repositories = document.get("repositories")
    if not isinstance(repositories, list) or not repositories:
        return errors + [f"{INVENTORY_PATH}: repositories must be a non-empty array"]

    seen: set[str] = set()
    for index, entry in enumerate(repositories):
        label = f"{INVENTORY_PATH}: repositories[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{label} must be an object")
            continue
        name = entry.get("full_name")
        if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", name):
            errors.append(f"{label}: full_name must be owner/name")
            continue
        label = f"{INVENTORY_PATH}: {name}"
        if name.lower() in seen:
            errors.append(f"{label}: duplicate entry")
        seen.add(name.lower())

        ownership = entry.get("ownership")
        if ownership not in POLICY_BY_OWNERSHIP:
            errors.append(f"{label}: unknown ownership {ownership!r}")
        elif entry.get("default_branch_policy") != POLICY_BY_OWNERSHIP[ownership]:
            errors.append(
                f"{label}: default_branch_policy must be "
                f"{POLICY_BY_OWNERSHIP[ownership]!r} for ownership {ownership!r}"
            )
        if entry.get("class") not in INVENTORY_CLASSES:
            errors.append(f"{label}: unknown class {entry.get('class')!r}")
        if (ownership == "unclassified") != (entry.get("class") == "unclassified"):
            errors.append(f"{label}: class and ownership must both be unclassified or neither")

        source = entry.get("classification_source")
        if ownership == "unclassified":
            if source is not None:
                errors.append(f"{label}: unclassified entries must have a null classification_source")
        elif not isinstance(source, str) or not (ROOT / source).is_file():
            errors.append(f"{label}: classification_source must name an existing file")
    return errors


def main() -> int:
    errors = (
        validate_required_files()
        + validate_manifest()
        + validate_local_links()
        + validate_inventory()
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Catylist repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

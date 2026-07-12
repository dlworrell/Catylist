#!/usr/bin/env python3
"""Validate Catylist's required governance files and local Markdown links."""

from __future__ import annotations

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


def main() -> int:
    errors = validate_required_files() + validate_manifest() + validate_local_links()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Catylist repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

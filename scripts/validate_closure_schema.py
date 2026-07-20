#!/usr/bin/env python3
"""Validate CAT-CON-001 closure-record fixtures.

Positive fixtures directly under examples/closure must validate.
Fixtures under examples/closure/invalid must fail validation.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/catalyst/engineering-closure-v1.schema.json"
POSITIVE_DIR = ROOT / "examples/closure"
NEGATIVE_DIR = POSITIVE_DIR / "invalid"


def load_json(path: Path) -> object:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"cannot load {path.relative_to(ROOT)}: {exc}") from exc


def format_errors(validator: Draft202012Validator, instance: object) -> list[str]:
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.absolute_path))
    formatted: list[str] = []
    for error in errors:
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        formatted.append(f"{location}: {error.message}")
    return formatted


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    failures: list[str] = []

    positive_files = sorted(
        path for path in POSITIVE_DIR.glob("*.json") if path.is_file()
    )
    negative_files = sorted(NEGATIVE_DIR.glob("*.json"))

    if not positive_files:
        failures.append("no positive closure fixtures found")
    if not negative_files:
        failures.append("no negative closure fixtures found")

    for path in positive_files:
        instance = load_json(path)
        errors = format_errors(validator, instance)
        if errors:
            failures.append(
                f"positive fixture {path.relative_to(ROOT)} failed:\n  "
                + "\n  ".join(errors)
            )
        else:
            print(f"PASS positive: {path.relative_to(ROOT)}")

    for path in negative_files:
        instance = load_json(path)
        errors = format_errors(validator, instance)
        if not errors:
            failures.append(
                f"negative fixture {path.relative_to(ROOT)} unexpectedly validated"
            )
        else:
            print(f"PASS negative: {path.relative_to(ROOT)} rejected")
            for error in errors:
                print(f"  expected rejection: {error}")

    if failures:
        print("\nClosure schema validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("\nAll closure schema fixtures behaved as expected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

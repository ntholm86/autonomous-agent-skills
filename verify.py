#!/usr/bin/env python3
"""verify.py — mechanical integrity check for the trail.

Replaces verify-suite.ps1 from v2. Pure-Python, zero dependencies, runs on
Windows / macOS / Linux.

Checks:
1. .trail/log.md exists and is non-empty.
2. Every entry heading matches `## YYYY-MM-DD — <slug>`.
3. Entries are in non-decreasing date order.
4. Every entry contains the mandatory metadata fields: target, agent, skill, outcome.
5. No U+FFFD replacement characters (mojibake) anywhere in the live tree
    (excludes archive/).
6. Live repo files that current docs depend on exist.
7. Required markdown docs do not contain duplicate H1 headings, and their local
    markdown links resolve.
8. Every `session-file:` reference in log.md points to an existing file.
9. Entries written under the v3.8.0 reflection contract (from
    `improve-step6b-trigger-observability` onward) record an explicit
    four-trigger evaluation — bare "N/A"/"TODO" rejected — and include a
    macro-Hansei subsection when any trigger fired.

Exit code: 0 if all checks pass, 1 otherwise.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOG = ROOT / ".trail" / "log.md"

REQUIRED_FILES = [
    "README.md",
    "CHANGELOG.md",
    "INSTALLING.md",
    "improve/SKILL.md",
    "probe/SKILL.md",
    "intent/SKILL.md",
    "trail/SKILL.md",
    "vision/SKILL.md",
    "retrospect/SKILL.md",
    ".trail/log.md",
]

ENTRY_HEADING = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2})\s+[\u2014-]\s+(.+?)\s*$")
META_FIELD = re.compile(r"^-\s+(target|agent|skill|outcome)\s*:", re.MULTILINE)
SESSION_FILE_META = re.compile(r"^-\s+session-file:\s+(.+?)\s*$", re.MULTILINE)
H1_HEADING = re.compile(r"^#\s+.+$", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
EXTERNAL_LINK = re.compile(r"^[a-z][a-z0-9+.-]*:", re.IGNORECASE)


def _strip_fenced_code_blocks(text: str) -> str:
    lines: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            lines.append(line)
    return "\n".join(lines)


def check_required_files() -> list[str]:
    failures: list[str] = []
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            failures.append(f"missing required file: {rel}")
    return failures


def check_log_format() -> list[str]:
    failures: list[str] = []
    if not LOG.exists():
        return [".trail/log.md does not exist"]
    text = LOG.read_text(encoding="utf-8")
    if not text.strip():
        return [".trail/log.md is empty"]

    entries: list[tuple[str, str, str]] = []
    current_date: str | None = None
    current_slug: str | None = None
    current_body: list[str] = []
    malformed_heading = re.compile(r"^#{1,3}\s*\d{4}-\d{2}-\d{2}")
    for line in text.splitlines():
        m = ENTRY_HEADING.match(line)
        if m:
            if current_date is not None:
                entries.append((current_date, current_slug or "", "\n".join(current_body)))
            current_date, current_slug = m.group(1), m.group(2)
            current_body = []
        elif malformed_heading.match(line):
            failures.append(f"malformed entry heading in .trail/log.md: {line}")
        elif current_date is not None:
            current_body.append(line)
    if current_date is not None:
        entries.append((current_date, current_slug or "", "\n".join(current_body)))

    if not entries:
        failures.append(".trail/log.md contains no entries matching '## YYYY-MM-DD — slug'")
        return failures

    prev_date: str | None = None
    for date, slug, body in entries:
        if prev_date is not None and date < prev_date:
            failures.append(f"entries out of chronological order: {date} after {prev_date}")
        prev_date = date

        meta_fields = set(META_FIELD.findall(body))
        for required in ("target", "agent", "skill", "outcome"):
            if required not in meta_fields:
                failures.append(f"entry '{date} {slug}' missing required metadata field: {required}")
    return failures


def check_no_mojibake() -> list[str]:
    failures: list[str] = []
    skip_dirs = {"archive", ".git"}
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in skip_dirs for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix.lower() not in {".md", ".txt", ".py", ".yml", ".yaml", ".cff", ".json"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            failures.append(f"non-UTF-8 file: {path.relative_to(ROOT)}")
            continue
        if "\ufffd" in text:
            failures.append(f"replacement character (mojibake) in {path.relative_to(ROOT)}")
    return failures


def check_required_markdown_docs() -> list[str]:
    failures: list[str] = []
    # PRINCIPLES.md is a verbatim external copy; its relative links point to its home repo
    markdown_files = [rel for rel in REQUIRED_FILES if rel.endswith(".md") and rel not in (".trail/log.md", "PRINCIPLES.md")]
    for rel in markdown_files:
        path = ROOT / rel
        if not path.exists():
            continue

        text = path.read_text(encoding="utf-8")
        analysis_text = _strip_fenced_code_blocks(text)
        if len(H1_HEADING.findall(analysis_text)) > 1:
            failures.append(f"multiple H1 headings in {rel}")

        for raw_target in MARKDOWN_LINK.findall(analysis_text):
            target = raw_target.strip()
            if not target or target.startswith("#") or EXTERNAL_LINK.match(target):
                continue

            link_path = target.split("#", 1)[0]
            if not link_path:
                continue

            resolved = (path.parent / link_path).resolve()
            if not resolved.exists():
                failures.append(f"broken local markdown link in {rel}: {target}")

    return failures


# Slug at and after which the v3.8.0 reflection contract applies.
# Entries strictly before this slug (in file order) are grandfathered.
TRIGGER_CONTRACT_SLUG = "improve-step6b-trigger-observability"

TRIGGER_KEYWORDS = ("recurring", "silence", "contradict", "operator")
MACRO_HANSEI_HEADING = re.compile(
    r"^\*\*Across-trail macro-Hansei", re.MULTILINE
)
TRIGGER_LINE = re.compile(
    r"^-\s+\*([^*]*?)\*\s*(.*)$",
    re.MULTILINE,
)
BARE_PLACEHOLDER = re.compile(r"^\s*(?:n/?a|todo)\s*\.?\s*$", re.IGNORECASE)
FIRED_NOT_NEGATED = re.compile(r"(?<!not\s)\bfired\b", re.IGNORECASE)


def _parse_entries(text: str) -> list[tuple[str, str, str]]:
    entries: list[tuple[str, str, str]] = []
    current_date: str | None = None
    current_slug: str | None = None
    current_body: list[str] = []
    for line in text.splitlines():
        m = ENTRY_HEADING.match(line)
        if m:
            if current_date is not None:
                entries.append((current_date, current_slug or "", "\n".join(current_body)))
            current_date, current_slug = m.group(1), m.group(2)
            current_body = []
        elif current_date is not None:
            current_body.append(line)
    if current_date is not None:
        entries.append((current_date, current_slug or "", "\n".join(current_body)))
    return entries


def check_trigger_evaluation() -> list[str]:
    """Enforce the v3.8.0 reflection contract for entries from the contract slug onward."""
    failures: list[str] = []
    if not LOG.exists():
        return failures
    entries = _parse_entries(LOG.read_text(encoding="utf-8"))

    contract_index: int | None = None
    for i, (_, slug, _) in enumerate(entries):
        if slug == TRIGGER_CONTRACT_SLUG:
            contract_index = i
            break
    if contract_index is None:
        return failures  # contract entry not yet present; nothing to enforce

    for date, slug, body in entries[contract_index:]:
        matches = TRIGGER_LINE.findall(body)
        # Map keyword -> content for trigger lines (label may include trailing ':').
        trigger_content: dict[str, str] = {}
        for label, content in matches:
            label_lc = label.lower()
            for kw in TRIGGER_KEYWORDS:
                if kw in label_lc:
                    trigger_content.setdefault(kw, content)
                    break
        for required in TRIGGER_KEYWORDS:
            if required not in trigger_content:
                failures.append(
                    f"entry '{date} {slug}' missing trigger evaluation line for: {required}"
                )

        any_fired = False
        for kw, content in trigger_content.items():
            placeholder_text = content.strip().strip("*").strip()
            if BARE_PLACEHOLDER.match(placeholder_text):
                failures.append(
                    f"entry '{date} {slug}' trigger '{kw}' uses bare placeholder"
                )
                continue
            if FIRED_NOT_NEGATED.search(content):
                any_fired = True

        if any_fired and not MACRO_HANSEI_HEADING.search(body):
            failures.append(
                f"entry '{date} {slug}' has a fired trigger but no 'Across-trail macro-Hansei' subsection"
            )

    return failures


def check_session_files() -> list[str]:
    """Check that every session-file: reference in log.md points to an existing file."""
    failures: list[str] = []
    if not LOG.exists():
        return failures
    text = LOG.read_text(encoding="utf-8")

    entries: list[tuple[str, str, str]] = []
    current_date: str | None = None
    current_slug: str | None = None
    current_body: list[str] = []
    for line in text.splitlines():
        m = ENTRY_HEADING.match(line)
        if m:
            if current_date is not None:
                entries.append((current_date, current_slug or "", "\n".join(current_body)))
            current_date, current_slug = m.group(1), m.group(2)
            current_body = []
        elif current_date is not None:
            current_body.append(line)
    if current_date is not None:
        entries.append((current_date, current_slug or "", "\n".join(current_body)))

    for date, slug, body in entries:
        for m in SESSION_FILE_META.finditer(body):
            rel_path = m.group(1).strip()
            if not (ROOT / rel_path).exists():
                failures.append(
                    f"entry '{date} {slug}' references missing session file: {rel_path}"
                )
    return failures


def main() -> int:
    all_failures: list[str] = []
    all_failures.extend(check_required_files())
    all_failures.extend(check_log_format())
    all_failures.extend(check_no_mojibake())
    all_failures.extend(check_required_markdown_docs())
    all_failures.extend(check_session_files())
    all_failures.extend(check_trigger_evaluation())

    if all_failures:
        print(f"FAIL — {len(all_failures)} issue(s):")
        for f in all_failures:
            print(f"  - {f}")
        return 1
    print("OK — trail integrity checks pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())

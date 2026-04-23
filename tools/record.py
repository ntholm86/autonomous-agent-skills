#!/usr/bin/env python3
"""record.py — append entries to trail/log.md and digest the latest one.

Replaces the kiroku-*.ps1 family from v2. Pure-Python, zero dependencies.

Subcommands:
  new --slug=<slug> [--target=<target>] [--skill=<skill>]
      Append a stub entry to trail/log.md and print the line range so the
      agent (or operator) can edit it.

  summary
      Print the most recent entry. Suitable for a 60-second observer view.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "trail" / "log.md"

ENTRY_HEADING = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2})\s+[\u2014-]\s+(.+?)\s*$")

STUB_TEMPLATE = """\

## {date} \u2014 {slug}

- target: {target}
- operator: TODO
- agent: TODO (provider, tool-call ID prefix)
- skill: {skill}
- outcome: TODO
- delta: TODO

### Interpretation of the ask

TODO

### Examination

TODO

### Decision

[!DECISION] TODO

### Action

TODO

### Reflection

TODO
"""


def cmd_new(args: argparse.Namespace) -> int:
    if not LOG.exists():
        print(f"ERROR: {LOG} does not exist. Create it first (it should already be in the repo).", file=sys.stderr)
        return 1
    date = _dt.date.today().isoformat()
    stub = STUB_TEMPLATE.format(
        date=date,
        slug=args.slug,
        target=args.target or "TODO",
        skill=args.skill or "improve",
    )
    existing = LOG.read_text(encoding="utf-8")
    if not existing.endswith("\n"):
        existing += "\n"
    new_text = existing + stub
    LOG.write_text(new_text, encoding="utf-8")

    # Compute and print the line range of the new entry.
    start_line = existing.count("\n") + 1
    end_line = new_text.count("\n")
    print(f"appended stub: trail/log.md lines {start_line}-{end_line}")
    print(f"  date: {date}")
    print(f"  slug: {args.slug}")
    return 0


def cmd_summary(_args: argparse.Namespace) -> int:
    if not LOG.exists():
        print(f"ERROR: {LOG} does not exist.", file=sys.stderr)
        return 1
    text = LOG.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Find the last entry heading.
    last_idx: int | None = None
    for i, line in enumerate(lines):
        if ENTRY_HEADING.match(line):
            last_idx = i
    if last_idx is None:
        print("(no entries in trail/log.md)")
        return 0

    # Print from the last heading to EOF, but cap at 80 lines for digest size.
    body = lines[last_idx:]
    if len(body) > 80:
        body = body[:80] + ["", f"... ({len(lines) - last_idx - 80} more lines; see trail/log.md)"]
    print("\n".join(body))
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="record.py", description="Append to and read from trail/log.md.")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_new = sub.add_parser("new", help="Append a stub entry to trail/log.md.")
    p_new.add_argument("--slug", required=True, help="Short slug for the entry (e.g. 'v3-redesign').")
    p_new.add_argument("--target", default=None, help="What is being operated on.")
    p_new.add_argument("--skill", default=None, help="Which skill is running (improve | probe).")
    p_new.set_defaults(func=cmd_new)

    p_sum = sub.add_parser("summary", help="Print the most recent entry as a 60-second digest.")
    p_sum.set_defaults(func=cmd_summary)
    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""record.py — append entries to .trail/log.md and digest the latest one.

Replaces the kiroku-*.ps1 family from v2. Pure-Python, zero dependencies.

Subcommands:
  new --slug=<slug> [--target=<target>] [--skill=<skill>]
      Append a stub entry to .trail/log.md and print the line range so the
      agent (or operator) can edit it.

  summary
      Print the most recent entry. Suitable for a 60-second observer view.

  history [--target=<target>]
      Print a per-iteration timeline: date, slug, outcome, and decisions.
      Shows convergence direction at a glance. Optionally filter by target.

  learning [--write]
      Print (or write to .trail/learning.md) a compact chronological extract
      of every [!REALIZATION] and [!REVERSAL] marker from .trail/log.md.
      The learning surface — what the loop has actually concluded across runs.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import os
import re
import sys
from pathlib import Path


def _resolve_root() -> Path:
    """Resolve the target repo root.

    Order: $TRAIL_ROOT env var, else current working directory.
    record.py lives in the skills install (read-only); it always writes
    into the target repo, never into its own folder.
    """
    env = os.environ.get("TRAIL_ROOT")
    if env:
        return Path(env).resolve()
    return Path.cwd().resolve()


ROOT = _resolve_root()
LOG = ROOT / ".trail" / "log.md"

ENTRY_HEADING = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2})\s+[\u2014-]\s+(.+?)\s*$")
META_FIELD = re.compile(r"^-\s+(target|outcome|delta):\s*(.+)$")
MARKER = re.compile(r"\[!(DECISION|REVERSAL|REALIZATION)\]\s*(.+?)\s*$")

STUB_TEMPLATE = """\

## {date} \u2014 {slug}

- target: {target}
- operator: TODO
- agent: TODO (provider, tool-call ID prefix)
- skill: {skill}
- session-file: .trail/sessions/{date}-{slug}.md
- outcome: TODO
- delta: TODO

### Interpretation of the ask

TODO

### Examination

TODO

### Decision

[!DECISION] TODO

### Prediction

TODO — state a falsifiable prediction of what this change will achieve and what will not happen, before taking action.

### Action and Outcome

TODO — detail what was done, and explicitly compare the actual outcome to the prediction above.

### Reflection

**Falsifiable claim about the target's current state:**

TODO — a specific, disprovable statement about what is true of the target right now.

**Named blind spot:**

TODO — what this examination likely missed, and why.

**Imagined-reader pushback:**

TODO — the strongest objection from someone who knows the target better.

**Across-trail trigger evaluation** *(every entry — one line per trigger, with brief evidence from the trail; bare "N/A" is not allowed)*:

- *Recurring finding-class:* TODO (FIRED / not fired — evidence from last N entries)
- *About to declare silence:* TODO
- *Contradicts prior [!REALIZATION]:* TODO
- *Operator explicitly asked:* TODO

**Across-trail macro-Hansei** *(only if a trigger above fired; otherwise omit this subsection)*:

TODO
"""


def _safe_read_log() -> str:
    """Read the log file, gracefully falling back if utf-8 strict decoding fails."""
    try:
        return LOG.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        # Fallback for Windows-1252 / ANSI encoded files containing em-dashes etc.
        return LOG.read_text(encoding="utf-8", errors="replace")

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
    existing = _safe_read_log()
    if not existing.endswith("\n"):
        existing += "\n"
    new_text = existing + stub
    LOG.write_text(new_text, encoding="utf-8")

    # Compute and print the line range of the new entry.
    start_line = existing.count("\n") + 1
    end_line = new_text.count("\n")
    print(f"appended stub: .trail/log.md lines {start_line}-{end_line}")
    print(f"  date: {date}")
    print(f"  slug: {args.slug}")
    return 0


def _parse_entries(text: str) -> list[dict]:
    """Parse .trail/log.md into a list of entry dicts."""
    lines = text.splitlines()
    entries: list[dict] = []
    current: dict | None = None

    for line in lines:
        m = ENTRY_HEADING.match(line)
        if m:
            if current is not None:
                entries.append(current)
            current = {
                "date": m.group(1),
                "slug": m.group(2),
                "target": "",
                "outcome": "",
                "delta": "",
                "decisions": [],
                "reversals": [],
                "realizations": [],
            }
            continue

        if current is None:
            continue

        meta = META_FIELD.match(line)
        if meta:
            current[meta.group(1)] = meta.group(2).strip()
            continue

        marker = MARKER.search(line)
        if marker:
            kind = marker.group(1).lower() + "s"
            current[kind].append(marker.group(2).strip())

    if current is not None:
        entries.append(current)
    return entries


def _render_history(entries: list[dict], markdown: bool) -> str:
    """Render entries as either a terminal timeline or a markdown document."""
    lines: list[str] = []

    if markdown:
        lines.append("# History")
        lines.append("")
        lines.append("Auto-generated from `.trail/log.md` by the `record.py history --write` command in the autonomous-agent-skills install.")
        lines.append("Do not edit by hand — re-run the command to refresh.")
        lines.append("")
        lines.append("| # | Date | Slug | Outcome | Delta |")
        lines.append("|---|------|------|---------|-------|")
        for i, e in enumerate(entries, 1):
            icon = "·" if "silence" in e["outcome"].lower() else "▸"
            outcome = (e["outcome"] or "").replace("|", "\\|")
            delta = (e["delta"] or "").replace("|", "\\|")
            slug = e["slug"].replace("|", "\\|")
            lines.append(f"| {icon} {i} | {e['date']} | {slug} | {outcome} | {delta} |")
        lines.append("")

        # Decisions / reversals per entry
        for i, e in enumerate(entries, 1):
            if not (e["decisions"] or e["reversals"]):
                continue
            lines.append(f"### Run {i} — {e['date']} — {e['slug']}")
            lines.append("")
            for d in e["decisions"]:
                lines.append(f"- **decided:** {d}")
            for r in e["reversals"]:
                lines.append(f"- **REVERSAL:** {r}")
            lines.append("")

        silence_count = sum(1 for e in entries if "silence" in e["outcome"].lower())
        change_count = len(entries) - silence_count
        lines.append(f"**{len(entries)} runs total — {change_count} with changes, {silence_count} silence**")
        return "\n".join(lines) + "\n"

    # Terminal format (original)
    for i, e in enumerate(entries, 1):
        icon = "·" if "silence" in e["outcome"].lower() else "▸"
        lines.append(f"{icon} Run {i:>2}  {e['date']}  {e['slug']}")
        if e["outcome"]:
            lines.append(f"         outcome:  {e['outcome']}")
        if e["delta"] and e["delta"].upper() != "TODO":
            lines.append(f"         delta:    {e['delta']}")
        for d in e["decisions"]:
            truncated = d if len(d) <= 80 else d[:77] + "..."
            lines.append(f"         decided:  {truncated}")
        for r in e["reversals"]:
            truncated = r if len(r) <= 80 else r[:77] + "..."
            lines.append(f"         REVERSAL: {truncated}")
        lines.append("")
    silence_count = sum(1 for e in entries if "silence" in e["outcome"].lower())
    change_count = len(entries) - silence_count
    lines.append(f"  {len(entries)} runs total — {change_count} with changes, {silence_count} silence")
    return "\n".join(lines)


def cmd_history(args: argparse.Namespace) -> int:
    if not LOG.exists():
        print(f"ERROR: {LOG} does not exist.", file=sys.stderr)
        return 1

    text = _safe_read_log()
    entries = _parse_entries(text)

    if not entries:
        print("(no entries in .trail/log.md)")
        return 0

    target_filter: str | None = getattr(args, "target", None)
    if target_filter:
        entries = [e for e in entries if target_filter.lower() in e["target"].lower()]
        if not entries:
            print(f"(no entries matching target '{target_filter}')")
            return 0

    write = getattr(args, "write", False)
    output = _render_history(entries, markdown=write)

    if write:
        out_path = LOG.parent / "history.md"
        out_path.write_text(output, encoding="utf-8")
        print(f"wrote {out_path} ({len(entries)} entries)")
    else:
        print(output)
    return 0


def _render_learning(entries: list[dict], markdown: bool) -> str:
    """Render the [!REALIZATION] / [!REVERSAL] markers across all entries.

    The compact learning surface — what the loop has concluded across runs.
    Each item carries its date+slug context so the source entry is locatable
    in log.md.
    """
    items: list[tuple[str, str, str, str]] = []  # (date, slug, kind, content)
    for e in entries:
        for r in e["realizations"]:
            items.append((e["date"], e["slug"], "REALIZATION", r))
        for r in e["reversals"]:
            items.append((e["date"], e["slug"], "REVERSAL", r))

    if markdown:
        lines: list[str] = []
        lines.append("# Learning")
        lines.append("")
        lines.append("Auto-generated from `.trail/log.md` by the `record.py learning --write` command in the autonomous-agent-skills install.")
        lines.append("Do not edit by hand — re-run the command to refresh.")
        lines.append("")
        lines.append("Compact chronological extract of every `[!REALIZATION]` and `[!REVERSAL]` marker. The learning surface — what the loop has actually concluded across runs. Read this before reading `log.md` in full; reach for `log.md` only when an item here needs its surrounding context.")
        lines.append("")
        if not items:
            lines.append("_(no markers found)_")
            return "\n".join(lines) + "\n"
        for date, slug, kind, content in items:
            lines.append(f"## {date} — {slug}")
            lines.append("")
            lines.append(f"**[!{kind}]** {content}")
            lines.append("")
        lines.append(f"---")
        lines.append("")
        realisation_count = sum(1 for it in items if it[2] == "REALIZATION")
        reversal_count = len(items) - realisation_count
        lines.append(f"**{len(items)} markers — {realisation_count} realisations, {reversal_count} reversals**")
        return "\n".join(lines) + "\n"

    # Terminal format
    lines = []
    if not items:
        lines.append("(no [!REALIZATION] or [!REVERSAL] markers found)")
        return "\n".join(lines)
    for date, slug, kind, content in items:
        truncated = content if len(content) <= 100 else content[:97] + "..."
        lines.append(f"{date}  {slug}")
        lines.append(f"  [!{kind}] {truncated}")
        lines.append("")
    realisation_count = sum(1 for it in items if it[2] == "REALIZATION")
    reversal_count = len(items) - realisation_count
    lines.append(f"  {len(items)} markers — {realisation_count} realisations, {reversal_count} reversals")
    return "\n".join(lines)


def cmd_learning(args: argparse.Namespace) -> int:
    if not LOG.exists():
        print(f"ERROR: {LOG} does not exist.", file=sys.stderr)
        return 1
    text = _safe_read_log()
    entries = _parse_entries(text)
    write = getattr(args, "write", False)
    output = _render_learning(entries, markdown=write)
    if write:
        out_path = LOG.parent / "learning.md"
        out_path.write_text(output, encoding="utf-8")
        item_count = sum(len(e["realizations"]) + len(e["reversals"]) for e in entries)
        print(f"wrote {out_path} ({item_count} markers from {len(entries)} entries)")
    else:
        print(output)
    return 0


def cmd_summary(_args: argparse.Namespace) -> int:
    if not LOG.exists():
        print(f"ERROR: {LOG} does not exist.", file=sys.stderr)
        return 1
    text = _safe_read_log()
    lines = text.splitlines()

    # Find the last entry heading.
    last_idx: int | None = None
    for i, line in enumerate(lines):
        if ENTRY_HEADING.match(line):
            last_idx = i
    if last_idx is None:
        print("(no entries in .trail/log.md)")
        return 0

    # Print from the last heading to EOF, but cap at 80 lines for digest size.
    body = lines[last_idx:]
    if len(body) > 80:
        body = body[:80] + ["", f"... ({len(lines) - last_idx - 80} more lines; see .trail/log.md)"]
    print("\n".join(body))
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="record.py", description="Append to and read from .trail/log.md.")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_new = sub.add_parser("new", help="Append a stub entry to .trail/log.md.")
    p_new.add_argument("--slug", required=True, help="Short slug for the entry (e.g. 'v3-redesign').")
    p_new.add_argument("--target", default=None, help="What is being operated on.")
    p_new.add_argument("--skill", default=None, help="Which skill is running (improve | probe).")
    p_new.set_defaults(func=cmd_new)

    p_sum = sub.add_parser("summary", help="Print the most recent entry as a 60-second digest.")
    p_sum.set_defaults(func=cmd_summary)

    p_hist = sub.add_parser("history", help="Print a per-iteration timeline of all trail entries.")
    p_hist.add_argument("--target", default=None, help="Filter entries by target name (substring match).")
    p_hist.add_argument("--write", action="store_true", help="Write .trail/history.md as committed markdown instead of printing.")
    p_hist.set_defaults(func=cmd_history)

    p_learn = sub.add_parser("learning", help="Extract every [!REALIZATION]/[!REVERSAL] marker — the compact learning surface.")
    p_learn.add_argument("--write", action="store_true", help="Write .trail/learning.md as committed markdown instead of printing.")
    p_learn.set_defaults(func=cmd_learning)

    return p


def main(argv: list[str] | None = None) -> int:
    # Ensure UTF-8 output on platforms where the default encoding is not UTF-8
    # (e.g. Windows cp1252 terminals). Trail entries contain em-dashes, arrows,
    # and other Unicode characters that cp1252 cannot encode.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())

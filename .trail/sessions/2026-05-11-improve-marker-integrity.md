# Session: improve-marker-integrity

**Date:** 2026-05-11  
**Skill:** improve + trail  
**Target:** autonomous-agent-skills

## Summary

Iteration 7 of the improvement loop. Two bundled changes: (1) MARKER regex fix in record.py, (2) staleness check in verify.py. A third incidental change: deduplication of check_session_files().

A fourth idea (check_non_canonical_markers) was attempted and reversed after producing 46 failures, most of them false positives from entries that discuss marker syntax rather than use it.

## Changes

- `tools/record.py`: removed `^` anchor from MARKER regex; changed `MARKER.match(line)` to `MARKER.search(line)`.
- `verify.py`: added `check_derived_artifact_freshness()` as check 10; refactored `check_session_files()` to use `_parse_entries()` helper; updated docstring.

## Outcome

- Marker count in learning.md: 78 → 118 (37 previously-dropped markers recovered, plus 3 new entries).
- verify.py: single pre-existing grandfathered failure remains; no new failures.

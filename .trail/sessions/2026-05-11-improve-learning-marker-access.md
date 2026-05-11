# Session — 2026-05-11 improve-learning-marker-access

Detail file for the trail entry of the same slug. Source of truth is `.trail/log.md`.

## What this run did

Added explicit `[!REALIZATION]`/`[!REVERSAL]` marker-surfacing guidance to improve step 1's log.md reading instruction. Bumped improve/SKILL.md 3.8.0 → 3.8.1.

## The finding

Vision names *learning* as the most underdeveloped component of memory/learning/meta-cognition. The learning mechanism depends on agents acting on prior `[!REALIZATION]` markers in subsequent sessions. But improve step 1 only said to "read log.md for evidence" — no access path when the log is 4500+ lines. The markers are defined in trail/SKILL.md's "Three resolutions" section but were not referenced in the improve spec agents read before every run. The mechanism was documented in the wrong place.

## Files changed

- `improve/SKILL.md` — one sentence added to step 1 log.md bullet; version 3.8.0 → 3.8.1.
- `.trail/log.md` — entry appended.
- `.trail/sessions/2026-05-11-improve-learning-marker-access.md` — this file.

## verify.py status

`FAIL — 1 issue(s)` — same single pre-existing `retrospect-run-2` failure. No regressions. Prediction held.

## Pre-committed for next run

`check_session_files()` in verify.py still has its own inline copy of the `_parse_entries()` parsing loop. The helper was extracted in the last run for `check_trigger_evaluation()` but not applied to `check_session_files()`. This is a secondary inconsistency — no strategic impact, but clean code and one less maintenance surface. The next run should treat this as the pre-committed candidate unless a strictly higher-leverage finding surfaces.

## Imagined-reader pushback (for future record)

"Adding 'search for markers' to the spec doesn't help an agent in a session where the log is too long to fit in context. The markers are still buried in a 4500-line file. The learning residue needs to live in a dedicated, compact artifact (like a `[!REALIZATIONS].md` extract) for the access-path fix to be operationally meaningful." — A valid objection. The fix makes the access path explicit but does not solve the context-budget problem if the log grows beyond model context limits.

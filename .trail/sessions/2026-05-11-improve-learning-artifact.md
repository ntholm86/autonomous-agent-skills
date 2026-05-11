# Session — 2026-05-11 improve-learning-artifact

Detail file for the trail entry of the same slug. Source of truth is `.trail/log.md`.

## What this run did

First operator-directed strategic run of the session. Operator override of the prior entry's pre-committed verify.py-deduplication candidate, in response to the agent's own assessment that 4 prior runs had been technically sound but strategically shallow (none directly engaging vision's "learning is most underdeveloped" claim).

Added `record.py learning [--write]` and `.trail/learning.md` — a compact chronological extract of every `[!REALIZATION]`/`[!REVERSAL]` marker. improve step 1 now reads it before log.md.

## The structural insight

Vision's three pillars (memory, learning, meta-cognition) each need a first-class compact artifact to work cross-session:

- **Memory:** log.md (full, source of truth) + history.md (compact derived view).
- **Meta-cognition:** log.md + retrospect.md (derived synthesis).
- **Learning:** log.md only — the inline markers were the entire surface. **Asymmetric.**

This run closes the asymmetry by adding learning.md, the equivalent of history.md but for the learning pillar.

## Files changed

- `tools/record.py` — added `_render_learning()`, `cmd_learning()`, wired `learning` subcommand. (Transient bug: dropped `cmd_summary` body during one replace; caught and restored immediately.)
- `improve/SKILL.md` — version 3.8.1 → 3.8.2; step 1 reads learning.md before log.md (replacing iteration-4's marker-search guidance with a stronger primary-surface instruction; log.md demoted to "rarely needed end-to-end").
- `trail/SKILL.md` — version 1.12.0 → 1.13.0; file map adds learning.md with one paragraph explaining its role.
- `.trail/learning.md` — generated. 74 markers from 104 entries. 35KB vs log.md's 376KB (9.5%).
- `.trail/log.md` — entry appended with macro-Hansei (operator-asked trigger fired).
- `.trail/sessions/2026-05-11-improve-learning-artifact.md` — this file.

## verify.py status

`FAIL — 1 issue(s)` — same single pre-existing `retrospect-run-2` failure. No regressions. learning.md passes the mojibake check.

## What this run does NOT fix

The agent's *capability* to act on what it reads. learning.md makes prior learning compactly available; whether a fresh agent then recognises when its current decision rediscovers a prior realization is a separate model-capability problem. The gap is now testable cleanly: a future fresh-session agent that misses a learning.md item is exhibiting capability failure, not infrastructure failure.

## Imagined-reader pushback (carried for future record)

"You generated learning.md once. It's stale the moment the next run appends to log.md. The on-demand pattern makes sense for history.md (humans look occasionally) but not for learning.md (agents look every run). You either need Trail to regenerate it on every append, or a verify.py check that fails when learning.md is older than log.md. Otherwise the very next run will read a learning.md missing the most recent realisation — including this one."

This is the pre-committed candidate for the next run: **regenerate learning.md as part of the trail commit step, OR add a verify.py check that fails when learning.md predates log.md's most recent entry.** The first option is more reliable; the second is less coupling.

## Why this run is different from the prior 4

The first 4 iterations of this session were all mechanism polish driven by the agent's safe pre-committed candidates. This run was operator-directed against vision's named gap. The arc-claim worth carrying: tactical pre-commitments are a useful continuity mechanism but they will not produce strategic moves on their own. The combination — agent surfaces strategic gaps in honest self-assessment, operator decides which one to engage — is what produced this run.

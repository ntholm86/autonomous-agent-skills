# retrospect.md — autonomous-agent-skills

_Last updated: 2026-05-11 (run: retrospect-after-marker-integrity)_

## Scope of this read

The arc from entry 63 (`feat-retrospect-skill`, 2026-05-01) through entry 106 (`improve-marker-integrity`, 2026-05-11) — 44 entries spanning the introduction of the Retrospect skill, the rationalization-loop mitigations sub-arc (May 5), and the 12-iteration trail-infrastructure sweep that closed today.

## Current claims

- **The target's centre of gravity has visibly shifted from skill mechanics to trail epistemics, and the shift has held for ~25 entries.** The May 5 arc-claim ("the remaining weight now sits in trail epistemics, not skill mechanics") was followed by 19 of the next 21 entries targeting trail/learning/memory infrastructure. This is no longer a hypothesis about where the work is — it is observably where the work has been.

- **The Memory Model's three pillars now have artifact symmetry.** Memory has `log.md` + `history.md`; meta-cognition has `log.md` + `retrospect.md`; learning has `log.md` + `learning.md`. The third pillar's compact artifact was the asymmetric gap until iteration 5 of today's sweep; iteration 6 made regeneration mandatory; iteration 7 fixed the parser so the artifact is actually accurate (78 → 118 markers recovered). The triad is now structurally complete. This is the most significant architectural change since the introduction of Retrospect itself.

- **The operator-gate pattern is empirically the strategic engine, but it is informal.** Across the May 11 sweep, the genuinely strategic moves (creating learning.md, mandating freshness, fixing the parser) all started from "what should we do next?" exchanges where the agent ranked options and the operator picked. The mechanical moves (template alignment, verify.py enforcement of an already-decided contract) did not require it. Vision states "what to implement is the irreducible human gate"; the trail shows this gate operating as ad-hoc dialogue, not as a defined skill step. Whether to formalize it (as a step in Improve, or as an Intent invocation pattern) is the open question.

- **The recurring-finding-class trigger has demonstrated load-bearing value.** The MARKER parser bug hit two consecutive iterations and was named explicitly in iter 6's pre-commitment. Without the trigger contract (introduced iter 1 of this sweep), the bug would likely have hit a third time — the operational pattern of "noticed but deferred" was visible in iter 5 too. The trigger surfaced the recurrence in time for iter 7 to act on it. This is the first arc evidence that step 6b's trigger contract changes behavior, not just documentation.

- **The reversal-to-realization ratio is 2:118 across the whole arc and 0:14 across this session's strategic moves.** This is far below what Retrospect's own adversarial-audit lens (step 2b) treats as plausible for non-trivial work. Today alone had at least one explicit course reversal (`check_non_canonical_markers` attempted and removed) — it was *narrated* in the entry but not marked with `[!REVERSAL]`. The arc shows authors reach for `[!REALIZATION]` readily and `[!REVERSAL]` rarely. Either the loop is genuinely converging at an implausible rate, or the reversal marker is under-used. The latter is the more likely reading.

- **The vision document is doing real work.** The "three pillars" framing in vision.md was treated as a literal architecture target by today's sweep, and it produced concrete code (learning.md). This is the first arc instance where a vision passage drove an artifact decision rather than just orienting reflection. Vision is no longer only the destination; it is also a source of architectural primitives the loop quotes back at itself.

## What the next runs should test

- **Cross-session learning-acted-on.** A future fresh-session agent should reach for `learning.md` at step 1 and reference specific prior realizations by date+slug rather than rediscovering them. If the next 3 sessions show no such reference, the artifact is being read but not acted on — capability gap, not infrastructure gap.

- **Reversal-density honesty.** Future entries that change course mid-iteration (not just from prior runs) should include `[!REVERSAL]`. The next 5 entries should be checked: any iteration that backs out of a planned change must mark it.

- **Operator-gate formalization vs. preservation.** Run an Intent or Vision dialogue specifically on whether the "what should we do next?" exchange should become a documented step. Either outcome is informative — formalizing it makes it auditable; explicitly preserving it as informal makes Vision's "operator-AI partnership" claim concrete.

- **The mtime-based staleness check on a fresh clone.** Iteration 7's named blind spot: after `git clone`, both `log.md` and `learning.md` have the same checkout timestamp, so the check passes regardless of pre-commit state. A future iteration should test this — clone the repo fresh, see what verify.py reports.

## Active operational rules

- **Every spec change must be paired with enforcement in the same session.** The recurring failure class across this arc is "spec written, enforcement deferred." Iter 1 (trigger contract spec) → iter 3 (verify.py enforcement) is a 2-iteration gap. The trail freshness mandate (iter 6) → enforcement (iter 7) is a 1-iteration gap. Aim for zero — write the spec change and the verify.py check in the same commit.

- **Mark `[!REVERSAL]` when the iteration backs out of a planned step, not only when reversing prior runs.** Today's `check_non_canonical_markers` removal was a within-iteration reversal that should have been marked. The retroactive guidance: if the Action and Outcome section says "attempted X then removed it," that's a `[!REVERSAL]`.

- **When changing the MARKER parser or related plumbing, smoke-check by comparing marker counts before and after.** Iter 5 and iter 6 both lost their own realizations to the parser bug, caught only when the count was checked. Iter 7's fix recovered 37 historical markers. Make this comparison part of any record.py change.

- **Treat the `learning.md` and `history.md` regeneration as part of the commit, not a separate step.** Per trail v1.14.0 and verify.py check 10. Forgetting this now fails verify.

- **Disregard "imminent silence" predictions.** Carried forward from prior retrospect — still proven by this arc. Iter 4's "technically well, strategically shallow" honest self-assessment was followed by 3 strategic iterations the agent did not predict.

- **A structural change creates a long tail of documentation/tooling inconsistencies.** Carried forward — confirmed again by today's sweep (the trail v1.13.0 → v1.14.0 spec change required a parser fix and an enforcement check before the change was actually load-bearing).

## Loop-effectiveness notes

The loop has measurably improved at strategic work since the May 5 mitigations arc. The reflection-mechanism redesign (run 54), the trigger contract (today, iter 1), the learning artifact (iter 5), and the parser fix (iter 7) are all genuinely strategic — each names a structural property of the trail and changes the architecture, not the documentation.

But two structural caveats remain:

1. **The strategic moves still depend on operator gating.** None of the four moves above arose unprompted. The operator's "what should we do next?" question is the trigger; the agent's ranking is the proposal; the operator's selection is the decision. Vision says this is the right architecture. The arc confirms it is the *operating* architecture. The question is whether it should be more visible.

2. **The reversal asymmetry is a confabulation signal Retrospect itself should be alert to.** A 2:118 ratio across 100+ entries on hard architectural work is implausible. The loop may be reaching for `[!REALIZATION]` defensively (to satisfy the marker check) and avoiding `[!REVERSAL]` because it implies prior error. The next Retrospect run should compare narrated course-changes against marked reversals — a discrepancy is a confabulation pattern, not an honesty one.

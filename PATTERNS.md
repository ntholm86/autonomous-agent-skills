# Implementation Patterns

Validated, optional, recommended implementation patterns that satisfy the [Manifesto principles](../../git/manifesto/PRINCIPLES.md) without claiming principle status themselves.

**Distinction from other documents:**
- **PRINCIPLES.md** (manifesto) — theory, mandatory, evidence-anchored.
- **PROBLEM.md** (manifesto) — gaps the framework targets.
- **PROOF.md** (manifesto) — empirical evidence backing principle-level claims.
- **DESIGN_BACKLOG.md** (this repo) — parked ideas, unscored, unvalidated, not adopted.
- **PATTERNS.md** (this repo) — implementation patterns with at least one validated instance, optional to adopt, no principle-level claim.

A pattern is promoted from DESIGN_BACKLOG when at least one validated instance exists. A pattern can be referenced by a skill but is never required by one — skills satisfy principles, not patterns.

**Promotion path:** principle-level claims about a pattern (i.e., the pattern reveals or refines a principle) belong in a manifesto refinement, not here. PATTERNS.md is implementation-layer.

---

## PT-001 — Sequential Cross-Family Convergence with Handoff

**Status:** Validated (2026-04-22). Recorded as the first formalized Pattern.

**Validated instances:**
- TPS skills suite SCORECARD Runs 96 (Gemini) and 97 (Grok) reproducing 8.83 baseline against Rubric v5.
- `c:\git\manifesto` Runs 4–6 (Grok / Gemini / GPT) silence-convergence chain at 36.5/40.0.

### The pattern

When P3 (Convergence Is Silence) requires diverse independent evaluator scrutiny but parallel multi-family orchestration is unavailable (current Copilot Chat limitation), run evaluations **sequentially** across distinct model families. Each peg is performed by a different family in a fresh session with cold re-derivation. State is carried between pegs by the kiroku Pending Handoff envelope in `TRAIL/SUMMARY.md`. The handoff itself — what the closing agent wrote, what the opening agent read — is the audit trail of the consolidation.

### Mechanics

- **Pool:** N ≥ 3 distinct model families (e.g., Claude / Gemini / Grok / GPT). N can grow as more families become available; the pattern is monotone in N.
- **Per-peg discipline:** cold derivation from source documents (PRINCIPLES.md, PROBLEM.md, PROOF.md), then comparison to existing rubric. Reading prior runs' session logs **before** independent derivation contaminates the peg.
- **Carrier:** `TRAIL/SUMMARY.md → ## Pending Handoff` envelope (kiroku v2.5.0+). Envelope is methodology-agnostic; payload (target family, reading order, do-not-read list, verbatim task statement) is methodology-specific.
- **Silence outcome:** convergence chain advances when N consecutive pegs reproduce the same dimensions and score with no additive or contradictory finding.
- **Divergence outcome:** legitimate signal that the rubric or scored artifact has changed materially; recorded as such, not reconciled away.
- **Contamination disclosure:** any prior conversation context (the agent having read the target in the same chat, the agent having authored prior-turn prescriptions on the same proposal) must be disclosed and the run excluded from the chain.

### Why this is a pattern, not a principle

The pattern *operationalizes* P3 — it does not extend it. The abstract claim ("diverse independent evaluators arriving at the same finding without coordinating is the strongest external evidence of validity") is P3 itself. PT-001 says *here is one mechanically achievable way to produce that evidence given today's tooling constraints.*

If parallel multi-family orchestration becomes available and produces strictly stronger signal, the natural successor pattern (currently DB-003, parallel form) may be promoted to PT-002, and at that point a P3 *refinement* may be justified.

### When NOT to use

- When fewer than N distinct families are available with comparable competence on the target.
- When the target is changing fast enough between pegs that re-derivation is measuring drift rather than convergence (re-anchor the chain instead).
- When the cost of N sequential evaluations exceeds the consequence of acting on a single-family finding.

### Skills that reference or implement this pattern

- **kiroku** (v2.5.0+) — provides the Pending Handoff envelope that carries state between pegs.
- **kata** — typically the methodology that opens and closes the per-peg sessions, but the pattern is methodology-agnostic and works equally well for per-skill-convergence runs (e.g., Intent skill peg chain).
- **shiken** — probe construction can be subjected to the same chain when independent probe authorship across families is desirable.

---

## Pattern lifecycle

1. **Idea** → DESIGN_BACKLOG.md (DB-NNN).
2. **First validated instance** → promoted to PATTERNS.md (PT-NNN).
3. **Repeated validated instances** → may inform a manifesto refinement or remain implementation-layer indefinitely.
4. **Superseded** → marked deprecated; reasons recorded.

A pattern that fails to validate further or is contradicted by later evidence is **demoted** back to DESIGN_BACKLOG with the contrary evidence noted.

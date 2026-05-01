# Compass — autonomous-agent-skills

_Last updated: 2026-05-01 (after runs 67–68; still operator-seeded, not yet a formal Retrospect run)_

_Compass is the Retrospect-derived current orientation: what the arc shows is currently true of the target, and what the next runs should test. It is rewritten each Retrospect run. Vision (`.trail/vision.md`) is the stable operator-held destination — read it first._

---

## Current claims about the reasoning layer

1. **The suite has shifted from convergence work to design work, and the README has not caught up.** The convergence baseline (three silences, three distinct model families) is pinned at v3.1.0 — five skills, no Retrospect, no compass, no vision, no Hunch. Runs 64–68 added all four of those structural pieces. The current v3.11.0 suite is **not** converged and has not been evaluated by independent model families since the additions. The README still implies convergence in a way that conflates "v3.1.0 was once converged" with "the current suite is converged." The next operator-facing change should make that distinction explicit; until then, every external read of this repo is slightly misleading.

2. **The loop is still closer to a text-consistency engine than a behavioral improvement engine — but the diagnosis has sharpened.** Runs 55–63 were doc propagation following operator-driven structural change. Runs 64–68 added behavioral mechanisms (Retrospect, compass, vision split, Hunch) — but every one of them was operator-prompted. The loop has not yet found a behavioral improvement on its own. Hunch (added run 68) is the first skill explicitly designed to reduce the operator's articulation cost; whether it shifts the discovery rate is an open empirical question.

3. **The orientation contract is now coherent for the first time.** Vision (operator-held, stable, never written by any skill), compass (Retrospect-derived, rewritten each run), trail (append-only evidence). Hunch sits outside the autonomous loop and surfaces guesses about where the operator is heading without writing to vision. A Retrospect run can now execute its spec literally without destroying operator content. This was incoherent through run 66.

4. **Retrospect, compass, and Hunch are all unproven in execution.** Retrospect has never been run end-to-end. This compass was seeded by the operator both times. Hunch has never been invoked even once — including in the natural opportunity at the end of run 68 when the operator's direction was an obvious thing to ask about. The protocol is increasingly precise on paper; the validation gap is widening.

5. **The work is research, not iterative refinement of a finished system.** The operator has named this explicitly: figuring out how to safely leverage AI in a way that is transparent, reviewable, and verifiable to the human at the wheel. That framing changes how convergence should be interpreted in this period — silence on a research artifact is not the same signal as silence on a production loop. The convergence protocol still applies, but only to settled designs; the present design is not yet settled.

## What the next runs should test

- **Invoke Hunch on this very conversation.** The first natural use was missed at the end of run 68. The next time direction feels even slightly unclear, the agent should run Hunch instead of guessing silently. The trail will then have at least one Hunch run to evaluate the skill against.
- **Run Retrospect for real.** Produce a falsifiable arc-claim from the trail that an Improve run would not have surfaced, and check whether it holds up. Until this happens, the meta-cognition layer of the protocol is asserted, not demonstrated.
- **Address the convergence-staleness in the README** — but use Hunch first to confirm with the operator how to frame it. The risk is propagating a doc edit that misnames the current state; the right framing (research artifact in active design vs. converged production protocol) is the operator's call.
- **Probe Intent's core claim** — that the agent is acting on what the operator means, not what they typed. With Hunch added, this probe can also test whether Hunch's hunches diverge from Intent's interpretation when they should.

## What this compass is not

This file was seeded from operator conversation, not from a Retrospect arc-read of the trail. The claims above are plausible and consistent with what the operator has said, but they have not been derived from reading the 69-entry trail as a single document. A Retrospect run will replace this file with claims that are. Treat the present file as a working hypothesis, to be falsified by the next real arc-read.

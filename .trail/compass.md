# Compass -- autonomous-agent-skills

_Last updated: 2026-05-02 (run: retrospect-second-real-pass-after-v3-16-0)_
_Derived from: full arc read, runs 55-71, plus follow-on improve passes across manifesto docs and resumed self-targeting entries. Vision read first (step 0)._

---

## Current claims

**1. Phase boundary crossed: documentation-convergence to validated-capability.**
Runs 55-63 were documentation propagation after structural changes. Runs 64-71 added four structural capabilities (Retrospect, compass/vision split, Hunch, .trail/ directory discipline) and validated three of them against real targets. The suite is no longer converging on a stable design -- it is proving a live design against external evidence. The convergence baseline at v3.1.0 does not apply to the current suite; a new convergence cycle has not yet started.

**2. Retrospect has a second real data point; the gap narrows from existence to reliability.**
Every prior compass entry named "Hunch unproven in execution" as the validation gap. As of 2026-05-02, Hunch has confirmed hunches on five runs across four targets (own vision, evo, vectorium, leifoglenedk, manifesto). The falsification condition was met. Retrospect now has two real executions: the first arc-read (session-v3-16-0-retrospect-first-run) and this second pass. The second pass is compatible with the first: it keeps the same unresolved structural bets (occasion-independence and external harness proof) while incorporating new evidence (manifesto consistency sweep completed). The remaining gap is no longer "does Retrospect produce arc claims at all" but "does it remain stable and decision-useful across more arcs and operators."

**3. Occasion-independence now has a first positive data point, but reliability is unproven.**
The trail previously named this as unresolved (runs 68, 71). In this run, an agent-initiated direction question produced one structural change (`improve/SKILL.md` v3.7.0 adds an underspecified-ask bootstrap in step 1). This closes the pure "zero evidence" state, but does not establish reliability across sessions. The open claim is now repeatability, not existence.

**4. The two-repo relationship (manifesto = principles layer, skills = one domain conformance) is now reflected in both READMEs.** ~~OPEN~~ **CLOSED 2026-05-02.**
Both READMEs now name the other repo and state the relationship explicitly. Skills README: "this suite is one conformance example of the Autonomous Agent Principles." Manifesto README: names skills suite as the reference implementation with "evidence, not proof" framing. Gap closed.

**Status note:** manifesto internal consistency sweep is complete (README, PROOF, PRINCIPLES, PROBLEM aligned; no known cross-file naming drift).

**5. The skills suite is specifiable and composable but has never been run by a harness that did not co-evolve with it.**
Vision names this as a hard requirement before integration with evo or any other harness. No evidence exists yet that the skills work cleanly when invoked by a system that did not participate in their design. This remains the most important unvalidated claim in the entire research bet.

---

## What the next runs should test

1. ~~**Retrospect self-validation:** second real pass completed (2026-05-02), compatible with first pass.~~
2. ~~**Commit pending mechanical debt:** done.~~
3. ~~**Manifesto PROOF.md rewrite:** done (2026-05-02). Restructured to lead with domain-agnostic conformance protocol per principle; kata evidence labeled as "reference evidence — one implementation, one domain.".~~
4. ~~**README relationship statement:** done (2026-05-02). Both READMEs updated.~~
5. **One external proof:** run the protocol on a target where the AI exceeds the operator on the underlying task and the operator is not the author.
6. ~~**Occasion-independence experiment:** first pass completed (2026-05-02). Agent-initiated direction question led to structural change in Improve v3.7.0.~~
7. **Occasion-independence reliability test:** repeat the same experiment on a different day/arc and check whether it again yields a structural finding without operator topic injection.
8. **Retrospect reliability test (next level):** run on a materially different future arc (not same-day cleanup arc) and compare claim stability plus decision usefulness.

---

## Loop-effectiveness notes

The loop is executing correctly as a structural-tightening and validation mechanism: every gap surfaced this session was found, fixed, and committed. With two Retrospect passes now compatible, the immediate uncertainty shifted from capability existence to capability reliability under varied arcs. Occasion-independence moved one step forward: there is now a first positive data point, but not yet a repeatable pattern.
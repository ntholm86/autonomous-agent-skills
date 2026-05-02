# Compass -- autonomous-agent-skills

_Last updated: 2026-05-02 (run: self-run-resume-after-v3-16-0)_
_Derived from: full arc read, runs 55-71, plus follow-on improve passes across manifesto docs. Vision read first (step 0)._

---

## Current claims

**1. Phase boundary crossed: documentation-convergence to validated-capability.**
Runs 55-63 were documentation propagation after structural changes. Runs 64-71 added four structural capabilities (Retrospect, compass/vision split, Hunch, .trail/ directory discipline) and validated three of them against real targets. The suite is no longer converging on a stable design -- it is proving a live design against external evidence. The convergence baseline at v3.1.0 does not apply to the current suite; a new convergence cycle has not yet started.

**2. The validation gap has shifted from Hunch to Retrospect.**
Every prior compass entry named "Hunch unproven in execution" as the validation gap. As of 2026-05-02, Hunch has confirmed hunches on five runs across four targets (own vision, evo, vectorium, leifoglenedk, manifesto). The falsification condition was met. The current unvalidated claim is: "a Retrospect run produces arc-level findings that an improve loop run in the same session would not." This run is the first real Retrospect execution; it is its own validation event.

**3. The loop still has no occasion-independence -- every structural change in runs 64-71 was operator-prompted.**
The trail names this repeatedly (runs 68, 71) but no run has resolved it. Hunch was designed to reduce operator-prompting dependency; it has reduced content dependency (agent surfaces direction rather than waiting for operator to articulate it) but not occasion dependency (operator still creates the moment). Whether Hunch will eventually surface direction questions without being invoked is an open empirical question.

**4. The two-repo relationship (manifesto = principles layer, skills = one domain conformance) is now reflected in both READMEs.** ~~OPEN~~ **CLOSED 2026-05-02.**
Both READMEs now name the other repo and state the relationship explicitly. Skills README: "this suite is one conformance example of the Autonomous Agent Principles." Manifesto README: names skills suite as the reference implementation with "evidence, not proof" framing. Gap closed.

**Status note:** manifesto internal consistency sweep is complete (README, PROOF, PRINCIPLES, PROBLEM aligned; no known cross-file naming drift).

**5. The skills suite is specifiable and composable but has never been run by a harness that did not co-evolve with it.**
Vision names this as a hard requirement before integration with evo or any other harness. No evidence exists yet that the skills work cleanly when invoked by a system that did not participate in their design. This remains the most important unvalidated claim in the entire research bet.

---

## What the next runs should test

1. **Retrospect self-validation:** run a second real Retrospect pass now that the arc includes post-v3.16.0 consistency work, and test whether it yields claims Improve would not surface in-session.
2. ~~**Commit pending mechanical debt:** done.~~
3. ~~**Manifesto PROOF.md rewrite:** done (2026-05-02). Restructured to lead with domain-agnostic conformance protocol per principle; kata evidence labeled as "reference evidence — one implementation, one domain.".~~
4. ~~**README relationship statement:** done (2026-05-02). Both READMEs updated.~~
5. **One external proof:** run the protocol on a target where the AI exceeds the operator on the underlying task and the operator is not the author.
6. **Occasion-independence experiment:** trigger one Hunch or Improve run without operator topic injection (agent-initiated direction question) and record whether it surfaces a structural finding independently.

---

## Loop-effectiveness notes

The loop is executing correctly as a structural-tightening and validation mechanism: every gap surfaced this session was found, fixed, and committed. The loop is not yet functioning as an independent finding mechanism -- direction has consistently been operator-supplied. This is honest for the current phase (design and validation, not convergence), but should be named. The operator-prompting dependency is structural, not accidental -- the trail names it in [!REALIZATION] markers in runs 68 and 71, and it has persisted across two sessions without resolution. This run resumes self-targeting after orientation artifacts (vision + compass) are in place; the next meaningful evidence is whether the loop can originate a structural question on its own.
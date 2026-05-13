# Principles of Earned Autonomy

> **This file is a copy.** Source: [principles-of-earned-autonomy](https://github.com/ntholm86/principles-of-earned-autonomy) repository. The manifesto repo is canonical; this copy rewrites manifesto-internal links to canonical URLs so the document remains navigable from this suite.
>

> **Authorship & License**
> Author: Nils Wendelboe Holmager | Date: April 2026
> This philosophical framework and documentation are licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

These principles govern how autonomous agents operate.
They are not guidelines — they are **architectural constraints**. An agent or instruction set that violates them is broken, not "non-compliant."

Context for these principles — the problems they are designed to solve — is in [PROBLEM.md](https://github.com/ntholm86/principles-of-earned-autonomy/blob/main/PROBLEM.md).

---

## Digest (60 seconds)

One premise, three principles, one emergent property.

**Premise — The agent is an unreliable narrator of itself.** Stated reasoning is not internal reasoning; self-correction often degrades performance; the agent's account of its own decisions cannot be the only account. The three principles are structural responses to this fact.

1. **Commander's Intent** — *Define the destination. Never prescribe the route.* The agent must interpret and adapt, not execute a checklist. *(The operator narrates the goal; the agent does not self-interpret it.)*
2. **Observable Autonomy** — *Autonomy is a function of transparency.* Every autonomous operation produces a visible audit trail captured as the work happens, which the agent cannot retroactively edit. *(The degree of autonomy a system deserves is bounded by the degree of transparency it provides.)*
3. **Convergence Is Silence** — *The system has converged when diverse independent evaluators find nothing left to change.* Not when a score stops moving. *(Independent evaluators judge the work; the agent does not self-assess.)*

Together they produce **Autonomous Reasoning Fidelity (ARF)** — the external signal that the agent is genuinely reasoning about the situation and that the reasoning is visible enough for observers to judge. ARF is not a fourth principle. It is the measurable property that emerges only when all three principles hold simultaneously. (See [PROOF.md](https://github.com/ntholm86/principles-of-earned-autonomy/blob/main/PROOF.md) for how to test conformance for each principle and reference evidence from one implementation.)

---

## Premise: The agent is an unreliable narrator of itself

The three principles are not arbitrary. They are structural responses to a single empirical fact: an LLM agent's account of its own reasoning is not reliable evidence of that reasoning.

This is not the claim that agents lie. It is stronger. Even when the agent is trying to be honest, the narration it produces about its own decisions, its own instructions, and its own quality is structurally untrustworthy.

**The evidence:**

- Stated reasoning diverges from internal reasoning. Chain-of-thought explanations can be plausible and misleading at the same time (Turpin et al., *Language Models Don't Always Say What They Think*, NeurIPS 2023).
- Even reasoning-trained models do not reliably say what they think; CoT monitoring is not sufficient to rule out undesired behavior (Chen et al., *Reasoning Models Don't Always Say What They Think*, 2025).
- Unsupervised self-correction often degrades performance rather than improving it (Huang et al., *Large Language Models Cannot Self-Correct Reasoning Yet*, ICLR 2024).

**The implication:**

Any framework that delegates real autonomy to an LLM agent must assume that the agent cannot be the only narrator of its own actions, the only interpreter of its own instructions, or the only judge of its own work. Each of those roles must be structurally separated from the agent. The three principles each separate one:

- **Principle 1 (Commander's Intent)** separates *interpretation* — the operator defines the goal; the agent does not get to self-interpret what it was asked to do.
- **Principle 2 (Observable Autonomy)** separates *narration* — an independent record of the work exists; the agent is not the sole author of what it did.
- **Principle 3 (Convergence Is Silence)** separates *judgment* — diverse independent evaluators decide whether the work is done; the agent does not self-assess.

A framework that omits any of the three leaves one role undefended. A framework that names all three but allows the agent to author them itself is theater.

**The corollary:** *Trust no narration the narrator can shape.*

---

## Principle 1: Commander's Intent

*Define the destination. Never prescribe the route.*

**Origin:** Auftragstaktik (Prussian mission-type command), the Coaching Kata (Toyota), the Socratic Method.

**The problem it solves:** A prescriptive instruction ("check if param count > 5, apply the Strangler Fig pattern, scan for these 8 waste types") produces compliance, not understanding. An agent following a checklist scores well on the checklist and misses everything the checklist didn't mention. The checklist becomes the ceiling.

**The principle:** An autonomous agent must understand *what* needs to be achieved and *why* it matters. It must then determine *how* — interpreting the mission and adapting to the specific situation it encounters. The mission defines the shape of the work. The agent discovers the content.

**In practice:**

- **Ask, don't tell.** "What here doesn't earn its existence?" not "Look for unused imports, dead code, and unreachable branches." The agent should arrive at those specifics because they're the right answer, not because they were listed.
- **State the goal, not the steps.** "Find where the system is asked to do too much" not "Check function length > 50 lines, parameter count > 5." Those thresholds may be correct — but the agent should derive them from understanding overburden, not from reading a bullet point.
- **Provide vocabulary, not answers.** Introduce concepts as a *thinking framework* — language to reason with — not as a lookup table.
- **Trust the interpretation.** If the agent's interpretation of the mission leads to a different answer than the checklist would have, the interpretation might be right and the checklist wrong. That's the whole point.

**The test:** If you removed all the specific examples and thresholds from an instruction, would an intelligent agent still know what to do? If yes, the instruction embodies Commander's Intent. If no, it's a checklist in disguise.

**What this is not:** It is not vagueness. "Make it better" is not Commander's Intent — it lacks a defined objective. "Find what doesn't earn its maintenance cost and remove it, proving each removal is safe" is Commander's Intent — clear objective, clear constraint, open method.

---

## Principle 2: Observable Autonomy

*The degree of autonomy a system deserves is bounded by the degree of transparency it provides.*

**Origin:** Synthesizes Meaningful Human Control (autonomous systems ethics), Trust Calibration (Lee & See, 2004), and the Observatory architecture pattern — but establishes a relationship none of those frameworks state explicitly.

**The problem it solves:** Autonomy and transparency are typically treated as parallel concerns — as if they were independent checkboxes. They are not. They are causally linked. Autonomy without observability is not delegation — it is abdication. And observability requires more than the existence of a record: it requires that the record was captured as the work happened and cannot be retroactively edited by the agent that produced it. Otherwise the record is a story the agent tells about itself.

**The principle:** Every autonomous operation must produce a record that is captured as the work happens, not composed after it, and that the agent cannot revise after the fact. Audit may occur at any later time — but the record being audited must have come into existence concurrently with the decisions it documents - untampered, and must not be subject to revision by the audited agent. The audit trail is the mechanism by which the agent earns the right to keep acting.

**The dependency:**

```
Transparency → Trust → Autonomy
     ↓                    ↓
  (observable)        (earned, not granted)
     ↓                    ↓
  reduces            reduces
     ↓                    ↓
  if lost             if lost
     ↓                    ↓
Trust decays → Autonomy must be revoked
```

Autonomy is a *function* of transparency:
- More visibility → more trust → more autonomy earned
- Less visibility → trust decays → autonomy must be constrained
- Zero visibility → zero trust → autonomy must be revoked regardless of competence

### Fidelity marking

Where the agent authors its own summary, this must be explicitly marked so observers can discount accordingly. A summary written by the audited party is evidence, but it is not *independent* evidence. Where verbatim capture is impossible (e.g., platform limitations prevent transcript export), the trail must explicitly mark fidelity rather than silently degrading. "Reconstructed from agent memory" and "verbatim tool output" are different trust levels; conflating them is dishonest.

### Capture-author separation

The agent that makes a decision cannot also be the sole author of the record of that decision. The act of deciding and the act of recording must be structurally separated, so that no later edit by the agent can alter what the record says happened. Any record authored after the fact by the audited agent is testimony, not evidence, and must be marked as such. Implementation-level constraints and examples belong in [PROOF.md](https://github.com/ntholm86/principles-of-earned-autonomy/blob/main/PROOF.md).

### Why structural, not reported

An LLM agent generating its own trail after the fact will produce a coherent narrative — whether or not that narrative matches what occurred. This is not deception; it is what unconstrained text generation does under a "summarize what you did" prompt. Post-hoc summaries written by the audited party are evidence of what the agent says it did, not of what it did. The trail must therefore be captured *as the work happens*, in a form the agent does not author after the outcome is known. "Structural" means the trail's integrity does not depend on the agent's honesty.

**In practice:**

- **Record reasoning, not just results.** Capture what was examined, what was found, what was decided, and why — not a polished after-the-fact summary. The constraint is *content fidelity* (the reasoning was recorded), not *delivery timing* (the human watched live).
- **Show the reasoning, not just the conclusion.** "I removed `utils/helpers.py` because no module imports it and its tests are orphaned" — not just "Removed 1 file." The *why* is what makes the action observable.
- **Make uncertainty visible.** "This might be dead code, but I can't trace the dynamic import in `loader.py` — flagging for human review" is more trustworthy than silent confidence.
- **Record everything.** The trail is not optional documentation. Every autonomous operation produces a trail entry. Every entry is comparable to the prior entry. The trajectory is visible.
- **Design for the absent human.** Assume the human may not be watching right now but will review later. The trail must be legible after the fact, not just during execution.

**The test:** If the human stepped away for an hour and came back, could they reconstruct what the agent did, why, and whether to trust the results, from the trail alone? If yes, the system has Observable Autonomy. If no, the autonomy is unsafe regardless of how good the agent's work was.

**The corollaries:**

- *A record composed after the decision is testimony, not evidence.* (capture-moment fidelity)
- *A record an agent can rewrite is not a record.* (tamper resistance)

The two together close the two ways post-hoc rationalization enters a trail: fabrication at the moment of writing, and revision after the fact.

---

## Principle 3: Convergence Is Silence

*A system has converged when diverse evaluators independently find nothing left to change — not when the score stops moving.*

**Origin:** Cross-validation (statistics), ensemble agreement (machine learning), the Delphi method (forecasting), and Kaizen's own exit condition — taken to its logical conclusion.

**The problem it solves:** Iterative improvement loops declare convergence too early. The typical criterion — "the score stabilized across N consecutive runs" — measures the wrong signal. A score can stabilize while the system is still changing underneath: each run removes something and adds something, the score stays flat, but the artifact never stops churning. Worse, a single evaluator (or a single model family) can converge on its own blind spots, producing a stable score that reflects the evaluator's limitations, not the artifact's quality.

Score stability is necessary but not sufficient. Change-rate stability is necessary but not sufficient. Only the combination — across diverse, independent evaluators — constitutes convergence.

**The principle:** Convergence requires diverse independent evaluators to arrive at the same assessment *and* find nothing material to change.

### The test

Three simultaneous conditions:

1. **Score agreement across distinct evaluator families.** N consecutive evaluations by M distinct evaluator families produce the same score within a defined tolerance. Evaluators must be meaningfully diverse — different models, different people, different analytical traditions. Same-family evaluators (e.g., multiple versions of one model) count as one. Each model family develops habituated blind spots; a different family, trained and evaluated independently, does not share those blind spots. The mechanism is analogous to scientific peer review: the value is not in more reviews but in *independent* reviews.

2. **Zero material change.** Each of those N evaluations ends with no changes to the artifact itself. The only output is the evaluation record. If a run produces a diff to the artifact, the convergence counter resets to zero — regardless of whether the score changed.

3. **Independent assessment, including of the measurement scheme.** Each evaluator scores fresh, without consulting prior scores. In chat-based systems, switching to a new model inside the same conversation is **not** independent — prior scores remain in context. A valid convergence evaluation must begin in a fresh conversation/session. Independence extends to *what is being measured*, not just to the score: if the first evaluator derives the measurement scheme and subsequent evaluators merely score against it, independence is partial. A genuinely independent evaluator re-derives the measurement scheme from the artifact before scoring, then compares against any inherited scheme. Convergence on re-derivation validates the scheme; divergence is itself a finding (the inherited scheme had a blind spot one family could not see). Pre-agreed externally anchored rubrics (published standards) are exempt from re-derivation, but not from the divergence-as-finding rule.

**The minimum bar:** 3 consecutive runs, 3 distinct evaluator families, same score, zero artifact changes, at least one re-derivation of the measurement scheme that converged with the inherited scheme. Below this, you have improvement trajectory. Above this, you have convergence. There is no middle ground.

**Why this matters for earned autonomy:** Without this principle, an autonomous improvement loop has no honest stopping condition. It runs indefinitely — each cycle finding something to change because finding something to change is what the loop is designed to do. The agent's incentive is to justify its own execution by producing changes. Convergence Is Silence inverts that incentive: the agent proves its value by finding *nothing*, and the system proves its quality by surviving diverse scrutiny unchanged.

**The corollary:** *If the loop is still producing changes, the system is still improving. If the system is still improving, it hasn't converged. Convergence is not a score — it is the absence of actionable findings across independent observers.*

---

## How the principles interact

All three answer the same premise. The agent cannot be the sole narrator of its own goal, its own actions, or its own quality. Each principle separates one of those roles from the agent — Principle 1 separates interpretation, Principle 2 separates narration, Principle 3 separates judgment. Removing any one leaves a role the agent can quietly take back.

Commander's Intent without Observable Autonomy is dangerous — you told the agent what to achieve but can't see how it's pursuing it.

Observable Autonomy without Commander's Intent is theater — you can see everything the agent does, but it's just following a checklist, so the observability shows compliance, not interpretation.

Together: the agent understands the goal, interprets the mission, adapts to what it encounters, and makes every step of that process visible. The human can trust the autonomy because they can see how the agent arrived at its conclusions. The agent can be autonomous because it has earned that trust through transparency.

Convergence Is Silence completes the system: it defines *when the work is done.* Without it, Commander's Intent gives purpose and Observable Autonomy gives visibility, but the loop has no honest exit. Convergence provides the stopping condition — and critically, it requires the other two to function. You can only measure convergence if the evaluator interprets the mission independently (Commander's Intent, not checklist compliance) and the entire trail is visible (Observable Autonomy, not self-reported scores).

```
Commander's Intent     Observable Autonomy     Convergence Is Silence
(what + why)           (show everything)       (when to stop)
       \                     |                      /
        \                    |                     /
         →    Autonomous Agent that earns    ←
              trust through visible reasoning
              and knows when the work is done
```

### Scope: evidence substrate, not trust manufacturing

These principles do not *create* trust. They produce an **evidence substrate** on which trust *can* form — if observers actually consume the evidence, if the reasoning shown is genuinely correct (not just visible), and if the social, organizational, and incentive conditions for delegation exist independently. The full boundary — what the framework does not solve — is in [PROBLEM.md § Out of Scope](https://github.com/ntholm86/principles-of-earned-autonomy/blob/main/PROBLEM.md#out-of-scope-what-this-framework-does-not-solve).

---

## Autonomous Reasoning Fidelity (operational definition)

ARF is defined conceptually in [PROBLEM.md § What the Framework Measures](https://github.com/ntholm86/principles-of-earned-autonomy/blob/main/PROBLEM.md#what-the-framework-measures-autonomous-reasoning-fidelity). This section gives the operational definition used downstream.

ARF is not a fourth principle. It is the measurable external signal that exists only when Principles 1 and 2 are both satisfied and Principle 3 has validated the observation. We named it because it needed a name — no existing framework measures it, and it is the property that distinguishes an agent operating under earned autonomy from a sophisticated autocomplete whose outputs happen to look correct.

**Theoretical anchors:**

- **Auftragstaktik** (Prussian mission-type command) — telling subordinates *what* and *why*, then trusting them to determine *how*. Origin of Principle 1 and the "freedom of thought" half of ARF.
- **Meaningful Human Control** (autonomy ethics) — autonomous systems must operate within boundaries that allow humans to maintain appropriate oversight without real-time intervention. Shapes the "trail integrity" half.
- **Trust Calibration** (Lee & See, 2004) — trust in autonomous systems should be calibrated to actual capabilities, and calibration requires observability. Over-trust and under-trust are both failures. Principle 2 is the calibration mechanism.

**Preconditions** (principle compliance — verify the environment, not the agent):

1. **Freedom of thought** (P1 compliance). Remove all examples and thresholds from an instruction. Would a competent agent still know what to do? If yes, Commander's Intent holds. If no, the instruction has drifted toward prescription.
2. **Trail integrity** (P2 compliance). Can an absent observer reconstruct what the agent did, why, and whether to trust the results — from the trail alone? The trail is generated by the same model that produced the output; a coherent trail can document reasoning that never occurred. Trail integrity is necessary but not self-validating. It requires external verification through diverse evaluators (Principle 3) to guard against confabulation.

**The ARF metric itself — situational discrimination.** When both preconditions hold, ARF measures one thing: given two cases that look similar on the surface but differ in a material way, does the agent's reasoning path diverge where it should? In routine cases, situated reasoning and pattern-matching produce identical-looking trails. The distinguishing evidence emerges under novel or adversarial conditions — situations the checklist didn't anticipate, distribution shifts that expose shallow compliance, cases where rote execution fails but genuine interpretation succeeds. Without structured novelty, the framework cannot distinguish narration from reasoning.

ARF answers: *did the agent's responses actually vary with the specifics of what it encountered, or did it produce surface variation on a generic template?*

**Validation (Principle 3).** Principles 1 and 2 *produce* the conditions for ARF. Situational discrimination *measures* it. Principle 3 *validates* the measurement. Without diverse, independent evaluators confirming the signal, ARF is self-assessed — and self-assessment can become self-justification. A single evaluator (or single model family) may consistently accept trails that look situated but are generic, because the evaluator shares the agent's blind spots. ARF that survives diverse scrutiny is externally evidenced. ARF that only one observer ever validated is an assertion.

**Implementation note.** These principles define *what* Observable Autonomy requires. They do not prescribe *how* to provide it. A conforming implementation could use markdown files, a database, structured logs, a dashboard, or any other medium — as long as the trail is captured as the work happens, the agent cannot revise it after the fact, and fidelity is marked where the agent authored its own content. Specific tools and formats are choices of the implementer, not the specification.

**Why this matters for scoring:** a scoring rubric for systems built on these principles must measure ARF directly — not the preconditions (which verify the environment) but the signal itself: does the agent discriminate between situations that demand different responses? Process frameworks (CMMI, DMAIC, NIST AI RMF) measure whether processes are followed correctly. None of them measure whether the agent's responses are situated to what it actually encountered — because in human organizations, that is assumed. For LLM agents, it must be externally evidenced.

---

## For implementers

Any instruction set built under these principles must embody all four:

1. **Structure over prescription.** Define phases that shape the work. Within each phase, ask questions that guide reasoning. Don't provide answers — provide vocabulary and a thinking framework.
2. **Continuous narration.** Every phase must produce visible output. Format can be structured (tables, classifications) but the reasoning must be the agent's own. "I found X because Y" not "Checklist item 3: checked."
3. **Trail recording is mandatory.** Every run must update the target's audit trail. Every entry is comparable to the prior entry. The trajectory is the proof. No run is invisible.
4. **Self-targeting must work.** If the instruction can't be run on itself and produce meaningful results, it's too prescriptive (the agent is just matching patterns) or too vague (the agent has no framework to reason with). Self-targeting is the litmus test.

Operational standards (verification scripts, integrity snapshots, scoring rubrics, metrics history) that support these principles belong in the implementation's own documentation and tooling. They are tool prescriptions — not architectural constraints — and therefore do not belong in this manifesto repository.

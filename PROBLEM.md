# The Problem

*What this work is trying to solve.*

> **Authorship & License**
> Author: Nils Holmager | Date: April 2026
> This philosophical framework and documentation are licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/). The accompanying execution tools and scripts are licensed under the MIT License.

---

## Digest (60 seconds)

**Two problems, one framework:**

1. **Autonomous reasoning** — How do we structure the relationship between human and AI so the AI must *interpret* the mission and *adapt* to the situation rather than execute prescribed steps?
2. **Earned autonomy** — How do we make that reasoning visible enough that different observers can justify granting or withholding authority, on evidence?

Neither can be solved alone. Observable compliance is not evidence of thought. Hidden reasoning is not a basis for trust. The framework is an **evidence substrate**: it produces the conditions on which trust *can* form, for five observer classes (practitioner, deployer, regulator, liability bearer, the agent itself). It does not manufacture trust, guarantee correctness, or solve the social conditions for delegation.

The property the framework measures is **Autonomous Reasoning Fidelity (ARF)** — the external signal that genuine, situated reasoning is both occurring and visible. ARF is validated by independent, diverse scrutiny, not self-assessment.

The operational discipline that connects the two problems is **delegability**: bounded, revocable authority granted on visible, situated reasoning — and withdrawable on the same evidence.

---

## Index

- [The Two Problems](#the-two-problems)
- [Delegability: the connecting discipline](#delegability-the-connecting-discipline)
- [Who the Evidence Must Serve](#who-the-evidence-must-serve)
- [What the Framework Measures: Autonomous Reasoning Fidelity](#what-the-framework-measures-autonomous-reasoning-fidelity)
- [What Existing Work Does and Does Not Solve](#what-existing-work-does-and-does-not-solve)
- [What Must Be Built on Top](#what-must-be-built-on-top)
- [Out of Scope: What This Framework Does Not Solve](#out-of-scope-what-this-framework-does-not-solve)
- [The Working Hypothesis](#the-working-hypothesis)

---

## The Two Problems

### Problem 1: Autonomous Reasoning

Most AI systems follow instructions — some brilliantly. But following instructions is not reasoning. An agent given a checklist executes the checklist. Its ceiling is the checklist. It finds what the checklist described and misses what the checklist didn't mention. It cannot adapt to a situation the instruction author never anticipated.

The alternative is an agent that receives a mission — *what* must be achieved and *why* — and determines *how* based on what it actually encounters. The human defines the objective; the agent determines the method. This is the difference between compliance and reasoning.

This matters because consequential domains are not checklists. A nurse's patient is not a textbook case. An engineer's system has quirks the documentation doesn't cover. The situations that matter most are the ones that depart from the expected pattern — and an agent that can only follow prescribed steps will fail precisely when it is needed most.

> **Problem 1:** How do you structure the relationship between human and AI so that useful performance depends on the AI interpreting objectives, adapting to context, and discovering what matters — rather than merely executing prescribed steps?

### Problem 2: Earned Autonomy

Even if an AI system is reasoning well, nobody can see it.

Outputs may be correct. Decisions may be sound. But from the outside, genuine reasoning and sophisticated pattern-matching produce identical-looking results. A human who grants authority to a system whose reasoning is invisible has not delegated — they have abdicated.

This is not only technical. It is institutional and psychological. People do not delegate meaningful authority to systems they cannot inspect, challenge, explain, or revoke. Organizations cannot insure what they cannot audit. Regulators cannot certify what they cannot examine. Practitioners cannot stake their judgment on what they cannot interrogate.

> **Problem 2:** On what basis should a human, team, or institution decide that this agent has earned autonomy in this context, for this scope, right now — and what evidence justifies that judgment?

### Why They Must Be Solved Together

Observable autonomy without genuine reasoning gives a window into compliance. You can see every step — but the steps were prescribed, so the observation confirms obedience, not thought. Trust calibrated to compliance is fragile: it breaks the first time the situation departs from the script.

Genuine reasoning without observable autonomy gives an unverifiable claim. The agent may be reasoning brilliantly or hallucinating confidently — and nobody can tell. The capability is real but invisible, so it cannot serve as the basis for granting authority.

Both together produce something qualitatively different: an agent that reasons freely about what to do AND makes that reasoning visible enough for observers to judge whether it justifies the authority being granted. The reasoning is the substance. The visibility is the evidence. Neither is sufficient without the other.

**Scope clarification.** In fully prescribable domains — commercial aviation, assembly-line automation — earned autonomy through static certification works: every mission decomposes into finite procedures, and trust is earned through exhaustive testing. This framework targets domains with **irreducible novelty**: medicine, law, engineering, analysis — domains where the situations that matter most cannot be fully anticipated by any checklist.

---

## Delegability: the connecting discipline

The discipline that connects both problems is **delegability**: the operational practice of converting demonstrated, visible, situated reasoning into *bounded, revocable* authority.

Delegability is not capability (the model can do the task). It is not safety (the model won't cause harm). It is the discipline that connects what the agent *appears to be doing* to what an observer *can justifiably let it keep doing* — and can withdraw on the same evidence.

**The operational test of delegability** (asked by each observer class, answered from the trail):

1. Is the reasoning visible enough, *at my resolution*, for me to judge it?
2. Is the reasoning *situated* to this case — would it have come out differently for a different case?
3. Is the *scope* of authority I'm granting bounded to what the evidence actually supports?
4. Can I *revoke* the authority on the same evidence, if the trail shows the reasoning stop being situated?

A system is delegable *here, now, at this scope* when all four answer yes. Any single "no" is a reason to narrow scope or withhold delegation — not a failure of the framework, but the framework functioning correctly.

---

## Who the Evidence Must Serve

Observable Autonomy (Principle 2) states that every autonomous operation must produce a visible, continuous trail. But "visible" is not a single thing. Different observers need different evidence from the same trail — and a framework for earned autonomy must account for all of them while still preserving the reasoning-fidelity question that the trail is meant to surface.

- **The practitioner** — nurse, engineer, analyst — needs case-level reasoning. *Why did the agent choose this action for this case? Did it actually reason about my specific situation, or did it pattern-match from training data?* Evidence must be specific, situated, and challengeable in the moment. Question: *Do I trust this decision — and did this agent actually think about it?*

- **The deployer** — the organization that fields the system — needs aggregate reliability. *Across a thousand cases, how often did the reasoning hold up? Where did it fail? Do failures cluster where the agent fell back to pattern-matching?* Question: *Should I keep granting this system this scope of authority?*

- **The regulator** — the body that sets standards for the domain — needs population-level validation. *Does this class of system meet the threshold for this domain? Does its success reflect genuine adaptation or brittle heuristics that only look good in aggregate?* Evidence must be standardized, reproducible, resistant to cherry-picking. Question: *Can this type of system be permitted to operate here, and on what basis do we believe its reasoning generalizes safely enough?*

- **The liability bearer** — insurer, legal entity, institution absorbing failure cost — needs tail-risk distribution. *What is the worst-case exposure? Do catastrophic failures cluster where the system stopped adapting?* Evidence must quantify downside, not just average performance. Question: *What is my exposure if this system fails in the worst way it can fail, and what does the trail say about why?*

- **The agent itself** — an autonomous system operating under these principles has access to its own trail. It can detect when its outputs become repetitive rather than situated, when it is operating outside the scope where its autonomy was earned. Self-assessment can become self-justification, so the agent's trail must remain legible to all other observers. *The agent is an observer, never the final one.*

These observers ask different questions. They require different aggregations, time horizons, units of analysis. They all depend on the same underlying property: a trail that is continuous, legible, and structurally guaranteed by the system's architecture, not bolted on.

A framework that satisfies the practitioner but not the regulator will be adopted and then revoked. A framework that satisfies the regulator but not the practitioner will be mandated and then circumvented. A framework that satisfies neither the deployer nor the liability bearer will never reach production regardless of how good the AI's outputs are. **Earned autonomy that only one observer can verify is not yet earned.**

---

## What the Framework Measures: Autonomous Reasoning Fidelity

The target property is **Autonomous Reasoning Fidelity** (ARF). ARF is the external signal that exists only when both problems are being addressed together.

ARF is not proof of consciousness and not certainty about internal cognition. It is the strongest practical *external* signal this framework can produce: evidence that an agent is reasoning about what to do rather than merely complying (Problem 1) *and* that this reasoning is visible enough for observers to judge whether it justifies the autonomy being granted (Problem 2).

ARF emerges only when both principles are satisfied simultaneously:

- **Commander's Intent** creates the conditions under which interpretation and adaptation are required for good performance — the agent must engage with the mission, not execute steps.
- **Observable Autonomy** makes the engagement visible — the trail shows *how* the agent arrived at its conclusions, not just what the conclusions were.

Neither half alone produces delegability. Unconstrained reasoning in a black box leaves the autonomy side unaddressed: no evidence an observer can act on. Visible compliance leaves the reasoning side unaddressed: evidence of obedience, not thought.

**A critical dependency.** In routine cases, situated reasoning and sophisticated pattern-matching produce identical-looking trails. The distinguishing signal emerges under *novel* conditions — when the situation departs from expected patterns and the agent must either genuinely adapt or reveal itself as generic. The framework therefore requires **structured novelty** as a necessary complement to the trail. Without it, the trail documents narration, not reasoning.

**Validation.** ARF is validated by **Convergence Is Silence** (Principle 3) — diverse, independent evaluators finding the same signal without consulting each other. ARF that survives diverse scrutiny is externally evidenced. ARF that only one observer ever validated is an assertion.

*(The operational definition of ARF — preconditions, situational discrimination, validation test — is in [PRINCIPLES.md](./PRINCIPLES.md#autonomous-reasoning-fidelity-operational-definition).)*

---

## What Existing Work Does and Does Not Solve

Current AI work addresses adjacent parts of both problems:

- **Capability evaluation** (MMLU, HumanEval, domain-specific benchmarks) asks whether a model can produce useful or correct outputs. It measures what the model *can do* — not whether it *reasoned* its way there or whether a human should *let it do it* unsupervised.
- **Safety and governance frameworks** (NIST AI RMF, the EU AI Act, ISO/IEC 42001) ask what harms must be controlled and what oversight is required. They define guardrails — not the basis on which an operator decides the system has earned enough trust to operate within them.
- **Alignment and interpretability research** (RLHF, constitutional AI, mechanistic interpretability, representation engineering) makes models safer and more transparent from the inside. It does not yet give external observers a deployable way to judge whether a specific agent is genuinely reasoning in a specific context. XAI research has confirmed that explainability alone does not produce trust — studies show explanations increase understanding but not confidence in delegation, because users want evidence that the system *adapted to their case*, not just a window into a fixed process. This validates the gap: the missing construct is not more explanation but delegability grounded in visible, situated reasoning.
- **Prompt engineering and agent frameworks** (ReAct, chain-of-thought, tool-use architectures) improve how agents execute tasks. They do not distinguish between an agent that follows a sophisticated prompt template and one that genuinely interprets a mission. The structure looks like reasoning. Whether it *is* reasoning remains invisible.

None of these fields — individually or together — yet answer the two operational questions this work cares about:

> **Is this agent genuinely reasoning about what to do, or merely complying?**
>
> **Has this agent earned the right to act more autonomously here, and what evidence justifies that judgment?**

That is the gap this work targets. Not capability, not safety, not alignment — but delegability as defined above.

This is not a claim that existing fields are wrong or useless. It is a claim that they do not yet add up to a deployable discipline for earned autonomy grounded in externally evidenced reasoning.

---

## What Must Be Built on Top

The principles are a foundation, not a complete solution. The layers that must be built on top include:

- **Novelty and anti-compliance evaluation.** The most critical layer. Routine situations cannot distinguish situated reasoning from pattern-matching; the trails look identical. The framework needs structured novelty: cases where rote instruction-following fails but situated interpretation succeeds, adversarially underspecified situations, and distribution shifts that expose shallow compliance. Without this, the framework's central claim — that it can measure ARF — is asserted rather than tested.
- **Domain-specific correctness standards.** The principles are domain-portable; the quality criteria are not. Medicine, law, and engineering each need their own definition of "correct" within the framework.
- **Legal liability and governance models.** The trail makes accountability *possible*; policy must define who bears it when earned autonomy produces a bad outcome.
- **Evaluator independence and diversity.** Convergence Is Silence requires diverse scrutiny. How evaluator pools are composed, rotated, and kept independent is an operational problem the principles define but do not solve.
- **Failure testing and revocation thresholds.** Under what conditions should earned autonomy be revoked? The trail provides the evidence; thresholds must be defined per domain.
- **Scope control as autonomy expands.** Autonomy earned in one scope does not automatically transfer to a broader one. The escalation path needs design.
- **Tail-risk quantification.** The liability bearer needs more than average performance. Worst-case exposure, failure propagation paths, and downside distributions must be extractable from the trail.
- **Long-horizon alignment.** The principles verify reasoning fidelity in the near term. Whether an agent's goals remain aligned over extended periods is a separate research problem.

These are the research and engineering agenda that sits on top of the foundation. The right claim is not "these principles solve autonomous AI." The right claim is that they establish necessary preconditions — and that without them, none of the layers above can function.

---

## Out of Scope: What This Framework Does Not Solve

This framework is an **evidence substrate**, not a trust generator. It produces the conditions under which trust *can* form on observable grounds. It does not manufacture trust, guarantee adoption, or solve the social, organizational, and human-factors problems that surround autonomous AI. Naming these limits prevents the framework from being judged against claims it never made.

1. **Reviewer engagement and scaling.** Earned autonomy is meaningful only if someone evaluates the evidence. If no one reads the trail, autonomy becomes de facto unconditional regardless of how much evidence exists. If everyone reads it, the reviewer becomes the bottleneck. The framework provides multi-resolution evidence to lower review cost, and an in-trail reviewer-engagement signal so non-engagement is at least visible — but it has no answer for *how* organizations actually staff, incentivize, and sustain meaningful human review at scale. **This is the framework's deepest unresolved gap.** It is named here so it cannot be hidden by the existence of the trail.
2. **Reasoning correctness.** Transparency proves *visibility*, not *correctness*. A trail can be honest, legible, and wrong. Convergence Is Silence is the framework's primary defense against this, but it depends on diverse evaluators being available, willing, and competent. Where they are not, transparency does not save you.
3. **Human intent stability.** Commander's Intent assumes the human can articulate a destination clearly enough for the agent to interpret it. Real missions are often vague, contradictory, politically constrained, or shifting. If upstream intent is unstable, every downstream decision inherits that instability.
4. **Organizational willingness to delegate.** Many organizations do not want AI to have autonomy at all — earned or not. Fear of loss of control, job displacement, liability, political consequences, and being blamed for AI mistakes are legitimate concerns the framework cannot address. The framework's claim is conditional: *if* you want to delegate, here is how to make the delegation observable. It does not argue that you should.
5. **Incentives, values, and the social layer of trust.** Reliability is one component of trust. Trust also requires shared values, aligned incentives, and demonstrated character over time — none of which the framework supplies. The framework is a **governance and evidence layer**, not a trust model.
6. **Domain measurability.** In some domains the next improvement is unclear, unmeasurable, or politically contested. The framework gives the agent discipline for navigating uncertainty, but it cannot manufacture a measurable target where none exists.
7. **Legal liability and accountability assignment.** The trail makes accountability *possible*; policy and law must define who bears it.
8. **Adoption and organizational psychology.** Whether stakeholders will accept the concept of "earned autonomy" at all is a sociological question the framework treats as a precondition. If the answer is no for a given organization or domain, the framework is inert there regardless of how well it functions.

These are not disclaimers added defensively. They are scope boundaries. A framework that claims to solve them would be overclaim. A framework that pretends they don't exist would be dishonest. Naming them here is itself an instance of Observable Autonomy applied to the framework's own design.

---

## The Working Hypothesis

Humanity can adopt more AI power if two conditions are met: AI systems reason about what to do rather than merely follow instructions, and that reasoning is made visible enough for autonomy to be **earned, legible, and challengeable** rather than opaque, vendor-asserted, or intuition-driven.

If that hypothesis is right, this work is not an academic exercise. It is the early articulation of an **adoption architecture for autonomous AI**: the missing layer between model capability and real-world delegation.

What may generalize across domains is not every surface instruction, threshold, or vocabulary term. What may generalize is the deeper pattern: give the agent a mission rather than a script, require a visible trail of how it reasoned, challenge the claim from diverse perspectives, and expand authority only when the evidence — of both genuine reasoning and earned trust — supports it.

The name may evolve. The function will not:

> **Give humans a practical, evidence-based way to grant AI systems more authority — by solving both the reasoning problem (is the AI genuinely interpreting and adapting to this situation?) and the trust problem (can observers justify the autonomy being granted?) — so that the enormous potential of autonomous AI becomes adoptable, not just impressive.**

# The Problem

*What this work is actually trying to solve.*

> **Authorship & License**
> Author: Nils Holmager | Date: April 2026
> This philosophical framework and documentation are licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/). You are free to share and adapt this material, provided you give appropriate credit and distribute your contributions under the same license.
> The accompanying execution tools and scripts are licensed under the MIT License.

---

## The Two Problems

This work addresses two problems that are distinct but inseparable. Both must be solved for autonomous AI to move from impressive demos to real-world adoption in consequential domains.

### Problem 1: Autonomous Reasoning

Most AI systems follow instructions. Some follow them brilliantly. But following instructions is not reasoning.

An agent given a checklist — "check parameter count, scan for unused imports, verify test coverage" — will execute that checklist. It may execute it flawlessly. But its ceiling is the checklist. It will find what the checklist describes and miss what the checklist didn't mention. It cannot adapt to a situation the instruction author never anticipated. It cannot discover that the real problem is something the checklist never asked about.

The alternative is an agent that receives a mission — *what* needs to be achieved and *why* it matters — and determines *how* to accomplish that mission based on what it actually encounters. The human defines the objective and constraints. The agent determines the method. This is the difference between compliance and reasoning, between executing a script and understanding a purpose.

This matters because the real world is not a checklist. A nurse's patient is not a textbook case. An engineer's system has quirks the documentation doesn't cover. A legal analyst's case has facts that don't fit neatly into precedent. In every consequential domain, the situations that matter most are the ones that depart from the expected pattern — and an agent that can only follow prescribed steps will fail precisely when it is needed most.

The autonomous reasoning problem is: **How do you structure the relationship between human and AI so that useful performance depends on the AI interpreting objectives, adapting to context, and discovering what matters — rather than merely executing prescribed steps?**

### Problem 2: Earned Autonomy

Even if an AI system is reasoning brilliantly, nobody can see it.

The outputs may be correct. The decisions may be sound. But from the outside, genuine reasoning and sophisticated pattern-matching produce identical-looking results. A human who grants authority to a system whose reasoning process is invisible has not delegated — they have abdicated. They are trusting, not verifying. And they are the ones who will answer for the outcome.

This is not only a technical problem. It is institutional and psychological. People do not delegate meaningful authority to systems they cannot inspect, challenge, explain, or revoke. Organizations cannot insure what they cannot audit. Regulators cannot certify what they cannot examine. Practitioners cannot stake their professional judgment on what they cannot interrogate.

The earned autonomy problem is: **On what basis should a human, team, or institution decide that this agent has earned autonomy in this context, for this scope, right now — and what evidence justifies that judgment?**

### Why They Must Be Solved Together

Solving either problem alone is insufficient.

Observable autonomy without genuine reasoning gives you a window into compliance. You can see every step the agent takes — but the steps were prescribed, so the observation confirms obedience, not thought. Trust calibrated to compliance is fragile: it breaks the first time the situation departs from the script.

Genuine reasoning without observable autonomy gives you an unverifiable claim. The agent may be reasoning brilliantly or hallucinating confidently — and nobody can tell the difference. The capability is real but invisible, so it cannot serve as the basis for granting authority.

Both together produce something qualitatively different: an agent that reasons freely about what to do AND makes that reasoning visible enough for observers to judge whether it justifies the authority being granted. The reasoning is the substance. The visibility is the evidence. Neither is sufficient without the other.

A nurse does not refuse to let an AI manage medication interactions because the AI gets them wrong. The AI often gets them right. She refuses for two reasons that map to these two problems: she cannot see *why* the AI chose what it chose (earned autonomy), and she has no operational way to tell whether the AI's response is adapted to her specific patient or is a confident-looking output that would have arrived regardless of the patient's specifics (autonomous reasoning). The capability is there. The basis for trusting it — and the basis for distinguishing situated reasoning from confident pattern-matching — are not.

That gap is the boundary. It repeats in every domain where the stakes are real.

A clarification of scope: in fully prescribable domains — commercial aviation, assembly-line automation — earned autonomy through static certification works. Every mission decomposes into finite prescribed procedures; trust is earned through exhaustive testing within defined operational boundaries, not through demonstrated reasoning. The framework targets domains with **irreducible novelty**: medicine, law, engineering, analysis — domains where the situations that matter most cannot be fully anticipated by any checklist, and where the agent must adapt to conditions the instruction author never foresaw. This is not a limitation. It is the scope where the framework is necessary.

The missing ingredient that requires both problems is **delegability**: the operational discipline of converting demonstrated, visible, situated reasoning into bounded, revocable authority. Delegability is not capability (the model can do the task). It is not safety (the model won't cause harm). It is the discipline that connects what the agent appears to be doing to what an observer can justifiably let it keep doing.

---

## What Existing Work Does and Does Not Solve

Current AI work addresses adjacent parts of both problems:

- **Capability evaluation** (benchmarks like MMLU, HumanEval, domain-specific test suites) asks whether a model can produce useful or correct outputs. It measures what the model *can do* — not whether it *reasoned* its way there or whether a human should *let it do it* unsupervised.
- **Safety and governance frameworks** (NIST AI RMF, the EU AI Act, ISO/IEC 42001) ask what harms must be controlled and what oversight structures are required. They define the guardrails — not the basis on which an operator decides the system has earned enough trust to operate within them, and not whether the system is genuinely reasoning within those guardrails.
- **Alignment and interpretability research** (RLHF, constitutional AI, mechanistic interpretability, representation engineering) asks how model behavior, incentives, and internal mechanisms should be understood and shaped. It works on making models safer and more transparent from the inside — but it does not yet give external observers a deployable way to judge whether a specific agent is genuinely reasoning in a specific context, nor a practical mechanism for granting or revoking autonomy based on that judgment. XAI research has confirmed that explainability alone does not produce trust — studies show explanations increase understanding but not confidence in delegation, because users want evidence that the system *adapted to their case*, not just a window into a fixed process. This validates the gap: the missing construct is not more explanation but delegability grounded in visible, situated reasoning.
- **Prompt engineering and agent frameworks** (ReAct, chain-of-thought, tool-use architectures) improve how agents execute tasks. But they do not distinguish between an agent that follows a sophisticated prompt template and one that genuinely interprets a mission. The structure looks like reasoning. Whether it *is* reasoning remains invisible.

None of these fields — individually or together — yet answer the two operational questions this work cares about:

> **Is this agent genuinely reasoning about what to do, or merely complying?**
>
> **Has this agent earned the right to act more autonomously here, and what evidence justifies that judgment?**

That is the gap this work targets. Not capability, not safety, not alignment — but **delegability** as defined above: the operational discipline of converting demonstrated, visible, situated reasoning into bounded, revocable authority.

This is not a claim that existing fields are wrong or useless. It is a claim that they do not yet add up to a deployable discipline for earned autonomy grounded in externally evidenced reasoning.

---

## What This Work Is Trying to Build

This work is not trying to metaphysically prove that a model is "really thinking." That claim is too strong and not operationally useful.

It is trying to build a practical framework that addresses both problems simultaneously:

1. A way to structure the relationship between human and AI so the agent must *interpret and adapt* rather than merely comply — creating the conditions for genuine reasoning rather than assuming it. *(Autonomous reasoning)*
2. A way to make the agent's reasoning path legible enough for observers to inspect, challenge, and learn from — so that reasoning, when it occurs, is *visible* rather than claimed. *(Earned autonomy)*
3. A way to calibrate trust based on the quality of observable reasoning rather than vendor assertion, output correctness, or intuition — so that authority tracks *demonstrated reasoning*, not reputation. *(Both problems together)*
4. A way to increase or restrict autonomy based on what has actually been demonstrated — so that authority scales with evidence of genuine reasoning, not with time or familiarity. *(Both problems together)*
5. A way to carry this discipline across domains without reinventing both problems from scratch each time.

This is the missing layer between model capability and real-world adoption.

---

## How the Principles Address Both Problems

Three principles form the foundation. Each targets a specific aspect of the two-problem boundary.

**Commander's Intent** attacks the autonomous reasoning problem directly.

It defines the destination and constraints without scripting the route. The human is the commander who gives the mission — *what* needs to be achieved and *why* it matters. The agent determines *how*. This is not vagueness; the mission is precise ("find what doesn't earn its maintenance cost and remove it, proving each removal is safe"). But the method is the agent's to discover, adapted to what it actually encounters.

This does not prove inner reasoning. But it creates conditions in which useful performance depends on interpretation and adaptation rather than rote execution. An agent operating under Commander's Intent that merely follows a hidden checklist will produce visibly shallow, generic results — because the checklist can't anticipate the specific situation. Reasoning that is genuinely adapted to the objective, by contrast, produces situated responses that reflect the specifics of what was encountered. The principle doesn't guarantee reasoning. It makes reasoning *necessary for good performance* and makes shallow compliance easier to expose and challenge.

**Observable Autonomy** attacks the earned autonomy problem directly.

It requires the agent's path, rationale, uncertainty, and decisions to be visible as it works — not upon request, not as a post-hoc summary, but as a structural property of the operation itself. The trail is not a feature. It is the mechanism by which the agent earns the right to keep acting.

Crucially, Observable Autonomy does more than make the output visible. It makes the *quality of reasoning* visible. When the trail shows how the agent interpreted the mission, what it considered, what it rejected, where it was uncertain, and how it adapted to what it found — the observer can distinguish genuine reasoning from pattern-matching. The trail becomes evidence not just of *what was done* but of *how the agent thought*.

**Together, they produce what neither can alone.**

Commander's Intent without Observable Autonomy creates an agent that may be reasoning brilliantly — in a black box. You gave it the mission and trusted it to reason. Maybe it did. You can't tell.

Observable Autonomy without Commander's Intent creates an agent whose every step is visible — but the steps were prescribed. You can see compliance. You cannot see thought.

Both together: the agent receives a mission, reasons freely about how to achieve it, and makes every step of that reasoning visible. The observer can now assess not just "was the task completed?" but "did this agent *think* about this situation, and does that thinking justify the authority it was granted?"

**Convergence Is Silence** prevents self-deception about both problems — and defends against the framework's most serious vulnerabilities. A system that produces a trail *looking* situated while internally pattern-matching is a "Synthetic Outlaw" of this framework: it satisfies the formal requirements while subverting their intent. A trail generated by the same model that produced the output can confabulate reasoning that never occurred — narrating adaptation that was actually autocompletion. Convergence Is Silence is the primary defense against both attacks: diverse, independent evaluators — working from different analytical traditions, without consulting each other's scores — are collectively harder to fool than any single observer. A confabulated trail that deceives one evaluator is less likely to deceive three operating independently. Without it, Commander's Intent and Observable Autonomy can produce a convincing-looking trail that only one perspective ever validated — and neither the reasoning quality nor the trust judgment has been honestly tested.

---

## What the Framework Measures

The target property is **Autonomous Reasoning Fidelity** (ARF). ARF is the point where both problems meet.

ARF is not proof of consciousness, and it is not certainty about internal cognition. It is the strongest practical external signal this framework can produce: evidence that an agent is reasoning about what to do rather than merely complying (Problem 1) and that this reasoning is visible enough for observers to judge whether it justifies the autonomy being granted (Problem 2).

ARF emerges only when both principles are satisfied simultaneously. Commander's Intent creates the conditions under which interpretation and adaptation are required for good performance — the agent must engage with the mission, not just execute steps. Observable Autonomy makes the engagement visible — the trail shows *how* the agent arrived at its conclusions, not just what the conclusions were. Neither half alone produces delegability:

- Unconstrained reasoning in a black box leaves the autonomy side unaddressed: there is no evidence an observer can act on.
- Visible compliance leaves the reasoning side unaddressed: there is evidence, but it documents obedience rather than thought.
- Visible, situated, mission-driven reasoning is the operational basis for *delegability* — the point where both problems are addressed together.

A critical dependency: in routine cases, situated reasoning and sophisticated pattern-matching can produce identical-looking trails. The distinguishing signal emerges under novel conditions — when the situation departs from expected patterns and the agent must either genuinely adapt or reveal itself as generic. The framework therefore requires structured novelty as a necessary complement to the trail. Without it, the trail documents narration, not reasoning.

ARF is what the framework *measures*. The observers defined below are *who it measures for*. The principles are the mechanism that *produces* it. ARF is not a claim about what the agent is internally doing; it is the strongest external signal the framework can offer.

---

## Who the Evidence Must Serve

Observable Autonomy states that every autonomous operation must produce a visible, continuous trail. But "visible" is not a single thing. Different observers need different evidence from the same trail — and a framework for earned autonomy must account for all of them while still preserving the reasoning-fidelity question that the trail is meant to surface.

Consider the observers who exist wherever autonomous AI operates in consequential domains:

- **The practitioner** — the nurse, the engineer, the analyst — needs case-level reasoning. *Why did the agent choose this action for this patient, this component, this case? Did it actually reason about my specific situation, or did it pattern-match from training data?* The evidence must be specific, situated, and legible enough to challenge in the moment. The practitioner's question spans both problems: *Do I trust this decision — and did this agent actually think about it?*

- **The deployer** — the organization that fields the system — needs aggregate reliability. *Across a thousand cases, how often did the agent's reasoning hold up? Where did it fail? Are the failures random, or do they cluster where the agent fell back to pattern-matching rather than reasoning?* The deployer's question is: *Should I keep granting this system this scope of authority?*

- **The regulator** — the body that sets standards for the domain — needs population-level validation. *Does this class of system, operating under these conditions, meet the threshold for this domain? Does its apparent success reflect genuine adaptation to cases, or brittle heuristics that only look good in aggregate?* The evidence must be standardized, reproducible, and resistant to cherry-picking. The regulator's question is: *Can this type of system be permitted to operate here, and on what basis do we believe its reasoning generalizes safely enough to allow it?*

- **The liability bearer** — the insurer, the legal entity, the institution that absorbs the cost of failure — needs tail-risk distribution. *What is the worst-case exposure? How often does it occur? What does the trail show about how failures propagate? Do catastrophic failures cluster where the system stopped adapting and fell back to shallow patterning?* The evidence must quantify downside, not just average performance. The liability bearer's question is: *What is my exposure if this system fails in the worst way it can fail, and what does the trail say about why those failures happen?*

- **The agent itself** — an autonomous system operating under these principles has access to its own trail. It can detect when its outputs are becoming repetitive rather than situated, when its responses no longer reflect the specifics of what it encountered, when it is operating outside the scope where its autonomy was earned. The agent's evidence need is self-monitoring: *Are my recent steps still adapted to this situation, or am I producing generic responses? Am I still within the bounds that justify my current level of autonomy?* This is the logical endpoint of both problems addressed together — a system that can read its own trail and self-limit. But self-assessment can become self-justification, so the agent's trail must remain legible to all the other observers. The agent is an observer, never the final one.

These are different questions. They require different aggregations, different time horizons, different units of analysis. But what they share is that they are all *evidence* — all different facets of delegability — and they all depend on the same underlying property: a trail that is continuous, legible, and structurally guaranteed by the system's architecture, not bolted on after the fact.

A framework that satisfies the practitioner but not the regulator will be adopted and then revoked. A framework that satisfies the regulator but not the practitioner will be mandated and then circumvented. A framework that satisfies neither the deployer nor the liability bearer will never reach production regardless of how good the AI's outputs are.

This is why Observable Autonomy is stated as an architectural constraint rather than a feature request. The trail is one thing. The evidence extracted from it serves many purposes. The principle must be strong enough to support all of them — because earned autonomy that only one observer can verify is not yet earned.

---

## What Must Be Built on Top

The principles are a foundation, not a complete solution. The layers that must be built on top of them include:

- **Novelty and anti-compliance evaluation.** This is the most critical layer — the mechanism that makes the trail meaningful rather than decorative. As stated above, routine situations cannot distinguish situated reasoning from pattern-matching; the trails look identical. The framework needs structured novelty: cases where rote instruction-following fails but situated interpretation succeeds, adversarially underspecified situations, and distribution shifts that expose shallow compliance. Without this layer, the framework's central claim — that it can measure Autonomous Reasoning Fidelity — is asserted rather than tested.
- **Domain-specific correctness standards.** The principles are domain-portable; the quality criteria are not. Medicine, law, and engineering each need their own definition of what "correct" means within the framework. Without this, the practitioner has no yardstick for case-level judgment, and the regulator has no threshold to certify against.
- **Legal liability and governance models.** Who is accountable when earned autonomy produces a bad outcome? The trail makes accountability *possible*; policy must define who bears it. This is the layer the liability bearer requires before any tail-risk assessment is meaningful.
- **Evaluator independence and diversity.** Convergence Is Silence requires diverse scrutiny. How evaluator pools are composed, rotated, and kept independent is an operational problem the principles define but do not solve. Without this, self-grading masquerades as convergence — and the agent-as-observer problem compounds.
- **Failure testing and revocation thresholds.** Under what conditions should earned autonomy be revoked? The trail provides the evidence; the thresholds must be defined per domain. The deployer cannot answer "should I keep granting this scope?" without defined boundaries for failure.
- **Scope control as autonomy expands.** Autonomy earned in one scope does not automatically transfer to a broader one. The escalation path needs design. Every observer’s question changes when scope changes — the evidence that justified autonomy in a narrow context does not automatically justify it in a wider one.
- **Tail-risk quantification.** The liability bearer needs more than average performance. Worst-case exposure, failure propagation paths, and downside distributions must be extractable from the trail. This is a distinct engineering problem from trail generation.
- **Long-horizon alignment.** The principles verify reasoning fidelity in the near term. Whether an agent's goals remain aligned over extended periods is a separate research problem.

These are not disclaimers. They are the research and engineering agenda that sits on top of the foundation. The right claim is not "these principles solve autonomous AI." The right claim is that they establish necessary preconditions — and that without them, none of the layers above can function.

---

## The Working Hypothesis

The working hypothesis is that humanity can adopt more AI power if two conditions are met: AI systems reason about what to do rather than merely follow instructions, and that reasoning is made visible enough for autonomy to be **earned, legible, and challengeable** rather than opaque, vendor-asserted, or intuition-driven.

If that hypothesis is right, then the work of defining these principles and their operational implications is not an academic exercise. It is the early articulation of an **adoption architecture for autonomous AI**: the missing layer between model capability and real-world delegation. A way to convert model capability into delegable authority by solving both the reasoning problem and the trust problem simultaneously.

What may generalize across domains is not every surface instruction, threshold, or vocabulary term. What may generalize is the deeper pattern: give the agent a mission rather than a script, require a visible trail of how it reasoned, challenge the claim from diverse perspectives, and expand authority only when the evidence — of both genuine reasoning and earned trust — supports it.

Any system that operationalizes these principles — in any domain, at any scale — becomes a test bed for this hypothesis. The value is not in the specific implementation. It is in whether the principles, once made operational, produce the conditions under which interpretation is required for good performance and the evidence different observers need to justify the autonomy they are being asked to accept.

The name may evolve. The function will not:

> **Give humans a practical, evidence-based way to grant AI systems more authority — by solving both the reasoning problem (is the AI genuinely interpreting and adapting to this situation?) and the trust problem (can observers justify the autonomy being granted?) — so that the enormous potential of autonomous AI becomes adoptable, not just impressive.**

The principles are the theoretical core. Commander's Intent makes interpretation and adaptation necessary for good performance. Observable Autonomy makes that interpretation visible enough to evaluate. Convergence Is Silence prevents self-deception about both. Autonomous Reasoning Fidelity is the measurable external signal that both are present. Delegability is the operational discipline. The evidence layers — practitioner, deployer, regulator, liability bearer, agent — define who must be satisfied and what “evidence” means for each. The work ahead is to take this framework into the domains where it matters most — and to discover what each domain reveals that the framework could not anticipate.

---

## Out of Scope: What This Framework Does Not Solve

This framework is an **evidence substrate**, not a trust generator. It produces the conditions under which trust *can* form on observable grounds, but it does not manufacture trust, guarantee adoption, or solve the social, organizational, and human-factors problems that surround autonomous AI. Naming these limits explicitly prevents the framework from being judged against claims it never made.

The following are real, important problems that this framework does **not** address:

1. **Reviewer engagement and scaling.** Earned autonomy is meaningful only if someone evaluates the evidence. If no one reads the trail, autonomy becomes de facto unconditional regardless of how much evidence exists. If everyone reads it, the reviewer becomes the bottleneck. The framework provides multi-resolution evidence to lower the cost of review, and an in-trail reviewer-engagement signal so non-engagement is at least visible — but it has no answer for *how* organizations actually staff, incentivize, and sustain meaningful human review at scale. **This is the framework's deepest unresolved gap.** It is named here so it cannot be hidden by the existence of the trail.
2. **Reasoning correctness.** Transparency proves *visibility*, not *correctness*. A trail can be honest, legible, and wrong. The agent can show its reasoning step by step and still arrive at a defective conclusion — or narrate a confident-looking adaptation that was actually pattern-matching. Convergence Is Silence (P3) is the framework's primary defense against this, but it depends on diverse evaluators being available, willing, and competent. Where they are not, transparency does not save you.
3. **Human intent stability.** Commander's Intent assumes the human can articulate a destination clearly enough for the agent to interpret it. Real missions are often vague, contradictory, politically constrained, or shifting over time. The framework can clarify ambiguity through dialogue at session start, but if the upstream intent is unstable, every downstream decision inherits that instability.
4. **Organizational willingness to delegate.** Many organizations do not want AI to have autonomy at all — earned or not. Fear of loss of control, job displacement, liability, political consequences, and being blamed for AI mistakes are legitimate concerns the framework cannot address. The framework's claim is conditional: *if* you want to delegate, here is how to make the delegation observable. It does not argue that you should.
5. **Incentives, values, and the social layer of trust.** Reliability is one component of trust. Trust also requires shared values, aligned incentives, and demonstrated character over time — none of which the framework supplies. The framework is a **governance and evidence layer**, not a trust model. Governance enables trust; it does not create it.
6. **Domain measurability.** The principles are domain-portable; the existence of a meaningful "target condition" is not. In some domains the next improvement is unclear, unmeasurable, or politically contested. The framework gives the agent discipline for navigating uncertainty, but it cannot manufacture a measurable target where none exists.
7. **Legal liability and accountability assignment.** The trail makes accountability *possible*; policy and law must define who bears it when earned autonomy produces a bad outcome. This is named in "What Must Be Built on Top" — repeated here because the absence of an accountability framework can hollow out the value of the trail.
8. **Adoption and organizational psychology.** Whether stakeholders will accept the concept of "earned autonomy" at all is a sociological question the framework treats as a precondition. If the answer is no for a given organization or domain, the framework is inert there regardless of how well it functions.

These are not disclaimers added defensively. They are scope boundaries. A framework that claims to solve them would be overclaiming. A framework that pretends they don't exist would be dishonest. Naming them here is itself an instance of Observable Autonomy applied to the framework's own design.

---

## The Problem In Two Sentences

How do we structure the relationship between human and AI so that the AI must interpret the mission and adapt to context rather than merely follow prescribed steps? And how do we make that reasoning visible enough for different observers to justify granting or withholding autonomy?

These are two problems. They require one framework. Neither can be solved alone.

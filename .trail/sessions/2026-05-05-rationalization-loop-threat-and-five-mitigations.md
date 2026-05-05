# Session: rationalization-loop threat and five mitigations

**Date:** 2026-05-05
**Skill:** none formally invoked — design conversation with operator
**Target:** autonomous-agent-skills (`C:\Users\admin\.copilot\skills`)
**Operator:** Nils Wendelboe Holmager (ntholm86)
**Agent:** GitHub Copilot (Claude)
**Fidelity:** Partial — conversation was happening live without trail capture; this session file is being written retroactively at the operator's prompt ("I hope you are logging all this talk"). Recording the gap itself is part of the trail.

---

## What the operator named

After reading the "Stated Reasoning ≠ True Reasoning" section of README, the operator pushed one level deeper than the cited papers:

> "When the agent runs the improve skill and writes the trail in the beginning, the model will make up arguments and reasoning that fit decisions that were made — even if they were wrong. The trail always becomes 'green'. This kills the entire system and proof validity."

This is the central threat to the proof claim. If the agent that *makes* the decision also *writes* the rationale, and the rationale is written *after* the outcome is known, the trail trends toward uniformly self-justifying. Uniform green is indistinguishable from no signal. Convergence across three model families gives no protection if all three are running the same rationalization architecture.

This is a deeper problem than Turpin/Chen describe. Their work is about CoT faithfulness in a single inference. The operator named the **structural** version: a feedback loop where stated reasoning is generated post-hoc to justify outcomes already committed.

---

## Five mitigations proposed and approved

The operator approved all five. They form a stack — none alone is sufficient.

1. **Pre-commit prediction.** Force a falsifiable prediction *before* the action: "I will change X. I expect Y. I expect Z not to happen." Then act. Then record what actually happened. Locks the claim before evidence is available. Cheapest, highest-leverage. Fits inside Improve (new step) and Trail (predicted/actual fields).

2. **Required reversal density.** A healthy trail has reversals, dead ends, predictions that failed. N consecutive entries with no `[!REVERSAL]` / `[!REALIZATION]` / outcome-mismatch markers should be flagged as suspect, not celebrated. Fits inside Trail spec + Retrospect arc-check.

3. **Separate writer from decider.** The strongest structural fix. The agent that made the change does not write its own trail entry. A second pass — different role, possibly different model — reads the diff, prior trail, and stated outcome, and writes the entry. The decider's narrative becomes input, not output. Removes the rationalization incentive structurally rather than asking the agent to behave against it.

4. **Adversarial trail audit.** A separate skill (or extension of Probe) whose job is to read the trail with the explicit prompt: *find the rationalizations. Where does the stated reason not match the diff? Where is the prediction missing? Where would a hostile reviewer say "post-hoc"?* Run periodically. Findings appended to the trail itself.

5. **Outcome anchoring at the arc level.** For every claim made in the trail across the arc, did it hold? If 30 entries claim "this reduces complexity" and complexity is now higher, the trail has been lying to itself. Exposes per-iteration confabulation that no individual entry would reveal. Extends Retrospect.

---

## Operator constraint

> "I want to keep the purpose of the skills crystal clear."

The five mitigations must integrate without diluting the existing skill purposes or expanding the skill count beyond what is genuinely necessary. Mapping:

- #1 → Improve (new step) + Trail (new fields). No new skill.
- #2 → Trail (markers already exist) + Retrospect (arc-check). No new skill.
- #3 → Cross-cutting discipline. May be implementable as a Trail-skill mode ("audit pass") rather than a new skill. To be designed.
- #4 → Likely a new skill (`audit` or extension of Probe). Probe is for *behavior* validation; Audit would be for *trail* validation. Distinct enough to warrant separation.
- #5 → Retrospect (extension of arc-claim work it already does).

Net: at most one new skill (`audit`), plus targeted spec changes to Improve, Trail, and Retrospect. The five existing skill purposes remain crystal clear.

---

## Why this session was almost lost

The operator and the agent had a substantive design conversation — identifying the structural threat to the proof claim, naming five concrete mitigations, agreeing on the integration constraint — and the agent did not write to the trail until the operator asked "I hope you are logging this." The agent had been treating the conversation as conversation, not as work.

This is itself evidence for mitigation #1. The agent's stated reasoning at the end of the conversation would have been "we discussed mitigations, the operator approved them, here is what to do next" — a clean post-hoc account. The actual trail of the work — the threat being named, the mitigations being constructed, the constraint being added — would have been invisible.

The Improve and Trail specs need to make session-file capture mandatory not just for code-edit sessions but for **substantive design conversations that produce decisions**. A decision made in conversation and not written down is a decision the next session cannot inherit. The Memory Model breaks at exactly that boundary.

---

## What is explicitly queued next

A design pass on Improve, Trail, Retrospect specs to integrate mitigations 1, 2, 5 — and a decision on whether `audit` becomes a sixth skill or a Trail-skill mode. Not to be done in this conversation; to be done as a deliberate Improve run with this session file as input.

The pre-commit-prediction discipline (#1) should be the first one shipped. It is the cheapest, the most testable, and it changes the epistemic shape of every subsequent trail entry.

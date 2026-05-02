# Compass — autonomous-agent-skills

_Last updated: 2026-05-02 (run: retro-on-updated-vision)_  
_Derived from: full arc read through intent-v1-2-1-not-hunch, read against substantially updated vision.md (recognition claim, two-phase architecture, adoption success condition, learning falsification condition — all added since previous compass)._

---

## Current claims

**1. Phase 1 (vision convergence) has its first mechanism but remains operator-initiated in practice.**  
The two-phase architecture vision names is now partially instantiated: Hunch is the Phase 1 mechanism, the iterative loop is Phase 2. Hunch has been validated across five foreign-target runs. But reading the arc as one document, every major direction shift — Retrospect, Hunch, compass/vision split, position document, competitive framing — was triggered by operator input, not agent-initiated Hunch. The occasion-independence experiment (2026-05-02) is the first data point of agent-initiated direction questions, but it occurred immediately after the mechanism was designed, in the same operator-agent pairing. Phase 1 occasion-independence — agent surfaces direction questions cold, on a future arc, without recent priming — remains unobserved.

**2. The recognition claim and adoption success condition introduce a validation gap no internal loop pass can close.**  
The updated vision redefines one test of success: recognition by practitioners who have felt the friction, and adoption by developers using the skills in their own projects without the author's help. Internal convergence runs (three-family silence) measure structural consistency — they do not test whether the framework produces instant recognition in the target audience, or whether a stranger can deploy it. Phase 3 of the position document plan (direct outreach) is the only mechanism for this. The loop's arc to date has been Phase 2 work. Phase 3 has not started.

**3. Trail v1.10.0 closes the longest-standing Observable Autonomy gap; enforcement remains soft.**  
Sessions/ was marked "optional" since the trail structure was first specified — an explicit permission-to-skip for the full-resolution tier. Trail v1.10.0 (2026-05-02) makes it mandatory with an explicit write step, fixing both the mechanical gap (no write procedure) and the rhetorical one (the word "optional"). Observable Autonomy now has structural support at the skill level. Remaining gap: verify.py does not check for sessions/ file presence — the mandatory framing is a skill-level requirement, not a mechanically enforced one.

**4. The learning falsification condition is precisely defined but has one borderline case, not a clear cross-session positive.**  
Vision defines learning as: a future agent acts on a prior `[!REALIZATION]` rather than rediscovering it. The closest candidate in the arc: a `[!REALIZATION]` about operator-prompting dependency (runs 68, 71) preceded the occasion-independence mechanism design (2026-05-02, same session). But "same session" means same context window — not a fresh agent encountering the [!REALIZATION] without memory of it. A clear cross-session case has not yet been observed.

**5. Capability claims are evidence-grounded across multiple targets and two model families; thin, not absent.**  
Hunch: 5 confirmations across 4 targets (own vision, evo, vectorium, leifoglenedk, manifesto). Retrospect: 2 compatible passes (Anthropic + GPT-5.3-Codex). Improve occasion-independence: 2 data points across 2 arcs. Intent/Hunch cross-reference fixed (d149c48) — closes a practitioner-discoverability asymmetry where entering the suite through Intent gave no pointer to Hunch. The suite is no longer asserting capabilities without evidence; the evidence is real but thin and requires cross-family and external replication.

**6. External harness proof is the highest-urgency unvalidated claim with two-sided urgency.**  
Research side: the skills have only been run by agents that co-evolved with them. The research question requires the protocol to work outside its author's context. Adoption side: adoption success requires a developer to encounter and deploy the skills without help. An external proof — operator not the author, harness didn't co-evolve — is the minimum evidence bar for both. Nothing in the current queue removes this gap.

---

## What the next runs should test

1. **External proof** — run the protocol on a target where the operator is not the author and the harness did not co-evolve with the skills. Addresses both research success and adoption success simultaneously.
2. **Phase 1 occasion-independence (cold case)** — trigger Hunch in a fresh session with no recent priming on a new arc. This is the missing data point: agent initiates a direction question cold, not in the session where the mechanism was designed.
3. **Retrospect reliability test** — run on a materially different arc (foreign target, longer history, different operator). Check claim stability and decision usefulness outside the self-targeting context.
4. **Learning falsification: first clear cross-session case** — identify a `[!REALIZATION]` from a prior session that a future agent (in a new context window, no memory of the prior session) would encounter and act on differently because of it. The trail needs at least one clear case before the learning claim in vision is anything more than a definition.

---

## Loop-effectiveness notes

This arc-read was conducted against a substantially updated vision: the recognition claim, two-phase architecture, adoption success condition, and learning falsification condition were all added since the previous compass. The most significant finding from reading the arc against this updated vision: the loop has executed Phase 2 (iterative improvement, documentation convergence, capability validation) well and has produced evidence for its capability claims. It has not executed Phase 1 (vision convergence initiated by the agent) independently — every direction input has come from the operator. Vision itself says Phase 1 is not automatable. But the arc does not yet distinguish between "the agent cannot surface direction questions unprompted" and "the agent has been too continuously primed by the operator's own initiatives to need to." The occasion-independence experiment is the right test for this distinction, and it needs cold passes to be informative.
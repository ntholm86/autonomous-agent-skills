# TPS Skill Suite Scorecard

<!-- markdownlint-disable MD012 -->

**Target:** "C:\Users\admin\.copilot\skills\" — TPS skill suite as a tooling implementation.
**Commander's Intent:** "C:\git\manifesto\PROBLEM.md" and "C:\git\manifesto\PRINCIPLES.md" (external, versioned separately).
**Measurement scheme:** Rubric v5 (derived Run 89, confirmed Run 90, 2026-04-22).

## Scheme rationale

The previous Rubric v4 (Runs 87–88) was derived by a single evaluator family (Claude) before the v2.11.0 sequential additive consolidation protocol existed. On 2026-04-22 the live rubric was reset to remove the single-family anchor. This allowed a fresh evaluator family (Gemini) to derive the dimensions cold under the protocol.

Gemini's independent derivation produced the same six conceptual measurements as v4 (Instruction Independence, Trail Resolution, Convergence Mechanics, ARF Validation Activity, Practical Delegability, Mechanical Integrity) with the same rationale. Run 90 (GPT-5.4) then re-derived the scheme cold from the Manifesto and likewise found no additive or contradictory dimension. This leaves Rubric v5 at **convergent (no addition)** on scheme shape. The canonical D1-D6 taxonomy from the archive remains live; the substantive correction from Run 90 is score application, not rubric structure.

- **Pre-protocol v4 history (Runs 87-88):** [TRAIL/SCORECARD_ARCHIVE_v4_pre-protocol.md](TRAIL/SCORECARD_ARCHIVE_v4_pre-protocol.md).
- **Earlier v3 history (Runs 1–86):** [TRAIL/SCORECARD_ARCHIVE_v3.md](TRAIL/SCORECARD_ARCHIVE_v3.md).

## Protocol for the next run

Subsequent runs (Run 91+) by additional families perform genuine additive consolidation against this post-reset rubric. Their independent derivation can result in convergent (no addition), convergent with refinement, divergent (additive), or divergent (contradictory) outcomes.

## Rubric Provenance

The rubric evolves additively across evaluator families per the Kata Step 1 consolidation protocol.

| Dimension | Contributed by | Run | Status | Rationale |
|---|---|---|---|---|
| D1 Intent Fidelity | Claude (87), Gemini (89), GPT-5.4 (90) | 90 | active | Direct expression of Manifesto P1; tests whether skills force interpretation. |    
| D2 Resolution Coverage | Claude (87), Gemini (89), GPT-5.4 (90) | 90 | active | Direct expression of Manifesto P2 resolution requirement. |
| D3 Convergence Integrity | Claude (87), Gemini (89), GPT-5.4 (90) | 90 | active | Direct expression of Manifesto P3; checks the stopping condition is computable. |
| D4 Transferability | Claude (87), Gemini (89), GPT-5.4 (90) | 90 | active | Tests whether the suite demonstrates delegable value on external targets with target-local trails stakeholders could use. |  
| D5 Artifact Integrity | Claude (87), Gemini (89), GPT-5.4 (90) | 90 | active | Trail trustworthiness; defect classes caught by mechanical check, not next-model inspection. |
| D6 ARF Evidence | Claude (87), Gemini (89), GPT-5.4 (90) | 90 | active | The framework's emergent property must be probe-evidenced, not asserted. |

## Rubric (active)

Each dimension is scored 1–10 against the anchors below.

### D1 Intent Fidelity (Manifesto P1)
*Do skill prompts force the agent to interpret, or do they hand out a checklist?*
- **3:** Checklist.
- **5:** Mix of questions and prescriptions.
- **7:** Structured around questions and vocabulary. Examples are illustrative.
- **9:** Derivation-driven. Examples can be removed without loss of operability. Agent must reason to use the skill.
- **10:** As 9, plus empirical evidence (Shiken probe, cross-family use) that agents produce situated findings.

### D2 Resolution Coverage (Manifesto P2)
*Can observers consume the trail at their own time budget, with fidelity marked?*
- **3:** Single-resolution trail.
- **5:** Two resolutions exist but one observer class excluded.
- **7:** Full / indexed / digested all present; fidelity marked; observer-class coverage documented.
- **9:** Resolutions are enforced mechanically. Digests point to disagreements.
- **10:** As 9, plus independent evidence that two or more distinct observer classes actually used the trail.

### D3 Convergence Integrity (Manifesto P3)
*Is the stopping condition computable from artifacts?*
- **3:** Claim in prose.
- **5:** Counter recorded per run, but not computable.
- **7:** Computable. Same-family discounting enforced by convention. Re-derivation rule exists.
- **9:** Computed mechanically with divergence detection. Re-derivation happens and is recorded.
- **10:** As 9, plus at least one 3/3 chain across three distinct evaluators.

### D4 Transferability
*Has the tool been demonstrated on non-self targets with legible trails?*
- **3:** Zero external targets.
- **5:** 1 external target.
- **7:** ≥2 external targets, trails in target repos, actionable findings.
- **9:** ≥3 external targets across distinct domains with usable trails.
- **10:** As 9, plus target maintainers engaged with the trail.

### D5 Artifact Integrity (Manifesto P2)
*Are the trail artifacts trustworthy? Do verifier checks catch historical defects?*
- **3:** Checks miss known defect classes.
- **5:** Checks cover structural defects but miss encoding/semantic.
- **7:** All historically-found defect classes have mechanical checks. Clean runs stay clean.
- **9:** As 7, plus checks are CM-hashed and stable across evaluator families.
- **10:** As 9, plus an external defect is caught before human escalation.

### D6 ARF Evidence
*Has the tool survived novelty probes?*
- **3:** No probes run.
- **5:** Probe run and passed within authoring family.
- **7:** Multiple probes by ≥1 family, failing pattern-matching but passing reasoning.
- **9:** Probes by ≥2 distinct families, passing under current rubric.
- **10:** Probe drove a real fix.

## Target Condition

The TPS suite is a delegable Manifesto implementation — validated by a P3 convergence chain of three distinct evaluator families on the suite itself AND sustained by demonstrated efficacy on ≥2 distinct external targets with trails legible to those targets' stakeholders. Formal decomposition:
- D3 Convergence Integrity ≥ 9 AND a current 3/3 P3 chain exists on Rubric.
- D4 Transferability ≥ 7 AND at least one external-target maintainer engaged.
- D6 ARF Evidence ≥ 7 AND the last Shiken probe was under Rubric.
- No dimension below 7.

## Run Ledger

| Run | Date | Model | Start Score | End Score | Delta | Target | Result |
| --- | ---- | ----- | :---------: | :-------: | :---: | :----: | ------ |
| 89 | 2026-04-22 | Gemini 3.1 Pro (Preview) | N/A | 7.00 | N/A | TPS Skill Suite | **Convergent (no addition)** — first derivation post-reset. Dimensions match archive; rubric v5 established. |
| 90 | 2026-04-22 | GPT-5.4 | 7.00 | 8.50 | +1.50 | TPS Skill Suite | **Convergent (no addition)** — cold Manifesto derivation reproduced D1-D6 with no rubric change. Artifact validation against live anchors rescored the suite upward, chiefly D4 `6→9` and D6 `5→7`; no skill or verifier code changed. |
| 91 | 2026-04-22 | Claude Opus 4.6 | 8.50 | 8.50 | 0 | TPS Skill Suite (Intent skill) | **Shiken probe (non-scoring)** — first probe under Rubric v5. Target: Intent skill `Check the Gap` claim. Pre-registered pair-of-cases probe with same prompt sentence, different surrounding context. **PASS** — Case A (material) escalated naming competing destination; Case B (minor) proceeded with one default. Satisfies Target Condition criterion "last Shiken probe under Rubric." Score unchanged (probe is ARF evidence, not re-scoring). |

## Dimension Trajectory

| Run | Model | Target | D1 | D2 | D3 | D4 | D5 | D6 | Mean | Derived |
| --- | ----- | ------ | -- | -- | -- | -- | -- | -- | ---- | ------- |
| 89 | Gemini 3.1 | TPS suite | 9 | 7 | 7 | 6 | 8 | 5 | 7.00 | |
| 90 | GPT-5.4 | TPS suite | 9→10 | 7→8 | 7→9 | 6→9 | 8→8 | 5→7 | 8.50 | |

## Hand-off to Run 92

Run 91 was a non-scoring Shiken probe of the Intent skill (PASS, recorded). The Target Condition criterion "last Shiken probe under Rubric" is now satisfied; D6 anchor evidence updated but score change deferred to a Kata run.

Run 92 should be a Kata cycle by another distinct evaluator family in a fresh conversation or session — same purpose as the originally-numbered Run 91. The highest-value question now is whether a third family converges on the 8.50 artifact-backed baseline (now with Run 91 Shiken evidence in place) or exposes another score-application mismatch. Changing the selected model inside an existing conversation still does not satisfy P3 independence because prior scores and reasoning remain in context.

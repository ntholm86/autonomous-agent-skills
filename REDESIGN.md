# v3 Redesign — Why This Exists

April 2026. Branch: `v3-redesign`. Predecessor: `v2.4.1`.

## What changed

| | v2 | v3 |
|---|---|---|
| Skill count | 6 (Kata, Kaizen, Kaikaku, Hansei, Shiken, Intent) | 2 (Improve, Probe) |
| Vocabulary | Japanese (Kata/Kaizen/Kaikaku/Hansei/Shiken/Kiroku/Genba/Mura/Muri/Muda) | English |
| Trail files | 3 (TRAIL/, GENBA.md, SCORECARD.md) | 1 (`trail/log.md`) |
| Self-scoring rubric | Tier 1 (10 weighted dimensions, ~600 lines) | Removed |
| Scripts | 5 PowerShell files (~66 KB) | 2 Python files |
| Skill text | ~3000 lines across 6 SKILL.md files | ~250 lines across 2 |

## Why

The v2 suite scored itself well on a rubric it wrote, in a vocabulary that obscured what each skill did, using three trail files that frequently disagreed because three parsers had to stay in sync. The framework's own first principle — Commander's Intent: *define the destination, never prescribe the route* — was being violated by the scaffolding meant to enforce it.

Concretely:

1. **6 skills was 4 too many.** Kaizen, Kaikaku, and Hansei were variations of "examine and change something." Kata orchestrated skills that wouldn't need orchestrating if there were fewer of them. Intent was a single-sentence rule wrapped in a skill folder.
2. **Japanese names were a tax.** They signalled "this is a system" but obscured behaviour. New observers had to translate before reasoning. The Toyota lineage is real but the names were decoration.
3. **Three trail files violated their own principle.** Multi-resolution evidence is a Principle 2 requirement, but it's a property of the *content*, not of file count. Three files meant three parsers, three drift surfaces, three places for run rows to disagree. v2 spent multiple runs fixing parser drift.
4. **Tier 1 self-scoring never escaped "who made up these metrics?"** Rubric v3 anchored to PDCA/CMMI was an improvement, but it was still a number an agent assigned to itself. Tier 2 (pass/fail on external outcomes — convergence) was the only measurement that survived scrutiny.
5. **PowerShell bound the suite to one OS.** A few markdown conventions plus one small Python script carry the same load and run anywhere.

## What v3 keeps unchanged

- **The three principles.** Commander's Intent + Observable Autonomy + Convergence Is Silence. No edits.
- **The convergence protocol.** Multi-family, multi-session, delta=0. This is the real research contribution. Most "AI evaluation" hand-waves on stopping conditions; this one is operational.
- **External targeting as a rule.** Hard-won lesson from 90+ self-targeting runs in v2.

## What v3 removes

- The Tier 1 rubric (10 dimensions, weighted scores, level descriptors).
- All Japanese vocabulary in skill files, scripts, and trail conventions. The repo name `kata` is kept as a historical codename — like a project name — but nothing inside uses it.
- Kata, Kaikaku, Hansei, Intent as separate skills. Their substance is folded into Improve.
- Kiroku as a separate skill. It's now `tools/record.py` — a utility, not a skill.
- The `metrics.ps1`, `verify-suite.ps1`, `insert80.ps1`, `insert_genba.ps1`, `swap.ps1` scripts.
- `SCORECARD.md`, `GENBA.md`, `METRICS_HISTORY.md`, `INTEGRITY.json`, `STANDARDS.md`, `PATTERNS.md`, `DESIGN_BACKLOG.md` from the live tree (kept under `archive/v2/`).

## What v3 adds

Nothing structural. Two skills, one trail format, two scripts, one principles document copied from the manifesto repo. Less, not more.

## How to roll back

`git checkout v2.4.1`. The v2 tree is preserved both as a tag and under `archive/v2/`.

## Convergence status at the time of redesign

- Manifesto: 3/3 evaluators converged at 9.0 (1 fresh + 2 verified independent).
- Skills suite v2: 2/3 evaluators converged at 8.83 (Gemini 3.1 Pro, Grok Code Fast 1). One run pending.

The redesign deliberately invalidates the in-progress v2 chain. The artifact has changed materially; convergence must restart from scratch on v3. This is the protocol working as designed (Principle 3, condition 2: "if a run produces a diff to the artifact, the convergence counter resets to zero").

## Authorship of this redesign

Designed and executed by an LLM agent (Claude) in dialogue with the maintainer, on April 23, 2026. The reasoning that produced this redesign is preserved in `trail/log.md` under the entry dated 2026-04-23 ("v3 redesign"). This document is the digest; that entry is the indexed evidence; the original conversation is the full evidence (held by the maintainer).

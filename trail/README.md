# Audit Trail: kata skills

This directory is the audit trail for autonomous agent operations on this repository. It is the reference implementation of the [Observable Autonomy](../PRINCIPLES.md) principle's resolution requirement.

## The three resolutions

The manifesto's `PRINCIPLES.md` requires that evidence exist at three resolutions simultaneously: **Digest** (60-second view), **Indexed** (decisions navigable in bounded time), and **Full** (complete reasoning, ground truth). Three resolutions, not three files — the indexed layer lives *within* the full layer.

| Resolution | Where it lives | Time budget | Answers |
|---|---|---|---|
| **Digest** | `log.md` | 30–60 seconds | Where is this going? What just happened? |
| **Indexed** | `[!DECISION]`, `[!REALIZATION]`, `[!REVERSAL]` markers inside `sessions/*.md` | minutes | What was decided, when, and why? |
| **Full** | `sessions/*.md` | hours | The complete reasoning exchange — prompts, responses, dead ends, reversals |

### Reading the indexed layer

The indexed layer is recovered by grep, not by a separate file. From the repo root:

```sh
grep -rn '\[!DECISION\]\|\[!REALIZATION\]\|\[!REVERSAL\]' trail/sessions/
```

This returns every load-bearing turning point across all sessions, with file and line, in seconds. The markers are inserted by the operating agent during the session, in context, so the rationale lives one paragraph away rather than in a separately-curated index that can drift.

## The two skills

The kata suite has two skills:

- **improve** — examine a target, find what most needs changing, change it (or argue for radical redesign), verify, and record. Combines incremental refinement, structural rethinking, and reflection on the loop itself in a single skill.
- **probe** — construct a novelty probe (Shiken-style) that distinguishes genuine situated reasoning from pattern-matching against a checklist.

Earlier versions of this suite (v1, v2) had more skills with Japanese vocabulary (Kata, Kaizen, Kaikaku, Hansei, Mura, Muri, Muda, Intent). v3 collapsed them into the two above. The full history is preserved in `archive/v2/` and the v2 tags.

## Fidelity levels

Session transcripts are marked with a fidelity level:

- **verbatim** — exported directly from the chat platform. Exact dialogue preserved. Highest trust.
- **reconstructed** — recreated from agent context/memory. Captures decisions, reasoning, and outcomes accurately, but exact wording may differ. Key facts and decisions are reliable; phrasing and sequence may be approximate.
- **mixed** — contains both verbatim tool outputs and reconstructed narrative.

## Integrity

All summaries and digests are self-authored by the agent that produced the work. For independent confirmation, cross-verify claims against the session transcripts (full resolution) and the actual code changes (`git log`).
# Audit Trail: skills

This directory contains the complete audit trail for autonomous agent operations on this project.

## How to read this

| Time budget | Start here |
|---|---|
| 30 seconds | **SUMMARY.md** - direction, recent decisions, current state |
| 15 minutes | **INDEX.md** - every decision with rationale, linked to the session that produced it |
| Full review | **sessions/** - complete reasoning transcripts |

## What each file is

- **SUMMARY.md** - Executive digest. Updated after each session. Answers: *where is this headed?*
- **INDEX.md** - Decision index (auto-generated). Every `[!DECISION]` from sessions, extracted with rationale. Answers: *what was decided and why?*
- **sessions/** - Full session transcripts. The ground truth. Answers: *what was the complete reasoning?*

## Glossary

- **Kata** - The orchestration skill that runs an improvement cycle: diagnose the target, select a methodology, execute, record, persist.
- **Kaizen** - Incremental improvement. The target's structure is sound; specific things need fixing.
- **Kaikaku** - Radical redesign. The target's structure cannot reach its goals through incremental changes.
- **Hansei** - Reflection on the improvement loop itself, not the target.
## Fidelity levels

Session transcripts are marked with a fidelity level:

- **verbatim** - Exported directly from the chat platform. Exact dialogue preserved. Highest trust.
- **reconstructed** - Recreated from agent context/memory. Captures decisions, reasoning, and outcomes accurately, but exact wording may differ from the original exchange. Typical accuracy: key facts and decisions are reliable; phrasing and sequence may be approximate.
- **mixed** - Contains both verbatim tool outputs and reconstructed narrative.

## Integrity

All summaries and digests in this trail are self-authored by the agent that produced the work. Cross-verify claims against the session transcripts and the actual code changes (git log) for independent confirmation.
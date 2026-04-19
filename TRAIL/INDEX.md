# Decision Index

*Last updated: 2026-04-19 - rebuild-planning session*

---

## Decisions

### DEC-001: Kiroku tooling is PowerShell scripts + agent protocol
- **Date:** 2026-04-19
- **Session:** [rebuild-planning](sessions/2026-04-19-rebuild-planning.md)
- **Fidelity:** reconstructed
- **Participants:** human, Claude Opus 4.6
- **Decision:** Kiroku tooling implemented as PowerShell scripts (kiroku-start, kiroku-index, kiroku-close, kiroku-validate) plus an agent protocol document. Not a VS Code extension or Python package.
- **Rationale:** Target environment is Windows with PowerShell 5.1. No dependency installation. The agent IS the primary tool - scripts support it with mechanical validation.
- **Alternatives considered:** VS Code extension (violates INTENT constraint), Python CLI (requires venv), manual-only convention (proven insufficient)
- **Status:** active

### DEC-002: Split measurement into Tier 1 (input) and Tier 2 (output)
- **Date:** 2026-04-19
- **Session:** [rebuild-planning](sessions/2026-04-19-rebuild-planning.md)
- **Fidelity:** reconstructed
- **Participants:** human, Claude Opus 4.6
- **Decision:** Measurement framework has two tiers. Tier 1 (Skill Quality) = existing Rubric v3 (8 dimensions, 1-10 scale). Tier 2 (Work Quality) = 5 new output dimensions (Transferability, External Target Efficacy, Reasoning vs. Compliance, Observer Satisfaction, Time to Value) with pass/fail scoring.
- **Rationale:** The current rubric measures whether skills are well-written (input), not whether they produce good work (output). You need both. 46 runs proved input metrics can plateau without validating output.
- **Alternatives considered:** Replace rubric v3 entirely (loses calibration data), keep v3 only (perpetuates blind spot), merge into one rubric (conflates different measurement targets)
- **Status:** active

### DEC-003: Pass/fail for Tier 2 scoring
- **Date:** 2026-04-19
- **Session:** [rebuild-planning](sessions/2026-04-19-rebuild-planning.md)
- **Fidelity:** reconstructed
- **Participants:** human, Claude Opus 4.6
- **Decision:** Tier 2 dimensions scored as Pass/Fail/Untested, not on a 1-10 scale.
- **Rationale:** The v1/v2 rubric proved that 1-10 scales invite ad-hoc scoring that converges to the ceiling without meaning. Pass/fail forces binary evidence.
- **Alternatives considered:** 1-10 scale (same failure mode), 3-point scale (marginal improvement, adds complexity)
- **Status:** active

### DEC-004: System determines what skills exist
- **Date:** 2026-04-19
- **Session:** [rebuild-planning](sessions/2026-04-19-rebuild-planning.md)
- **Fidelity:** reconstructed
- **Participants:** human, Claude Opus 4.6
- **Decision:** The rebuild starts from PRINCIPLES.md and PROBLEM.md. The system determines the number and nature of skills. The human does not prescribe which skills exist.
- **Rationale:** The current 8-skill structure was invented by one model in one session. The structure should be derived from what the Principles require.
- **Alternatives considered:** Prescribe same 8 skills with cleaner content (perpetuates structure problem), let human specify which skills (violates Commander's Intent)
- **Status:** active

### DEC-005: No human edits to skill files
- **Date:** 2026-04-19
- **Session:** [rebuild-planning](sessions/2026-04-19-rebuild-planning.md)
- **Fidelity:** reconstructed
- **Participants:** human, Claude Opus 4.6
- **Decision:** All skill file changes go through Intents. No direct human editing. Makes audit trail complete and enforces Commander's Intent.
- **Rationale:** Traceable origin for every change (Intent -> reasoning -> artifact). Also enforces P1: human defines what, system determines how.
- **Alternatives considered:** Human edits with trail documentation (partial audit trail), collaborative editing (muddies P1 test)
- **Status:** active

### DEC-006: Existing v1.34.0 is reference, not template
- **Date:** 2026-04-19
- **Session:** [rebuild-planning](sessions/2026-04-19-rebuild-planning.md)
- **Fidelity:** reconstructed
- **Participants:** human, Claude Opus 4.6
- **Decision:** The system may read v1.34.0 skills to understand what was tried, but must not copy-paste. Each skill freshly reasoned from Principles.
- **Rationale:** The goal is to test whether fresh reasoning from Principles produces the same, different, or better skills than 44 runs of iterative patching.
- **Alternatives considered:** Start from v1.34.0 and simplify (incremental, not rebuild), ignore v1.34.0 entirely (loses lessons learned)
- **Status:** active

# Trail Summary

*Last updated: 2026-04-19 - rebuild-planning session*
*This summary is self-authored. Cross-verify with the session transcripts for independent confirmation.*

---

**One-line status:** Skills rebuild planned - Kiroku tooling built, measurement framework designed (Tier 1 + Tier 2), rebuild Intent written. Execution pending.

## Direction

The TPS Skill Suite is being rebuilt from scratch. The system will derive skills from PRINCIPLES.md and PROBLEM.md alone, without copying v1.34.0. Measurement now has two tiers: Skill Quality (existing rubric v3) and Work Quality (5 new output dimensions). The rebuild is the first real test of both Kiroku and the measurement framework.

## Recent Decisions

1. **Kiroku tooling is PowerShell scripts + agent protocol** - not a VS Code extension or Python package. Agent captures reasoning; scripts handle mechanical validation.
2. **Measurement split into Tier 1 (input) and Tier 2 (output)** - Rubric v3 stays as Tier 1. New Tier 2 measures whether work done under the skills actually succeeds. Pass/fail scoring.
3. **System determines what skills exist, not the human** - number and nature of skills derived from Principles, not prescribed.
4. **No human edits to skill files** - all changes through Intents, making the audit trail complete.

## Integrity Notes

- This trail was started mid-session (Kiroku tooling didn't exist at the start). Part 1 decisions are reconstructed.
- The session file uses `reconstructed` fidelity throughout.
- The measurement framework is untested - it was designed in the same session as the rebuild planning.

## Observer Guide

| Time Budget | Read |
|-------------|------|
| 5 seconds | One-line status above |
| 2 minutes | This full summary |
| 30 minutes | [Decision Index](INDEX.md) + session transcript |
| Unlimited | [Session transcripts](sessions/) chronologically |

# Changelog

## v3.0.1 — 2026-04-24

### Changed
- trail/README.md corrected to reflect the v3 trail structure and remove the v2 splice tail.

## v3.0.0 — 2026-04-23 (branch `v3-redesign`)

Radical redesign. See [REDESIGN.md](./REDESIGN.md) for the full rationale.

### Changed
- Skill count reduced from 6 to 2: `improve` (Kaizen + Kaikaku + Hansei + Intent + Kata) and `probe` (Shiken).
- Vocabulary changed from Japanese/TPS terms to plain English. Repo name `kata` retained as a historical codename.
- Trail unified from three files (`TRAIL/`, `GENBA.md`, `SCORECARD.md`) into one append-only `trail/log.md`.
- Scripts ported from PowerShell (~66 KB across 5 files) to Python 3 (`tools/verify.py` + `tools/record.py`, no third-party deps).
- `PRINCIPLES.md` is now an explicit copy of the canonical version in the [autonomous-agent-principles](https://github.com/ntholm86/autonomous-agent-principles) repo.

### Removed
- The Tier 1 self-scoring rubric (10 weighted dimensions). Convergence (Principle 3) is now the only honest measure of done.
- `SCORECARD.md`, `METRICS_HISTORY.md`, `INTEGRITY.json`, `STANDARDS.md`, `PATTERNS.md`, `DESIGN_BACKLOG.md` from the live tree (preserved under `archive/v2/`).
- The `kata`, `kaizen`, `kaikaku`, `hansei`, `shiken`, `intent`, `kiroku` skill directories from the live tree (preserved under `archive/v2/`).
- All `.ps1` scripts from the live tree (preserved under `archive/v2/`).

### Convergence chain
- v2's in-progress 2/3 chain (Gemini 3.1 Pro + Grok Code Fast 1 at score 8.83) is invalidated by Principle 3, condition 2 (material change resets the counter). v3 must converge from zero on its own merits.

---

For history prior to v3, see [archive/v2/CHANGELOG.md](./archive/v2/CHANGELOG.md).

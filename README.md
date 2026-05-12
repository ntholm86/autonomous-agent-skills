# Principles of Earned Autonomy - Skills Suite

A discipline framework for autonomous iterative work — works on any target, not just code.

Compatible with Claude (skills / Agent SDK), GitHub Copilot (custom skills), and any LLM agent that can read markdown and append to a file.

It is built on two core claims:

1. **It works on any target an LLM can reason about.**
   The target can be code, prose, strategy, design, a psychological profile, medical diagnosis, or an organizational structure, anything.
2. **It uses structural controls to reduce post-hoc rationalization.**
   The trail is append-only, reversals are recorded, and convergence requires agreement from independent evaluators.

## Evidence

The suite has run the IMPROVE skill on itself for more than 200 iterations, including two full rewrites.

Convergence was declared only after three independent evaluators from different model families (Claude, GPT, Gemini) each found no further actionable change.
Evidence is recorded in [.trail/log.md](./.trail/log.md).

Self-application is a validity check for the framework: if the loop cannot improve itself, claims about improving external targets are weak.

Relevant research:
- Jie Huang et al., [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798) (ICLR 2024)
- "LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction." — Jie Huang et al., [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798) (ICLR 2024)

## Skills

| Skill | Problem | Function |
| :--- | :--- | :--- |
| [Intent](./intent/SKILL.md) | Literal execution can miss user intent | Interprets the request goal before action and makes that interpretation visible |
| [Vision](./vision/SKILL.md) | Long-term goals are often implicit or incomplete | Surfaces and confirms the operator's intended direction |
| [Trail](./trail/SKILL.md) | Audit trail of all autonomous decisions made and why | Appends decisions, predictions, reversals, and outcomes to an evidence log |
| [Improve](./improve/SKILL.md) | Iterative improvement loop | Runs a structured improvement loop with prediction, action, and reflection |
| [Retrospect](./retrospect/SKILL.md) | Retrospect on previous improvement runs | Reviews the full trail and produces cross-iteration claims |
| [Probe](./probe/SKILL.md) | Measure Autonomous Reasoning Fidelity | Runs paired novelty tests to evaluate reasoning fidelity |

Conceptual foundations include [Commander's Intent](https://en.wikipedia.org/wiki/Commander%27s_intent), [Coaching Kata](https://www.amazon.com/Toyota-Kata-Managing-Improvement-Adaptiveness/dp/0071635238), and the [Socratic Method](https://plato.stanford.edu/entries/socrates/).

- "No-one knows exactly what they want." — David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/)
- "Without data, you're just another person with an opinion." — W. Edwards Deming
- "Invest in the design of the system every day." — Kent Beck, [Extreme Programming Explained](https://www.amazon.com/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)
- "Life can only be understood backwards; but it must be lived forwards." — Soren Kierkegaard, Journals (1843)

## Memory Model

The suite maintains persistent context across sessions through trail files:
- `.trail/log.md`
- `.trail/vision.md`
- `.trail/retrospect.md`

This context is shared across model swaps and reused by each skill.

At run start, skills read existing trail context before acting. Operators can inspect the same records.

## Workflow

1. Run [Vision](./vision/SKILL.md) to confirm the target and goal.
2. Run [Improve](./improve/SKILL.md) for one or more iterations.
3. Run [Retrospect](./retrospect/SKILL.md) when you need cross-iteration analysis.
4. Run [Probe](./probe/SKILL.md) when you need reasoning-quality validation.

## Quickstart

1. Install with one command:
   - macOS / Linux: `bash install.sh`
   - Windows: `pwsh install.ps1`
2. Or copy these skill folders manually into `.copilot/skills/`: `intent/`, `vision/`, `improve/`, `trail/`, `retrospect/`, `probe/`. See [INSTALLING.md](./INSTALLING.md) for details.
3. Optional: install the pre-commit hook in your target repo to enforce trail discipline structurally — `bash tools/install-hooks.sh` or `pwsh tools/install-hooks.ps1`.
4. If the target is not a repository, keep `.trail/` artifacts next to the target material.
5. Start with a verifiable task and review the resulting trail entry.

## Known Limitation

Trail records stated reasoning. Stated reasoning can still differ from actual internal decision process.

Relevant research:
- Miles Turpin et al., [Language Models Don't Always Say What They Think](https://arxiv.org/abs/2305.04388) (NeurIPS 2023)
- Yanda Chen et al., [Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410) (2025)
- "CoT explanations can be plausible yet misleading, which risks increasing our trust in LLMs without guaranteeing their safety." — Miles Turpin et al., [Language Models Don't Always Say What They Think](https://arxiv.org/abs/2305.04388) (NeurIPS 2023)
- "CoT monitoring is a promising way of noticing undesired behaviors during training and evaluations, but that it is not sufficient to rule them out." — Yanda Chen et al., [Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410) (2025)

Mitigations implemented by this suite:
1. **Pre-commit prediction (Improve, Trail):** The agent records a falsifiable prediction before acting.
2. **Outcome anchoring (Retrospect):** Later reviews compare outcomes to prior predictions.
3. **Reversal density checks (Trail, Retrospect):** Uniform success patterns are treated as potential rationalization.
4. **Adversarial audit lens (Retrospect):** Cross-entry inconsistencies are explicitly checked.
5. **Writer/decider separation (Improve, Trail):** High-fidelity mode separates change execution from final trail writing.

## Reference

- Convergence criterion: three independent model families report no further actionable change.
- Principles source: [Autonomous Agent Principles](https://github.com/ntholm86/autonomous-agent-principles).

## Citation and License

MIT License.
[CITATION.cff](./CITATION.cff) | Zenodo: [10.5281/zenodo.19842994](https://doi.org/10.5281/zenodo.19842994)

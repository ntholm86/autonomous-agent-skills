# Principles of Earned Autonomy - Skills Suite

AI agents forget everything between sessions — and many things within a session. No memory of what was tried. No memory of why a decision was made. No memory of where you were heading. Forgets what it already created.

These five skills fix that. Together they form a **Memory Model** — a persistent layer of context that survives session resets and model swaps. The agent reads it before every run. You read it to stay in control.

These are the skills I use daily as a software engineer to safely delegate complex goals to AI agents. When an agent runs without constraints, it creates massive technical debt. These skills force it to stay on track, double-check its assumptions, and leave a clear record of why it made each change.

Implementation repo for [Principles of Earned Autonomy](https://github.com/ntholm86/principles-of-earned-autonomy). The manifesto defines the principles; this suite enacts them.

Compatible with Claude (skills / Agent SDK), GitHub Copilot (custom skills), and any LLM agent that can read markdown and append to a file.

## The Suite Improved Itself 200+ iterations

The suite ran on itself **200+ times**. Along the way, it autonomously decided to rewrite itself from scratch. Twice.

Convergence was declared only when **three independent evaluators from distinct model families** (Claude, Gpt, Gemini) each ran the loop and found nothing left to change. The full evidence trail is in [.trail/audit-trail.md](./.trail/audit-trail.md).

> "LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction."
>
> — Jie Huang et al., [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798) (ICLR 2024)

If the loop can't improve itself, the claim that it improves anything else is empty. It can.

## The Skills

| Skill | Problem | Solution |
| :--- | :--- | :--- |
| **[Intent](./intent/SKILL.md)** | The agent did what you said — not what you meant | Force the agent to understand the intent behind your prompt |
| **[Vision](./vision/SKILL.md)** | The agent doesn't know your vision — because it's in your head | The agent will read your mind, uncover your vision and produce vision.md that other skills will use |
| **[Trail](./trail/SKILL.md)** | The work is unauditable | Logs every autonomous decision made by the agent and the reason behind it |
| **[Improve](./improve/SKILL.md)** | The agent makes superficial, undisciplined edits | A structured, iterative improvement loop that reflects and learns before acting |
| **[Retrospect](./retrospect/SKILL.md)** | The agent can't see its own arc | Self-evaluates the progress of all iterations and determines what is next |

### Validation skill

**[Probe](./probe/SKILL.md)** — included for research and validation use. Constructs a "spot the difference" test to measure whether the agent is genuinely reasoning or pattern-matching. Used to validate [Autonomous Reasoning Fidelity](https://github.com/ntholm86/principles-of-earned-autonomy/blob/main/PRINCIPLES.md#autonomous-reasoning-fidelity-operational-definition) — not a skill you'd run in daily development.

## The Memory Model

Each skill externalizes what normally only lives inside a single model session — the goal, the destination, the decisions, the arc. Together they form a persistent memory layer that no model reset can erase.

The files (`.trail/audit-trail.md`, `.trail/vision.md`, `.trail/retrospect.md`) provide the literal storage, but the interaction of the skills with those files creates **contextual awareness**.

Memory alone is just retrieval; awareness is orientation. Because `Retrospect` reads the arc, `Vision` uncovers the destination, and `Intent` aligns the goal, the suite uses that memory to understand where it is and where it is going.

When you swap from Claude to Gpt to Gemini, the next model picks up this exact orientation. That accumulation is what makes the suite get smarter over time.

## Why These Skills Exist

### #1: INTENT — The agent did what you wrote, not what you meant

**Problem:** The agent did literally exactly what you wrote — word-by-word — not what you actually meant.
**Solution:** Intent forces the agent to explicitly state its interpretation of your task *before* executing anything. It acts as an early warning system for misaligned assumptions.

*Rooted in [Commander's Intent](https://en.wikipedia.org/wiki/Commander%27s_intent) (U.S. Army doctrine) · [Coaching Kata](https://www.amazon.com/Toyota-Kata-Managing-Improvement-Adaptiveness/dp/0071635238) (Mike Rother, Toyota Kata) · [Socratic Method](https://plato.stanford.edu/entries/socrates/) (Stanford Encyclopedia of Philosophy)*

### #2: VISION — The agent drifted over time

**Problem:** During a long autonomous run, the agent loses the plot, fixing minor issues rather than addressing the core architectural problem.
**Solution:** Vision surfaces the agent's implicit assumptions about your destination, letting you course-correct early. Retrospect steps back, analyzes the full history of the work, and re-orients the loop.

> "No-one knows exactly what they want."
>
> — David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/)

### #3: TRAIL — The work is unauditable

**Problem:** The agent modified dozens of files. You have no idea why it chose one implementation over another, making it impossible to confidently take ownership of the work.
**Solution:** Trail enforces observable autonomy. Every decision, rationale, and discarded alternative is appended to a readable `.trail/audit-trail.md`. If it isn't logged, it didn't happen.

> "Without data, you're just another person with an opinion."
>
> — W. Edwards Deming

### #4: IMPROVE — The agent makes superficial edits

**Problem:** The agent edits what's easy. Typos, whitespace, obvious renames. The real problems stay untouched.
**Solution:** Improve is the workhorse of this suite. Point it at any target and run it repeatedly. Each iteration: it examines what's there, challenges its own first instinct, makes exactly one high-leverage change, and reflects. It reads the full memory suite before every run — so it never wastes an iteration on something already tried.

> "Invest in the design of the system every day."
>
> — Kent Beck, [Extreme Programming Explained](https://www.amazon.com/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)

### #5: RETROSPECT — The agent can't see its own arc

**Problem:** After 50 iterations, the agent has been diligently improving — but nobody stepped back to ask whether those 50 iterations were solving the right problem. Each step looked locally optimal. The overall arc drifted.
**Solution:** Retrospect reads the entire trail history as a single document and forms arc-level claims: what is the target becoming, where has the loop's attention been, and is that where the real weight lies? It surfaces what no individual iteration would reveal.

> "Life can only be understood backwards; but it must be lived forwards."
>
> — Søren Kierkegaard, Journals (1843)

## Workflow

1. **Set the target:** Run `vision` first to determine the destination before starting work.
2. **Execute:** Run `improve` for as many iterations as needed until you reach a plateau.
3. **Reflect:** Run `retrospect` to evaluate the entire loop history and reflect on progress.

## Quickstart

1. Install with one command:
   - macOS / Linux: `bash install.sh`
   - Windows: `pwsh install.ps1`
2. Or copy these skill folders manually into `.copilot/skills/`: `intent/`, `vision/`, `improve/`, `trail/`, `retrospect/`, `probe/`. See [INSTALLING.md](./INSTALLING.md) for details.
3. Optional: install the pre-commit hook in your target repo to enforce trail discipline structurally — `bash tools/install-hooks.sh` or `pwsh tools/install-hooks.ps1`.
4. If the target is not a repository, keep `.trail/` artifacts next to the target material.
5. Start with a verifiable task and review the resulting trail entry.

## Known Limitation: Stated Reasoning ≠ True Reasoning

Trail logs what the agent *says* it decided. Research shows this is not always the same as what actually drove the decision.

> "CoT explanations can be plausible yet misleading, which risks increasing our trust in LLMs without guaranteeing their safety."
>
> — Miles Turpin et al., [Language Models Don't Always Say What They Think](https://arxiv.org/abs/2305.04388) (NeurIPS 2023)

> "CoT monitoring is a promising way of noticing undesired behaviors during training and evaluations, but that it is not sufficient to rule them out."
>
> — Yanda Chen et al., [Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410) (2025)

**How this suite mitigates it:** To prevent LLMs from generating post-hoc justifications to fit decisions already made, the suite enforces structural constraints:
1. **Pre-commit prediction (Improve, Trail):** The agent must record a falsifiable prediction of what a change will and will not achieve *before* acting or observing the actual outcome.
2. **Outcome anchoring (Retrospect):** Subsequent arc-reads systematically evaluate actual outcomes against those prior predictions to expose localized confabulation.
3. **Reversal density (Trail, Retrospect):** A uniform, unbroken trail of "successes" is actively flagged as suspect rationalization. True reasoning leaves a trail of reversals, dead ends, and tested predictions.
4. **Adversarial audit (Retrospect):** A dedicated lens to actively hunt for outcome mismatch and logical discontinuities across the trail history.
5. **Separating writer and decider (Improve, Trail):** In maximum-trust sequences (High-Fidelity Mode), the agent making the change is procedurally forbidden from writing the final trail entry, handing off to a second independent evaluator.

Together, these force the agent to lock its reasoning *before* acquiring evidence, and introduce explicit adversarial structures to break the post-hoc rationalization loop.

## Reference

- Convergence criterion: three independent model families report no further actionable change.
- Principles source: [Principles of Earned Autonomy](https://github.com/ntholm86/principles-of-earned-autonomy).

## Citation and License

MIT License.
[CITATION.cff](./CITATION.cff) | Zenodo: [10.5281/zenodo.19842994](https://doi.org/10.5281/zenodo.19842994)

# Autonomous Development Skills Suite

Five skills that make your AI agent show its work, so you stay in control of your codebase.

These are the skills I use daily as software engineer to safely delegate complex goals to AI agents.

When an AI agent runs without constraints, it creates massive technical debt. These skills force the AI to stay on track, double-check its assumptions, and leave a clear record of why it made each change.

## The Suite Improved Itself 200+ iterations

The suite ran on itself **200+ times**. Along the way, the agent decided — autonomously — to re-write itself from scratch. Twice.

Convergence was declared only when **three independent evaluators from distinct model families** (Claude, Gpt, Gemini) each ran the loop and found nothing left to change. The full evidence trail is in [.trail/log.md](./.trail/log.md). Earlier iterations are preserved in [archive/v2/TRAIL/](./archive/v2/TRAIL/) (v2) and [archive/v2/v1_archive/](./archive/v2/v1_archive/) (v1).

> "LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction."
>
> — Jie Huang et al., [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798) (ICLR 2024)

If the loop can't improve itself, the claim that it improves anything else is empty. It can.

## The Skills

| Skill 🛠️ | Problem ⚠️ | Solution ✅ |
| :--- | :--- | :--- |
| 🛡️ **[Intent](./intent/SKILL.md)** | The agent did literally what you wrote - not what you meant | Force the agent to understand the intent behind your prompt |
| 👁️ **[Vision](./vision/SKILL.md)** | The agent doesn't know your vision - because it's in your head | The agent will read your mind, uncover your vision and produce vision.md and other skills will use it |
| 📜 **[Trail](./trail/SKILL.md)** | The work is unauditable | Logs every autonomous decision made by the agent and the reason behind it |
| ⚔️ **[Improve](./improve/SKILL.md)** | The agent makes superficial, undisciplined edits | A structured, iterative improvement loop that reflects and learns before acting |
| 🗺️ **[Retrospect](./retrospect/SKILL.md)** | The agent can't see its own arc | Self-evaluates the progress of all iterations and determines what is next |

### Validation skill

🧪 **[Probe](./probe/SKILL.md)** — included for research and validation use. Constructs a "spot the difference" test to measure whether the agent is genuinely reasoning or pattern-matching. Used to validate [Autonomous Reasoning Fidelity](https://github.com/ntholm86/autonomous-agent-principles/blob/v1.0.0/PRINCIPLES.md#autonomous-reasoning-fidelity-operational-definition) — not a skill you'd run in daily development.

## Meta-learning - The Skills Get Smarter Over Time

The more you use it, the better it knows your codebase. Every run logs to `.trail/log.md`; the agent reads it before acting. The log is both audit-trail and memory.

## Why These Skills Exist

### #1: INTENT - The agent did literally exactly what you wrote - not what you meant

**The Failure Mode:** You describe a goal. The agent did litterally exactly what you said - but not what you actually meant.
**The Solution:** Intent forces the agent to explicitly state its interpretation of your task *before* executing anything. It acts as an early warning system for misaligned assumptions.

*Rooted in [Commander's Intent](https://en.wikipedia.org/wiki/Commander%27s_intent) (U.S. Army doctrine) · [Coaching Kata](https://www.amazon.com/Toyota-Kata-Managing-Improvement-Adaptiveness/dp/0071635238) (Mike Rother, Toyota Kata) · [Socratic Method](https://plato.stanford.edu/entries/socrates/) (Stanford Encyclopedia of Philosophy)*

### #2: VISION - The Agent Drifted Over Time

**The Failure Mode:** During a long autonomous run, the agent loses the plot, fixing minor issues rather than addressing the core architectural problem.
**The Solution:** Vision surfaces the agent's implicit assumptions about your destination, letting you course-correct early. Retrospect steps back, analyzes the full history of the work, and re-orients the loop.

> "No-one knows exactly what they want."
>
> — David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/)

### #3: TRAIL - The Work is Unauditable

**The Failure Mode:** The agent modified dozens of files. You have no idea why it chose one implementation over another, making it impossible to confidently take ownership of the code.
**The Solution:** Trail enforces observable autonomy. Every decision, rationale, and discarded alternative is appended to a readable .trail/log.md. If it isn't logged, it didn't happen.

> "Without data, you're just another person with an opinion."
>
> — W. Edwards Deming

### #4: IMPROVE - The Agent Makes Superficial Edits

**The Failure Mode:** Agents spot superficial syntax issues but ignore deep, structural waste. They fire off scattered changes without a cohesive strategy.
**The Solution:** Improve runs a disciplined, iterative improvement loop (examine-challenge-decide-act-reflect). It explicitly questions the code and learns from the context, ensuring exactly one high-leverage change is made per iteration.

> "Invest in the design of the system every day."
>
> — Kent Beck, [Extreme Programming Explained](https://www.amazon.com/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)

### #5: RETROSPECT - The Agent Can't See Its Own Arc

**The Failure Mode:** After 50 iterations, the agent has been diligently improving — but nobody stepped back to ask whether those 50 iterations were solving the right problem. Each step looked locally optimal. The overall arc drifted.
**The Solution:** Retrospect reads the entire trail history as a single document and forms arc-level claims: what is the target becoming, where has the loop's attention been, and is that where the real weight lies? It surfaces what no individual iteration would reveal.

> "Life can only be understood backwards; but it must be lived forwards."
>
> — Søren Kierkegaard, Journals (1843)

## The Workflow

1. **Set the Target:** Run `vision` first to determine the destination before starting work.
2. **Execute:** Run `improve` for X amount of iterations until you reach a plateau.
3. **Reflect:** Run `retrospect` to evaluate the entire loop history and reflect on progress.

## Quickstart

1. Read [INSTALLING.md](./INSTALLING.md) for configuration instructions.
2. Copy the skill directories (intent/, vision/, improve/, trail/, retrospect/) into your repository's .copilot/skills/ folder.
3. Start assigning verifiable, autonomous tasks.

## Reference
- **Convergence:** The agent loop converges only when 3 independent models (e.g., Claude, Gpt, Gemini) confirm no further improvements exist.
- **Principles:** Built on the [Autonomous Agent Principles](https://github.com/ntholm86/autonomous-agent-principles).

## Known Limitation: Stated Reasoning ≠ True Reasoning

Trail logs what the agent *says* it decided. Research shows this is not always the same as what actually drove the decision.

> "CoT explanations can be plausible yet misleading, which risks increasing our trust in LLMs without guaranteeing their safety."
>
> — Miles Turpin et al., [Language Models Don't Always Say What They Think](https://arxiv.org/abs/2305.04388) (NeurIPS 2023)

> "CoT monitoring is a promising way of noticing undesired behaviors during training and evaluations, but that it is not sufficient to rule them out."
>
> — Yanda Chen et al., [Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410) (2025)

**How this suite partially addresses it:** Trail gives you the agent's *stated* rationale — the same thing a human collaborator provides, and equally worth having. The convergence requirement (three independent model families must agree) reduces the risk that all three are rationalizing in the same unfaithful direction. Probe validates behavioral evidence independently of stated reasoning. No single mechanism is sufficient; the suite uses all three in combination.

## Citation & License
MIT License.
[CITATION.cff](./CITATION.cff) | Zenodo: [10.5281/zenodo.19842994](https://doi.org/10.5281/zenodo.19842994)

# Autonomous Development Skills Suite

Six skills that make your AI agent show its work, so you stay in control of your codebase.

When an AI agent runs without constraints, it creates massive technical debt. These skills force the AI to stay on track, double-check its assumptions, and leave a clear record of why it made each change.

These are the exact skills I use daily as software engineer to safely delegate complex goals to AI agents.

## Proof: The Suite Improved Itself 200+ iteration

The suite ran on itself **200+ times**. Along the way, the agent decided — autonomously — to re-write itsself from scratch. Twice.

Convergence was declared only when **three independent evaluators from distinct model families** (Claude, Gpt, Gemini) each ran the loop and found nothing left to change. The full evidence trail is in [.trail/log.md](./.trail/log.md). Earlier iterations are preserved in [archive/v2/TRAIL/](./archive/v2/TRAIL/) (v2) and [archive/v2/v1_archive/](./archive/v2/v1_archive/) (v1).

If the loop can't improve itself, the claim that it improves anything else is empty. It can.

## The Skills Arsenal

| Skill 🛠️ | Problem ⚠️ | Solution ✅ |
| :--- | :--- | :--- |
| 🛡️ **[Intent](./intent/SKILL.md)** | The agent did literally what you wrote - not what you meant | Force the agent to understand the intent behind your prompt |
| 👁️ **[Vision](./vision/SKILL.md)** | The agent doesn't know your vision - because it's in your head | The agent will read your mind, uncover your vision and produce vision.md and other skills will use it |
| ⚔️ **[Improve](./improve/SKILL.md)** | The agent makes superficial, undisciplined edits | A structured, iterative improvement loop that reflects and learns before acting |
| 📜 **[Trail](./trail/SKILL.md)** | The Work is Unauditable | Logs every autonomous decision made by the agent and the reason behind it. |
| 🗺️ **[Retrospect](./retrospect/SKILL.md)**| The agent drifts over time | Self-evaluates the progress of all iterations and determines what is next |
| 🧪 **[Probe](./probe/SKILL.md)** | Measure Autonomous Reasoning Fidelity | Forces a "spot the difference" test to prove the agent is actually reasoning |

## Why These Skills Exist

### #1: The Agent Built the Wrong Thing

**The Failure Mode:** You describe a goal. The agent immediately writes code. Ten minutes later, you review a pull request that completely missed the mark.
**The Solution:** Intent forces the agent to explicitly state its interpretation of your task *before* executing anything. It acts as an early warning system for misaligned assumptions.

### #2: The Agent Drifted Over Time

**The Failure Mode:** During a long autonomous run, the agent loses the plot, fixing minor issues rather than addressing the core architectural problem.
**The Solution:** Vision surfaces the agent's implicit assumptions about your destination, letting you course-correct early. Retrospect steps back, analyzes the full history of the work, and re-orients the loop.

### #3: The Agent is Parroting, Not Thinking

**The Failure Mode:** You suspect the agent isn't actually thinking—it's just regurgitating standard boilerplate or blindly complying without grasping your specific constraints.
**The Solution:** Probe forces the agent into a "spot the difference" test. It injects two scenarios that look identical but have a hidden, critical difference. If the agent gives the same generic answer to both, it fails the test.

### #4: The Work is Unauditable

**The Failure Mode:** The agent modified dozens of files. You have no idea why it chose one implementation over another, making it impossible to confidently take ownership of the code.
**The Solution:** Trail enforces observable autonomy. Every decision, rationale, and discarded alternative is appended to a readable .trail/log.md. If it isn't logged, it didn't happen.

### #5: The Agent Makes Superficial Edits

**The Failure Mode:** Agents spot superficial syntax issues but ignore deep, structural waste. They fire off scattered changes without a cohesive strategy.
**The Solution:** Improve runs a disciplined, iterative improvement loop (examine-challenge-decide-act-reflect). It explicitly questions the code and learns from the context, ensuring exactly one high-leverage change is made per iteration.

## The Workflow

*Note: All skills automatically invoke `trail` in the background to capture evidence. The trail accumulates knowledge across iterations — every decision, rationale, and reflection — so the agent becomes increasingly aware of the target, the vision, and everything that has already been done.*

1. **Set the Target:** Run `vision` first to determine the destination before starting work.
2. **Execute:** Run `improve` for X amount of iterations until you reach a plateau.
3. **Reflect:** Run `retrospect` to evaluate the entire loop history and reflect on progress.
4. **Validate:** Run `probe` to prove Autonomous Reasoning Fidelity (ARF) and ensure the agent lives up to the principles.

## Quickstart

1. Read [INSTALLING.md](./INSTALLING.md) for configuration instructions.
2. Copy the skill directories (intent/, vision/, improve/, probe/, trail/, retrospect/) into your repository's .copilot/skills/ folder.
3. Start assigning verifiable, autonomous tasks.

## Reference
- **Convergence:** The agent loop converges only when 3 independent models (e.g., Claude, Gpt, Gemini) confirm no further improvements exist.
- **Principles:** Built on the [Autonomous Agent Principles](https://github.com/ntholm86/autonomous-agent-principles).

## Citation & License
MIT License.
[CITATION.cff](./CITATION.cff) | Zenodo: [10.5281/zenodo.19842994](https://doi.org/10.5281/zenodo.19842994)

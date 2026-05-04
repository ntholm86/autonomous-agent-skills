# Autonomous Development Skills Suite

Six skills that make your AI agent show its work, so you stay in control of your codebase.

When an AI agent runs without constraints, it creates massive technical debt. These skills force the AI to stay on track, double-check its assumptions, and leave a clear record of why it made each change.

These are the exact skills I use daily as software engineer to safely delegate complex goals to AI agents.

## Why These Skills Exist

### #1: The Agent Built the Wrong Thing

**The Failure Mode:** You describe a goal. The agent immediately writes code. Ten minutes later, you review a pull request that completely missed the mark.
**The Solution:** Intent forces the agent to explicitly state its interpretation of your task *before* executing anything. It acts as an early warning system for misaligned assumptions.

### #2: The Agent Drifted Over Time

**The Failure Mode:** During a long autonomous run, the agent loses the plot, fixing minor issues rather than addressing the core architectural problem.
**The Solution:** Vision surfaces the agent's implicit assumptions about your destination, letting you course-correct early. Retrospect steps back, analyzes the full history of the work, and re-orients the loop.

### #3: The Agent is Pattern-Matching, Not Thinking

**The Failure Mode:** You suspect the agent is just copy-pasting standard boilerplate instead of reasoning about your specific constraints.
**The Solution:** Probe injects two structurally similar but materially different scenarios. If the agent gives the exact same response, you immediately know it's failing to reason autonomously.

### #4: The Work is Unauditable

**The Failure Mode:** The agent modified dozens of files. You have no idea why it chose one implementation over another, making it impossible to confidently take ownership of the code.
**The Solution:** Trail enforces observable autonomy. Every decision, rationale, and discarded alternative is appended to a readable .trail/log.md. If it isn't logged, it didn't happen.

### #5: The Loop Lacks Discipline

**The Failure Mode:** Agents spot superficial syntax issues but ignore deep, structural waste.
**The Solution:** Improve runs a rigorous, TPS-inspired cycle (examine-challenge-decide-act-reflect). It explicitly looks for waste and inconsistency, ensuring exactly one high-leverage change is made per iteration.

## The Skills Arsenal

| Skill 🛠️ | Reads 📖 | Writes ✍️ | Core Mechanic ⚙️ | Tactical Advantage 🎯 |
| :--- | :--- | :--- | :--- | :--- |
| 🛡️ **[Intent](./intent/SKILL.md)** | `vision.md`, `retrospect.md`, `log.md` | — | Forces interpretation *before* execution. | Intercepts misaligned assumptions at step zero. |
| 👁️ **[Vision](./vision/SKILL.md)** | `log.md`, `retrospect.md` | `vision.md` (with user) | Surfaces implicit guesses about the destination. | Prevents the loop from drifting over long sessions. |
| ⚔️ **[Improve](./improve/SKILL.md)** | `vision.md`, `retrospect.md`, `log.md` | *(Target codebase)* | Runs a TPS-inspired examine/challenge/decide loop. | Ensures exactly *one* high-leverage change per iteration. |
| 🧪 **[Probe](./probe/SKILL.md)** | *(Target codebase)* | — | Injects structurally similar but distinct scenarios. | Catches shallow pattern-matching and tests reasoning fidelity. |
| 📜 **[Trail](./trail/SKILL.md)** | — | `log.md`, `sessions/` | Logs every decision, discarded alternative, and rationale. | Makes every autonomous action fully auditable and observable. |
| 🗺️ **[Retrospect](./retrospect/SKILL.md)**| `vision.md`, `log.md`, `sessions/` | `retrospect.md` | Steps back to read the full history and re-orients the loop. | Breaks local-maxima loops and connects back to the strategy. |

## Quickstart

1. Read [INSTALLING.md](./INSTALLING.md) for configuration instructions.
2. Copy the skill directories (intent/, improve/, probe/, 	rail/, 
retrospect/, and vision/) into your repository's .copilot/skills/ folder.
3. Start assigning verifiable, autonomous tasks.

## Reference
- **Convergence:** The agent loop converges only when 3 independent models (e.g., Claude, Grok, Gemini) confirm no further improvements exist.
- **Principles:** Built on the [Autonomous Agent Principles](https://github.com/ntholm86/autonomous-agent-principles).
- **Verify:** Run python verify.py to validate your evidence trail.

## Citation & License
MIT License.
[CITATION.cff](./CITATION.cff) | Zenodo: [10.5281/zenodo.19842994](https://doi.org/10.5281/zenodo.19842994)

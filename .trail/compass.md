# Compass — autonomous-agent-skills

_Last updated: 2026-05-01 (seeded from operator conversation, not a formal Retrospect run)_

---

## What this suite is for

The skills suite is the **reasoning layer** for autonomous software agents. Evo (`c:\git\evo`) is the **execution harness** — it implements, merges, releases, and maintains a proof trail. They are two halves of one system that have not yet been connected.

The skills as they currently exist are behavioral specs for a conversational agent. The next form they need to take — callable phases with defined inputs, outputs, and contracts that evo can invoke — has not been built yet. That work does not begin until the reasoning layer has proven itself.

## Current claims

1. **The skills are a prototype of the right protocol, not the finished protocol.** Retrospect, compass, trail, intent — the concepts are correct. The format is optimized for human-readable conversational use, not machine-orchestrated pipeline invocation. Both forms can coexist; neither currently exists in the machine-callable form.

2. **The loop is a text-consistency engine, not a behavioral improvement engine.** Runs 55–66 were predominantly documentation propagation following structural changes. The two genuinely behavioral changes (Retrospect skill, compass.md mechanism) both originated from operator observation, not the loop finding them autonomously. This is not a failure — it is a structural limit of a file-reading loop.

3. **The missing reasoning gaps in evo are three and specific:**
   - ANALYZE lacks an Intent phase — it identifies what is measurable, not what matters for this codebase's purpose
   - PROPOSE lacks vision-alignment — proposals are evaluated against metrics, not against what the codebase is trying to become
   - EVOLVE has diagnostic memory (lessons journal) but not strategic memory — it records "this fix worked" not "this is what this codebase is becoming"

4. **The path to full autonomy is front-loaded reasoning, not more gates.** One human interaction — before the pipeline runs — to confirm: "this is what I believe this codebase is for, these are the constraints." After that, no gates. More autonomy requires better reasoning, not tighter controls.

5. **Retrospect has not yet been run on an external target.** Its value is an open empirical question. The constraint stands: no evo integration until the reasoning layer demonstrates it works on real codebases with Retrospect in the loop.

## What the next runs should test

- Run Retrospect against an external codebase (not self-targeting) and check whether the arc-claims it produces are distinct from what Improve step 6b would have found
- Run Probe against Intent's core claim: "the agent is acting on what the operator means, not what they typed"
- These are behavioral tests, not documentation fixes — they require running the skills, not reading them

## Constraints that must hold before evo integration

1. Retrospect has demonstrated it produces arc-claims an Improve run would not have found
2. The compass mechanism has proven it orients subsequent runs more accurately than cold-starting from the trail
3. The skills have been run on at least one non-trivial external codebase by an operator who was not the author

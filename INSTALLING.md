# Installing the skills

## How VS Code Copilot discovers skills

Copilot looks for skills at exactly **one level deep** under `.copilot/skills/`:

```
.copilot/
  skills/
    intent/
      SKILL.md     ← found
    improve/
      SKILL.md     ← found
    some-folder/
      subfolder/
        SKILL.md   ← NOT found (too deep)
```

**This means: do not drop the entire repo folder into your skills directory.** That adds an extra nesting level and Copilot finds nothing. Copy the individual skill folders directly.

---

## Minimum install (one skill)

To get started with just the Intent skill:

```
your-repo/
  .copilot/
    skills/
      intent/
        SKILL.md
```

No sibling files required. Each skill is self-contained.

---

## Full install (all five skills)

```
your-repo/
  .copilot/
    skills/
      intent/
        SKILL.md
      vision/
        SKILL.md
      improve/
        SKILL.md
      trail/
        SKILL.md
      retrospect/
        SKILL.md
```

That's it. The skills are plain markdown files — no scripts, no dependencies, nothing to install or execute.

Optionally copy `PRINCIPLES.md` next to the skill folders — the skills reference it but work fully without it (the principles are inlined in each SKILL.md).

### Also included: Probe (research and validation)

`probe/SKILL.md` is included in the repo but is **not part of the daily workflow**. It measures [Autonomous Reasoning Fidelity](https://github.com/ntholm86/autonomous-agent-principles/blob/v1.0.0/PRINCIPLES.md#autonomous-reasoning-fidelity-operational-definition) — useful if you want to validate that the agent is genuinely reasoning and not pattern-matching. Copy it in if you need it; leave it out if you don't.

---

## What each skill needs at runtime

All skills work with only their own `SKILL.md`. No required sibling files.

| Skill | Optional sibling files |
|---|---|
| **intent** | `PRINCIPLES.md` (cross-reference link; content is inlined) |
| **vision** | `PRINCIPLES.md` |
| **improve** | `PRINCIPLES.md` |
| **trail** | nothing — creates `.trail/log.md` on first use |
| **retrospect** | nothing — reads `.trail/log.md` written by trail |

---

## The trail — where it lives

The trail is **per project**. The AI writes it automatically — no scripts required.

When the trail skill runs for the first time on a project it creates:
`<repo-root>/.trail/log.md` (the append-only evidence log)

Commit `.trail/log.md` after each session. That's the full workflow.

---

## For maintainers: experiment tooling

*This section is for people running the improvement loop on the skills repo itself. If you're adopting the skills for your own project, you don't need any of this.*

`tools/record.py` and `verify.py` exist to support the experiment that produced this suite — running the loop 200+ times and proving the trail is intact.

**`tools/record.py`** — generates a human-readable `history.md` from the trail log. Run from the repo root:
```
python tools/record.py history --write    # writes .trail/history.md
python tools/record.py summary            # prints the latest entry
```
It only writes into `.trail/`. No network calls.

**`verify.py`** — read-only integrity check. Confirms the trail is well-formed, dates are in order, required files exist, and referenced session files are present. Writes nothing.
```
python verify.py
```
Exit 0 = all checks pass, exit 1 = something is wrong.

---

## Using a skill

Once installed, type the skill name prefixed with `/` in the Copilot chat to invoke it directly. Or just describe your task — skills whose `description` field matches will be suggested automatically.

Available slash commands: `/intent`, `/vision`, `/improve`, `/trail`, `/retrospect`, `/probe`

Example:
```
/improve review the checkout module for waste and overburden
```

---

## Updating

Skills are just markdown files. Replace the SKILL.md files with newer versions to update. The trail log is separate from the skills and does not change when you update.

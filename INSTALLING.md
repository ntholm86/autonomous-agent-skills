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

## Full install (all six skills)

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
      probe/
        SKILL.md
      trail/
        SKILL.md
      retrospect/
        SKILL.md
      tools/
        record.py
```

Optionally copy `PRINCIPLES.md` next to the skill folders — the skills reference it but work fully without it (the principles are inlined in each SKILL.md).

---

## What each skill needs at runtime

All skills work with only their own `SKILL.md`. No required sibling files.

| Skill | Optional sibling files |
|---|---|
| **intent** | `PRINCIPLES.md` (cross-reference link; content is inlined) |
| **vision** | `PRINCIPLES.md` |
| **improve** | `PRINCIPLES.md` |
| **probe** | `PRINCIPLES.md` |
| **trail** | nothing — creates `.trail/log.md` on first use |
| **retrospect** | nothing — reads `.trail/log.md` written by trail |

---

## The trail — where it lives and how to use it

The trail is **per project**. It lives in the root of the repo being worked on — not inside `.copilot/skills/`.

When the trail skill runs for the first time on a project it creates a single file:
`<repo-root>/.trail/log.md` (the append-only evidence log).

Nothing else gets installed into the target repo. `record.py` stays in the skills install and is invoked from there — it writes into the current working directory by default, or whatever `$TRAIL_ROOT` points to.

After every run that adds an entry to `log.md`, regenerate the readable summary **from the target repo root**:
```
python <skills>/tools/record.py history --write    # writes .trail/history.md
```
Replace `<skills>` with your skills install path.
- Windows example: `C:\Users\you\.copilot\skills\tools\record.py`
- macOS/Linux example: `~/.copilot/skills/tools/record.py`

For ad-hoc viewing:
```
python <skills>/tools/record.py history    # timeline to stdout
python <skills>/tools/record.py summary    # digest of the most recent run
```

Commit `.trail/log.md` and `.trail/history.md`. **Do not** commit `record.py` to the target repo — it lives in the skills install only.

### What the scripts actually do

**`tools/record.py`** — writes trail entries into `.trail/log.md` in the current working directory (or `$TRAIL_ROOT` if set). It never reads or modifies anything outside that folder. No network calls. Three subcommands: `new` (append a blank entry stub), `summary` (print the latest entry), `history` (print a timeline of all runs).

**`verify.py`** — read-only audit. It reads `.trail/log.md` and checks formatting, date ordering, required metadata fields, and that all referenced session files exist. It writes nothing and makes no network calls. Exit 0 = all checks pass, exit 1 = something is wrong.

### Multi-iteration runs

Each iteration is a separate trail entry. The commit sequence is:

```
iteration 1 → append trail entry → record.py history --write → commit
iteration 2 → append trail entry → record.py history --write → commit
...
```

Append and commit **before** starting the next iteration. A partial run (agent crashes, user stops at iteration 4 of 10) must produce partial trail — batch writing at the end of all iterations defeats the purpose.

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

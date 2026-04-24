# Observable Loops — v0.1 Draft

> **Status:** draft, not adopted. This document is a design proposal recorded in [trail/log.md](./trail/log.md) under `2026-04-23 — observable-loops-decision`. No skill, runtime, or packaging in this repository conforms to it yet.

## What this is

**Observable Loops** is a packaging and execution contract for autonomous agent loops that satisfies the three principles in [PRINCIPLES.md](./PRINCIPLES.md). It is built as an addendum on top of the [Ralph Loops specification](https://ralphloops.io/specification/), which it accepts as the inner transport layer.

The relationship is strictly additive:

- A valid Observable Loop is a valid Ralph Loop.
- A valid Ralph Loop is **not** automatically a valid Observable Loop.
- A Ralph-conformant runtime can execute an Observable Loop's instructions, but it cannot produce a convergence-eligible result, because the trail and evaluator-independence requirements live in the addendum.

The differentiator is not features. It is that **the trail is mandatory and the runtime enforces it.** A loop that finishes without a verifiable trail entry is, by definition, not an Observable Loop run.

## Why Ralph is not enough

Ralph defines a portable directory format with a required `RALPH.md` entrypoint, optional frontmatter (`agent` / `commands` / `args`), path resolution rules, and three compatibility classes. That solves real problems the suite currently has:

- **Third-party reproducibility.** Today, verifying a convergence claim from this suite requires cloning the repo, reading the README, and trusting that the reproducer ran the same entrypoint the maintainer ran. Ralph collapses that to "point your runtime at this directory."
- **Clean-room cross-family evaluation.** Independent evaluation across model families (a hard requirement of Principle 3) is currently a manual port per family. A standard package format is the precondition for cheap cross-family evaluation.
- **CI as evaluator.** A scheduled job that runs the loop nightly with a different agent each week is the diverse-evaluator-over-time pattern Principle 3 wants. Ralph-style packaging makes that ergonomic.

But Ralph's execution contract is silent on:

- Whether the loop emits any trail at all.
- Whether agent-authored summaries are distinguished from verbatim tool output.
- Who declares the loop done, and on what evidence.
- Whether the same evaluator may declare convergence by re-running itself.

A loop that runs silently is exactly what Principle 2 forbids. A loop whose stopping condition is set by the loop's own author is exactly what Principle 3 forbids. Adopting Ralph neat would publish this suite in a format whose baseline contradicts its claims.

## The three rings

```
+--------------------------------------------------+
|  Ring 3 — Convergence layer (this addendum)      |
|  Evaluator-family declaration, fresh-session     |
|  contract, convergence-readable trail.           |
|                                                  |
|  +--------------------------------------------+  |
|  |  Ring 2 — Observability layer (this addendum)|
|  |  Mandatory trail, fidelity marks, integrity  |
|  |  check after every iteration.                |
|  |                                              |
|  |  +----------------------------------------+  |
|  |  |  Ring 1 — Ralph (substrate, accepted    |
|  |  |  as-is)                                  |
|  |  |  RALPH.md, frontmatter, path resolution, |
|  |  |  package-as-directory portability.       |
|  |  +----------------------------------------+  |
|  +--------------------------------------------+  |
+--------------------------------------------------+
```

A package may conform to Ring 1 alone (a plain Ralph Loop). Conformance to Ring 2 requires Ring 1. Conformance to Ring 3 requires Rings 1 and 2. Convergence claims are only valid at Ring 3.

## Ring 1 — Ralph (substrate)

Accepted from [the Ralph Loops specification](https://ralphloops.io/specification/) v0.1 without modification. Summarised here only for self-containment:

- `RALPH.md` is the required entrypoint.
- The package root is the directory containing `RALPH.md`.
- Optional frontmatter has exactly three fields: `agent`, `commands`, `args`.
- Bundled files are referenced relative to the package root.
- Compatibility classes: Reader, Executor, Publisher.

If Ralph evolves, this addendum tracks the latest spec version it was reconciled against in its own version history.

## Ring 2 — Observability layer

A package conforms to Ring 2 if and only if all of the following hold.

### 2.1 Required files

In addition to `RALPH.md`, the package MUST contain:

- `trail/log.md` — append-only markdown trail in the format defined by [trail/README.md](./trail/README.md).
- `tools/verify.py` (or any executable named in `RALPH.md` frontmatter under a reserved key `observable.verify`) — a mechanical integrity check that exits non-zero if the trail or required files are malformed.

The trail format is the v3 trail format already used by this suite; it is not redefined here.

### 2.2 Frontmatter contract

The `RALPH.md` frontmatter MUST include a reserved namespace `observable:` with at least:

```yaml
observable:
  trail: trail/log.md           # path, relative to package root
  verify: tools/verify.py       # path or shell command
  fidelity_marking: required    # required | optional — required for Ring 2
```

A runtime that does not understand the `observable:` namespace MUST refuse to claim Ring 2 execution. It MAY still execute the loop as a Ring 1 Ralph package; the trail will simply not be enforced and no convergence claim is producible.

### 2.3 Runtime obligations

A Ring 2 conformant runtime MUST:

1. Locate and parse `observable.trail` and `observable.verify` before invoking the agent.
2. After every loop iteration that touches files, append at least one entry to the trail. An iteration that produces no trail entry is a runtime failure, not a successful no-op.
3. Distinguish verbatim tool output from agent-authored prose in the trail. The mechanism is unspecified (surrounding fences, metadata fields, separate sections); the *distinction* is mandatory.
4. Run the configured `observable.verify` after each iteration. A non-zero exit halts the loop. A halted loop's failure must itself be recorded in the trail before the runtime exits.
5. Identify the agent in each entry by provider and (where observable) tool-call ID prefix. "Some LLM" is not a conformant identification.

### 2.4 Failure modes that violate Ring 2

- A loop that completes with no trail entries.
- A trail entry that conflates summary and verbatim output.
- A successful run reported by a runtime whose `observable.verify` was never invoked.
- An entry whose `agent` field is unspecified or model-family-ambiguous.

## Ring 3 — Convergence layer

A *run* conforms to Ring 3 if and only if it conforms to Ring 2 **and** all of the following hold.

### 3.1 Evaluator-family declaration

Each trail entry MUST declare the evaluator family in a structured form sufficient to determine whether two evaluators are independent. The minimum is provider + model-family identifier (e.g. `anthropic/claude-3.x`, `google/gemini-2.x`, `openai/gpt-5.x`). Different versions of the same model family count as the same family.

### 3.2 Fresh-session contract

A run that claims to advance the convergence chain MUST begin in a session with no inherited context from prior runs. The runtime is responsible for guaranteeing this; the package SHOULD document how the runtime should achieve it (new conversation, new container, no shared cache).

### 3.3 Convergence chain readable from the trail

The convergence chain MUST be derivable from `trail/log.md` alone, without consulting an external counter. The derivation rule is the one already published in [trail/README.md](./trail/README.md): the chain length is the number of consecutive most-recent entries whose `outcome` records no material change to the artifact and whose `agent` field names a distinct evaluator family from the entry before it. Any entry recording a change resets the chain to zero.

### 3.4 Re-derivation requirement

At least one entry in any claimed convergence chain MUST record that the evaluator re-derived the measurement scheme from the artifact rather than inheriting it. Convergence on re-derivation validates the scheme; divergence is itself a finding.

### 3.5 What Ring 3 does not require

- A specific scoring rubric. Convergence is the absence of actionable findings, not a score.
- A specific runtime. Any runtime that meets the obligations above qualifies.
- Synchronous evaluation. Distributed-over-time chains are valid; the runtime requirement is fresh-session-per-run, not single-machine.

## Reference implementation pointers (non-normative)

The current v3 suite already implements Rings 2 and 3 informally:

- [trail/log.md](./trail/log.md) implements the trail format that Ring 2.1 requires.
- [tools/verify.py](./tools/verify.py) implements the integrity gate Ring 2.3.4 calls for.
- The convergence-from-trail derivation rule in [trail/README.md](./trail/README.md) is the rule Ring 3.3 normalises.

What is missing to make the suite *itself* a conforming Observable Loop:

- A `RALPH.md` per skill (or one at repo root) declaring the `observable:` frontmatter namespace.
- A reference runtime (a thin wrapper around an LLM CLI) that honours the Ring 2 obligations.
- A demonstration: the same Observable Loop executed against the same target by three runtimes hosting three distinct model families, fresh-session each, producing a 3/3 convergence chain in the target's trail.

These are not undertaken by this document. They are tracked as the next concrete steps in the design backlog.

## Versioning and stability

This document is v0.1 draft. Breaking changes are expected before any external party is asked to adopt it. The intent is that v1.0 is published only after at least one conforming runtime exists, at least one Observable Loop has been executed end-to-end on a non-self target, and the suite itself has been ported to the format.

## Relationship to upstream Ralph

The constructive long-term move is to propose an `observable:` field upstream so that observability becomes part of the Ralph spec rather than a sibling addendum. That RFC is not yet drafted. Whether or not the upstream proposal is accepted, this addendum stands: the suite's claims require the layer, and the suite controls its own conformance even if the wider Ralph ecosystem does not adopt the same requirement.

## What this document is not

- It is not a runtime. No code is added by this document.
- It is not a packaging change. No `RALPH.md` files are introduced.
- It is not an improve-skill output. The improve skill examines existing artifacts; it does not invent new subsystems. This is a redesign-track artifact recorded in `trail/log.md` so the reasoning is preserved at the same evidence resolution as any other autonomous run.

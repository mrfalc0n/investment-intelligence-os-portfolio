# AI Toolchain

## TL;DR

This system uses LLMs as architecture, research, and workflow assistants. The toolchain is built around durable repos, explicit contracts, and human review rather than one-off prompts.

## Toolchain Layers

| Layer | Tools / Pattern | Public-Safe Role |
|---|---|---|
| Repo architecture | Codex | Inspect repos, edit docs/code, run checks, and keep workflow changes versioned. |
| Second-opinion review | Claude / Cowork | Challenge framing, critique docs, and pressure-test portfolio storytelling. |
| Runtime orchestration | Hermes | Route work between domain-qualified agents through profile/board boundaries. |
| Knowledge cockpit | Notion | Store review queues, trackers, and status surfaces in structured form. |
| Broker adapters | Read-only API integrations | Reconcile state, never execute by default. |
| Notification layer | Telegram and dashboard summaries | Present review packets and status updates. |

## Broader OS Context

Investment Intelligence OS is one domain inside a broader multi-domain agentic OS. Hermes is the current runtime target for routing work between domain-qualified profiles, while GitHub repos hold source-of-truth docs, contracts, synthetic examples, and implementation code. The investment domain is intentionally isolated from business-development and personal-operations domains because it carries higher financial and privacy risk.

The useful pattern is not "one assistant with lots of access." The useful pattern is a routed system:

```text
human request
-> active runtime router
-> investment lead
-> options or stocks lane
-> risk / reconciliation / review gate
-> human-readable packet
```

That routing model keeps the system legible, auditable, and safer than a broad agent that can blur research, advice, and action.

## Design Bias

- Agents should have job descriptions.
- Runtime state should be inspectable.
- Financial actions need human approval.
- Broker state should be reconciled before advice becomes action-ready.
- Research output should preserve caveats and source quality.
- Risk guards block; they do not negotiate.

## What This Demonstrates

- LLM-assisted systems engineering.
- Agent workflow design.
- Tool-boundary modeling.
- High-risk automation safety posture.

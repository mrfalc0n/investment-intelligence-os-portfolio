# AI Toolchain

## TL;DR

This system uses LLMs as architecture, research, and workflow assistants. The toolchain is built around durable repos, explicit contracts, and human review rather than one-off prompts.

## Toolchain Layers

| Layer | Pattern | Public-Safe Role |
|---|---|---|
| Repo architecture | Codex-style repo inspection and editing | Keep workflows documented, testable, and versioned. |
| Second-opinion review | Claude/Cowork-style critique | Challenge framing and improve documentation. |
| Runtime orchestration | Hermes-style profile/board model | Route work between domain-qualified agents. |
| Knowledge cockpit | Notion-style structured state | Store review queues, trackers, and status surfaces. |
| Broker adapters | Read-only API integrations | Reconcile state, never execute by default. |
| Notification layer | Telegram/dashboard style summaries | Present review packets and status updates. |

## Design Bias

- Agents should have job descriptions.
- Runtime state should be inspectable.
- Financial actions need human approval.
- Broker state should be reconciled before advice becomes action-ready.
- Research output should preserve caveats and source quality.

## What This Demonstrates

- LLM-assisted systems engineering.
- Agent workflow design.
- Tool-boundary modeling.
- High-risk automation safety posture.

# Agent Architecture

## TL;DR

Investment Intelligence OS uses a domain-qualified agent hierarchy. The point is not to create many agents for theater. The point is to separate responsibilities so research, risk, reconciliation, notification, and broker boundaries are visible.

## Top-Level Hierarchy

```text
investment-intelligence-os
├── investment-lead
│
├── options-income-lane
│   ├── options-income-workflow
│   ├── options-scanner
│   ├── options-risk-guard
│   ├── options-reconciler
│   ├── options-cockpit-sync
│   ├── options-notification
│   └── options-audit
│
└── stocks-research-lane
    ├── stocks-research-workflow
    ├── stocks-scanner
    ├── stocks-researcher
    ├── stocks-news-reporter
    ├── holdings-reviewer
    ├── allocation-advisor
    ├── rebalancing-advisor
    ├── portfolio-risk-guard
    ├── stocks-cockpit-sync
    └── stocks-audit
```

## Agent Responsibilities

| Agent | Public-Safe Purpose | Cannot Do |
|---|---|---|
| Investment Lead | Routes requests, checks lane ownership, enforces safety posture. | Scan markets directly or touch brokers. |
| Options Scanner | Produces income candidate packets from configured rules and market data. | Approve trades or submit orders. |
| Options Risk Guard | Blocks candidates that violate liquidity, sizing, DTE, concentration, or account-fit rules. | Override broker state or human approval. |
| Options Reconciler | Compares local lifecycle state against read-only broker truth. | Place, cancel, replace, or modify orders. |
| Options Audit | Records inputs, decisions, blocks, and outputs. | Decide what to trade. |
| Stocks Researcher | Synthesizes thesis-aware research and classifies relevance. | Create trade authority from a single article. |
| Holdings Reviewer | Reviews current positions against thesis health and portfolio role. | Sell or alter holdings. |
| Allocation Advisor | Drafts account-aware allocation ideas. | Convert ideas into executable orders. |
| Rebalancing Advisor | Converts evidence into a manual rebalance plan for review. | Execute the plan. |
| Portfolio Risk Guard | Checks concentration, account-domain fit, stale data, and hard exclusions. | Ignore policy because a signal is exciting. |

## Design Rules

- Agent names should answer "where does this live?"
- Research agents and broker adapters are separate.
- Risk guards block; they do not negotiate.
- Notion/dashboard/cockpit sync is an operating-state layer, not a broker layer.
- Anything external, financial, or account-changing requires explicit human review.

## Why This Matters

Generic agent labels like `scanner`, `researcher`, or `admin` become dangerous when multiple domains exist. Domain-qualified naming and explicit boundaries keep the system readable and safer to operate.

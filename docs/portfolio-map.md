# Portfolio Map

## TL;DR

This public repo is a sanitized portfolio layer over a private Investment OS. It preserves the agent/workflow architecture while excluding account data, broker credentials, real holdings, and actionable trade instructions.

## Public Boundary

| Private Source Area | Public Representation | Why It Matters |
|---|---|---|
| Investment agent hierarchy | Sanitized agent architecture | Shows domain-qualified agent design and routing discipline. |
| Options income workflow | Generic scanner/reconciliation workflow | Shows operational scanning, triage, lifecycle, and review gates. |
| Stock income workflow | Research and rebalance architecture | Shows thesis-aware research, holdings review, and action-queue discipline. |
| Account-domain policy | Generalized taxable/tax-advantaged reasoning | Shows portfolio logic beyond single-account optimization. |
| Broker integrations | Read-only boundary model | Shows safety posture around financial APIs. |
| Notion/dashboard cockpit | Sanitized status model | Shows how workflow state becomes reviewable. |

## Excluded By Design

- Real holdings, watchlists, account balances, P/L totals, or tax lots.
- Broker account IDs, credentials, tokens, API keys, session files, or raw exports.
- Notion database IDs, private URLs, or live workspace schemas.
- Real trade candidates, open orders, close-order prompts, or execution instructions.
- Personal investment thesis details that would expose actual portfolio intent.
- Full private repository history.

## Public Story

The public version demonstrates how to design a governed agentic investment workflow:

1. Define domain-qualified agents.
2. Separate options-income workflows from long-term stock thesis workflows.
3. Keep broker integrations read-only until explicitly promoted.
4. Use synthetic examples for scanner, reconciliation, and research packets.
5. Treat final actions as human-reviewed decisions, not agent outputs.

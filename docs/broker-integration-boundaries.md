# Broker Integration Boundaries

## TL;DR

Broker integrations are treated as high-risk infrastructure. The safe default is read-only reconciliation, not execution.

## Boundary Model

| Capability | Public Architecture Status | Reason |
|---|---|---|
| Read broker balances/positions/orders | Allowed in private system under credential and audit controls. | Needed for reconciliation and stale-state detection. |
| Normalize broker state | Allowed. | Converts broker truth into reviewable workflow state. |
| Compare broker state to local tracker | Allowed. | Finds stale rows, manual trades, closed positions, and mismatches. |
| Preview orders | Separate gated capability. | Must be explicitly promoted and reviewed. |
| Submit/cancel/replace orders | Not included in this public repo. | Financial action requires human approval and private controls. |

## Read-Only Reconciliation

Read-only reconciliation answers:

- What does the broker currently show?
- Which local rows map cleanly to broker positions?
- Which local rows are stale or closed?
- Which broker positions were manually adopted or adjusted?
- Which rows need human review before any next step?

## Forbidden In This Public Repo

- Credentials.
- Account identifiers.
- Live API endpoints tied to a private account.
- Order payloads.
- Submit/cancel/replace code.
- Real positions, balances, tax lots, or P/L.

## What This Demonstrates

- Financial API safety posture.
- Separation of analysis from execution.
- Audit-friendly reconciliation.
- Human approval boundaries for high-risk actions.

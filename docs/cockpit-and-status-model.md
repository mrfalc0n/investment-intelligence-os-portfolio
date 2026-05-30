# Cockpit And Status Model

## TL;DR

The cockpit model turns agent outputs into reviewable state: what changed, what needs attention, what is blocked, and what is safe to do next.

## Cockpit Surfaces

| Surface | Role |
|---|---|
| Holdings review | Summarizes thesis health and relook flags. |
| Research radar | Tracks ideas that are interesting but not action-ready. |
| Options strategy tracker | Tracks options candidate and lifecycle state. |
| Action queue | Holds human-reviewed manual actions, not raw research. |
| Reconciliation summary | Shows broker-vs-local state and blockers. |
| Status feed | Reports workflow freshness, warnings, and next safe action. |

## Status Fields

A public-safe status packet can include:

- System domain.
- Workflow lane.
- Last updated timestamp.
- Runtime posture.
- Approved actions.
- Prohibited actions.
- Current blockers.
- Next safe action.
- Source docs.

## Dashboard Principle

Dashboards should not imply authority. Showing a candidate does not mean "do it." It means "review this with context."

## What This Demonstrates

- Operational state design.
- Human-friendly review surfaces.
- Distinction between signal, recommendation, and approved action.
- Status reporting suitable for orchestration layers.

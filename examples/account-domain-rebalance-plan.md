# Synthetic Account-Domain Rebalance Plan

## TL;DR

This example shows how the system distinguishes total-portfolio correctness from account-domain correctness.

## Scenario

The total portfolio is underweight AI infrastructure, but the taxable account already has enough near-term exposure. The retirement account has room for longer-duration growth exposure.

## Recommendation Packet

| Field | Value |
|---|---|
| Candidate | Synthetic AI Infrastructure Basket |
| Total portfolio fit | Underweight |
| Taxable / accessible fit | Near target |
| Retirement / tax-advantaged fit | Underweight |
| Suggested domain | Retirement / tax-advantaged |
| Action status | Manual review only |

## Reasoning

- The idea fits the total thesis.
- The taxable account should preserve liquidity and avoid unnecessary turnover.
- The retirement account is better aligned with long-duration compounding.
- Domain-aware routing avoids making the total portfolio look right while one account domain becomes overloaded.

## Pre-Execution Checks

- Confirm current cash.
- Confirm allocation targets.
- Confirm price and whole-share math.
- Confirm no pending or duplicate action queue row.
- Confirm human approval.

## Output Classification

```text
portfolio_action_ready: false
manual_review_required: true
broker_execution_allowed: false
```

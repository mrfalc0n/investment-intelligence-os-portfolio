# Synthetic Broker Reconciliation Packet

## TL;DR

This example shows how read-only broker reconciliation can surface state mismatches without exposing real accounts or enabling execution.

## Reconciliation Summary

| Check | Result |
|---|---|
| Broker connection mode | Read-only |
| Broker writes allowed | No |
| Local tracker rows reviewed | 4 |
| Matched positions | 2 |
| Closed positions expected | 1 |
| Manual / broker-adopted variant | 1 |
| Blockers | 0 |

## Synthetic Findings

### Matched Position

Local row and broker state match on underlying, strategy shape, quantity, and open/closed state.

### Closed Position Expected

Local tracker row is marked closed and no matching open broker position exists. This is expected and does not require action.

### Broker-Adopted Variant

The broker shows a manually adjusted variant of a scanner-originated idea. The system should preserve the original scanner row for audit, map broker truth to the adjusted variant, and avoid calling it a generic mismatch.

## Forbidden Actions

- No order submit.
- No order cancel.
- No order replace.
- No broker credential storage.
- No public exposure of account identifiers.

## Review Outcome

```text
safe_to_summarize: true
safe_to_sync_status: true
safe_to_trade: false
```

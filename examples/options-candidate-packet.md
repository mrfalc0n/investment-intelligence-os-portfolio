# Synthetic Options Candidate Packet

## TL;DR

This packet shows how an options-income candidate can be summarized for human review without turning the scanner output into an order ticket.

## Candidate

| Field | Value |
|---|---|
| Synthetic underlying | `SYN-INDEX` |
| Strategy | Defined-risk credit spread |
| Expiration window | Short-duration income window |
| Candidate state | Review required |
| Scanner verdict | Watch / tactical review |
| Broker action | None |

## Scanner Rationale

- Premium met the minimum review threshold.
- Defined risk was calculable.
- Liquidity was acceptable in the synthetic example.
- DTE was inside the configured income-review window.
- Existing exposure check did not show a duplicate synthetic position.

## Risk Guard Notes

- Requires human review before any action.
- Do not submit, preview, cancel, replace, or modify orders.
- Confirm account fit and buying-power impact in the private system.
- Re-check pricing before any manual decision.

## Output Classification

```text
research_packet: true
order_ticket: false
human_approval_required: true
broker_write_allowed: false
```

## Why This Matters

The scanner can produce structure and ranking. It cannot create financial authority.

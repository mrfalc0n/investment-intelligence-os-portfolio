# Account Domain Policy

## TL;DR

The system evaluates investment ideas across account domains, not only total portfolio exposure. A portfolio can look balanced globally while being wrong inside taxable or tax-advantaged accounts.

## Domains

| Domain | Typical Role | Public-Safe Bias |
|---|---|---|
| Total portfolio | Overall thesis and risk map. | Keep the whole system coherent. |
| Taxable / accessible | Liquidity, flexibility, tax awareness, and usable cash-flow posture. | Avoid unnecessary turnover and respect near-term accessibility. |
| Retirement / tax-advantaged | Long-duration compounding and higher-volatility thesis exposure where appropriate. | Use tax sheltering for longer-term growth and turnover-tolerant strategies. |

## Policy Principle

Each account domain should carry the same investment DNA with different weights. The system should not put all of a thesis sleeve in one domain and pretend the portfolio is balanced because the total view looks clean.

## Agent Behavior

Before an idea becomes action-ready, the system should ask:

- Does this improve the total portfolio?
- Does this improve or worsen the target account domain?
- Is the funding source appropriate?
- Is the idea tax-sensitive?
- Does this account already have too much of the same theme?
- Would a different account domain be more appropriate?

## Public Example

```text
Candidate: add to AI infrastructure basket
Total portfolio: underweight
Taxable domain: already near target
Retirement domain: underweight and better fit for long-duration volatility
Verdict: route to retirement-domain rebalance review, not taxable action queue
```

## What This Demonstrates

- Portfolio reasoning beyond single-position recommendations.
- Tax/account-domain awareness without exposing private account details.
- Governance that prevents globally correct but account-wrong recommendations.

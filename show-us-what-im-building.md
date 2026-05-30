# What I Am Building

## TL;DR

I am building a multi-domain agentic operating system. This repository documents the investment intelligence domain: a governed research, scanning, reconciliation, and review system that helps turn messy investment inputs into structured, human-reviewed decision packets.

The operating principle is:

> Research, summarize, reconcile, and prepare. Do not execute.

## The Short Version

The private Investment OS is designed to support investment research and portfolio operations without becoming an autonomous trading bot. It separates the work into explicit agent lanes:

- an investment lead that routes and checks safety posture,
- an options-income lane for scanner, triage, lifecycle, risk, reconciliation, and notifications,
- a stock/ETF research lane for thesis-aware research, holdings review, market intelligence, allocation, and rebalance planning,
- a portfolio policy layer that checks account-domain fit across total, taxable/accesssible, and retirement/tax-advantaged views.

This public repo is the sanitized version: architecture, synthetic examples, and small executable demo code. It does not expose real holdings, accounts, broker credentials, private run commands, or actionable trade instructions.

## Why This Matters

Most AI demos stop at "the model gave me an answer." This system is built around what happens before and after the answer:

- Which agent owns the request?
- What data is safe to read?
- What is synthetic/public versus private/account-specific?
- Did broker read-only state agree with local workflow state?
- Did a risk guard block the path?
- Is the result research-only, review-required, or action-queue eligible?
- What should the human review before acting?

## Production Philosophy

The system assumes consequential domains need stricter design:

- Research agents do not get broker authority.
- Broker adapters start read-only.
- Risk guards block; they do not negotiate.
- Notifications are review packets, not commands.
- Account-domain logic prevents globally plausible but account-wrong recommendations.
- Human approval remains the final boundary.

## What This Public Repo Shows

- The domain-qualified agent architecture.
- The options-income scanner/reconciliation workflow.
- The stock research and rebalance workflow.
- The taxable versus tax-advantaged allocation policy.
- The broker integration safety model.
- Synthetic output packets that look like the private system's shape without leaking private data.
- A small Python demo that scores synthetic candidates and formats review packets.

## What It Does Not Show

- Real account data.
- Real holdings or balances.
- Broker credentials or order endpoints.
- Private Notion workspace details.
- Current trade ideas.
- Personalized financial advice.

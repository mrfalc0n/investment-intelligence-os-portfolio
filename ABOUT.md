# About The System

## TL;DR

Investment Intelligence OS is a personal research and portfolio-operations architecture. It shows how agentic workflows can support investment research, options-income review, account-domain allocation, and broker-state reconciliation without becoming an autonomous trading system.

## Why It Exists

Most personal investing workflows collapse into scattered notes, brokerage screens, watchlists, spreadsheets, and half-remembered thesis fragments. This system was built to make investment reasoning more explicit:

- What is the thesis?
- Which account domain does an action belong in?
- What changed since the last review?
- What is research-only versus action-ready?
- What did the broker actually show?
- What needs human approval before anything happens?

## What It Is

- A repo-backed operating model for investment research and review.
- A multi-agent architecture for separating scanning, research, reconciliation, risk, and reporting.
- A human-in-the-loop workflow system.
- A safety-first design for broker/API integrations.

## What It Is Not

- It is not financial advice.
- It is not a public trading strategy.
- It is not an autonomous execution bot.
- It is not a copy of private account data or private code.
- It should not be used to make investment decisions.

## Design Bias

The useful signal here is not "an AI picked stocks." The useful signal is that the system has boundaries: research agents do research, risk guards block weak paths, broker adapters begin read-only, account-domain rules prevent simplistic allocation advice, and the human remains the final decision-maker.

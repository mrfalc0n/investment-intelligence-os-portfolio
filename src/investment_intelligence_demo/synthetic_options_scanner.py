"""Synthetic options-income scanner demo.

This module intentionally uses fake inputs and simple scoring. It demonstrates
the public architecture pattern only: scan, risk-gate, and prepare review
packets. It does not connect to brokers, market data, accounts, or APIs.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class SyntheticCandidate:
    symbol: str
    strategy: str
    dte: int
    credit: float
    max_loss: float
    liquidity_score: float
    existing_exposure: bool = False
    event_risk: bool = False


@dataclass(frozen=True)
class ReviewPacket:
    symbol: str
    strategy: str
    adjusted_score: float
    verdict: str
    blockers: tuple[str, ...]
    review_notes: tuple[str, ...]
    broker_write_allowed: bool = False


def score_candidate(candidate: SyntheticCandidate) -> float:
    """Return a simple public-demo score from 0 to 10."""
    if candidate.max_loss <= 0:
        return 0.0

    credit_to_risk = min(candidate.credit / candidate.max_loss, 0.35)
    dte_fit = 1.0 if 7 <= candidate.dte <= 45 else 0.55
    liquidity_fit = max(0.0, min(candidate.liquidity_score, 1.0))

    score = (credit_to_risk / 0.35) * 4.0
    score += dte_fit * 3.0
    score += liquidity_fit * 3.0

    if candidate.existing_exposure:
        score -= 1.25
    if candidate.event_risk:
        score -= 1.5

    return round(max(0.0, min(score, 10.0)), 2)


def build_review_packet(candidate: SyntheticCandidate) -> ReviewPacket:
    """Apply review gates and produce a human-readable packet."""
    blockers: list[str] = []
    notes: list[str] = []

    if candidate.max_loss <= 0:
        blockers.append("max loss must be positive")
    if candidate.dte < 3:
        blockers.append("DTE below minimum review window")
    if candidate.liquidity_score < 0.55:
        blockers.append("liquidity below review threshold")
    if candidate.existing_exposure:
        notes.append("existing exposure requires concentration review")
    if candidate.event_risk:
        notes.append("event risk requires human review")

    adjusted_score = score_candidate(candidate)

    if blockers:
        verdict = "Blocked"
    elif adjusted_score >= 8.5:
        verdict = "Review Candidate"
    elif adjusted_score >= 6.5:
        verdict = "Watch"
    else:
        verdict = "Skip"

    notes.append("synthetic demo only; not financial advice")
    notes.append("broker writes disabled")

    return ReviewPacket(
        symbol=candidate.symbol,
        strategy=candidate.strategy,
        adjusted_score=adjusted_score,
        verdict=verdict,
        blockers=tuple(blockers),
        review_notes=tuple(notes),
    )


def scan_candidates(candidates: Iterable[SyntheticCandidate]) -> list[ReviewPacket]:
    """Score a batch of synthetic candidates."""
    packets = [build_review_packet(candidate) for candidate in candidates]
    return sorted(packets, key=lambda packet: packet.adjusted_score, reverse=True)


def demo_candidates() -> list[SyntheticCandidate]:
    """Return fake candidate data for docs/tests."""
    return [
        SyntheticCandidate(
            symbol="SYN-INDEX",
            strategy="defined-risk credit spread",
            dte=21,
            credit=1.15,
            max_loss=4.85,
            liquidity_score=0.82,
        ),
        SyntheticCandidate(
            symbol="SYN-VOL",
            strategy="iron condor",
            dte=35,
            credit=0.95,
            max_loss=9.05,
            liquidity_score=0.48,
        ),
        SyntheticCandidate(
            symbol="SYN-GRID",
            strategy="cash-secured put review",
            dte=12,
            credit=0.8,
            max_loss=10.0,
            liquidity_score=0.73,
            existing_exposure=True,
        ),
    ]


if __name__ == "__main__":
    from investment_intelligence_demo.notification_formatter import format_review_digest

    print(format_review_digest(scan_candidates(demo_candidates())))


"""Format synthetic scanner output into a review packet."""

from __future__ import annotations

from .synthetic_options_scanner import ReviewPacket


def format_review_digest(packets: list[ReviewPacket]) -> str:
    """Return a compact human-review digest.

    The digest deliberately avoids order language. It is a review surface, not
    an execution instruction.
    """
    lines = [
        "Synthetic Options Review",
        "",
        "Research, summarize, reconcile, and prepare. Do not execute.",
        "",
    ]

    for packet in packets:
        lines.append(
            f"- {packet.symbol}: {packet.verdict} "
            f"({packet.strategy}, score {packet.adjusted_score:.2f})"
        )
        if packet.blockers:
            lines.append(f"  blockers: {', '.join(packet.blockers)}")
        if packet.review_notes:
            lines.append(f"  notes: {', '.join(packet.review_notes)}")

    lines.append("")
    lines.append("broker_write_allowed=false")
    return "\n".join(lines)


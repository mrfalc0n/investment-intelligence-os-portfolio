import unittest

from investment_intelligence_demo.notification_formatter import format_review_digest
from investment_intelligence_demo.synthetic_options_scanner import (
    SyntheticCandidate,
    build_review_packet,
    demo_candidates,
    scan_candidates,
)


class SyntheticOptionsScannerTests(unittest.TestCase):
    def test_blocks_low_liquidity(self) -> None:
        packet = build_review_packet(
            SyntheticCandidate(
                symbol="SYN-LOWLIQ",
                strategy="defined-risk credit spread",
                dte=21,
                credit=1.0,
                max_loss=5.0,
                liquidity_score=0.25,
            )
        )

        self.assertEqual(packet.verdict, "Blocked")
        self.assertIn("liquidity below review threshold", packet.blockers)
        self.assertFalse(packet.broker_write_allowed)

    def test_scan_orders_highest_score_first(self) -> None:
        packets = scan_candidates(demo_candidates())

        self.assertGreaterEqual(packets[0].adjusted_score, packets[-1].adjusted_score)
        self.assertTrue(all(packet.broker_write_allowed is False for packet in packets))

    def test_digest_keeps_execution_disabled(self) -> None:
        digest = format_review_digest(scan_candidates(demo_candidates()))

        self.assertIn("Do not execute", digest)
        self.assertIn("broker_write_allowed=false", digest)
        self.assertNotIn("submit order", digest.lower())


if __name__ == "__main__":
    unittest.main()


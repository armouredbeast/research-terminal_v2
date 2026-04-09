from limit_engine.nucleus.order_book import OrderBook


def test_engine():
    lb = OrderBook()

    # Add liquidity
    lb.add_limit_order("A", "sell", 100.10, 10)
    lb.add_limit_order("B", "sell", 100.20, 20)
    lb.add_limit_order("C", "sell", 100.50, 50)

    print(f"Initial Spread: {lb.get_spread():.4f}")

    # Market buy that sweeps the first two levels
    qty, avg_p, slip = lb.execute_market_order("buy", 25)

    print(f"Market Buy 25 units -> Avg Price: {avg_p:.2f}, Slippage: {slip:.4f}")

    bid_d, ask_d = lb.get_volume_at_levels()
    print(f"Remaining Best Ask: {ask_d[0]}")


if __name__ == "__main__":
    test_engine()
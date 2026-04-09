import numpy as np
import time


class TickGenerator:
    """Generates synthetic Level 2 order flow for testing."""

    def __init__(self, start_price=100.0, vol=0.01):
        self.price = start_price
        self.vol = vol

    def generate_order_stream(self, n=100):
        orders = []
        for i in range(n):
            # Random walk for price
            self.price += np.random.normal(0, self.vol)
            side = 'buy' if np.random.random() > 0.5 else 'sell'

            # Distance from mid-price (spread)
            offset = np.random.uniform(0.01, 0.10)
            order_price = round(self.price - offset if side == 'buy' else self.price + offset, 2)
            qty = np.random.randint(1, 100)

            orders.append({
                'order_id': f"mkt_{i}",
                'side': side,
                'price': order_price,
                'qty': qty
            })
        return orders
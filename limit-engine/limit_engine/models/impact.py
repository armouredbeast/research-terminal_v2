import numpy as np

class MarketImpactModel:
    """Estimates the price impact of a large trade."""
    def __init__(self, daily_vol, daily_volume):
        self.sigma = daily_vol
        self.V = daily_volume

    def estimate_slippage(self, order_qty):
        """
        Standard Square Root Law: Impact = Y * sigma * sqrt(Q / V)
        Y is typically around 0.1 to 0.3 for liquid stocks.
        """
        Y = 0.2
        impact_pct = Y * self.sigma * np.sqrt(order_qty / self.V)
        return impact_pct

    def optimal_execution_chunks(self, total_qty, n_chunks):
        """Suggests how to break an order to minimize impact."""
        return [total_qty / n_chunks] * n_chunks
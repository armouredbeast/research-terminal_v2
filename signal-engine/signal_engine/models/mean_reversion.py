import numpy as np


class ZScoreSignal:
    """Generates Buy/Sell signals based on statistical deviation."""

    def __init__(self, window=20):
        self.window = window
        self.prices = []

    def get_signal(self, current_price, smoothed_price):
        self.prices.append(current_price)
        if len(self.prices) < self.window:
            return 0  # Neutral

        # Calculate Rolling Standard Deviation
        rolling_std = np.std(self.prices[-self.window:])

        # Z-Score: (Actual - Smooth) / Std
        z_score = (current_price - smoothed_price) / rolling_std if rolling_std > 0 else 0

        # Signal Logic: Mean Reversion
        if z_score > 2.0: return -1  # Overbought (Sell)
        if z_score < -2.0: return 1  # Oversold (Buy)
        return 0
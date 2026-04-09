import numpy as np


def moving_average(data, window):
    """Simple Moving Average (SMA)."""
    if len(data) < window:
        return np.mean(data)
    return np.mean(data[-window:])


def exponential_moving_average(data, window, last_ema=None):
    """
    Exponential Moving Average (EMA).
    Formula: EMA_t = (Price_t * k) + (EMA_{t-1} * (1 - k))
    """
    k = 2 / (window + 1)
    current_price = data[-1]

    if last_ema is None:
        return np.mean(data[-window:])

    return (current_price * k) + (last_ema * (1 - k))


def relative_strength_index(prices, window=14):
    """
    Standard RSI Implementation.
    Measures the velocity and magnitude of price movements.
    """
    if len(prices) < window + 1:
        return 50.0  # Neutral

    deltas = np.diff(prices)
    seed = deltas[:window]
    up = seed[seed >= 0].sum() / window
    down = -seed[seed < 0].sum() / window

    if down == 0: return 100
    rs = up / down

    # Calculate RSI using the Wilder's smoothing method logic
    for i in range(window, len(deltas)):
        delta = deltas[i]
        if delta > 0:
            up_val = delta
            down_val = 0.0
        else:
            up_val = 0.0
            down_val = -delta

        up = (up * (window - 1) + up_val) / window
        down = (down * (window - 1) + down_val) / window

    rs = up / down
    return 100.0 - (100.0 / (1.0 + rs))


def calculate_volatility(prices, window=20):
    """Calculates rolling historical volatility (Annualized)."""
    if len(prices) < window:
        return 0.0
    returns = np.diff(np.log(prices[-window:]))
    return np.std(returns) * np.sqrt(252)
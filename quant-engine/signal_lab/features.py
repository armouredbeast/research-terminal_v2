import torch
from signal_lab.indicators import moving_average
from signal_lab.statistical import rolling_z_score

def generate_alpha_vector(prices:torch.Tensor):
    """
    Combines Momentum, Mean-Reversion and Volatility into one 'Decision Matrix'
    """
    #1. Momentum signal (MA Crossover)
    ma_fast= moving_average(prices, window = 10)
    ma_slow = moving_average(prices, window=50)
    # align lengths
    momentum = ma_fast[-len(ma_slow):]-ma_slow

    #2. Mean reversion signal (Z-score)
    z = rolling_z_score(prices, window=20)

    return {
        "momentum": momentum,
        "mean_reversion":z
    }
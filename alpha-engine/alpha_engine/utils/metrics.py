import numpy as np

def calculate_sharpe(returns, rf=0.04):
    excess_ret = np.mean(returns) * 252 - rf
    vol = np.std(returns) * np.sqrt(252)
    return excess_ret / vol if vol != 0 else 0

def calculate_max_drawdown(returns):
    cumulative = np.cumsum(returns)
    peak = np.maximum.accumulate(cumulative)
    drawdown = peak - cumulative
    return np.max(drawdown)
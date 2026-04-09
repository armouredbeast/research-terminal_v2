import torch

def vector_backtest(prices: torch.Tensor, signals:torch.Tensor):
    """
    computes equity curve without a single 'for' loop.
    assumes signals are -1, 0 or 1.
    """
    returns = torch.log(prices[1:]/prices[:-1])
    # signal is shifted by 1 because we trade on yesterday's signal
    strategy_returns = signals[:-1]* returns
    equity_curve = torch.exp(torch.cumsum(strategy_returns, dim=0))
    return equity_curve


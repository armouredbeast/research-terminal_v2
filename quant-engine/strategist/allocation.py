import torch

def kelly_criterion(win_prob: torch.Tensor, win_loss_ratio: torch.Tensor):
    """
    Calculate the optimal fraction of capital to risk.
    Formula: f* = p -(1-p)/b
    """
    fraction = win_prob-(1-win_prob)/(win_loss_ratio+1e-10)
    return torch.clamp(fraction,0.0, 1.0) # No leverage for now
def equal_weight(n_assets: int):
    """Simplest allocation: 1/N"""
    return torch.ones(n_assets)/n_assets


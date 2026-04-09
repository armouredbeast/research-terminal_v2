import torch

def rolling_z_score(data: torch.Tensor, window: int)-> torch.Tensor:
    """Calculates how many Standard Deviations the price is from its mean."""
    # Unfold creates sliding windows of the data
    windows = data.unfold(0,window, 1)
    mean = windows.mean(dim=1)
    std = windows.std(dim=1)

    # Align current values with the calculated stats
    current_val = data[window-1:]
    return (current_val - mean)/(std+1e-10)

def calculate_log_returns(prices: torch.Tensor) -> torch.Tensor:
    """Standard input for statistical models."""
    return torch.log(prices[1:]/prices[:-1])

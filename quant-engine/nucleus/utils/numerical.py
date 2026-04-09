import torch
def central_difference(func, x, h= 1e-4):
    """
    standard numerical dervative(Finite difference).
    Equivalent to measuring the slope of a physical part's curve.
    """
    return (func(x+h)-func(x-h))/(2*h)
def calculate_volatility(paths: torch.Tensor, dt:float):
    """
    Realized volatility: Measuring the vibration of the price paths.
    """
    log_returns = torch.log(paths[1:]/paths[:1])
    # Annualized standard deviation of log returns
    return torch.std(log_returns)* torch.sqrt(torch.tensor(1.0/dt))

def calculate_moments(data:torch.Tensor):
    """
    Measures Mean, Variance, Skewness and Kurtosis.
    Tells you if your distribution has 'Fat Tails'(High Kurtosis).
    """
    mean = torch.mean(data)
    std = torch.std(data)
    skew = torch.mean(((data - mean)/std) ** 3)
    kurt = torch.mean(((data - mean)/std) ** 4)
    return {"mean": mean, "std": std, "skew": skew, "kurtosis": kurt}
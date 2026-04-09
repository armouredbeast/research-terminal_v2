import torch
from nucleus.base import BaseSDE
class GBM(BaseSDE):
    """
    Geometric Brownian Motion: the standard for Equities.
    Equation: dSt = mu * St * dt + sigma * St * sWt
    """

    def __init__(self, mu: float, sigma: float):
        self.mu = mu
        self.sigma = sigma

    def drift(self, x: torch.Tensor, t:float) -> torch.Tensor:
        # mu*St
        return self.mu*x
    def diffusion(self,x:torch.Tensor, t:float)-> torch.Tensor:
        # sigma * St
        return self.sigma*x
    def diffusion_prime(self,x:torch.Tensor, t: float) -> torch.Tensor:
        return torch.full_like(x, self.sigma)

class Vasicek(BaseSDE):
    """
    mean-reverting engine: the standard for Interest Rates/Fixed Income.
    Equation: drt = a*(b-rt) * dt + sigma * dwt
    """
    def __init__(self,a:float, b:float, sigma:float):
        self.a = a # Speed of mean reversion
        self.b = b # Long-term mean level
        self.sigma = sigma  # Volatility

    def drift(self,x:torch.Tensor, t:float)-> torch.Tensor:
        # a * (b-rt)
        return self.a * (self.b - x)
    def diffusion(self, x:torch.Tensor, t: float)-> torch.Tensor:
        return torch.full_like(x,self.sigma)
    def diffusion_prime(self,x:torch.Tensor, t: float) -> torch.Tensor:
        # d(sigma) /dx = 0
        return torch.zeros_like(x)


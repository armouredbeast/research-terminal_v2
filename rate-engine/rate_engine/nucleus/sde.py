# the SDE for the rate engine
from abc import ABC, abstractmethod
import torch

class StochasticProcess(ABC):
    @abstractmethod
    def drift(self,x,t):
        pass

    @abstractmethod
    def diffusion(self,x,t):
        pass

class Vasicek(StochasticProcess):
    def __init__(self, a,b,sigma ):
        self.a, self.b, self.sigma = a, b, sigma
    def drift(self,x,t):
        return self.a*(self.b -x)

    def diffusion(self, x, t):
        return torch.full_like(x, self.sigma)
# this is the blueprint, (we would not build piston without knowing the bore),
# in software, Abstract Base Classes(ABCs) is used to define these requirements.


from abc import ABC, abstractmethod
import torch

class BaseSampler(ABC):
    """ Blueprint for all random number generators (RNG)"""
    @abstractmethod
    def get_standard_normal(self, size: tuple) -> torch.Tensor:
        pass
class BaseSDE(ABC):
    """Blueprint for all stochastic differential equations"""
    @abstractmethod
    def drift(self,x:torch.Tensor, t:float)-> torch.Tensor:
        """The mu(x,t) term """
        pass
    @abstractmethod
    def diffusion(self,x:torch.Tensor, t:float)-> torch.Tensor:
        pass
    def diffusion_prime(self, x:torch.Tensor, t:float) -> torch.Tensor:
        """The d_sigma/dx term (Required for Milstein)"""
        return torch.zeros_like(x)

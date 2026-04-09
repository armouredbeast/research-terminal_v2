import torch
import numpy as np
from nucleus.base import BaseSampler

class Sampler(BaseSampler):
    """
    Generates Gaussian nose directly on the GPU/CPU.
    """
    def __init__(self,device: torch.device, seed: int = 61):
        self.device = device
        self.generator = torch.Generator(device = self.device).manual_seed(seed)
    def get_standard_normal(self, size:tuple)->torch.Tensor:
        return torch.randn(size,device=self.device, generator= self.generator)
    def box_muller_transform(self,n_samples=int)-> torch.Tensor:
        #this to convert Uniform to Normals
        #1. Generate two independent uniforms U1, U2 ~ U(0,1)
        u = torch.rand((2, n_samples),device = self.device,generator = self.generator)
        u1,u2=u[0],u[1]
        #2. Apply the Box-Muller Transformation
        #Z = sqrt(-2 ln u1)*cos(2pi u2)
        radius = torch.sqrt(-2.0 * torch.log(u1))
        theta = 2.0 * torch.pi*u2
        return radius * torch.cos(theta)
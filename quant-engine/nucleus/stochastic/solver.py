import torch
from nucleus.base import BaseSDE, BaseSampler
from nucleus.stochastic.dynamics import GBM, Vasicek

class SDESolver:
    """
    This class converts the random noise into asset price paths.
    Supports Euler-Maruyama (Basic) and Milstein (High-Precision)
    """
    def __init__(self, device: torch.device):
        self.device = device
    def simulate(self,sde: float, s0: float, sampler:BaseSampler, t:float, steps: int, n_paths: int, method:str = "milestein")-> torch.Tensor:
        """
        Runs the simulation loop on the GPU/CPU
        """
        dt= t/steps
        dt_sqrt = torch.sqrt(torch.tensor(dt, device= self.device))
        #1. Pre=allocate the path matrix (memory efficiency)
        #shape: [Time steps + 1, Number of paths]
        paths = torch.zeros((steps+1, n_paths), device = self.device)
        paths[0] = s0
        for i in range(1, steps+1):
            current_s = paths[i-1]
            # Generate noise(dw)
            z = sampler.get_standard_normal((n_paths,))
            dw = z * dt_sqrt

            # get dynamics from the sde
            mu = sde.drift(current_s,(i-1)*dt)
            sigma = sde.diffusion(current_s,(i-1)*dt)

            # Euler step (standard)
            paths[i] = current_s + (mu*dt) + (sigma* dw)

            # Milstein correction ( the elite second order term)
            if method == "milstein":
                sigma_p = sde.diffusion_prime(current_s, (i-1)*dt)
                # correction : 0.5 * sigma*sigma_p * (dw^2 - dt)
                correction = 0.5 * sigma * sigma_p * (dw**2 - dt)
                paths[i]+=correction
        return paths
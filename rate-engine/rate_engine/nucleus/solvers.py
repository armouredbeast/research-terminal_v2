#  The vectorized solver framework
import torch

class MonteCarloFramework:
    def __init__(self, sde, device = 'mps'):
        self.sde, self.device = sde, device

    def simulate(self,x0,T,steps, n_paths):
        dt= T/steps
        x = torch.full((n_paths,),x0,device=self.device)
        path_integral= torch.zeros(n_paths,device = self.device)

        for _ in range(steps):
            dw = torch.randn(n_paths, device = self.device)* torch.sqrt(torch.tensor(dt))
            # Use the drift and diffusion from SDE class
            dx = self.sde.drift(x, None)* dt + self.sde.diffusion(x,None)*dw
            # Trapezoidal rule: (x_old + x_new)/2*dt
            x_next = x + dx
            path_integral += 0.5*(x+x_next)*dt
            x = x_next


        return x, path_integral

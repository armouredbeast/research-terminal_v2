import torch
import numpy as np


class MertonJumpDiffusion:
    def __init__(self, mu, sigma, lamb, mu_j, sigma_j, device=None):
        self.device = device if device else torch.device("cpu")
        self.mu = torch.tensor(mu, device=self.device)
        self.sigma = torch.tensor(sigma, device=self.device)
        self.lamb = torch.tensor(lamb, device=self.device)
        self.mu_j = torch.tensor(mu_j, device=self.device)
        self.sigma_j = torch.tensor(sigma_j, device=self.device)

        # kappa = E[Y - 1], where ln(Y) ~ N(mu_j, sigma_j^2)
        # This is the 'Compensator' to keep the process risk-neutral
        self.kappa = torch.exp(self.mu_j + 0.5 * self.sigma_j ** 2) - 1

    def simulate_paths(self, S0, T, steps, n_paths):
        dt = T / steps
        dt_t = torch.tensor(dt, device=self.device)
        paths = torch.ones((steps + 1, n_paths), device=self.device) * S0

        # Corrected Drift: (mu - 0.5 * sigma^2 - lamb * kappa)
        # We must ensure the 'mean' of the jumps is pulled out of the drift
        drift_adj = (self.mu - 0.5 * self.sigma ** 2 - self.lamb * self.kappa) * dt_t
        vol_term = self.sigma * torch.sqrt(dt_t)

        current_S = torch.full((n_paths,), S0, device=self.device, dtype=torch.float32)
        paths[0] = current_S

        for t in range(1, steps + 1):
            # 1. Standard Brownian Motion
            dW = torch.randn(n_paths, device=self.device)

            # 2. Poisson Jump Arrivals
            p_jump = self.lamb * dt_t
            has_jump = (torch.rand(n_paths, device=self.device) < p_jump).float()

            # 3. Log-Normal Jump Sizes
            Z_j = torch.randn(n_paths, device=self.device)
            # Jump Size Y = exp(mu_j + sigma_j * Z_j)
            ln_Y = self.mu_j + self.sigma_j * Z_j

            # 4. The Log-Return Step
            # Important: Jump impact is ln(Y) only IF a jump occurred
            jump_impact = has_jump * ln_Y

            # Update using the log-return formula: S_t = S_{t-1} * exp(drift + diffusion + jump)
            exponent = drift_adj + (vol_term * dW) + jump_impact
            current_S = current_S * torch.exp(exponent)
            paths[t] = current_S

        return paths
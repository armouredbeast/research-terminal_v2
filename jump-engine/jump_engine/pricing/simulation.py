import torch
from jump_engine.nucleus.sde import MertonJumpDiffusion


class JumpPricer:
    def __init__(self, model: MertonJumpDiffusion):
        self.model = model

    def price_european(self, S0, K, T, steps, n_paths, option_type="call"):
        paths = self.model.simulate_paths(S0, T, steps, n_paths)
        S_T = paths[-1]

        if option_type == "call":
            payoff = torch.maximum(S_T - K, torch.tensor(0.0, device=self.model.device))
        else:
            payoff = torch.maximum(K - S_T, torch.tensor(0.0, device=self.model.device))

        # Discount back at rate mu
        discount = torch.exp(-self.model.mu * T)
        price = torch.mean(payoff) * discount

        # Standard Error for convergence validation
        std_err = torch.std(payoff) / torch.sqrt(torch.tensor(n_paths, dtype=torch.float32))

        return price.item(), std_err.item()
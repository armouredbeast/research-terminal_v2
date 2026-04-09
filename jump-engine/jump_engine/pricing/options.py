import torch


class JumpOptionPricer:
    def __init__(self, model):
        self.model = model

    def price_european(self, S0, K, T, steps, n_paths, option_type='call'):
        paths = self.model.simulate_paths(S0, T, steps, n_paths)
        terminal_prices = paths[-1]

        if option_type == 'call':
            payoffs = torch.maximum(terminal_prices - K, torch.tensor(0.0))
        else:
            payoffs = torch.maximum(K - terminal_prices, torch.tensor(0.0))

        # Discount back at the drift rate mu (assuming risk-free r = mu here)
        price = torch.mean(payoffs) * torch.exp(torch.tensor(-self.model.mu * T))
        std_err = torch.std(payoffs) / torch.sqrt(torch.tensor(float(n_paths)))

        return price.item(), std_err.item()
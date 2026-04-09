import torch

class RiskManager:
    def __init__(self, confidence_level: float = 0.95):
        self.confidence_level = confidence_level
    def calculate_var(self, simulated_returns: torch.Tensor):
        """
        Var: the 'worst case' loss at a given confidence.
        uses the monte carlo paths from our Nucleus.
        """
        # Sort returns and pick the percentile
        sorted_returns,_=torch.sort(simulated_returns)
        index = int((1-self.confidence_level)*len(sorted_returns))
        return sorted_returns[index]

    def apply_stop_loss(self, current_price:torch.Tensor, entry_price: float, limit: float = 0.02):
        """Hard stop if price drops by 'limit' percent. """
        return current_price < (entry_price*(1-limit))

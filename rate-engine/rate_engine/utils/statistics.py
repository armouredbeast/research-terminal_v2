import torch

def check_martingale_consistency(initial_value, discounted_paths):
    """
    Validate if E[Discounted Payoff] is equal to initial value.
    Essential for verifying risk-neutral pricing logic.
    """
    expectation = torch.mean(discounted_paths)
    abs_error= torch.abs(expectation - initial_value)
    rel_error = abs_error/initial_value

    return {
        "expected_value":expectation.item(),
        "theoretical_value": initial_value,
        "relative_error": rel_error.item(),
        "is_consistent": rel_error < 0.01 # 1% tolerance

    }

def validate_martingale(initial_r, simulated_rates, T, dt):
    mean_terminal_rate = torch.mean(simulated_rates)
    return {'mean_terminal': mean_terminal_rate.item()}

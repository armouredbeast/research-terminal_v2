from jump_engine.nucleus.sde import MertonJumpDiffusion
from jump_engine.pricing.simulation import JumpPricer
from jump_engine.pricing.analytical import merton_analytical_call
import torch


def test_convergence():
    S0, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.2
    lamb, mu_j, sigma_j = 2.0, -0.1, 0.1

    # 1. Get the 'Gold Standard'
    target = merton_analytical_call(S0, K, T, r, sigma, lamb, mu_j, sigma_j)

    # 2. Run Simulation on MPS
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    model = MertonJumpDiffusion(r, sigma, lamb, mu_j, sigma_j, device=device)
    pricer = JumpPricer(model)

    sim_price, stderr = pricer.price_european(S0, K, T, 252, 1_000_000)

    diff = abs(sim_price - target)
    print(f"Analytical Price: {target:.4f}")
    print(f"Simulation Price: {sim_price:.4f}")
    print(f"Abs Error: {diff:.4f} (StdErr: {stderr:.4f})")

    assert diff < 3 * stderr, "Convergence test failed: Error outside of 3-sigma range."
    print("SUCCESS: Simulation converged to analytical target.")


if __name__ == "__main__":
    test_convergence()
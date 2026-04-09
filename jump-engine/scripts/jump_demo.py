import time
import matplotlib.pyplot as plt
from jump_engine.utils.device import get_device
from jump_engine.nucleus.sde import MertonJumpDiffusion
from jump_engine.pricing.simulation import JumpPricer

def run_demo():
    device = get_device()
    print(f"Running on: {device}")

    # Parameters for 'Crisis' scenario
    # 2 jumps a year, average -15% drop per jump
    model = MertonJumpDiffusion(
        mu=0.05, sigma=0.2, lamb=2.0, mu_j=-0.15, sigma_j=0.1, device=device
    )
    pricer = JumpPricer(model)

    # 1. Price check
    start = time.time()
    price, stderr = pricer.price_european(S0=100, K=100, T=1.0, steps=252, n_paths=100_000)
    print(f"Price: {price:.4f} | StdErr: {stderr:.6f} | Time: {time.time()-start:.4f}s")

    # 2. Visual Check (Plotting 5 paths to see the 'Jumps')
    paths = model.simulate_paths(S0=100, T=1.0, steps=252, n_paths=5).cpu().numpy()
    plt.figure(figsize=(10, 6))
    plt.plot(paths)
    plt.title("Merton Jump-Diffusion: Black Swan Paths")
    plt.xlabel("Days")
    plt.ylabel("Asset Price")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run_demo()
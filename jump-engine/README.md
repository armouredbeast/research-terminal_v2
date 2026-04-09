Jump-Engine ⚡️
High-Performance Merton Jump-Diffusion (MJD) Framework

jump-engine is a hardware-accelerated stochastic simulation library designed to model discontinuous asset price paths ("Black Swans") and price path-dependent derivatives. Optimized for Apple Silicon (MPS) and NVIDIA (CUDA) via PyTorch.

1. The "So What?" (Quantitative Rationale)
Standard Geometric Brownian Motion (GBM) assumes price continuity (Gaussian returns). However, real-world markets exhibit Leptokurtosis (Fat Tails) and Discontinuities (Jumps) during geopolitical shocks or liquidity crises.

jump-engine allows researchers to:

Quantify Tail Risk: Simulate 1M+ paths to calculate Value-at-Risk (VaR) and Expected Shortfall (CVaR) in milliseconds.

Price Gap Risk: Value OTM options correctly by incorporating the Poisson-Normal jump component.

Hardware Efficiency: Achieve 50x-100x throughput increases over CPU-based NumPy implementations by leveraging GPU tensor cores.

2. Installation

```
git clone https://github.com/armouredbeast/jump-engine.git
cd jump-engine
pip install -r requirements.txt
```



4. Quick Start: Pricing a "Crisis" Scenario

``` python
from jump_engine.nucleus.sde import MertonJumpDiffusion
from jump_engine.pricing.simulation import JumpPricer

# Configure a high-volatility, jump-heavy regime
model = MertonJumpDiffusion(
    mu=0.05,        # Risk-free rate
    sigma=0.20,     # Diffusion Vol
    lamb=2.0,       # 2 Jumps per year (expected)
    mu_j=-0.15,     # Average jump is a -15% crash
    sigma_j=0.10,    # Jump size volatility
    device='mps'    # Accelerated on ArmouredBeast GPU
)

pricer = JumpPricer(model)
price, stderr = pricer.price_european(S0=100, K=100, T=1.0, steps=252, n_paths=1_000_000)

print(f"Jump-Adjusted Option Price: {price:.4f} (±{stderr:.4f})")

```

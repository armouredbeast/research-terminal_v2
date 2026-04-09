# Quant-Nucleus 0.1.0
**A High-Performance Stochastic Simulation & Alpha Research Library**

Quant-Nucleus is a cross-platform framework designed for high-frequency financial modeling. It bridges the gap between hardware-aware numerical methods and trade-signal generation.

## Key Features
- **Hardware-Agnostic Engine:** Automatic detection and utilization of Apple Silicon (MPS) and NVIDIA (CUDA).
- **High-Order SDE Solvers:** Implements vectorized Milstein discretization for superior convergence over standard Euler schemes.
- **Modular Pipeline:** Distinct separation between Stochastic Physics, Signal Extraction, and Risk Management.

## Installation
```bash
git clone [https://github.com/your-username/quant-nucleus](https://github.com/your-username/quant-nucleus)
cd quant-nucleus
pip install -e .
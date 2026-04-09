# 🛡️ ArmouredBeast: High-Frequency Research Terminal (V2.0)

**ArmouredBeast** is a modular, production-grade quantitative research suite designed for the modeling of stochastic processes, market microstructure, and portfolio optimization. This application serves as a unified interface for six proprietary Python libraries developed to bridge the gap between financial theory and execution infrastructure.

## 🚀 Live Dashboard
https://cvksaijagadish-qfl.streamlit.app


---

## 🏗️ Architectural Overview
The system is built on a decoupled, micro-library architecture. Each core engine is independently deployed as a PyPI-distributed package to ensure high modularity and scalability.
```
| Component | Library (PyPI) | Responsibility |
| :--- | :--- | :--- |
| **SDE Engine** | `quant-jump-engine` | Merton Jump-Diffusion & Stochastic Volatility modeling. |
| **LOB Engine** | `quant-limit-engine` | Limit Order Book depth and microstructure simulation. |
| **Connectivity**| `quant-engine` | Infrastructure for high-speed data piping (Latency-focused). |
| **Signal Ops** | `quant-signal-engine`| Time-series processing and feature engineering. |
| **Alpha Lab** | `alpha-engine-quant` | Mean-Variance and Black-Litterman optimization. |
| **Rates Unit** | `quant-rate-engine` | Interest rate modeling and Yield Curve construction. |

---
```
## 🛠️ Operating Instructions
1. **Simulation Suite:** Navigate to the **Stochastic Simulator** tab. Calibrate drift (μ) and volatility (σ) to observe path-wise asset trajectories with Poisson jumps.
2. **Microstructure Analysis:** Use the **LOB** tab to visualize real-time bid/ask depth and spread dynamics.
3. **Risk Management:** Adjust the **VaR Confidence** and **Vol Target** in the sidebar to observe how the Alpha Genome shifts the efficient frontier.

## 💻 Tech Stack
- **Languages:** Python (C++ backends for simulation logic).
- **Core Libs:** NumPy, Pandas, Plotly, SciPy, Torch.
- **Deployment:** Streamlit Cloud + PyPI Distribution.
- **CI/CD:** Automated package builds via GitHub Actions.

---
*Developed for Quantitative Research applications in HFT and Global Macro environments.*



🏗️ The ArmouredBeast Ecosystem
Each library is independently distributed via PyPI. Below are the specific instructions and logic for integrating each engine into your own quantitative research workflow.

1. 💹 Signal Engine (quant-signal-engine)

Used for time-series feature engineering and signal extraction.

Installation: pip install quant-signal-engine

Import Name: import signal_engine

Example:

```Python
import signal_engine
# Apply a Kalman Filter to noisy market data
filtered_signal = signal_engine.apply_kalman(price_data)
```


2. 🔗 Connectivity Engine (quant-engine)

High-speed data piping and infrastructure management.

Installation: pip install quant-engine

Import Name: import connectivity

Example:

```Python
import connectivity
# Establish a low-latency connection to a mock LOB feed
stream = connectivity.DataStream(provider="Internal")
stream.connect()
```

3. 🧬 Alpha Engine (alpha-engine-quant)

Portfolio optimization and Mean-Variance analysis.

Installation: pip install alpha-engine-quant

Import Name: import alpha_engine

Example:

```Python
import alpha_engine
# Solve for the Tangency Portfolio given expected returns
weights = alpha_engine.optimize_frontier(expected_returns, cov_matrix)
```

4. 📊 Limit Engine (quant-limit-engine)

Order book microstructure and liquidity depth simulation.

Installation: pip install quant-limit-engine

Import Name: import limit_engine

Example:

```Python
import limit_engine
# Initialize a local LOB and check the current spread
lob = limit_engine.OrderBook()
lob.add_order(side="ASK", price=100.05, size=50)
print(f"Current Spread: {lob.spread}")
```



5. 📈 Rate Engine (quant-rate-engine)

Interest rate modeling and yield curve construction.

Installation: pip install quant-rate-engine

Import Name: import rate_engine

Example:

```Python
import rate_engine
# Construct a Zero-Coupon Yield Curve from market rates
curve = rate_engine.YieldCurve(maturities=[1, 2, 5, 10], rates=[0.03, 0.035, 0.04, 0.042])
```
6. ⚡ Jump Engine (quant-jump-engine)

Modeling discontinuous asset price paths via Merton Jump-Diffusion.

Installation: pip install quant-jump-engine

Import Name: import jump_engine

Example:

```Python
import jump_engine
# Simulate a jump-diffusion path for stress testing
model = jump_engine.MertonSDE(mu=0.05, sigma=0.2, intensity=0.1)
path = model.simulate_path(steps=252)
```


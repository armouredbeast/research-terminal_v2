# 🛡️ ArmouredBeast: High-Frequency Research Terminal (V2.0)

**ArmouredBeast** is a modular, production-grade quantitative research suite designed for the modeling of stochastic processes, market microstructure, and portfolio optimization. This application serves as a unified interface for six proprietary Python libraries developed to bridge the gap between financial theory and execution infrastructure.

## 🚀 Live Dashboard
[INSERT YOUR STREAMLIT URL HERE]

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
# Alpha-Engine 📊
**Modern Portfolio Theory & Risk Parity Suite**

`alpha-engine` is a quantitative library for multi-asset portfolio construction. It bridges the gap between raw signals and trade execution by optimizing capital allocation.

## Core Features
* **Mean-Variance Optimization:** Uses SLSQP solvers to find the Tangency Portfolio (Max Sharpe).
* **Risk Parity:** Implements risk-budgeting techniques to equalize risk contributions across assets.
* **Performance Attribution:** Built-in metrics for Sharpe, Volatility, and Max Drawdown.

## Example
```python
from alpha_engine.nucleus.optimizer import PortfolioOptimizer
opt = PortfolioOptimizer(returns_data)
weights = opt.optimize_max_sharpe()
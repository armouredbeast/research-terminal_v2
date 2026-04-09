import numpy as np
from scipy.optimize import minimize


class PortfolioOptimizer:
    """Implements Mean-Variance Optimization and Max Sharpe Ratio."""

    def __init__(self, returns_matrix):
        """
        returns_matrix: np.ndarray of shape (assets, time_steps)
        """
        self.returns = returns_matrix
        self.mean_returns = np.mean(returns_matrix, axis=1)
        self.cov_matrix = np.cov(returns_matrix)
        self.n_assets = len(self.mean_returns)

    def _get_stats(self, weights):
        """Calculates annualized portfolio return and volatility."""
        # Annualized scaling (252 trading days)
        port_ret = np.sum(self.mean_returns * weights) * 252
        port_vol = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights))) * np.sqrt(252)
        return port_ret, port_vol

    def _neg_sharpe(self, weights, rf_rate=0.04):
        """Objective function to minimize."""
        ret, vol = self._get_stats(weights)
        return -(ret - rf_rate) / vol

    def optimize(self, target="sharpe"):
        """Finds the weights for the optimal portfolio."""
        # Constraints: Weights must sum to 1.0
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        # Bounds: Long-only (weights between 0 and 1)
        bounds = tuple((0, 1) for _ in range(self.n_assets))
        init_guess = [1 / self.n_assets] * self.n_assets

        res = minimize(self._neg_sharpe, init_guess, method='SLSQP',
                       bounds=bounds, constraints=constraints)

        return res.x
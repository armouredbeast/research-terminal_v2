import numpy as np
from scipy.optimize import minimize


class RiskParityModel:
    """Allocates weights so each asset contributes equally to total risk."""

    def __init__(self, returns_matrix):
        self.cov = np.cov(returns_matrix)
        self.n = len(self.cov)

    def _risk_contribution(self, weights):
        """Calculates the percentage of risk contributed by each asset."""
        weights = np.array(weights)
        portfolio_vol = np.sqrt(np.dot(weights.T, np.dot(self.cov, weights)))
        # Marginal Risk Contribution
        mrc = np.dot(self.cov, weights) / portfolio_vol
        # Total Risk Contribution
        rc = weights * mrc
        return rc / np.sum(rc)

    def _objective(self, weights):
        """Minimizes the squared difference between risk contributions."""
        target = np.ones(self.n) / self.n
        current_rc = self._risk_contribution(weights)
        return np.sum(np.square(current_rc - target))

    def get_weights(self):
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0.01, 1) for _ in range(self.n))  # Min 1% allocation
        res = minimize(self._objective, [1 / self.n] * self.n, method='SLSQP',
                       bounds=bounds, constraints=constraints)
        return res.x
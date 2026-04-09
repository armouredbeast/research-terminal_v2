import numpy as np


class KalmanPriceFilter:
    """Optimal estimator for noisy price signals."""

    def __init__(self, process_variance=1e-5, observation_variance=1e-3):
        # Initial guesses
        self.post_estimate = 0.0
        self.post_error_cov = 1.0

        # Hyperparameters (The Q and R matrices)
        self.process_var = process_variance  # How much we trust the model
        self.obs_var = observation_variance  # How much we trust the market data

    def update(self, measurement):
        """Standard Kalman Gain update cycle."""
        # 1. Prediction Step
        pri_estimate = self.post_estimate
        pri_error_cov = self.post_error_cov + self.process_var

        # 2. Update Step (Kalman Gain)
        gain = pri_error_cov / (pri_error_cov + self.obs_var)
        self.post_estimate = pri_estimate + gain * (measurement - pri_estimate)
        self.post_error_cov = (1 - gain) * pri_error_cov

        return self.post_estimate
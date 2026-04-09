import torch
import math
from scipy.stats import norm


def black_scholes_call(S, K, T, r, sigma):
    if T <= 0: return max(S - K, 0)
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)


def merton_analytical_call(S, K, T, r, sigma, lamb, mu_j, sigma_j):
    """Merton (1976) Jump-Diffusion Analytical Price"""
    price = 0
    # kappa = expected jump size - 1
    kappa = math.exp(mu_j + 0.5 * sigma_j ** 2) - 1

    # Sum the first 50 components of the infinite series
    for n in range(50):
        n_fact = math.factorial(n)
        # Probability of n jumps occurring (Poisson)
        prob_n = (math.exp(-lamb * T) * (lamb * T) ** n) / n_fact

        # Adjusted volatility and interest rate for the n-th state
        sigma_n = math.sqrt(sigma ** 2 + n * sigma_j ** 2 / T)
        r_n = r - lamb * kappa + (n * mu_j / T)

        price += prob_n * black_scholes_call(S, K, T, r_n, sigma_n)
    return price
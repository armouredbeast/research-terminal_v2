import torch
from nucleus.utils.device_manager import GLOBAL_DEVICE
from nucleus.sampling.samplers import Sampler
from nucleus.stochastic.dynamics import GBM
from nucleus.stochastic.solver import SDESolver

#1. Setup the machine
sampler = Sampler(device= GLOBAL_DEVICE)
solver = SDESolver(device= GLOBAL_DEVICE)

#2. Define the 'Stock' (10% growth, 30% volatility)
stock_dna = GBM(mu=0.1, sigma=0.3)
#3. Run 100,000 simulations for 1 year (252 trading days)
paths = solver.simulate(
    sde = stock_dna,
    s0=100.0,
    sampler = sampler,
    t = 1.0,
    steps= 252,
    n_paths = 100000,
    method = 'milstein'
)

print(f"Simulation complete on {GLOBAL_DEVICE}!")
print(f"Final average price: {paths[-1].mean():.2f}")


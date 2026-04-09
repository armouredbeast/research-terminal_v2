import torch
from nucleus.utils.device_manager import GLOBAL_DEVICE
from nucleus.sampling.samplers import Sampler
from nucleus.stochastic.dynamics import GBM
from nucleus.stochastic.solver import SDESolver
from connectivity.data_handler import DataHandler
from signal_lab.indicators import moving_average
from strategist.risk_manager import RiskManager

def run_pipeline():
    print(f"---Quant-Nucleus Engine starting on {GLOBAL_DEVICE}---")
    #1. CONNECTIVITY: Load Data
    handler = DataHandler(device=GLOBAL_DEVICE)
    # prices = handler.load_from)csv("your_data.csv") # Placeholder for your file

    #2. Signal lab: find alpha
    # ma_signal = moving_average(prices, window = 20)

    #3. NUCLEUS : simulate risk
    sampler = Sampler(device=GLOBAL_DEVICE)
    solver = SDESolver(device=GLOBAL_DEVICE)
    stock_model = GBM(mu=0.05, sigma=0.2)

    paths = solver.simulate(sde=stock_model, s0= 100.0, sampler=sampler,
                            t=1.0, steps=252, n_paths=100000)
    #4. STRATEGIST: Calculate VaR
    rm = RiskManager(confidence_level=0.99)
    returns = (paths[-1]-100.0)/100.0
    var_99= rm.calculate_var(returns)
    print(f"Integration Success. 1-Year 99% VaR: {var_99.item()*100:.2f}%")
if __name__=='__main__':
    run_pipeline()
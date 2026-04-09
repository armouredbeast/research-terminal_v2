import torch
from rate_engine.nucleus.solvers import MonteCarloFramework

from rate_engine.utils.device import get_device
from rate_engine.nucleus.sde import Vasicek

class BondPricer:
    def __init__(self, sde, device):
        self.solver = MonteCarloFramework(sde,device)
        self.device = device
    def price_zcb(self,r0, T, steps, n_paths):
        """
        P(0,T) = E[exp(-Integral(r_s ds))]
        """
        _, path_integral=self.solver.simulate(r0,T,steps,n_paths)
        discount_factors = torch.exp(-path_integral)

        price = torch.mean(discount_factors)
        std_err = torch.std(discount_factors)/torch.sqrt(torch.tensor(n_paths))
        return price.item(), std_err.item()

if __name__ == '__main__':
    def run_demo():
        device = get_device()
        # Parameters: a (speed) = 0.5, b (long-term mean)=0.05, sigma = 0.02
        model = Vasicek(a=0.5,b=0.05,sigma=0.02)
        pricer = BondPricer(model, device)
        pricer, error = pricer.price_zcb(r0=0.03,T=1.0,steps=252, n_paths = 100000)

        print(f"--- Rate Engine Output ---")
        print(f"Device: {device}")
        print(f"Zero-Coupon Bond Price (T=1): {pricer:.6f}")
        print(f"Standard Error: {error:.6f}")

    run_demo()

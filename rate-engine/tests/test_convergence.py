import time
from rate_engine.nucleus.sde import Vasicek
from rate_engine.pricing.bonds import BondPricer
from rate_engine.utils.device import get_device

def test_scaling():
    device = get_device()
    model = Vasicek(0.5,0.05,0.02)
    pricer = BondPricer(model,device)

    path_counts = [10000,100000,1000000]

    print(f"{'Paths':>12} | {'Price':>10} | {'StdError':>10} | {'Time(s)':>10}")
    print('_'*50)
    for n in path_counts:
        start = time.time()
        price, error = pricer.price_zcb(0.03,1.0,100,n)
        elapsed = time.time()-start
        print(f"{n:12,d} | {price:10.6f} | {error:10.6f}  | {elapsed:10.4f}")

def run_convergence_test():
    device = get_device()
    model = Vasicek(0.5,0.05, 0.02)
    pricer = BondPricer(model, device)
    for n in [10**4,10**5,10**6,10**7]:
        start = time.time()
        price, error = pricer.price_zcb(0.03, 1.0,252,n)
        print(f"Paths:{n:,} | Price: {price:.5f} | Error: {error:.6f} | Time: {time.time()-start:.4f}s")

if __name__ == '__main__':
    test_scaling()
    run_convergence_test()


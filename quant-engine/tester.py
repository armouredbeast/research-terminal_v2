import torch
import time
import numpy as np
from nucleus.utils.device_manager import GLOBAL_DEVICE
from nucleus.sampling.samplers import Sampler

# Initialize our sampler on the detected hardware
sampler = Sampler(device = GLOBAL_DEVICE)
N = 10000000 # 1 million samples
# ----> Test 1: the slow way(std python loop)
start = time.time()
slow_samples = [np.random.normal() for _ in range(10000000)]
print(f"Python loop (1 million samples):{time.time()-start:.4f}seconds")


# ----> Test 2: the nucleus way(parallel GPU)
start = time.time()
fast_samples = sampler.get_standard_normal((N,))
if GLOBAL_DEVICE.type == 'cuda': torch.cuda.synchronize()
print(f"Nucleus GPU(1 million samples): {time.time() - start:.4f} seconds")
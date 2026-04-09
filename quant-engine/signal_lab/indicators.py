import torch
import torch.nn.functional as F

def moving_average(data: torch.Tensor, window: int)-> torch.Tensor:
    """
    Vectorized Moving Average using 1D convolution(Hardware accelerated).
    """
    # Creating a smoothing kernel [1/w,1/w,1/w,.....]
    kernel = torch.ones(1,1,window, device = data.device)/window
    # Reshape data to [Batch, Channels, Length]
    x = data.view(1,1,-1)
    # Apply convolution (valid padding means output is shorter by window-1)
    ma = F.conv1d(x, kernel, padding=0)
    return ma.view(-1)

def exponential_moving_average(data: torch.Tensor, span:int)-> torch.Tensor:
    """EMA: Gives more weight to recent prices."""
    alpha = 2/(span+1)
    # Should use a recursive approach here, to see the true GPU speed,
    # some should use a specialized CUDA kernel or linear recurrence.(Checklist for late)
    ema = torch.zeros_like(data)
    ema[0]= data[0] #---> this is for equating the data loaders in the method of vectorization
    for i in range(1, len(data)):
        ema[i] = alpha * data[i] + (1-alpha)* ema[i-1]
    return ema

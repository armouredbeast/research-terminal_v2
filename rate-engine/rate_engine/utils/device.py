import torch

def get_device():
    """
    Selects the best device available hardware accelerator.
    Returns 'mps' for Mac, 'cuda' for NVIDIA or 'cpu'
    """
    if torch.backends.mps.is_available():
        return torch.device("mps")
    elif torch.cuda.is_available():
        return torch.device("cuda")
    else:
        return torch.device("cpu")

def to_tensor(data, device= None):
    if device is None:
        device = get_device()
    return torch.as_tensor(data,device = device, dtype= torch.float32)


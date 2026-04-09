import torch
def get_device():
    if torch.backends.mps.is_available():
        return torch.device('mps')
    elif torch.backends.cuda.is_available():
        return torch.device('cuda')
    return torch.device('cpu')

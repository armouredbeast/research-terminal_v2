import torch

def fast_fourier_transform(data: torch.Tensor):
    """Identifies dominant cycles (frequencies) in price data."""
    return torch.fft.rfft(data)
def normalize_signal(signal: torch.Tensor):
    """
    Squashes any raw signal into a range of [-1,1].
    -1 = Strong Sell Signal, 1 = Strong Buy Signal.
    """
    return torch.tanh(signal)

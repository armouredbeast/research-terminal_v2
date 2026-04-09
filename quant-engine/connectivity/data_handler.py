import pandas as pd
import torch
from connectivity.schema import MarketDataSchema
class DataHandler:
    def __init__(self, device: torch.device):
        self.device = device
    def load_from_csv(self, path: str) -> torch.Tensor:
        """Loads CSV and moves 'Close' prices to the hardware accelerator"""
        df = pd.read_csv(path)
        MarketDataSchema.validate(df.columns.tolist())
        # Convert to tensor and cast to float32 for high-speed GPU math
        prices = torch.tensor(df['close'].values, dtype= torch.float32, device= self.device)
        return prices
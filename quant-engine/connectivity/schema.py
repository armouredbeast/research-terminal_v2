from typing import List
class MarketDataSchema:
    """Ensures incoming data fits the expected format for the Nucleus."""
    REQUIRED_COLUMNS = ["timestamp", "open", "high", "low", "close", "volume"]

    @staticmethod
    def validate(columns: List[str]):
        missing = [col for col in MarketDataSchema.REQUIRED_COLUMNS if col not in columns]
        if missing:
            raise ValueError(f"Connectivity Error: Missing required columns: {missing}")
        return True
    
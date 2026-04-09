# Signal-Engine 📡
**Real-time Signal Processing & Alpha Generation**

`signal-engine` provides the statistical machinery to extract tradable signals from noisy financial time series.

## Core Features
* **Kalman Filtering:** Recursive state estimation to identify the "latent" price trend in volatile regimes.
* **Mean Reversion:** Statistical Z-Score modeling for identifying overextended price moves.
* **Stat-Arb Ready:** Optimized for high-frequency signal calculation with minimal latency.

## Usage
```python
from signal_engine.nucleus.kalman_filter import KalmanPriceFilter
kf = KalmanPriceFilter()
clean_price = kf.update(raw_market_price)
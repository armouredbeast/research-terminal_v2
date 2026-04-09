# Limit-Engine 📉
**High-Frequency Order Book & Microstructure Simulator**

`limit-engine` is a matching engine implementation designed to simulate L2 market depth and analyze the impact of large institutional trades.

## Key Features
* **O(log N) Matching:** Uses Priority Queues (Heaps) for high-performance order insertion and price-time priority.
* **Slippage Analysis:** Real-time calculation of transaction costs and market "sweep" impact.
* **Impact Modeling:** Implements the Square Root Law for estimating price decay on large block trades.

## Usage
```python
from limit_engine.nucleus.order_book import OrderBook
lb = OrderBook()
lb.add_limit_order("oid_1", "sell", 100.50, 500)
# Execute a market buy that hits the book
filled, avg_p, slippage = lb.execute_market_order("buy", 100)
import heapq
import time


class OrderBook:
    def __init__(self):
        # Bids: Max-heap. We store (negative_price, timestamp, qty, order_id)
        # Python's heapq is a min-heap, so we negate the price to get Max-heap.
        self.bids = []

        # Asks: Min-heap. We store (price, timestamp, qty, order_id)
        self.asks = []

        # Map for O(1) order tracking and cancellations
        # {order_id: [price, qty, side, timestamp]}
        self.order_map = {}

    def add_limit_order(self, order_id, side, price, qty):
        """Adds a limit order to the book with price-time priority."""
        timestamp = time.time()
        side = side.lower()

        if side == 'buy':
            # Negative price for Max-Heap
            heapq.heappush(self.bids, (-price, timestamp, qty, order_id))
        elif side == 'sell':
            heapq.heappush(self.asks, (price, timestamp, qty, order_id))

        self.order_map[order_id] = [price, qty, side, timestamp]
        return True

    def get_best_bid_ask(self):
        """Returns the current Top of Book (Level 1)."""
        best_bid = -self.bids[0][0] if self.bids else None
        best_ask = self.asks[0][0] if self.asks else None
        return best_bid, best_ask

    def get_spread(self):
        """Calculates the current Bid-Ask spread."""
        bid, ask = self.get_best_bid_ask()
        if bid and ask:
            return ask - bid
        return float('inf')

    def execute_market_order(self, side, qty):
        """
        Executes a market order against the limit orders in the book.
        Returns: (total_filled_qty, average_price, slippage)
        """
        side = side.lower()
        total_filled = 0
        total_cost = 0.0

        # If buying, we hit the 'Asks'. If selling, we hit the 'Bids'.
        target_heap = self.asks if side == 'buy' else self.bids
        initial_best_price = target_heap[0][0] if target_heap else None

        if initial_best_price is not None and side == 'buy':
            pass  # price is already positive
        elif initial_best_price is not None:
            initial_best_price = -initial_best_price

        while qty > 0 and target_heap:
            # Pop the best available limit order
            best_price_raw, ts, avail_qty, oid = heapq.heappop(target_heap)
            actual_price = -best_price_raw if side == 'sell' else best_price_raw

            fill_qty = min(qty, avail_qty)
            total_cost += fill_qty * actual_price
            total_filled += fill_qty
            qty -= fill_qty

            # If the limit order wasn't fully consumed, push the remainder back
            if avail_qty > fill_qty:
                heapq.heappush(target_heap, (best_price_raw, ts, avail_qty - fill_qty, oid))
                self.order_map[oid][1] -= fill_qty
            else:
                del self.order_map[oid]

        avg_price = total_cost / total_filled if total_filled > 0 else 0
        slippage = avg_price - initial_best_price if initial_best_price else 0

        return total_filled, avg_price, abs(slippage)

    def get_volume_at_levels(self, levels=5):
        """Returns the depth of the book for visualization."""
        bid_depth = [(-p, q) for p, t, q, i in heapq.nsmallest(levels, self.bids)]
        ask_depth = [(p, q) for p, t, q, i in heapq.nsmallest(levels, self.asks)]
        return bid_depth, ask_depth
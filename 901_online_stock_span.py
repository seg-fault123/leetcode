class StockSpanner:
    # same as daily temparatures
    def __init__(self):
        self.stack = []
    
    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        self.stack.append((price, span))
        return span


    # def __init__(self):
    #     self.stocks = []
    #     self.checkpoints = []

    # def next(self, price: int) -> int:
    #     self.stocks.append(price)
    #     current = len(self.stocks)-1
    #     prev = current - 1
    #     while prev>=0 and self.stocks[prev] <= price:
    #         prev = self.checkpoints[prev]
        
    #     self.checkpoints.append(prev)
    #     return current - prev


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

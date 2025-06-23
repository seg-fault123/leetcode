class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # whenever stock is going up, keep the stock with you
        # whenever stock falls, sell on the last price and buy new today
        result = 0
        start = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                # if stock falls, sell on the last price
                result += prices[i-1] - start
                # buy new today
                start = prices[i]
        result += prices[-1] - start
        return result

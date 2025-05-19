class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = {}
        def dfs(index, can_buy):
            if index >= len(prices):
                return 0
            if (index, can_buy) in result:
                return result[(index, can_buy)]
            
            cool_down = dfs(index+1, can_buy)
            if can_buy:
                buy = dfs(index+1, not can_buy) - prices[index]
                result[(index, can_buy)] = max(buy, cool_down)
            else:
                sell = dfs(index+2, not can_buy) + prices[index]
                result[(index, can_buy)] = max(cool_down, sell)
            return result[(index, can_buy)]
        
        return dfs(0, True)


        # n = len(prices)
        # result = [0]*n
        # result[-1] = 0
        # for i in range(n-2, -1, -1):
        #     result[i] = result[i+1]
        #     j = i+1
        #     while j < n:
        #         profit = prices[j]-prices[i]
        #         if j+2 < n:
        #             profit += result[j+2]
        #         result[i] = max(profit, result[i])
        #         j += 1

        # return result[0]
        

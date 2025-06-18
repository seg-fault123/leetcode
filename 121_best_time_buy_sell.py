class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        start = 0
        end = 1
        n = len(prices)
        # if you find a lower price, shift your buy to that day and look for more profit.
        while end < n:
            if prices[start] > prices[end]:
                start = end
            answer = max(answer, prices[end]-prices[start])
            end += 1
        
        return answer

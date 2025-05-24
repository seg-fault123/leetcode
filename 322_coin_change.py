import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = [math.inf]*(amount+1)
        result[0] = 0
        for coin in coins:
            for num in range(coin, amount+1):
                result[num] = min(result[num], 1+result[num-coin])
        return -1 if result[amount]==math.inf else result[amount] 
        

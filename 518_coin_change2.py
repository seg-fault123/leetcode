class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # add coin denominations one by one in the combinations
        ways = [0]*(amount+1)
        ways[0]=1
        for coin in coins:
            for i in range(coin, amount+1):
                ways[i] += ways[i-coin]
        
        return ways[amount]
                

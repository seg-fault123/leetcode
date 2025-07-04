class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [None]*len(stoneValue)

        def optimal(index):
            if index>=len(stoneValue):
                return 0
            
            return dp[index]
        
        curr = 0
        cum_sum = []
        for num in stoneValue:
            curr += num
            cum_sum.append(curr)

        for i in range(len(stoneValue)-1, -1, -1):
            total = None # will represent the sum of arr starting from i till end
            if i>0:
                total = cum_sum[-1] - cum_sum[i-1]
            else:
                total = cum_sum[-1]
            # next turn is of another player, we want the to take the max,
            # if we take 1, we get total-optimal(i+1), beacuse optimal(i+1) will be the value the other player gets
            # if we take 2, we get total-optimal(i+2)
            # if we take 3, we get total-optimal(i+3)
            dp[i] = max(total-optimal(i+1), total-optimal(i+2), total-optimal(i+3))
        
        if dp[0] > cum_sum[-1]/2:
            return 'Alice'
        elif dp[0] < cum_sum[-1]/2:
            return 'Bob'
        else:
            return 'Tie'

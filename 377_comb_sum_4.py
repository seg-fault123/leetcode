class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # it can be treated a generalized climbing stairs problem.
        # we have to reach at the target(th) stair and we have have nums options available at each stair
        # dp[i] stores number of ways/combinations to reach target starting at i
        # dp[0] will store our result beacause we start at 0
        dp = [0]*target + [1]
        for i in range(target-1, -1, -1):
            for num in nums:
                if i + num <= target:
                    dp[i] += dp[i+num]
        
        return dp[0]
    

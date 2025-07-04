# an O(1) solution exists fro the problem
# https://leetcode.com/problems/integer-break/solutions/80689/a-simple-explanation-of-the-math-part-and-a-o-n-solution/
# comments
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [float('-inf')]*(n+1)
        dp[1]= 1

        for i in range(2, n+1):
            for j in range(i-1, i//2 - 1, -1):
                diff = i - j
                dp[i] = max(dp[i], dp[j]*diff, j*dp[diff], j*diff)
        return dp[-1]


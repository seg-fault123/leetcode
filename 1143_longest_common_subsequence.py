class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        # dp[0] to compare empty string with text2
        # dp[i] to compare text1[:i] with text2, dp[1] is text1 till first character. (text1[:1]) 
        dp = [0]*(m+1)
        # dp holds values for previous iteration
        # new holds values for current iteration
        for char in text2:
            new = [0]*(m+1)
            for i in range(1, m+1):
                # from 1st character till mth character
                if char==text1[i-1]:
                    new[i] = dp[i-1] + 1
                else:
                    new[i] = max(new[i-1], dp[i])
            dp = new
        
        return dp[m]

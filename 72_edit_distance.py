class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [i for i in range(len(word1)+1)]

        for i in range(1, len(word2)+1):
            updated = dp[:]
            updated[0] = i
            for j in range(1, len(word1)+1):
                if word1[j-1] == word2[i-1]:
                    updated[j] = dp[j-1]
                else:
                    updated[j] = min(updated[j-1], dp[j], dp[j-1]) + 1
            dp = updated
        return dp[-1]

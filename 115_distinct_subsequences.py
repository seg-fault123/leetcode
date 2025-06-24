class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # if t has greater length then cannot be contained in s. Return 0
        if len(s) < len(t):
            return 0

        # the idea is that we add characters of t one by one and see how many possiblities we can make in s.
        # at any step, dp[j] will contain the possiblities till the jth character of s.
        # initially, when no characters of t are added, it means that we want to find "" in s. Set all dp[j] to 1. This is base case and will never be encountered because of the contraints of the problem which states that both s and t have at least 1 char.
    
        # now suppose at any step of iteration, we add some character of t. If it is the ith character of t, then new_dp (result of current step) will have all 0's before the ith position, because for any j<i the answer is 0(we cannot have a smaller s to fit in t).
        # if the ith character of t matches the jth character of s (j>i), then we have two possibilities
        # 1) we consider it in the subsequence. In which case, both these chars are matched and the total possiblities when these will be matched and kept is stored in dp[j-1], 
        # 2) we don't consider this match and look for more matches of this character. The total possibilities where these two don't match is new_dp[j-1]
        # we need to consider both possibilities, so add them to make new_dp[j]

        #dp[j-1] : result till i-1th character of t
        # new_dp[j-1]: result till ith character of t without considering jth character of s 


        # if they don't match, there is only one possiblity already calculated in new_dp[j-1]
        dp = [1]*(len(s)+1)
        for i in range(1, len(t)+1):
            new_dp = [0]*(len(s)+1)
            for j in range(i, len(s)+1):
                if t[i-1]==s[j-1]:
                    new_dp[j] = new_dp[j-1] + dp[j-1]
                else:
                    new_dp[j] = new_dp[j-1]
            dp = new_dp
        return dp[-1]
        

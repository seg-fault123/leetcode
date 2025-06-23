class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordDict.sort()
        # def binary_search(target):
        #     start = 0
        #     end = len(wordDict)-1
        #     while start <= end:
        #         mid = (start+end)//2
        #         if wordDict[mid] == target:
        #             return True
        #         elif wordDict[mid] < target:
        #             start = mid + 1
        #         else:
        #             end = mid -1
        #     return False
        
        # memo = [None]*len(s)
        # def check_word_break(start, s):
        #     if start==len(s):
        #         return True
        #     elif memo[start] is not None:
        #         return memo[start]
            
        #     end = start+1
        #     while end <=len(s):
        #         if binary_search(s[start:end]) and check_word_break(end, s):
        #             memo[start] = True
        #             return True
        #         end += 1
            
        #     memo[start]=False
        #     return False
        
        # return check_word_break(0, s)


        # dp[i] represents if s[i:] can be broken down. dp[len(s)] is set to true
        dp = [False]*len(s) + [True]

        # for each index starting from last, we check if we can match a word in wordDict from that index. If we can match that then we check if after matching, what the new starting index is and if we can breakdown the string from there. Notice that we would have already calculated the result from the next starting point, since we are coming in reverse
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if i+len(word)<=len(s) and s[i:i+len(word)]==word:
                    # if word matches , then check if the string can be broken down from the new starting point
                    dp[i] = dp[i+len(word)]
                    if dp[i]:
                        break
        
        return dp[0]
        

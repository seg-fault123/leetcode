class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pallindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        # dp[i] contains the substring partition for s[0:i]
        # dp[0] is just [[]] because there is no partition
        dp = [[[]]]

        # end pointer to calculate dp[end]
        for end in range(1, len(s)+1):
            result = []
            # check for all strings starting from s[0:end] to s[end-1:end]
            for start in range(0, end):
                if not is_pallindrome(start, end-1):
                    continue
                # if s[start:end] is a pallindrome, then add this to the already calculated partitions of s[0:start] usign dp[start], start is not included in dp[start]

                for partition in dp[start]:
                    result.append(partition+[s[start:end]])

            dp.append(result)
        
        return dp[-1]

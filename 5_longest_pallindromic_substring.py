class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_string = [0, 0]
        def count_pallindrome(start, end):
            diff = max_string[1] - max_string[0] + 1
            while 0 <= start and end < len(s) and s[start]==s[end]:
                current_diff = end - start + 1
                if  current_diff > diff:
                    diff = end - start + 1
                    max_string[0] = start
                    max_string[1] = end
                
                start -= 1
                end += 1
        
        for i in range(len(s)):
            count_pallindrome(i, i)
            count_pallindrome(i, i+1)
        
        return s[max_string[0] : max_string[1]+1]


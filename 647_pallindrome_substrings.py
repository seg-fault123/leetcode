class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_subs(start, end):
            # expands string from the middle on both sides and counts the substrings
            # if initially start == end, then odd pallindromes are calculated
            # if start+1 == end, then even pallindromes are calculated
            count = 0
            while start>=0 and end<len(s) and s[start]==s[end]:
                count += 1
                start -= 1
                end += 1
            return count
        
        total_count = 0
        for i in range(len(s)):
            total_count += count_subs(i, i) # odd pallindromes with i in middle
            total_count += count_subs(i, i+1) # even pallindromes with i and i+1 in middle
        
        return total_count
    


        # n = len(s)
        # result = [[0]*n for _ in range(n)]

        # def is_pallindrome(start, end):
        #     while start < end:
        #         if s[start]!=s[end]:
        #             return False
        #         else:
        #             start += 1
        #             end -= 1
        #     return True

        # for i in range(n):
        #     result[i][i] = 1
        # # expand the window size and keep storing the results
        # for window in range(1, n):
        #     start = 0
        #     end = window
        #     while end < n:
        #         result[start][end] = result[start+1][end] + result[start][end-1]
        #         if window > 1:
        #             result[start][end] -= result[start+1][end-1] # since this part is copied twice
        #         if is_pallindrome(start, end):
        #             result[start][end] += 1
        #         start += 1
        #         end += 1
        
        # return result[0][n-1]

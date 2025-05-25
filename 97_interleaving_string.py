class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # m = len(s1)
        # n = len(s2)
        # if len(s3) != m+n:
        #     return False
        # result = [[False]*(n+1) for _ in range(m+1)]
        # result[0][0] = True
        # # result[i][j] is True if s1[:i] and s2[:j] can be interleaved to make s3[:i+j]. result[0][j] or result[i][0] is for base case when the other string is empty.
        # for i in range(1, m+1):
        #     # result[i-1][0] to check for previous character, and
        #     # since we want result for ith character, we check for s1[i-1]==s3[i-1]
        #     result[i][0] = result[i-1][0] and s1[i-1]==s3[i-1]
        # for j in range(1, n+1):
        #     result[0][j] = result[0][j-1] and s2[j-1]==s3[j-1]
        
        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         result[i][j] = ((result[i-1][j] and s1[i-1]==s3[i+j-1]) or
        #                             result[i][j-1] and s2[j-1]==s3[i+j-1])
        
        # return result[m][n]


        # space optimised, using only 1-D array
        m = len(s1)
        n = len(s2)
        if len(s3) != m+n:
            return False
        
        result = [False]*(n+1)
        result[0] = True
        for j in range(1, n+1):
            result[j] = result[j-1] and s2[j-1]==s3[j-1]
        
        for i in range(1, m+1):
            result[0] = result[0] and s1[i-1]==s3[i-1]
            for j in range(1, n+1):
                result[j] = ((result[j] and s1[i-1]==s3[i+j-1]) or 
                                (result[j-1] and s2[j-1]==s3[i+j-1]))
        return result[n]


        

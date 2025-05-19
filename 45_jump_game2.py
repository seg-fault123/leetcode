class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # in each iteration we maintain the range of indices reachable in those many jumps
        # so in first iteration, no jumps have been made and we only reach 0 index
        # in second iteration, we can reach from 1 to nums[0] (1 jump). We stop our iteration when we can reach the end index
        jumps = 0
        near = 0 
        far = 0 
        farthest = 0
        while far < n-1:
            # for the current range, check how far can we reach
            for i in range(near, far+1):
                farthest = max(farthest, nums[i]+i)
            
            # since it is alsways possible to reach the end, we can atleast reach 
            # far + 1
            near = far+1
            far = farthest
            jumps += 1
        
        return jumps


        # inefficient solution
        # n = len(nums)
        # result = [0]*n
        # number of jumps needed from the end to reach the end is zero (base case)
        # for i in range(n-2, -1, -1):
        #     j = i+1
        #     result[i] = 1 + result[j]
        #     max_j = min(n-1, i+nums[i]) #(the range of indices directly reachable from i)
        #     while j <= max_j:
        ## check which case leads to the least solution
        #         result[i] = min(result[i], 1 + result[j])
        #         j += 1
        
        # return result[0]

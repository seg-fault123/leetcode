class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # find a window starting from 0 position in which the target is achieved.
        # either this is the solution or a better solution exists
        # reduce the window from the left until the target is not satisfied.
        # if the current window does not satisfy, then slide it without expanding
        start = 0 
        end = 0
        n = len(nums)
        min_len = None
        total = 0
        # find a window with 0 as the start
        while end < n:
            total += nums[end]
            if total >= target:
                min_len = end-start+1
                break
            end += 1
        
        # not found then solution doesn't exist
        if not min_len:
            return 0
        
        # start reducing from the end
        while end < n:
            if total >= target:
                while start < end:
                    # if excluding current start still satisfies, then reduce the window size
                    if total - nums[start] >= target:
                        total -= nums[start]
                        start+=1
                    else:
                        break
                min_len = end-start+1 # update the solution
            
            # slide the window
            end+=1
            if end < n:
                total += nums[end] - nums[start]
            start+=1

        return min_len             


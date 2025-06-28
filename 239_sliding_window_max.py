# import heapq
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # maintain a monotonic deque whose first element is always the maximum element
        q = deque()
        result = []
        curr = 0
        # for first k-1 elements we do not update the result because we don't have the whole window formed.
        # suppose curr in the index of the element which we have to insert into the deque. If it is greater than the last element of the deque, then we just pop the last element. This is because, in all the windows in which the last element will be in from now on, the current element will also be there, since current element is already bigger than the last element, it can never be the max, so popping it won't hamper our calculations

        # so till we find smaller elements in the deque, we pop them and then insert our current element
        while curr < len(nums):
            while q and q[-1] < nums[curr]:
                q.pop()
            
            q.append(nums[curr])

            # we check if current maximum needs to be deleted
            if curr>=k and nums[curr-k]==q[0]:
                q.popleft()
                
            # check if we can add to result
            if curr>=k-1:
                result.append(q[0])
            
            curr+= 1
        
        return result
            





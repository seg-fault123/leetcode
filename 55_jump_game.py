class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = len(nums)-1
        for i in range(n-2, -1, -1):
            max_reach = nums[i] + i
            # if I can reach the goal from here, the previous positions only need
            # to reach to the current position to recah to the last index. So I 
            # update the goal
            goal = i if max_reach >= goal else goal
        
        return goal==0 


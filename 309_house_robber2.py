class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(start, end):
            result_1, result_2 = 0, 0
            for i in range(start, end+1):
                result_2, result_1 = result_1, max(result_1, nums[i]+result_2)
            
            return result_1
        # first exclude the first entry, then exclude the last entry
        return max(rob_linear(0, len(nums)-2), rob_linear(1, len(nums)-1))

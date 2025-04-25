# Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        total = 0
        for element in nums:
            if total < 0:
                total = 0
            total += element
            result = max(result, total)
        return result

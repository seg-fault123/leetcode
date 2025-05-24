class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        curr_max = 1
        curr_min = 1
        for n in nums:
            temp1 = curr_max*n
            temp2 = curr_min*n
            curr_max = max(temp1, temp2, n)
            curr_min = min(temp1, temp2, n)
            result = max(result, curr_max)
        return result

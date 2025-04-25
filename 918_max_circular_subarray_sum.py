class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_all = 0 # for the whole array
        total_max = 0 # for the non circular case
        total_min = 0 # for the circular case
        # we will calculate the max subarray sum and min subarray sum for 
        # non circular case. For min sub array sum, we calculate the max subaarray
        # sum of the negative of the numbers and take the negative of the result.
        # the max sub array sum for the circular case is the total sum - min subarray
        # sum. We return max of the circular and non circular case
        result_max = nums[0]
        result_min = -nums[0]
        for num in nums:
            total_all += num
            if total_max < 0:
                total_max = 0
            if total_min < 0:
                total_min = 0
            total_max += num
            total_min -= num
            result_max = max(result_max, total_max)
            result_min = max(result_min, total_min)
        
        result_circ = total_all + result_min

        # if all numbers are negative then result_circ will be 0, in that case, 
        # the greatest number is the answer and it will be captured by result_max
        if result_circ == 0:
            return result_max
        else:
            return max(result_max, result_circ)

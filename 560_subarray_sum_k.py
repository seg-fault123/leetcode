class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        current_sum = 0
        prefix_sum = {0: 1}
        # at each position we maintain the sum till that position from the beginning. Now At each position we check what amount can be subtracted from the current cum_sum to achieve the target k. This value is equal to current_sum - k.
        # If this value is already there in the prefix_sum, we know that there exits subarrays starting from the beginning which can be deleted/chopped off, because after chopping them, we will achieve the target with the remaining subarray. Whatever is the count of prefix_sum[current-k], those many subarrays can be created to make the target.
        # so maintain a map where keys are cum_sums and value is the count of the cum_sums encountered till now.
        # prefix[0] = 1 intially beacuse it represents, that if current_sum=k, then chop nothing off and keep the array as it is. The base case.
        for num in nums:
            current_sum += num
            result += prefix_sum.get(current_sum-k, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        
        return result

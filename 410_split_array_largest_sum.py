class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # the minimum  answer is equal to the maximum number present in the array and any subaaray with that element will be atleast that amount.
        # the max answer for safety will be equal the sum of the total array. The answer lies within this range.
        # we apply binray search within this range to check for the answer
        # to check if a target value is valid, the array can be split into atmost k arrays with each having sum less than target, we try to greedily create such subarrays.
        def is_valid(target, k):
            curr_sum = 0
            n_arrays = 0
            for num in nums:
                curr_sum += num
                # if the current subarray exceeds target, create new subarray
                if curr_sum > target:
                    curr_sum = num
                    n_arrays += 1
            # check if num sub arrays is less than k
            return n_arrays + 1 <= k
        
        start = max(nums)
        end = sum(nums)
        while start <= end:
            mid = (start+end)//2

            if is_valid(mid, k):
                end = mid - 1
            else:
                start = mid + 1
        
        return start
        


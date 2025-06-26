class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # xor all indices and the actual number, then xor the len(nums). This will mae sure that all numbers in the range [0, n] have been xored once. The elements present in the arr will be xor twice cancelling out. Only the missing number will be xor once, so that will be remaining
        result = 0

        for i in range(len(nums)):
            result ^= i^nums[i]
        
        result ^= len(nums)
        return result

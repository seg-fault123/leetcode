class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutation(nums, current):
            if len(nums)==0:
                return [current]
            result = []
            for i in range(len(nums)):
                result += permutation(nums[:i]+nums[i+1:], current+[nums[i]])
            return result
        return permutation(nums, [])
            
        

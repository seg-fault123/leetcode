class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1 # place holder of the next unique value
        for curr in range(1, len(nums)):
            # if unique is encountered, place at correct position
            if nums[curr-1] != nums[curr]:
                nums[k] = nums[curr]
                k += 1
        
        return k

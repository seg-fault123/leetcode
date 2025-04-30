class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_index={}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in val_index:
                return [i, val_index[needed]]
            else:
                val_index[nums[i]] = i
        

            
            


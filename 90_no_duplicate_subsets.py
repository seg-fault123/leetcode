class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def power_set(index, current):
            if index>=len(nums):
                return [current]
            
            temp = power_set(index+1, current+[nums[index]])
            next_index = index+1
            while next_index < len(nums) and nums[next_index-1]==nums[next_index]:
                next_index+=1
            temp += power_set(next_index, current)

            return temp
        
        return power_set(0, [])

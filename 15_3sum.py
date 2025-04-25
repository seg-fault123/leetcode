class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        # first we fix index i and then move index j and k such that their sum is 0
        for i in range(len(nums)-2):
            # if i is already encountered, move on as the triplets produced will be same
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i+1
            k = len(nums) -1
            while j < k:
                target = nums[i] + nums[j] + nums[k]
                if target > 0:
                    # need something les, so decrement k in the hope that 
                    # something less is picked and valid triplet is produced
                    k -= 1
                elif target < 0:
                    # need something more, so increment j in the hope that 
                    # something more is picked and valid triplet is produced
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # to avoid duplicate triplets
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        
        return result

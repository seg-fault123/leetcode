class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def three_sum(fourth, start):
            result = []
            for i in range(start, len(nums)-2):
                if i > start and nums[i-1]==nums[i]:
                    continue
                j = i+1
                k = len(nums)-1
                while j < k:
                    total = fourth + nums[i] + nums[j] + nums[k]
                    if total < target:
                        j += 1
                    elif total > target:
                        k -= 1
                    else:
                        result.append([fourth, nums[i], nums[j], nums[k]])
                        j += 1
                        while j < k and nums[j]==nums[j-1]:
                            j +=1
            return result
        
        result = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            result.extend(three_sum(nums[i], i+1))
            print(result)
        
        return result



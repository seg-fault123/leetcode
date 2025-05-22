class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def permute(arr, current):
            if len(arr)==0:
                result.append(current)
            for i in range(len(arr)):
                if i>0 and arr[i-1]==arr[i]:
                    continue
                permute(arr[:i]+arr[i+1:], current+[arr[i]])
        permute(nums, [])
        return result
        

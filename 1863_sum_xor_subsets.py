class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        for element in nums:
            result = result | element
        
        return result << (len(nums) - 1)


        # instead of calculating the subsets explicitly, we just maintain the
        # xor_total of the subset

        # self.total = 0
        # def dfs(index, current_xor):
        #     if index == len(nums):
        #         self.total += current_xor
        #         return
        #     dfs(index+1, current_xor)
        #     dfs(index+1, current_xor ^ nums[index])

        # dfs(0, 0)
        # return self.total



        # def power_set(arr, index=0, current=[]):
        #     if len(arr) == index:
        #         return [current]
        #     return power_set(arr, index+1, current) + power_set(arr, index+1, current+[arr[index]])
        
        # xor_sum = 0
        # for subset in power_set(nums):
        #     if len(subset) == 0:
        #         continue
        #     xor_temp = subset[0]
        #     for i in range(1, len(subset)):
        #         xor_temp = xor_temp ^ subset[i]
        #     xor_sum += xor_temp
        
        # return xor_sum

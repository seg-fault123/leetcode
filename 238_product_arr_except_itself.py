class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n 
        current = 1
        for i in range(n):
            result[i] *= current
            current *= nums[i]
        # after this step, result[i] will be the product from nums[0] till nums[i-1], product from left excluding this term, 1 for result[0]

        # similarly adding the product from right side excluding itself
        current = 1
        for i in range(n-1, -1, -1):
            result[i]*=current
            current*=nums[i]

        # after this step, result[i] will be product from both left and right sides excluding itself

        return result 



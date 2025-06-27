class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #  boyers moores algo

        count = 0
        majority = None
        for num in nums:
            if num==majority:
                count += 1
            elif count==0:
                majority = num
                count = 1
            else:
                count -= 1
        
        return majority

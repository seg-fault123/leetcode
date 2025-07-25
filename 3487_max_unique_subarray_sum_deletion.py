class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        total = 0
        unique = set()
        max_element = float('-inf')
        for num in nums:
            max_element = max(max_element, num)
            if num >= 0 and num not in unique:
                # if the num is greater than zero then it would add to the sum. If it is not present, then add it
                total += num
                unique.add(num)
            
            # if the positive number was already present, then its contribution has already been added to the total. Moreover, it can be thought that previous occurrence was deleted and now we consider the current occurrence. 
        

        # if the max_element is negative, then return the max_element as that is the maximum subarray total, addidng anything will only reduce the total
        return total if max_element > 0 else max_element


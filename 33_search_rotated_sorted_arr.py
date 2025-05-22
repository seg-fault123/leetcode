class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the index of minimum element, if the target is less than equal to nums[-1], then find between this index and nums[-1], else find between nums[0] and nums[index-1]
    
        n = len(nums)
        start = 0
        end = n-1
        while start <= end:
            mid = (start+end)//2
            if nums[start] > nums[mid] or nums[mid] < nums[end]:
                end = mid
            else:
                start = mid + 1
        
        min_element = end
        if target <= nums[-1]:
            start = min_element
            end = n-1
        else:
            start = 0
            end = min_element - 1
        
        while start <= end:
            mid = (start + end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] < target:
                start = mid+1
            else:
                end = mid - 1
        
        return -1

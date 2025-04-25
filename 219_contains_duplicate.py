class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        unique=set()
        for i in range(min(k+1, len(nums))):
            if nums[i] in unique:
                return True
            else:
                unique.add(nums[i])
        for i in range(k+1, len(nums)):
            unique.remove(nums[i-k-1])
            if nums[i] in unique:
                return True
            else:
                unique.add(nums[i])
        return False

# since I have to constantly check if a number is in a window of numbers, and
# keep adding and removind elements based on the window, a set is the best data structure 
# to use which has average O(1) time complexity for all these operations

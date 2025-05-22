class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums)-1
        # we will check which part is sorted part of the array and check if the target is present in the sorted part. If yes, we search in the sorted part, otherwise search in the unsorted part. If we cannot decide which part is sorted part, then just increment left by 1.

        while start <= end:
            mid = (start+end)//2
            if nums[mid]==target:
                return True
            elif nums[start]==nums[mid]:
                # duplicated encountered
                # cannot decide which part is sorted part since this case arise in the followinf two cases:
                # [1, 1, 2] (mid is index 1 and left part is sorted)
                # [1, 2, 1, 1, 1] (mid is index 2 and right part is sorted)
                # since duplicates are encounterd, moving the left index does not harm
                start += 1
                continue
            
            elif nums[start] < nums[mid]:
                # left part is sorted
                if nums[start] <= target < nums[mid]:
                    # target lies in the sorted range, search in that range
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                # right part is sorted
                if nums[mid] < target <= nums[end]:
                    # target lies in sorted range, search in sorted range
                    start = mid + 1
                else:
                    end = mid - 1
        
        return False
            
            
            
        

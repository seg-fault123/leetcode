# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

# lee's solution (same approach but more optimized way)
# https://leetcode.com/problems/find-in-mountain-array/solutions/317607/java-c-python-triple-binary-search/
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        start = 0
        end = n-1
        values = {-1: float('-inf'), n: float('inf')}
        mount = None
        # search for the peak element
        # search for target in strictly increasing array, if not found then strictly search for target in strictly decreasing array.
        while start <= end:
            mid = (start+end)//2
            mid_element = None
            if mid not in values:
                values[mid] = mountainArr.get(mid)
            mid_element = values[mid]
            
            prev_element = None
            if mid-1 not in values:
                values[mid-1] = mountainArr.get(mid-1)
            prev_element = values[mid-1]

            next_element = None
            if mid+1 not in values:
                values[mid+1] = mountainArr.get(mid+1)
            next_element = values[mid+1]
            if prev_element < mid_element > next_element:
                # peak is found
                mount = mid
                break
            elif prev_element < mid_element:
                start = mid + 1
            else:
                end = mid - 1
        
        if target == values[mount]:
            return mount
        
        start = 0
        end = mount -1
        while start <= end:
            mid = (start+end)//2
            mid_element = None
            if mid not in values:
                values[mid] = mountainArr.get(mid)
            mid_element = values[mid]
            if mid_element==target:
                return mid
            elif mid_element < target:
                start = mid + 1
            else:
                end = mid -1 
        
        start = mount + 1
        end = n-1
        while start <= end:
            mid = (start+end)//2
            mid_element = None
            if mid not in values:
                values[mid] = mountainArr.get(mid)
            mid_element = values[mid]
            if mid_element==target:
                return mid
            elif mid_element < target:
                end = mid -1 
            else:
                start = mid + 1
        
        return -1
        

        


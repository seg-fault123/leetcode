from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find the left and right pointers such that left points to the position smaller than x and right points to position greater than x
        def binary_search(x):
            start = 0
            end = len(arr)-1
            while start <= end:
                mid = (start+end)//2
                if arr[mid] == x:
                    # if you find the element, make left the pointer that points to its position
                    return mid, mid+1
                elif arr[mid] < x:
                    start = mid+1
                else:
                    end = mid -1
            # start points to the position x would have taken if it would be added to array. Hence, start points to an element greater than x. Similarly end points to a position smaller than x 
            return end, start
        left , right = binary_search(x)
        result = deque()
        # check if left and right are valid positions
        while left>=0 and right<len(arr) and k>0:
            if abs(arr[left]-x) <= abs(arr[right]-x):
                result.appendleft(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
            k -= 1
        
        while left>=0 and k>0:
            result.appendleft(arr[left])
            left -= 1
            k -= 1
        
        while right < len(arr) and k>0:
            result.append(arr[right])
            right += 1
            k -= 1
        
        return list(result)

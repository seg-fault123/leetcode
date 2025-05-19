class Solution:
    def maxArea(self, height: List[int]) -> int:
        # we start with the maximum width, farhest possible points
        # we keep the longer pipe, since only an increase in height can improve 
        # the solution
        max_area = 0
        left = 0
        right = len(height)-1
        while left < right:
            area = 0
            if height[left] < height[right]:
                area = (right - left)*height[left]
                left += 1
            else:
                area = (right-left)*height[right]
                right -= 1
            max_area = max(area, max_area)
        
        return max_area

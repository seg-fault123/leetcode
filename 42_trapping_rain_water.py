class Solution:
    def trap(self, height: List[int]) -> int:
        # the main intuition is that the water trapped at current position can be calculated as follows:
        # calculate the max height of the bars present at the left of the position
        # calculate the max heigth of the bars present at the right of the position
        # take the minimum of these two heights call it "temp"
        # subtract current height from temp to get the water
        # if result is negative then 0 water can be stored.
        # in the optimal solution, we don't need to calculate the max height values for each position, simply two pointers can help 

        left = 0 # to keep track of position
        right = len(height) - 1 # to keep track of position
        max_left = height[left]  # max height encountered till left (includes left)
        max_right = height[right] # max height encounterd till right (includes right)
        water = 0 # the total water trapped (result)

        while left < right:
            if max_left < max_right:

                left += 1
                # now at this updated left position (we treat this as current position), we have the correct max height from the left. Even though we might not have the correct max height from the right (wrt to the current position), the correct max height from the right will only increase and be greater than max height from the left. Since we only care about the min of the max heights, max_left will be chosen for water calculation
                # first max_left is updated because it avoids the need for negative water
                max_left = max(max_left, height[left])
                water += max_left - height[left]
            else:
                right -= 1
                # now at this updated right position (we treat this as current position), we have the correct max height from the right. Even though we might not have the correct max height from the left (wrt to the current position), the correct max height from the left will only increase and be greater than max height from the right. Since we only care about the min of the max heights, max_right will be chosen for water calculation
                max_right = max(max_right, height[right])
                water += max_right - height[right]
        
        return water

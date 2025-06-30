class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # maintain how much a bar can be extended to both left and right
        stack = []
        result = 0
        n = len(heights)
        for i in range(n):
            prev_index = i # to track till which index the current bar can be extended towards the left (backwards)
            # if the previous bar stored in the stack is larger, that bar cannot be extended to the right, so pop it and note its index.
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                width = i - index # calculate how much can it be extended
                result = max(result, height*width) # update the area
                prev_index = index # since that bar was larger than the current bar, the current bar can be extended backwards, so update the prev index
            
            # insert into the stack either empty or has a bar smaller/equal to the current bar
            stack.append((prev_index, heights[i]))
        
        # all bars left in the stack can be extended till the end, calculate the area
        while stack:
            index, height = stack.pop()
            width = n - index
            result = max(result, height*width)
        
        return result


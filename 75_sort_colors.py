class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0 # the index before which all numbers are 0,
        white = 0 # the current index before which all numbers are 0 or 1 in sorted order
        blue = len(nums)-1 # the index after which all numbers are 2
        while white <= blue:
            if nums[white]==0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 2:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
            else:
                white += 1
        
        return

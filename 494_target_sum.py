class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # maintain the map of possible_sums and counter
        # for each number in array, add and subtract from the current possible sums and update the count of new sums appropritely.
        possible_sums = {0:1}
        for i in range(len(nums)-1, -1, -1):
            temp = {}
            for total in possible_sums:
                temp[total-nums[i]] = temp.get(total-nums[i], 0) + possible_sums[total]
                temp[total+nums[i]] = temp.get(total+nums[i], 0) + possible_sums[total]
                            
            possible_sums = temp
        
        return possible_sums.get(target, 0)


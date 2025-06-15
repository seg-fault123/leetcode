class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        # if num-1 is not in num_set, then it is the start of a sequence
        for num in num_set:
            if num-1 not in num_set:
                temp = num+1
                while temp in num_set:
                    temp += 1
                max_length = max(max_length, temp-num)
        return max_length
        

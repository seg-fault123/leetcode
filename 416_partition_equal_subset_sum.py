class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # if sum cannot be divided by 2 then it can't be split, return False
        if total%2!=0:
            return False
        
        # keep a set of possible sums, if total/2 is encountered, return true
        possible_sums = {0}
        for num in nums:
            new_set = set()
            for t in possible_sums:
                if t+num==total/2:
                    return True
                elif t+num<total/2:
                    new_set.add(t+num)
            possible_sums |= new_set

        return False

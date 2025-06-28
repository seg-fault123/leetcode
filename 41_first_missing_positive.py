class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # the answer always lies in the interval [1, len(nums)+1]. All numbers outside this range are irrelevant. So first we iterate throught the array and replace these numbers with some sentinal value.
        # we will use the array itself to keep track of the numbers that have been seen far. Since all negative numbers numbers were replaced by a high sentinal value in the previous step, we use negative numbers to keep track.
        # the procedure is as follows, if we encounter a sentinal value, we skip, otherwise if see a value between x belongs [1, len(nums)] we go to index x-1 and make the number there to be negative. So we use index positions to mark the seen numbers. Since in the current step, we can mark a later index to be negative, we have to check for abs(x) rather than just x.
    
        # then we again iterate through the array, the first index i where the value is still positive, i+1 is our result. If all indices contain negative, we return len(nums)+1.
        # the sentinal value can be len(nums)+1 because it is the first integer which does not have an index associated to it.

        n = len(nums)
        for i in range(n):
            if nums[i]<=0 or nums[i]>n:
                nums[i] = n+1
        
        for i in range(n):
            num = abs(nums[i])
            if num<=n and nums[num-1]>0:
                nums[num-1] *= -1
        
        for i in range(n):
            if nums[i]>0:
                return i+1
        
        return n+1

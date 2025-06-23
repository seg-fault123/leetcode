class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # thresh = len(nums)//3
        # counts = {}
        # for num in nums:
        #     counts[num] = counts.get(num, 0) + 1
        
        # return [num for num in counts if counts[num]>thresh]

        # there cannot be more than 2 elements in the array that have more than [n/3] occurrences
        # idea like Boyer Moores algo to find an element which occurs more than half times. In this case we find two majority elements and verify if they are actually the majority

        majority_1=majority_2=count_1=count_2=0
        for num in nums:
            if num==majority_1:
                count_1 += 1
            elif num==majority_2:
                count_2 += 1
            # replace if count is zero for any element
            elif count_1==0:
                majority_1 = num
                count_1 = 1
            elif count_2==0:
                majority_2 = num
                count_2 = 1
            else:
                count_1 -= 1
                count_2 -= 1
        # verify the result
        count_1 = count_2 = 0
        for num in nums:
            if majority_1==num:
                count_1 += 1
            elif majority_2==num:
                count_2 += 1
        
        res = []
        thresh = len(nums)//3
        if count_1 > thresh:
            res.append(majority_1)
        if count_2 > thresh:
            res.append(majority_2)
        return res

        

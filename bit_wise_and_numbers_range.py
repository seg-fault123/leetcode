import math
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left==right:
            return left

        # find number of differing bits, remove those bits, take bit wise and after removing, left shift the result by adding the redundant bits
        bit_diff = math.log(right-left, 2)
        
        bit_diff = int(bit_diff) + 1

        temp = bit_diff
        while left!=0 and temp>0:
            left >>= 1
            right >>= 1
            temp -= 1
        
        return (left&right)<<bit_diff

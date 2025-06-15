class Solution(object):
    def getSum(self, a, b):
        # Xor gives addition without carry, And followed by left shift gives carry
        # the new problem becomes adding xor output with carry. Perform this until carry becomes 0
        mask = 0xffffffff
        max_int = 2**31-1
        while b!=0:
            temp = (a&b)<<1
            a = ((a^b)&mask)
            b = (temp&mask)

        return a if a<=max_int else ~(a^mask)

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # so wherever we find a 1 in x's bit representation, that bit cannot be changed and has to be 1 in all the numbers in the array.
        # wherever there is a zero in x's representation, that bit can be 0 or 1.
        # so we will manipulate only those bits where 0 is found
        # one observation is that the dirst element of the array will always be x. No number smaller than x can be the first element of the array
        # so now we want to find n-1 elements.
        # The basic trick is to create n-1 combinations using the least significant 0 bits of x.
        # now, lets ask this question, what is the least amount of bits required to create n-1 combinations. The answer is whatever is present in the bit representation of n-1.
        # so whatever is the bit representation of n-1, if we insert that into the 0 bits of x, we have essentially found n-1 combinations such that all of them have the same corresponding set bits as x, these are the smallest possible numbers because we have used the least amount of bits required to create n-1

        bit_x = 1 # the mask that will be used to check x
        n = n-1 # update n
        while n>0:
            if (x & bit_x) == 0:
                # free bit is found
                # find the last bit of n and set that as the current bit of x at the free position
                x |= (n&1)*bit_x
                n >>= 1 # free this bit and move to the next significant bit
            
            bit_x <<= 1

        return x


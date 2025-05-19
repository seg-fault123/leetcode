class Solution:
    def reverseBits(self, n: int) -> int:
        # string = bin(n)[2:][::-1]
        # string = string + '0'*(32-len(string))

        # return int(string, 2)

        result = 0
        for _ in range(32):
            result <<= 1
            result |= (n&1)
            n >>= 1
        
        return result
        

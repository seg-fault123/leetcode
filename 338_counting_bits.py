class Solution:
    def countBits(self, n: int) -> List[int]:
        # number of set bits in a number is equal to:
        # 1 + number of set bits in the right shift (divide by 2) of the number if
        # the number is odd
        # number of set bits in the right shift of the number if the number is even
        result = [0]
        for i in range(1, n+1):
            if i%2 == 1:
                result.append(1+result[i//2])
            else:
                result.append(result[i//2])
        return result

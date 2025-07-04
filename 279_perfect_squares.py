class Solution:
    def numSquares(self, n: int) -> int:
        # generalized coin change problem where instead of given denominations we have options in perfect squares
        # collect all the perfect squares
        perfect_squares = []
        for i in range(1, n+1):
            if i*i <= n:
                perfect_squares.append(i*i)
            else:
                break
        # check is n is itself a perfect square
        if perfect_squares[-1]==n:
            return 1
        
        # min_squares[i] is the result for n=i
        min_squares = [float('inf')]*(n+1)
        min_squares[0] = 0
        # add each denomination one by one
        for square in perfect_squares:
            min_squares[square] = 1
            for num in range(square+1, n+1):
                # check if by adding this denomination, can the result be reduced
                min_squares[num] = min(min_squares[num], min_squares[num-square]+1)
        
        return min_squares[-1]

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # max possible stones with start, end, both inclusive
        memo = {}
        cum_total = [] # holds the cummulative sum, will be needed later
        curr = 0
        for num in piles:
            curr += num
            cum_total.append(curr)

        def optimal(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            elif start==end:
                # only one choice
                memo[(start, end)] = piles[start]
                return piles[start]
            
            # calculate the total stones in the subarray [start:end] both included, here cum_sum is needed
            total = None
            if start==0:
                total = cum_total[end]
            else:
                total = cum_total[end] - cum_total[start-1]
            
            # next chance will be of opponent, which want to minimize
            # if we choose pile[start], opponent will gain optimal(start+1, end) out of total, hence we will have total-optimal(start+1, end). Similarly we will have total-optimal(start, end-1) if we choose pile[end]. Maximize between these choices
            result = max(total - optimal(start+1, end), total - optimal(start, end-1))
            memo[(start, end)] = result
            return result
        
        alice = optimal(0, len(piles)-1)

        return alice>cum_total[-1]/2


        # Alice will always win actually. If summation of piles present at the even indices is greater than summation of piles present at the odd indices, alice always picks even.
        # piles[0]+piles[2]+ ...+ piles[n-2] > piles[1]+piles[3]+...+piles[n-1]
        # this is possible beacuse alice will always have a choice to pick between an even index and an odd index.
        # Initially with 0 and n-1, alice picks 0, Bob will be left with choice between, 1 and n-1, both odd. Next alice chance will always have an even index.

        # similary if the other case is true, alice always picks the odd indices, leaving bob with even ones.
        # Hence alice always wins
        # return True
        

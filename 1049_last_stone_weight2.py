class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        '''
        Let me also chip in for EXPLAINing why this is a KNAPSACK problem.

For any sequence of operations, the algebra boils down to difference of two sums

For example,
(((a - b) - c) - d) = a - b - c - d = (a) - (b + c + d)
((d - (a - b) )- c) = d - a + b - c = (d + b) - (a + c)

Given that if there are two or more items, we have to do a subtraction ( two stones reduce to 0 or another stone ), it's guaranteed that there will be two groups of items.

Hope it's clear so far.
This is why, the original problem of finding the smallest difference (remaining stone) reduces to finding two complementary sets of (mutually exclusive) items, with the idea that:

the potential answer to the question is the difference of the sums of these two groups
this is an optimization problem, so we want to minimize the difference between the sums
The optimization problem explained:

Since we are finding two complementary sets of items, it's sufficient to find one set. (The other one is complementary!)
We are interested in minimizing the difference in sums of these sets.
The sets are not empty. In other words we can't have all items in one set.
So this reduces to the problem of finding a set whose sum is as close to total/2 as possible. Because the sum of the complementary set will be total - this_sum. Hence the "potential" answer will be (total - this_sum) - this_sum
-- This value to be minimum we want total - 2 * this_sum ==> 0 (close to 0)
--- This means total ==> 2 * this_sum
--- Meaning this_sum ==> total / 2
This is a knapsack problem where we want to find a set of items that sum to a maximum of total / 2, maximally so. We are only limited by the sum having to be <= total / 2.
So how do we solve this problem? Find all subsets of the original set, find their sum, keep track of the sum that is <= total / 2. If we ever reach sum = total / 2, we are done. No need to keep going. If we reach sum > total / 2 discard those values.
This author's solution for generating all possible combinations is:
-- keep track of sums with each item included or not included, in combination with already generated sets. (I know this is kind of oversimplified, that's what it is)
        '''

        possible_sums = {0}
        total = sum(stones)
        for num in stones:
            temp = set()
            for element in possible_sums:
                new_sum = num+element
                if new_sum == total/2:
                    return 0
                elif new_sum < total/2:
                    temp.add(new_sum)
            possible_sums |= temp

        return min(abs(total - summation - summation) for summation in possible_sums)
            

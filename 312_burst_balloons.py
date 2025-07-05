class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # add padding to both ends, only to make calculation simpler
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        # dp[start][end] includes the result for sub array starting from start and ending at end both inclusive
        # we create a window of size 1,2,....,n-2 (n-2) is the size of the original array
        for size in range(1, n-1):
            for start in range(1, n-size):
                end = start+size-1
                # for each position in the inerval [start, end], we check what if ith balloon is the last one to pop. This way, since ith ballon is the last one to burst, so, the balloons in subarray [start, i-1] and [i+1, end] will be popped first and there will be clear boundary between these arrays. The boundary will be the ith balloon itself. Hence these two sub problems can be calculated independently.
                # the position i, that yield the maximum result for interval [start, end] will serve as the result dp[start][end]
                for i in range(start, end+1):
                    result = dp[start][i-1] + nums[start-1]*nums[i]*nums[end+1] + dp[i+1][end]
                    # dp[start][i-1] will already be calculated since it has a size less than the current size. This will be equal to the maximum coins gained in the subarray left of the i. When i=start, dp[start][start-1] will yield 0 as we are checking in the interval of lenght -1 (not possible)
                    # nums[start-1]*nums[i]*nums[end+1] is the balloons gained by popping the ith balloon at the end. Since ith balloon i is popped at the end, the boundaries will be start-1 and end+1 respectively.
                    # dp[i+1][end] will similarly be already computed (less window size). Maximum coins gained in the subarray right of i. When i=end, dp[end+1][end] will yield 0 (-1 interval, not possible)
                    dp[start][end] = max(dp[start][end], result)
        
        # the final result will be dp[1][n-2], the new indices of first and last element of the original array
        return dp[1][n-2]

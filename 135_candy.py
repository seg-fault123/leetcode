class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]*len(ratings)
        # traverse the ratings twice once seing the next neighbor, and once seing the previous neighbor
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = 1 + candies[i-1]
        
        result = 0

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], 1+candies[i+1])
            result += candies[i]
        
        return result+candies[-1]

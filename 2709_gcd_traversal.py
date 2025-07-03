import math
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        
        adj_list = defaultdict(list) # which indices are connected

        # yields the prime factors of num
        def get_prime_factors(num):
            for i in range(2, int(math.sqrt(num))+1):
                if num%i==0:
                    # reduce num until this factor cannor divide num
                    # this is done to prevent multiples of i to be registered as prime factors
                    while num%i==0:
                        num //= i
                    yield i
            
            if num!=1:
                yield num
        
        prime_index = {} # key is prime number and value is the first index that has nums[index] which has this prime factor as one of the factors.

        for i, num in enumerate(nums):
            if num==1:
                return False # gcd will always be 1

            for prime in get_prime_factors(num):
                if prime in prime_index:
                    # add edge between this index and the previous index which had this as a prime factor
                    index = prime_index[prime]
                    adj_list[i].append(index)
                    adj_list[index].append(i)
                else:
                    prime_index[prime] = i
        
        visited = [False]*len(nums)

        def dfs(node):
            visited[node] = True
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        dfs(0)
        # if any node is still not visited then it means that it cannot be visited and the graph is not connected 
        for i in range(len(nums)):
            if not visited[i]:
                return False
        
        return True
            

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # O(k^n), each element has k options to go into one of the subsets, TLE
        total = sum(nums)
        if total%k!=0:
            return False

        target = total//k
        sums = [0]*k
        nums.sort(reverse=True)
        def partition(index, k, target):
            # print(sums)
            if index == len(nums):
                for i in range(k):
                    if sums[i]!=target:
                        return False
                return True
            
            for i in range(k):
                if sums[i]+nums[index] <=target:
                    sums[i] += nums[index]
                    if partition(index+1, k, target):
                        return True
                    sums[i] -= nums[index]

                    if sums[i]==0:
                        # it means that we added first element to subset but that also failed. Erroneus assignment has been done by previous steps. Return False
                        break
            
            return False
        
        return partition(0, k, target)

        

        # O(k2^n) create one subset at a time
        # total = sum(nums)
        # if total%k != 0:
        #     return False
        
        # target = total//k

        # visited = [False]*len(nums)

        # def create_subset(index, remaining, curr_sub, target):
        #     if remaining==1:
        #         return True
        #     elif curr_sub == target:
        #         return create_subset(0, remaining-1, 0, target)
            
        #     for i in range(index, len(nums)):
        #         if not visited[i] and curr_sub + nums[i] <= target:
        #             visited[i] = True
        #             if create_subset(index+1, remaining, curr_sub+nums[i], target):
        #                 return True
        #             visited[i] = False
            
        #     return False
        
        # nums.sort(reverse=True)
        # return create_subset(0, k, 0, target)

                

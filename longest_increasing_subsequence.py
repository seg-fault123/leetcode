# https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn/


# an O(n^2) dp solution exists wherin you check for each index you check what is the max subsequence 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        # gives the correct index of insertion in sub
        def binary_search(target):
            start = 0
            end = len(sub)-1
            while start <= end:
                mid = (start+end)//2
                if sub[mid]==target:
                    return mid
                elif sub[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return start
        
        for i in range(1, len(nums)):
            element = nums[i]
            # if new element is the largest wrt to all elements in sub, extend sub
            if element > sub[-1]:
                sub.append(element)
            else:
            # update sub by replacing eith element at the correct index
                index = binary_search(element)
                sub[index] = element
        
        return len(sub)

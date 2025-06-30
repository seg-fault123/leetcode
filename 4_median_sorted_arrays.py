class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        n1 = len(nums1)
        n2 = len(nums2)
        half = (n1+n2)//2 # we would need these many elements in the left hand side of the merged sorted array. If the total number is odd, the the number at (half+1)th element in the merged sorted array is the median
        # otherwise it is the mean of (half)th and (half+1)th element in the merged sorted array.

        # we try to find the indices i and j such that A[:i+1] and B[:j+1] form the first half elements of the merged sorted array. So half = i + j + 2. 
        # we binary serach i in the range(0, n1) and we always make sure that if we consider first i+1 elements from A, then we automatically consider first j+1 elements from B such that their sum is half. 
        # In this manner we try we try to partition A and B such that the lower partitions of these arrays gives us the first half of the elements in the merged sorted array.
        # Suppose we find such a partition, then as discussed above, if the total is odd, then the median is the next element in the order after half elements. That can be extracted with min(A[i+1], B[j+1]). Otherwise it is the mean of (half)th and (half+1)th element in the merged sorted array. (half)th element is max(A[i], B[j]) and (half+1)th element is min(A[i+1], B[j+1])

        left = 0
        right = n1 -1
        while True:
            i = (left+right)//2
            j = half - i -2

            left1=None
            right1 = None
            # check if i is in bounds
            if i>=0:
                left1 = nums1[i]
            else:
                # means that don't consider any element from nums1 in half
                left1 = float('-inf')
            
            if i+1 < n1:
                right1 = nums1[i+1]
            else:
                # means that consider all elements of nums1 in half
                right1 = float('inf')
            
            # similarly
            left2 = nums2[j] if j>=0 else float('-inf')
            right2 = nums2[j+1] if j+1<n2 else float('inf')

            # check if we encounter a valid 
            if left1<=right2 and left2<=right1:
                if (n1+n2)%2==1:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2))/2
            elif left1 > right2:
                # we have kept more elements in the partition of nums1
                right = i - 1
            else:
                # we have kept less elements in partiton of nums2
                left = i+1
        
        return None

            

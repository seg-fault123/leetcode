class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        max_size = 1
        greater_needed = None
        current_size = 1
        for i in range(1, n):
            if greater_needed is None:
                if arr[i-1] < arr[i]:
                    current_size += 1
                    greater_needed = False
                elif arr[i-1] > arr[i]:
                    current_size +=1
                    greater_needed = True
                else:
                    current_size = 1
                    greater_needed = None
            elif greater_needed:
                if arr[i-1] < arr[i]:
                    current_size += 1
                    greater_needed = False
                elif arr[i-1] > arr[i]:
                    current_size = 2
                    greater_needed = True
                else:
                    current_size = 1
                    greater_needed = None
            else:
                if arr[i-1] < arr[i]:
                    current_size = 2
                    greater_needed = False
                elif arr[i-1] > arr[i]:
                    current_size += 1
                    greater_needed = True
                else:
                    current_size = 1
                    greater_needed = None
            max_size = max(max_size, current_size)
        
        return max_size

        

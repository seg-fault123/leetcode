class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def index_cord(index, n):
            return index//n, index%n
        def matrix_entry(index, matrix, n):
            r, c = index_cord(index, n)
            return matrix[r][c]

        m, n = len(matrix), len(matrix[0])
        start = 0
        end = m*n-1

        while start <= end:
            mid= (start+end)//2
            mid_val= matrix_entry(mid, matrix, n)
            if mid_val == target:
                return True
            elif mid_val < target:
                start = mid+1
            else:
                end=mid-1
        return False


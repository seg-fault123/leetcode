class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def row_reverse(n):
            for j in range(n):
                start = 0
                end = n-1
                while start < end:
                    matrix[start][j], matrix[end][j] = matrix[end][j], matrix[start][j]
                    start += 1
                    end -= 1
        

        def transpose(n):
            for i in range(n):
                for j in range(i+1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
    
        n = len(matrix)
        row_reverse(n)
        transpose(n)
        

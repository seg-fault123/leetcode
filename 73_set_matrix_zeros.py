class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # we use the firt column to record which rows (except first) have zeros in them
        # we use the first row to record which columns (except first) have zeros in them
        # for frist row and column, we keep track of them having zeros separately
        m, n = len(matrix), len(matrix[0])
        row_zero = False
        col_zero = False

        # check if first column has a zero
        for i in range(m):
            if matrix[i][0]==0:
                col_zero = True
                break
        
        # check if first row has a zero
        for j in range(n):
            if matrix[0][j]==0:
                row_zero=True
                break
        
        # checking for all elements (except in first column and row) and update accordingly
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        # if a row (except first) has zero, 0 the whole row. We don't check the first row because the first row contains information about which columns have zeros. So if we zero the whole first row, we lose the column info
        for i in range(1, m):
            if matrix[i][0]==0:
                for j in range(n):
                    matrix[i][j]=0

        # similarly zero the whole column (except the first column)
        for j in range(1, n):
            if matrix[0][j]==0:
                for i in range(m):
                    matrix[i][j]=0

        # check if the first col had a zero, if yes then zero it
        if col_zero:
            for i in range(m):
                matrix[i][0]=0
        
        # check if the first row had a zero, if yes zero it
        if row_zero:
            for j in range(n):
                matrix[0][j]=0
        
        return

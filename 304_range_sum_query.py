class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.cum_sum = matrix
        m = len(matrix)
        n = len(matrix[0])

        for i in range(1, m):
            self.cum_sum[i][0] += self.cum_sum[i-1][0]
        for j in range(1, n):
            self.cum_sum[0][j] += self.cum_sum[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                self.cum_sum[i][j] += self.cum_sum[i-1][j] + self.cum_sum[i][j-1] - self.cum_sum[i-1][j-1]
         
    def get_cum_sum(self, row, col):
        if row<0 or col<0:
            return 0
        else:
            return self.cum_sum[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.cum_sum[row2][col2] - self.get_cum_sum(row1-1, col2) - self.get_cum_sum(row2, col1-1) + self.get_cum_sum(row1-1, col1-1)    


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

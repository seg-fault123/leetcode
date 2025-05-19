class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m-1
        left, right = 0, n-1
        result = []
        while len(result) < m*n:
            for i in range(left, right+1):
                if len(result) < m*n:
                    result.append(matrix[top][i])
                else:
                    break
            top += 1
            
            for i in range(top, bottom+1):
                if len(result) < m*n:
                    result.append(matrix[i][right])
                else:
                    break
            right -= 1

            for i in range(right, left-1, -1):
                if len(result) < m*n:
                    result.append(matrix[bottom][i])
                else:
                    break
            bottom -= 1
            
            for i in range(bottom, top-1, -1):
                if len(result) < m*n:
                    result.append(matrix[i][left])
                else:
                    break
            
            left += 1
            
        
        return result




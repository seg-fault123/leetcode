class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # result = []
        # # our strategy is to fill queens row by row
        # visited = [[False]*n for _ in range(n)] # mark what positions have been visited

        # # will mark the position that will be invalid if a queen is placed at i, j.
        # # it also returns all the marked positions which were invalidated buy this procedure and were not invalidated beforehand
        # def mark_visit(i, j, n):
        #     visited[i][j] = True
        #     marked_list = [[i, j]]
        #     # p is the difference that needs to be added to the current row. We dont need to check for positions which are invalidated in previous rows and the current row, beacuse the next queen will be placed in the upcomming rows, so only invalidate the positions that have greater row number than current row.
        #     for p in range(1, n-i):
        #         diffs = [[i+p, j], [i+p, j-p], [i+p, j+p]]
        #         for x, y in diffs:
        #             if 0<=x<n and 0<=y<n and not visited[x][y]:
        #                 visited[x][y] = True
        #                 marked_list.append([x, y])
        #     return marked_list # list of all positions that are invalidated uniquely by the current position
        
        # def mark_free(marked_list):
        #     # mark the passed nodes are valid
        #     for x, y in marked_list:
        #         visited[x][y] = False

        # def dfs(index, n, curr):
        #     if index==n:
        #         # we have successfully placed n queens, add to result
        #         result.append(curr)
        #         return
            
        #     # try to place a queen in each column in the current row
        #     for col in range(n):
        #         # if this position is valid place a queen here and move on to next row
        #         if not visited[index][col]:
        #             marked_list = mark_visit(index, col, n) # invalidate the appropriate postions in the upcoming row
        #             # update the current solution
        #             dfs(index+1, n, curr+['.'*col + 'Q' + '.'*(n-col-1)])
        #             mark_free(marked_list) # free those nodes which were uniquely invalidated by this current position. If we don't maintain this then it can incorrectly validate positions which were invalidated by queens placed in the previous rows.
            
        # dfs(0, n, [])
        # return result


        # another approach 
        # instead of using a visited array for each coordinate, we 3 values that determine if a coordinate is valid or not
        # visited_cols conatain col indices which have a queen placed on it
        # \    a negative diagonal. Notice that along this diagonal, each
        #  \   coordinate has a fixed row-column value. As we move downward
        #   \  row and col values are incremented by 1, keeping the diff same.
        # each diag has a unique value associated to it.

        #   / a positive diagonal. Along this diagonal, each coordinate has a 
        #  /  fixed row+col value. As we move up, row is decremented but col is
        # /   incremented by 1 keeping the sum same.

        visited_cols = set()
        visited_pos_diags = set()
        visited_neg_diags = set()

        result = []

        def dfs(index, curr):
            if index==n:
                result.append(curr)
            
            for col in range(n):
                pos_diag = index + col
                neg_diag = index - col
                if (col not in visited_cols) and (pos_diag not in visited_pos_diags) and (neg_diag not in visited_neg_diags):
                    visited_cols.add(col)
                    visited_pos_diags.add(pos_diag)
                    visited_neg_diags.add(neg_diag)
                    dfs(index+1, curr+['.'*col+'Q'+'.'*(n-col-1)])

                    visited_cols.remove(col)
                    visited_pos_diags.remove(pos_diag)
                    visited_neg_diags.remove(neg_diag)
            return
        
        dfs(0, [])
        return result

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Time complexity: O(n.m)
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {} #(r,c) -> LIP

        def dfs(r,c,prevVal):
            if (r<0 or r==ROWS or 
                c<0 or c==COLS or 
                matrix[r][c] <= prevVal):
                return 0 
            # if we have already computed then we will justv return the value 
            if (r,c) in dp:
                return dp[(r,c)]
                
            # 1 because it is the min possible value we can fill in a position 
            res = 1 
            # we will run dfs on one of the neighbors 
            # we have to check in all 4 directions 
            res = max(res, 1 + dfs(r+1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r-1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c+1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c-1, matrix[r][c]))
            # res will have the max value by the time we reach here and it will be assigned to that particular position of the matrix 
            dp[(r,c)] = res
            return res 
        
        for r in range(ROWS):
            for c in range(COLS):
                # we are passing -1 because, none of the position will comply accoriding to the condition: matrix[r][c] <= prevVal as we don't have any value < -1 in our matrix  
                dfs(r,c,-1)
        return max(dp.values())


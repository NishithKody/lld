class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n  = len(matrix)
        m = len(matrix[0])

        dp  = {}

        def util(i,j,prev):
            if(i>=n or i<0 or j>=m or j<0 or matrix[i][j]<=prev):
                return 0
            
            if((i,j) in dp):
                return dp[(i,j)]
            
            res = 1
            res = max(res, util(i+1, j, matrix[i][j])+1)
            res = max(res, util(i-1, j, matrix[i][j])+1)
            res = max(res, util(i, j+1, matrix[i][j])+1)
            res = max(res, util(i, j-1, matrix[i][j])+1)

            dp[(i,j)] = res

            return res

        
        for i in range(n):
            for j in range(m):
                util(i,j,-1)
        
        return max(dp.values())


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []

        for i in range(n):
            val = [0]*m
            grid.append(val)
        
        for i in range(m):
            grid[n-1][i] = 1
        
        for i in range(n):
            grid[i][m-1] = 1

        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                grid[i][j] = grid[i+1][j]+grid[i][j+1]
        
        return grid[0][0]
        
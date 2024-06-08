class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        res = 0
        n = len(grid)
        m = len(grid[0])

        def util(r,c):
            if(r>=n or c>=m or r<0 or c<0 or grid[r][c]!=1):
                return 0
            
            grid[r][c]='2'
            z = util(r+1,c)
            x = util(r-1,c)
            v = util(r,c+1)
            u = util(r,c-1)

            return z+x+v+u+1
        
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1):
                    val = util(i,j)
                    if(val>res):
                        res = val
        
        return res

        
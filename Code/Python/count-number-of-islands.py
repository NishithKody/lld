
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def util(r,c):
            if(r<0 or c<0 or r>=n or c>=m or grid[r][c]!='1'):
                return
            else:
                grid[r][c]='0'
                util(r+1,c)
                util(r-1,c)
                util(r,c+1)
                util(r,c-1)
        res = 0
        n = len(grid)
        m = len(grid[0])        
        
        for i in range(0,n):
            for j in range(0,m):
                if(grid[i][j]=='1'):
                    res = res + 1
                    util(i,j)
    
        return res
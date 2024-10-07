class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visit = set()
        def util(r,c):

            if((r,c) in visit):
                return 0

            if(r>=n or r<0 or c>=m or c<0 or grid[r][c]!=1):
                return 1
            
            visit.add((r,c))
            top = util(r+1,c)
            bottom = util(r-1,c)
            left = util(r,c+1)
            right = util(r,c-1)

            return top + right + left + bottom
        
        for i in range(n):
            for j in range(m):
                if(grid[i][j] == 1):
                    res = util(i,j)
                    return res
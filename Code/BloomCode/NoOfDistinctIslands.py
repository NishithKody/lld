from typing import (
    List,
)

class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def numberof_distinct_islands(self, grid: List[List[int]]) -> int:
        # write your code here
        n = len(grid)
        m = len(grid[0])
        chk = set()


        def util(r,c,path):
            if(r>=n or c>=m or r<0 or c<0):
                return ""
            
            if(grid[r][c]!=1):
                return ""

            grid[r][c] = '#'
            q = util(r+1, c, path+"1")
            w = util(r, c-1, path+"2")
            e = util(r-1, c, path+"3")
            x = util(r, c+1, path+"4")

            return path + q + w + e + x
        
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1):
                    val = util(i,j,"S")
                    print('val',val)
                    chk.add(val)

        return len(chk)

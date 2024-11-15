from collections import deque

class Solution:
    def wallsAndGates(self, grid: List[List[int]]) -> None:
        q = deque()
        n = len(grid)
        m = len(grid[0])
        visit = set()

        dirs = [[0,1],[1,0],[-1,0],[0,-1]]

        for i in range(n):
            for j in range(m):
                if(grid[i][j]==0):
                    q.append([i,j,0])
                    visit.add(str(i)+'|'+str(j))
        while(len(q)>0):
            [r,c,val] = q.popleft()

            for d in dirs:
                nr = r+d[0]
                nc = c+d[1]

                if(nr>=n or nc>=m or nc<0 or nr<0 or grid[nr][nc]==-1):
                    continue
                
                if(str(nr)+'|'+str(nc) in visit):
                    continue
                
                grid[nr][nc] = min(grid[nr][nc], val+1)
                q.append([nr,nc,grid[nr][nc]])
                visit.add(str(nr)+'|'+str(nc))
            
#This is a simple dfs 
#The tricky part is the backtracking
#in dfs, there is a posibility of going back to the prev cell
#this could pose a problem is this case = "A B A"
#to avoid this we set the cell to '#' and revert once the iteration is complete

class Solution:
    def exist(self, b: List[List[str]], word: str) -> bool:

        n = len(b)
        m = len(b[0])
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]        

        def util(r,c,i):
            
            if(i == len(word)):
                return True

            if(r>=n or c>=m or r<0 or c<0):
                return False
            
            if(b[r][c] == word[i]):
                b[r][c] = '#'
                for d in dirs:
                    val = util(r+d[0],c+d[1],i+1)
                    if(val == True):
                        return val
                b[r][c] = word[i]
            return False

        for i in range(n):
            for j in range(m):
                if(b[i][j]==word[0]):
                   res = util(i,j,0)
                   if(res == True):
                        return True
        return False
                
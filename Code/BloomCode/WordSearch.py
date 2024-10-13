class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        def util(r,c,i):
            if(i==len(word)):
                return True
                
            if(r<0 or c<0 or r>=n or c>=m ):
                return False
            
            if(board[r][c]!=word[i]):
                return False
    
            temp = board[r][c]
            board[r][c] = '#'

            a = util(r+1, c, i+1)
            b = util(r, c+1, i+1)
            x = util(r-1, c, i+1)
            d = util(r, c-1, i+1)

            board[r][c] = temp

            return a or b or x or d

        for i in range(n):
            for j in range(m):
                if(board[i][j]==word[0]):
                    res = util(i,j,0)
                    if(res == True):
                        return True
        return False
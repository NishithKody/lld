class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = []
        res = []
        for i in range(n):
            tmp = ["."]* n
            board.append(tmp)

        col = [0] * n
        diag = [0] * 2*n
        anDiag = [0] * ((2*n))

        def util(i):
            if(i==n):
                tmp = []
                for row in board:
                    tmp.append(''.join(row))
                res.append(tmp)
                return
            
            for j in range(n):
                if (col[j] + diag[i+j] + anDiag[n-i+j] == 0):
                    board[i][j] = 'Q'
                    col[j] = 1
                    diag[i+j] = 1
                    anDiag[n-i+j] = 1

                    util(i+1)

                    board[i][j] = '.'
                    col[j] = 0
                    diag[i+j] = 0
                    anDiag[n-i+j] = 0

        util(0)
        return res

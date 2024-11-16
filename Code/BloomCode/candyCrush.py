from typing import (
    List,
)

class Solution:
    """
    @param board: a 2D integer array
    @return: the current board
    """
    def candy_crush(self, board: List[List[int]]) -> List[List[int]]:
        # Write your code here
        n = len(board)
        m = len(board[0])

        done = False

        while(done==False):
            done = True
            for i in range(n):
                for j in range(m-2):
                    num1 = abs(board[i][j])
                    num2 = abs(board[i][j+1])
                    num3 = abs(board[i][j+2])

                    if(num1 == num2 == num3 and num1!=0):
                        board[i][j] = -num1
                        board[i][j+1] = -num2
                        board[i][j+2] = -num3
                        done = False

            for i in range(n-2):
                for j in range(m):
                    num1 = abs(board[i][j])
                    num2 = abs(board[i+1][j])
                    num3 = abs(board[i+2][j])

                    if(num1 == num2 == num3 and num1!=0):
                        board[i][j] = -num1
                        board[i+1][j] = -num2
                        board[i+2][j] = -num3
                        done = False
            
            for j in range(m):
                idx = n-1
                for i in range(n-1,-1,-1):
                    if(board[i][j]>0):
                        board[idx][j] = board[i][j]
                        idx -= 1
                
                while(idx>=0):
                    board[idx][j] = 0
                    idx -= 1
        
        return board

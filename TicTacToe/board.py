from player import Player

class Board:
    def __init__(self) -> None:
        self.board = []
        for i in range(3):
            val = ['-'] * 3
            self.board.append(val)
        self.board_count = 0
    
    def make_move(self, player: Player, move_r, move_c):
        if(self.board[move_r][move_c]!='-'):
            print('the cell has been selected')
        else:
            self.board[move_r][move_c] = player.get_symbol()
            self.board_count +=1
            self.print_board()

    def check_win(self, player: Player):
        sym = player.get_symbol()

        for i in range(3):
            if(self.board[i][0]!='-' and (self.board[i][0]==self.board[i][1]==self.board[i][2]==sym)):
                return True
        
        for i in range(3):
            if(self.board[0][i]!='-' and (self.board[0][i]==self.board[1][i]==self.board[2][i]==sym)):
                return True
        
        if(self.board[0][0]==self.board[1][1]==self.board[2][2]==sym):
            return True
        
        if(self.board[0][2]==self.board[1][1]==self.board[2][0]==sym):
            return True
        
        return False

    def is_finish(self):
        if(self.board_count==9):
            return True
        else:
            return False

    def print_board(self):
        print('--------')
        for row in self.board:
            print(row,'\n')

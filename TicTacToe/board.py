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

    def check_win(self):
        pass

    def is_finish(self):
        if(self.board_count==9):
            return True
        else:
            return False

    def print_board(self):
        print('--------')
        for row in self.board:
            print(row,'\n')

from player import Player
from board import Board

class Game:
    def __init__(self, player1: Player, player2: Player) -> None:
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.current_player = self.player1
    
    def play(self):
        self.board.print_board()
        while(self.board.is_finish()==False):
            print('turn',self.current_player.get_name())
            r = int(input('enter row '))
            c = int(input('enter column '))

            self.board.make_move(self.current_player,r,c)

            if(self.board.check_win(self.current_player)==True):
                print('winner!',self.current_player.get_name())
                return
            self.switch_player()

        print('draw')

    def switch_player(self):
        if(self.current_player!=self.player1):
            self.current_player = self.player1
        else:
            self.current_player = self.player2

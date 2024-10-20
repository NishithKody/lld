from player import Player
from game import Game

class TicTacToe:
    def run(self):
        p1 = Player('p1','X')
        p2 = Player('p2','O')
        gm = Game(p1,p2)
        gm.play()

if(__name__=='__main__'):
    game = TicTacToe()
    game.run()

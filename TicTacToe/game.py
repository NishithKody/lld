from player import Player
from board import Board

class Game:
    def __init__(self, player1: Player, player2: Player) -> None:
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
    
    def play(self):
        pass
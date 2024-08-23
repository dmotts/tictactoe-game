from board import Board
from player import Player
from logger import Logger

class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.logger = Logger("game.log")
    
    def start_game(self):
        self.logger.log("Game started")
        player1 = Player("Player 1", "X")
        player2 = Player("Player 2", "O")
        current_player = player1
        
        while True:
            self.board.display()
            move = int(input(f"{current_player.name}, choose your move (0-8): "))
            if self.board.update_board(move, current_player.symbol):
                self.logger.log(f"{current_player.name} placed {current_player.symbol} on {move}")
                if self.board.check_winner(current_player.symbol):
                    self.board.display()
                    print(f"{current_player.name} wins!")
                    self.logger.log(f"{current_player.name} wins!")
                    break
                elif self.board.is_full():
                    self.board.display()
                    print("It's a draw!")
                    self.logger.log("Game ended in a draw")
                    break
                current_player = player2 if current_player == player1 else player1
            else:
                print("Invalid move! Try again.")
                self.logger.log(f"{current_player.name} attempted invalid move on {move}")

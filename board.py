class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
    
    def display(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---------")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---------")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")
    
    def update_board(self, position, symbol):
        if self.board[position] == ' ':
            self.board[position] = symbol
            return True
        return False
    
    def check_winner(self, symbol):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
            [0, 4, 8], [2, 4, 6]              # diagonal
        ]
        for condition in win_conditions:
            if all(self.board[i] == symbol for i in condition):
                return True
        return False
    
    def is_full(self):
        return all(space != ' ' for space in self.board)

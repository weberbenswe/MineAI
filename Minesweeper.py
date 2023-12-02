import numpy as np

class Minesweeper:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = np.zeros((rows, cols), dtype=int)
        self.revealed = np.zeros((rows, cols), dtype=bool)

    def place_mines(self):
        mine_locations = np.random.choice(self.rows * self.cols, self.mines, replace=False)
        self.board.flat[mine_locations] = -1

    def reveal_cell(self, row, col):
        if not self.revealed[row, col]:
            self.revealed[row, col] = True
            return self.board[row, col]

    def is_mine(self, row, col):
        return self.board[row, col] == -1

    def count_adjacent_mines(self, row, col):
        count = 0
        for i in range(max(0, row-1), min(self.rows, row + 2)):
            for j in range(max(0, col-1), min(self.cols, col + 2)):
                if self.is_mine(i, j):
                    count += 1
        return count
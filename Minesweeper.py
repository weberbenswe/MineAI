import numpy as np
from cell import Cell

class Minesweeper_Board:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = np.array([[Cell(i, j) for j in range(cols)] for i in range(rows)])

    def place_mines(self):
        mine_indices = np.random.choice(self.rows * self.cols, self.mines, replace=False)

        for index in mine_indices:
            row, col = divmod(index, self.cols)
            self.board[row][col].setMine()

    def reveal_cell(self, row, col):
        # Moving control logic to the cell.py class
        if not self.board[row][col].isHidden:
            self.revealed[row, col] = True
            print(self.board[row][col].isMine)
            return self.board[row, col]

    def is_mine(self, row, col):
        return self.board[row][col].isMine

    def count_adjacent_mines(self, row, col):
        count = 0
        for i in range(max(0, row-1), min(self.rows, row + 2)):
            for j in range(max(0, col-1), min(self.cols, col + 2)):
                if self.is_mine(i, j):
                    count += 1
        return count
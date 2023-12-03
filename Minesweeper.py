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
            self.board[row][col].set_mine()

    def calculate_adjacent_mines(self):
        for i in range(self.rows):
            for j in range(self.cols):
                cell = self.board[i][j]
                if not cell.isMine:
                    adjacent_mines = self.count_adjacent_mines(i, j)
                    cell.set_adjacent_value(adjacent_mines)

    def count_adjacent_mines(self, row, col):
        count = 0

        for i in range(max(0, row - 1), min(self.rows, row + 2)):
            for j in range(max(0, col - 1), min(self.cols, col + 2)):
                if not (i == row and j == col) and self.is_mine(self.board[i][j]):
                    count += 1

        return count

    def reveal_cell(self, cell):
        # Moving control logic to the cell.py class
        if not cell.revealed:
            return cell.reveal()

    def is_mine(self, cell):
        return cell.isMine

    def is_revealed(self, cell):
        return cell.revealed

    def cell_adjacent_value(self, cell):
        return cell.adjacentValue

    
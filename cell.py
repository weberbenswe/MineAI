# This is the object for each cell that has certian attributes

class Cell:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.isMine = False
        self.revealed = False
        self.adjacentValue = 0

    def set_mine(self):
        self.isMine = True

    def reveal(self):
        self.revealed = True

    def set_adjacent_value(self, value):
        self.adjacentValue = value
    

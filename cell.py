# This is the object for each cell that has certian attributes

class Cell:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.isMine = False
        self.isHidden = True

    def setMine(self):
        self.isMine = True

    def selected(self):
        self.isHidden = False

    def isHidden(self):
        return self.isHidden
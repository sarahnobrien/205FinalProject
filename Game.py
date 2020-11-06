from time import sleep

from Intersection import Intersection
import random

class Game:
    global rows, cols, boxWidth, stoneRadius
    rows = 15
    cols = 15
    boxWidth = 50
    stoneRadius = 20
    objectGameBoard = []
    jcheckC = 0
    icheckC = 0
    check = [False]
    countfiv = [0, 0, 0, 0]

    def __init__(self):
        self.rows = 15
        self.cols = 15
        self.boxWidth = 50
        self.objectGameBoard
        self.stoneRadius = 20
        self.turn = "player"
        self.jcheckC = 0
        self.icheckC = 0
        self.check = [False]
        self.countfiv = [0, 0, 0, 0]

    def StartGameBoard(self):
        for i in range(rows):
            objectRow = []
            row = []
            row2 = []
            for j in range(cols):
                x = int(i * boxWidth + (boxWidth/2))
                y = int(j * boxWidth + (boxWidth/2))
                intersection = Intersection(x, y, boxWidth, stoneRadius)
                objectRow.append(intersection)
                row.append(0)
                row2.append(1)
            self.objectGameBoard.append(objectRow)

    def getGameBoard(self):
        return self.objectGameBoard

    def getTurn(self):
        return self.turn

    def setTurn(self, player):
        self.turn = player

    def placePieceCPU(self):

        piecePlaced = False
        while not piecePlaced:
            randColumn = random.randint(0, 14)
            randRow = random.randint(0, 14)

            if not self.getGameBoard()[randColumn][randRow].hasStone:
                self.getGameBoard()[randColumn][randRow].click("CPU")
                piecePlaced = True
                self.setTurn("player")


    def countfive(self):
        self.icheck = self.icheckC
        self.jcheck = self.jcheckC
        c = 0
        if self.getGameBoard()[self.icheckC][self.jcheckC].hasStone:
            while self.icheck <= 14 and self.jcheck <= 14:
                if self.getGameBoard()[self.icheck][self.jcheck].hasStone:
                    c += 1
                    self.countfiv[0] = c
                else:
                    c = 0
                    self.countfiv[0] = c
                self.icheck += 1
            self.icheck = self.icheckC
            self.jcheck = self.jcheckC
            c = 0
            while self.icheck <= 14 and self.jcheck <= 14:
                if self.getGameBoard()[self.icheck][self.jcheck].hasStone:
                    c += 1
                    self.countfiv[1] = c
                else:
                    c = 0
                    self.countfiv[1] = c

                self.jcheck += 1
            self.icheck = self.icheckC
            self.jcheck = self.jcheckC
            c = 0
            while self.icheck <= 14 and self.jcheck <= 14:
                if self.getGameBoard()[self.icheck][self.jcheck].hasStone:
                    c += 1
                    self.countfiv[2] = c
                else:
                    c = 0
                    self.countfiv[2] = c
                self.icheck += 1
                self.jcheck -= 1
            self.icheck = self.icheckC
            self.jcheck = self.jcheckC
            c = 0
            while self.icheck <= 14 and self.jcheck <= 14:
                if self.getGameBoard()[self.icheck][self.jcheck].hasStone:
                    c += 1
                    self.countfiv[3] = c
                else:
                    c = 0
                    self.countfiv[3] = c

                self.icheck += 1
                self.jcheck += 1

            if 5 in self.countfiv:
                self.check[0] = True
            else:
                self.countfiv = [0, 0, 0, 0]
                if self.jcheckC < 14:
                    self.icheckC += 1
                    self.countfive()
                elif self.jcheckC == 14 and self.icheckC < 14:
                    self.icheckC += 1
                    self.jcheckC = 0
                    self.countfive()
                elif self.icheckC == 14 and self.jcheckC == 14:
                    self.check[0] = False
        else:
            if self.jcheckC < 14:
                self.jcheckC += 1
                self.countfive()
            elif self.jcheckC == 14 and self.icheckC < 14:
                self.icheckC += 1
                self.jcheckC = 0
                self.countfive()
            elif self.icheckC == 14 and self.jcheckC == 14:
                self.check[0] = False
    def checkGet(self):
        return self.check[0]
    # TODO: add countFive.py after a piece is placed

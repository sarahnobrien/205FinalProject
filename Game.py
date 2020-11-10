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
    check = [False]
    countfiv = [0, 0, 0, 0]

    def __init__(self):
        self.rows = 15
        self.cols = 15
        self.boxWidth = 50
        self.objectGameBoard = []
        self.stoneRadius = 20
        self.turn = "player"
        self.check = [False]
        self.countfiv = [0, 0, 0, 0]
        self.checkcom = [False]
        self.countfivcom = [0, 0, 0, 0]

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
        icheckC = 0
        jcheckC = 0
        while icheckC <= 14 and jcheckC <= 14:
            icheck = icheckC
            jcheck = jcheckC
            c = 0
            if self.getGameBoard()[icheckC][jcheckC].hasStone and self.getGameBoard()[icheckC][jcheckC].getOwner() == "player":
                while icheck <= 14 and jcheck <= 14:
                    if self.getGameBoard()[icheck][jcheck].hasStone and self.getGameBoard()[icheck][jcheck].getOwner() == "player":
                        c += 1
                        self.countfiv[0] = c
                    elif c != 5 and not (self.getGameBoard()[icheck][jcheck].hasStone):
                        c = 0
                        self.countfiv[0] = c
                    icheck += 1
                icheck = icheckC
                jcheck = jcheckC
                c = 0
                while icheck <= 14 and jcheck <= 14:
                    if self.getGameBoard()[icheck][jcheck].hasStone and self.getGameBoard()[icheck][jcheck].getOwner() == "player":
                        c += 1
                        self.countfiv[1] = c
                    elif c != 5 and not (self.getGameBoard()[icheck][jcheck].hasStone):
                        c = 0
                        self.countfiv[1] = c

                    jcheck += 1
                icheck = icheckC
                jcheck = jcheckC
                c = 0
                while icheck <= 14 and jcheck <= 14:
                    if self.getGameBoard()[icheck][jcheck].hasStone and self.getGameBoard()[icheck][jcheck].getOwner() == "player":
                        c += 1
                        self.countfiv[2] = c
                    elif c != 5 and not (self.getGameBoard()[icheck][jcheck].hasStone):
                        c = 0
                        self.countfiv[2] = c
                    icheck += 1
                    jcheck -= 1
                icheck = icheckC
                jcheck = jcheckC
                c = 0
                while icheck <= 14 and jcheck <= 14:
                    if self.getGameBoard()[icheck][jcheck].hasStone and self.getGameBoard()[icheck][jcheck].getOwner() == "player":
                        c += 1
                        self.countfiv[3] = c
                    elif c != 5 and not (self.getGameBoard()[icheck][jcheck].hasStone):
                        c = 0
                        self.countfiv[3] = c

                    icheck += 1
                    jcheck += 1
                if 5 in self.countfiv:
                    self.check[0] = True
                    return self.check[0]
                else:
                    self.countfiv = [0, 0, 0, 0]
                    if jcheckC < 14:
                        icheckC += 1

                    elif jcheckC == 14 and icheckC < 14:
                        icheckC += 1
                        jcheckC = 0

                    elif icheckC == 14 and jcheckC == 14:
                        break
            else:
                if jcheckC < 14:
                    jcheckC += 1

                elif jcheckC == 14 and icheckC < 14:
                    icheckC += 1
                    jcheckC = 0
                elif icheckC == 14 and jcheckC == 14:
                    break

        return self.check[0]
    def comcountfive(self):
        icheckC = 0
        jcheckC = 0
        while icheckC <= 14 and jcheckC <= 14:
            icheck = icheckC
            jcheck = jcheckC
            c = 0
            if self.getGameBoard()[icheckC][jcheckC].hasStone and self.getGameBoard()[icheckC][jcheckC].getOwner() == "CPU":
                while icheck <= 14 and jcheck <= 14:
                    if self.getGameBoard()[icheck][jcheck].hasStone and self.getGameBoard()[icheck][jcheck].getOwner() == "CPU":
                        c += 1
                        self.countfivcom[0] = c
                    elif c != 5 and not (self.getGameBoard()[icheck][jcheck].hasStone):
                        c = 0
                        self.countfivcom[0] = c
                    icheck += 1
                icheck = icheckC
                jcheck = jcheckC
                c = 0
                while icheck <= 14 and jcheck <= 14:
                    if self.getGameBoard()[icheck][jcheck].hasStone and self.getGameBoard()[icheck][jcheck].getOwner() == "CPU":
                        c += 1
                        self.countfivcom[1] = c
                    elif c != 5 and not (self.getGameBoard()[icheck][jcheck].hasStone):
                        c = 0
                        self.countfivcom[1] = c

                    jcheck += 1
                icheck = icheckC
                jcheck = jcheckC
                c = 0
                while icheck <= 14 and jcheck <= 14:
                    if self.getGameBoard()[icheck][jcheck].hasStone and self.getGameBoard()[icheck][jcheck].getOwner() == "CPU":
                        c += 1
                        self.countfivcom[2] = c
                    elif c != 5 and not (self.getGameBoard()[icheck][jcheck].hasStone):
                        c = 0
                        self.countfivcom[2] = c
                    icheck += 1
                    jcheck -= 1
                icheck = icheckC
                jcheck = jcheckC
                c = 0
                while icheck <= 14 and jcheck <= 14:
                    if self.getGameBoard()[icheck][jcheck].hasStone and self.getGameBoard()[icheck][jcheck].getOwner() == "CPU":
                        c += 1
                        self.countfivcom[3] = c
                    elif c != 5 and not (self.getGameBoard()[icheck][jcheck].hasStone):
                        c = 0
                        self.countfivcom[3] = c

                    icheck += 1
                    jcheck += 1

                if 5 in self.countfivcom:
                    self.checkcom[0] = True
                    return self.checkcom[0]
                else:
                    self.countfivcom = [0, 0, 0, 0]
                    if jcheckC < 14:
                        icheckC += 1

                    elif jcheckC == 14 and icheckC < 14:
                        icheckC += 1
                        jcheckC = 0

                    elif icheckC == 14 and jcheckC == 14:
                        break
            else:
                if jcheckC < 14:
                    jcheckC += 1

                elif jcheckC == 14 and icheckC < 14:
                    icheckC += 1
                    jcheckC = 0
                elif icheckC == 14 and jcheckC == 14:
                    break

        return self.checkcom[0]
    # TODO: add countFive.py after a piece is placed

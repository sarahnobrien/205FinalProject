from time import sleep

from Intersection import Intersection
import random
import time

class Game:
    global rows, cols, boxWidth, stoneRadius
    rows = 15
    cols = 15
    boxWidth = 50
    stoneRadius = 20
    objectGameBoard = []
    check = [False]
    countfiv = [0, 0, 0, 0]
    checkcom = [False]
    countfivcom = [0, 0, 0, 0]


    def __init__(self):
        self.rows = 15
        self.cols = 15
        self.boxWidth = 50
        self.objectGameBoard = []
        self.stoneRadius = 20
        self.currTurn = self.chooseFirstPlayerEasyDifficulty()
        self.firstPlayer = self.chooseFirstPlayerEasyDifficulty()
        self.check = [False]
        self.countfiv = [0, 0, 0, 0]
        self.checkcom = [False]
        self.countfivcom = [0, 0, 0, 0]
        print("First Player: " + self.getFirstPlayer())


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

    def getCurrTurn(self):
        return self.currTurn

    def setCurrTurn(self, player):
        self.currTurn = player

    # Decide which player should go first (Human player or CPU), (50/50) chance
    def chooseFirstPlayerEasyDifficulty(self):
        randomInt = random.randrange(0, 2)
        if randomInt == 0:
            self.firstPlayer = "Player"
            self.secondPlayer = "CPU"
        else:
            self.firstPlayer = "CPU"
            self.secondPlayer = "Player"
        return self.firstPlayer

    # Decide which player should go first (Human player or CPU), CPU goes first more of the time roughly 75% of the time
    def chooseFirstPlayerHardDifficulty(self):
        randomInt = random.randrange(0, 3)
        if randomInt == 0:
            self.firstPlayer = "Player"
            self.secondPlayer = "CPU"
        else:
            self.firstPlayer = "CPU"
            self.secondPlayer = "Player"
        return self.firstPlayer

    def getFirstPlayer(self):
        return self.firstPlayer

    def getSecondPlayer(self):
        return self.secondPlayer

    # Try to implement generic placePiece function, which has logic for checking whose turn it is,
    # and placing their respective piece
    def placePieceGeneric(self, locI, locJ):
        currTurn = self.getCurrTurn()
        if not self.getGameBoard()[locI][locJ].hasStone:

            # Check who's turn it is
            if currTurn == "Player":
                if not self.getGameBoard()[locI][locJ].hasStone:
                    self.getGameBoard()[locI][locJ].click(currTurn)
                    self.setCurrTurn("CPU")
                    self.placePieceCPU()
            elif currTurn == "CPU":
                 self.placePieceCPU()
            else:
                return -1 # A problem occurred

    def placePieceCPU(self):

        piecePlaced = False
        while not piecePlaced:
            randColumn = random.randint(0, 14)
            randRow = random.randint(0, 14)

            if not self.getGameBoard()[randColumn][randRow].hasStone:
                self.getGameBoard()[randColumn][randRow].click("CPU")
                piecePlaced = True

                self.setCurrTurn("Player")


    def countfive(self):
        icheckC = 0
        jcheckC = 0
        while icheckC <= 14 and jcheckC <= 14:
            icheck = icheckC
            jcheck = jcheckC
            c = 0
            if self.getGameBoard()[icheckC][jcheckC].hasStone and self.getGameBoard()[icheckC][jcheckC].getOwner() == "Player":
                while icheck <= 14 and jcheck <= 14:
                    if self.getGameBoard()[icheck][jcheck].hasStone and self.getGameBoard()[icheck][jcheck].getOwner() == "Player":
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
                    if self.getGameBoard()[icheck][jcheck].hasStone and self.getGameBoard()[icheck][jcheck].getOwner() == "Player":
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
                    if self.getGameBoard()[icheck][jcheck].hasStone and self.getGameBoard()[icheck][jcheck].getOwner() == "Player":
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
                    if self.getGameBoard()[icheck][jcheck].hasStone and self.getGameBoard()[icheck][jcheck].getOwner() == "Player":
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
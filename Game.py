from time import sleep
from Intersection import Intersection
import random


class Game:
    global rows, cols, boxWidth, stoneRadius
    firstPlayer = ""
    secondPlayer = ""
    rows = 15
    cols = 15
    boxWidth = 50
    currTurn = ""
    stoneRadius = 20
    objectGameBoard = []

    def __init__(self):
        self.rows = 15
        self.cols = 15
        self.boxWidth = 50
        self.objectGameBoard
        self.stoneRadius = 20
        self.currTurn = self.chooseFirstPlayerEasyDifficulty()

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
        randomInt = random.randrange(0, 1)
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
                self.getGameBoard()[locI][locJ].click(currTurn)
                self.setCurrTurn("CPU")

            elif currTurn == "CPU":
                self.getGameBoard()[locI][locJ].click(currTurn)
                self.setCurrTurn("Player")
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
                self.setTurn("Player")

    def countfive(self):

        # i = 0
        # j = 0
        # check = [False]
        # countfiv = [0, 0, 0, 0]
        global i, j, countfiv, arrayi, check
        icheck = i
        jcheck = j
        c = 0
        if arrayi[i][j] == 1:
            while icheck <= 14 and jcheck <= 14:
                if arrayi[icheck][jcheck] == 1:
                    c += 1
                    countfiv[0] = c
                else:
                    c = 0
                    countfiv[0] = c
                icheck += 1
            icheck = i
            jcheck = j
            c = 0
            while icheck <= 14 and jcheck <= 14:
                if arrayi[icheck][jcheck] == 1:
                    c += 1
                    countfiv[1] = c
                else:
                    c = 0
                    countfiv[1] = c

                jcheck += 1
            icheck = i
            jcheck = j
            c = 0
            while icheck <= 14 and jcheck <= 14:
                if arrayi[icheck][jcheck] == 1:
                    c += 1
                    countfiv[2] = c
                else:
                    c = 0
                    countfiv[2] = c
                icheck += 1
                jcheck -= 1
            icheck = i
            jcheck = j
            c = 0
            while icheck <= 14 and jcheck <= 14:
                if arrayi[icheck][jcheck] == 1:
                    c += 1
                    countfiv[3] = c
                else:
                    c = 0
                    countfiv[3] = c

                icheck += 1
                jcheck += 1

            if 5 in countfiv:
                check[0] = True
            else:
                countfiv = [0, 0, 0, 0]
                if j < 14:
                    j += 1
                    countfive()
                elif j == 14 and i < 14:
                    i += 1
                    j = 0
                    countfive()
                elif i == 14 and j == 14:
                    check[0] = False
        else:
            if j < 14:
                j += 1
                countfive()
            elif j == 14 and i < 14:
                i += 1
                j = 0
                countfive()
            elif i == 14 and j == 14:
                check[0] = False


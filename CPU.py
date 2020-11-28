import random
import copy

class CPU:

    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.check = [False]
        self.countfiv = [0, 0, 0, 0]
        self.checkcom = [False]
        self.countfivcom = [0, 0, 0, 0]


    def miniMaxDecision(self, gameBoard):

        actionsList = self.getMinActions(gameBoard)

        for action in actionsList:
            if self.getMinValue(action, 0) == -1:
                print("Computer move:")
                return action
        for action in actionsList:
            if self.getMinValue(action, 0) == 0:
                print("Computer Move:")
                return action
        else:
            return actionsList[0]


    def getMinActions(self, gameBoard):
        actionsList = []

        for i in range(self.cols):
            for j in range(self.rows):
                if not gameBoard[i][j].hasStone:
                    board = copy.deepcopy(gameBoard)
                    board[i][j].click("CPU")
                    actionsList.append(board)
        return actionsList


    def getMaxActions(self, gameBoard):
        actionsList = []

        for i in range(self.cols):
            for j in range(self.rows):
                if not gameBoard[i][j].hasStone:
                    board = copy.deepcopy(gameBoard)
                    board[i][j].click("Player")
                    actionsList.append(board)
        return actionsList

    def getMinValue(self, gameBoard, depth):
        # return -1 if cpu wins, 1 if player wins, 0 otherwise
        depth += 1
        if depth == 15:
            return 0

        #win state
        if self.endStateCPU(gameBoard):
            return -1
        if self.endStatePlayer(gameBoard):
            return 1
        else:
            return 0
        #
        # else:
        #     # If not a win state generate the next set of moves
        #     minActionsList = self.getMaxActions(gameBoard)
        #     for action in minActionsList:
        #
        #         actionValue = self.getMaxValue(action, depth)
        #         if actionValue == 1:
        #             return actionValue
        #     for action in minActionsList:
        #         actionValue = self.getMaxValue(action, depth)
        #         if actionValue == 0:
        #             return actionValue
        #     for action in minActionsList:
        #         actionValue = self.getMaxValue(action, depth)
        #         return actionValue

    def getMaxValue(self, gameBoard, depth):
        # return -1 if cpu wins, 1 if player wins, 0 otherwise
        depth+=1
        # win state
        if self.endStateCPU(gameBoard):
            return -1
        if self.endStatePlayer(gameBoard):
            return 1
        else:
            return 0
        #
        # else:
        #     # If not a win state generate the next set of moves
        #     minActionsList = self.getMinActions(gameBoard)
        #     for action in minActionsList:
        #
        #         actionValue = self.getMinValue(action, depth)
        #         if actionValue == 1:
        #             return actionValue
        #     for action in minActionsList:
        #         actionValue = self.getMinValue(action, depth)
        #         if actionValue == 0:
        #             return actionValue
        #     for action in minActionsList:
        #         actionValue = self.getMinValue(action, depth)
        #         return actionValue

    def endStateCPU(self, gameBoard):
        icheckC = 0
        jcheckC = 0
        while icheckC <= 14 and jcheckC <= 14:
            icheck = icheckC
            jcheck = jcheckC
            c = 0
            if gameBoard[icheckC][jcheckC].hasStone and gameBoard[icheckC][
                jcheckC].getOwner() == "CPU":
                while icheck <= 14 and jcheck <= 14:
                    if gameBoard[icheck][jcheck].hasStone and gameBoard[icheck][
                        jcheck].getOwner() == "CPU":
                        c += 1
                        self.countfivcom[0] = c
                    elif c != 5 and not (gameBoard[icheck][jcheck].hasStone):
                        c = 0
                        self.countfivcom[0] = c
                    icheck += 1
                icheck = icheckC
                jcheck = jcheckC
                c = 0
                while icheck <= 14 and jcheck <= 14:
                    if gameBoard[icheck][jcheck].hasStone and gameBoard[icheck][
                        jcheck].getOwner() == "CPU":
                        c += 1
                        self.countfivcom[1] = c
                    elif c != 5 and not (gameBoard[icheck][jcheck].hasStone):
                        c = 0
                        self.countfivcom[1] = c

                    jcheck += 1
                icheck = icheckC
                jcheck = jcheckC
                c = 0
                while icheck <= 14 and jcheck <= 14:
                    if gameBoard[icheck][jcheck].hasStone and gameBoard[icheck][
                        jcheck].getOwner() == "CPU":
                        c += 1
                        self.countfivcom[2] = c
                    elif c != 5 and not (gameBoard[icheck][jcheck].hasStone):
                        c = 0
                        self.countfivcom[2] = c
                    icheck += 1
                    jcheck -= 1
                icheck = icheckC
                jcheck = jcheckC
                c = 0
                while icheck <= 14 and jcheck <= 14:
                    if gameBoard[icheck][jcheck].hasStone and gameBoard[icheck][
                        jcheck].getOwner() == "CPU":
                        c += 1
                        self.countfivcom[3] = c
                    elif c != 5 and not (gameBoard[icheck][jcheck].hasStone):
                        c = 0
                        self.countfivcom[3] = c

                    icheck += 1
                    jcheck += 1

                if 5 in self.countfivcom:
                    self.checkcom[0] = True
                    print("cpu win: " + str(self.checkcom[0]))
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
        print("cpu win: " + str(self.checkcom[0]))
        return self.checkcom[0]

    def endStatePlayer(self, gameBoard):
        icheckC = 0
        jcheckC = 0
        while icheckC <= 14 and jcheckC <= 14:
            icheck = icheckC
            jcheck = jcheckC
            c = 0
            if gameBoard[icheckC][jcheckC].hasStone and gameBoard[icheckC][
                jcheckC].getOwner() == "Player":
                while icheck <= 14 and jcheck <= 14:
                    if gameBoard[icheck][jcheck].hasStone and gameBoard[icheck][
                        jcheck].getOwner() == "Player":
                        c += 1
                        self.countfiv[0] = c
                    elif c != 5 and not (gameBoard[icheck][jcheck].hasStone):
                        c = 0
                        self.countfiv[0] = c
                    icheck += 1
                icheck = icheckC
                jcheck = jcheckC
                c = 0
                while icheck <= 14 and jcheck <= 14:
                    if gameBoard[icheck][jcheck].hasStone and gameBoard[icheck][
                        jcheck].getOwner() == "Player":
                        c += 1
                        self.countfiv[1] = c
                    elif c != 5 and not (gameBoard[icheck][jcheck].hasStone):
                        c = 0
                        self.countfiv[1] = c

                    jcheck += 1
                icheck = icheckC
                jcheck = jcheckC
                c = 0
                while icheck <= 14 and jcheck <= 14:
                    if gameBoard[icheck][jcheck].hasStone and gameBoard[icheck][
                        jcheck].getOwner() == "Player":
                        c += 1
                        self.countfiv[2] = c
                    elif c != 5 and not (gameBoard[icheck][jcheck].hasStone):
                        c = 0
                        self.countfiv[2] = c
                    icheck += 1
                    jcheck -= 1
                icheck = icheckC
                jcheck = jcheckC
                c = 0
                while icheck <= 14 and jcheck <= 14:
                    if gameBoard[icheck][jcheck].hasStone and gameBoard[icheck][
                        jcheck].getOwner() == "Player":
                        c += 1
                        self.countfiv[3] = c
                    elif c != 5 and not (gameBoard[icheck][jcheck].hasStone):
                        c = 0
                        self.countfiv[3] = c

                    icheck += 1
                    jcheck += 1
                if 5 in self.countfiv:
                    self.check[0] = True
                    print("Player win: " + str(self.check[0]))
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
        print("Player win: " + str(self.check[0]))
        return self.check[0]
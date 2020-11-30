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

    def getMove(self, gameBoard):
        self.check = [False]
        self.countfiv = [0, 0, 0, 0]
        self.checkcom = [False]
        self.countfivcom = [0, 0, 0, 0]

        oldBoard = self.convertBoard(gameBoard)
        board = self.miniMaxDecision(gameBoard)

        for i in range(self.cols):
            for j in range(self.rows):
                if oldBoard[i][j] != board[i][j]:
                    return i, j


    # def findTwo(self, board):
    #     list = []
    #     for i in range(self.cols):
    #         for j in range(self.rows):
    #             if board[i][j] == 1:
    #
    #                 for k in range(-1, 2):
    #                     for l in range(-1, 2):
    #                         if board[k][l] == 1:
    #                             if j == l:
    #
    #                             if i == k:
    #
    #                             choords = [i, j, k, l]
    #                             list.append(choords)

    def findThree(self, board):
        for i in range(self.cols):
            for j in range(self.rows):
                if board[i][j] == 1:
                    #if
                    pass


    def convertBoard(self, gameBoard):
        # board has a 1 if the cpu has a stone, -1 if player has a stone, 0 if no stone
        board = []
        for i in range(self.cols):
            col = []
            for j in range(self.rows):
                if gameBoard[i][j].hasStone:
                    if gameBoard[i][j].getOwner() == "CPU":
                        col.append(1)
                    else:
                        col.append(-1)
                else:
                    col.append(0)
            board.append(col)
        return board


    def miniMaxDecision(self, gameBoard):

        board = self.convertBoard(gameBoard)
        print("Board:")
        for col in board:
            print(col)

        actionsList = self.getMinActions(board)

        print("Actions: ")
        actionCount = 0
        for action in actionsList:
            print("Action: " + str(actionCount))
            actionCount+=1
            for col in action:
                print(col)

        minActions = []

        for action in actionsList:
            if self.getMinValue(action, 1) == -1:
                print("Computer move:")
                print("action -1:")
                for col in action:
                    print(col)
                return action
        for action in actionsList:
            if self.getMinValue(action, 1) == 0:
                print("Computer Move:")
                print("Computer move:")
                print("action 0:")
                for col in action:
                    print(col)
                return action
        else:
            print("random move: " + str(random.randint(0, len(actionsList))))
            return actionsList[random.randint(0, len(actionsList)-1)]


    def getMinActions(self, gameBoard):
        actionsList = []

        for i in range(self.cols):
            for j in range(self.rows):
                nearStone = False
                for k in range(-1,2):
                    for l in range(-1,2):
                        if i+k >= 0 and j+l >= 0 and i+k<15 and j+l < 15:
                            if not gameBoard[i+k][j+l] == 0:
                                nearStone = True
                if gameBoard[i][j] == 0 and nearStone == True:
                    board = copy.deepcopy(gameBoard)
                    board[i][j] = 1
                    actionsList.append(board)
        if len(actionsList) == 0:
            board = copy.deepcopy(gameBoard)
            board[7][8] = 1
            actionsList.append(board)
        return actionsList


    def getMaxActions(self, gameBoard):
        actionsList = []

        for i in range(self.cols):
            for j in range(self.rows):
                nearStone = False
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if i + k >= 0 and j + l >= 0 and i + k < 15 and j + l < 15:
                            if not gameBoard[i + k][j + l] == 0:
                                nearStone = True
                if gameBoard[i][j] == 0 and nearStone == True:
                    board = copy.deepcopy(gameBoard)
                    board[i][j] = -1
                    actionsList.append(board)

        if len(actionsList) == 0:
            board = copy.deepcopy(gameBoard)
            board[7][8] = -1
            actionsList.append(board)
        return actionsList

    def getMinValue(self, gameBoard, depth):
        # return -1 if cpu wins, 1 if player wins, 0 otherwise
        depth += 1

        #win state
        gameOver = self.endState(gameBoard)
        if gameOver != 0:
            return gameOver
        # else:
        #      return 0
        else:
            minActions = []
            # If not a win state generate the next set of moves
            minActionsList = self.getMaxActions(gameBoard)
            for action in minActionsList:
                actionValue = self.getMaxValue(action, depth)
                if actionValue == -1:
                    return actionValue
            for action in minActionsList:
                actionValue = self.getMaxValue(action, depth)
                if actionValue == 0:
                    return actionValue
            for action in minActionsList:
                actionValue = self.getMaxValue(action, depth)
                return actionValue

    def getMaxValue(self, gameBoard, depth):
        # return -1 if cpu wins, 1 if player wins, 0 otherwise

        # if depth > 7:
        #     return 0

        print("depth" + str(depth))
        gameOver = self.endState(gameBoard)
        if gameOver != 0:
            return gameOver
        # else:
        #     return 0
        else:
            # If not a win state generate the next set of moves
            minActionsList = self.getMinActions(gameBoard)
            for action in minActionsList:

                actionValue = self.getMinValue(action, depth)
                if actionValue == 1:
                    return actionValue
            for action in minActionsList:
                actionValue = self.getMinValue(action, depth)
                if actionValue == 0:
                    return actionValue
            for action in minActionsList:
                actionValue = self.getMinValue(action, depth)
                return actionValue

    def endStateCPU(self, gameBoard):
        icheckC = 0
        jcheckC = 0
        while icheckC <= 14 and jcheckC <= 14:
            icheck = icheckC
            jcheck = jcheckC
            c = 0
            if gameBoard[icheckC][jcheckC] == 1:
                while icheck <= 14 and jcheck <= 14:
                    if gameBoard[icheck][jcheck] == 1:
                        c += 1
                        self.countfivcom[0] = c
                    elif c != 5 and gameBoard[icheck][jcheck] == 0:
                        c = 0
                        self.countfivcom[0] = c
                    icheck += 1
                icheck = icheckC
                jcheck = jcheckC
                c = 0
                while icheck <= 14 and jcheck <= 14:
                    if gameBoard[icheck][jcheck] == 1:
                        c += 1
                        self.countfivcom[1] = c
                    elif c != 5 and gameBoard[icheck][jcheck] == 0:
                        c = 0
                        self.countfivcom[1] = c

                    jcheck += 1
                icheck = icheckC
                jcheck = jcheckC
                c = 0
                while icheck <= 14 and jcheck <= 14:
                    if gameBoard[icheck][jcheck] == 1:
                        c += 1
                        self.countfivcom[2] = c
                    elif c != 5 and gameBoard[icheck][jcheck] == 0:
                        c = 0
                        self.countfivcom[2] = c
                    icheck += 1
                    jcheck -= 1
                icheck = icheckC
                jcheck = jcheckC
                c = 0
                while icheck <= 14 and jcheck <= 14:
                    if gameBoard[icheck][jcheck] == 1:
                        c += 1
                        self.countfivcom[3] = c
                    elif c != 5 and gameBoard[icheck][jcheck] == 0:
                        c = 0
                        self.countfivcom[3] = c

                    icheck += 1
                    jcheck += 1

                if 5 in self.countfivcom:
                    self.checkcom[0] = True
                    #print("cpu win: " + str(self.checkcom[0]))
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
        #print("cpu win: " + str(self.checkcom[0]))
        return self.checkcom[0]

    def endStatePlayer(self, gameBoard):
        icheckC = 0
        jcheckC = 0
        while icheckC <= 14 and jcheckC <= 14:
            icheck = icheckC
            jcheck = jcheckC
            c = 0
            if gameBoard[icheckC][jcheckC] == -1:
                while icheck <= 14 and jcheck <= 14:
                    if gameBoard[icheck][jcheck] == -1:
                        c += 1
                        self.countfiv[0] = c
                    elif c != 5 and gameBoard[icheck][jcheck] == 0:
                        c = 0
                        self.countfiv[0] = c
                    icheck += 1
                icheck = icheckC
                jcheck = jcheckC
                c = 0
                while icheck <= 14 and jcheck <= 14:
                    if gameBoard[icheck][jcheck] == -1:
                        c += 1
                        self.countfiv[1] = c
                    elif c != 5 and gameBoard[icheck][jcheck] == 0:
                        c = 0
                        self.countfiv[1] = c

                    jcheck += 1
                icheck = icheckC
                jcheck = jcheckC
                c = 0
                while icheck <= 14 and jcheck <= 14:
                    if gameBoard[icheck][jcheck] == -1:
                        c += 1
                        self.countfiv[2] = c
                    elif c != 5 and gameBoard[icheck][jcheck] == 0:
                        c = 0
                        self.countfiv[2] = c
                    icheck += 1
                    jcheck -= 1
                icheck = icheckC
                jcheck = jcheckC
                c = 0
                while icheck <= 14 and jcheck <= 14:
                    if gameBoard[icheck][jcheck] == -1:
                        c += 1
                        self.countfiv[3] = c
                    elif c != 5 and gameBoard[icheck][jcheck] == 0:
                        c = 0
                        self.countfiv[3] = c

                    icheck += 1
                    jcheck += 1
                if 5 in self.countfiv:
                    self.check[0] = True
                    #print("Player win: " + str(self.check[0]))
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
        #print("Player win: " + str(self.check[0]))
        return self.check[0]

    def endState(self, gameBoard):
        if self.endStateCPU(gameBoard):
            return -1
        if self.endStatePlayer(gameBoard):
            return 1
        else:
            return 0
import Intersection

def placePiece(xCoord, yCoord):

    # PSUEDO place piece
    i = 0
    j = 0
    check = [False]
    countfiv = [0, 0, 0, 0]

    def countfive():
        global i, j, countfiv, arrayi, check
        icheck = i
        jcheck = j
        c = 0
        if arrayi[i][j]:
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

    # TODO: add countFive.py after a piece is placed

import pygame

from Intersection import Intersection

pygame.init()

# All neccessary attributes
nBoxes = 19
boxMargin = 1
boxWidth = 30
boxLength = 30
pieceRadius = 8
windowWidth = (boxWidth + boxMargin) * nBoxes
windowLength = (boxLength + boxMargin) * nBoxes
turnOne = True

pygame.display.set_caption('Gomoku')
screen = pygame.display.init()
windowSurface = pygame.display.set_mode((windowLength, windowWidth))
background = pygame.Surface((windowWidth, windowLength))
background.fill(pygame.Color(0,0,0))
foreground = pygame.Surface((windowWidth,windowLength))

board = [[]*nBoxes]*nBoxes




is_running = True

while is_running:
    x = 0
    y = 0
    rowDepth = 0

    for i in range(nBoxes * nBoxes):
        intersectionRect = Intersection(x, y, boxWidth, boxLength)
        intersectionRect.draw(background, x, y)
        #board[x/boxWidth][y/boxLength] = intersectionRect

        #pygame.draw.rect(background, (255, 255, 255), (x, y, boxWidth, boxLength))
        x += (boxWidth + boxMargin)
        rowDepth += 1

        if rowDepth == 19:
            rowDepth = 0
            x = 0
            y = y + (boxLength + boxMargin)
    print(board)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        # Logic for alternating between black and white pieces
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pieceX, pieceY = pygame.mouse.get_pos()

            # Define piece colours
            pieceOne = (0,128,128)
            pieceTwo = (128,0,128)

            # Draw white piece
            if turnOne:
                pygame.draw.circle(foreground, pieceOne, (pieceX,pieceY), pieceRadius)
                turnOne = False

            # Draw black piece
            else:

                pygame.draw.circle(foreground, pieceTwo, (pieceX, pieceY), pieceRadius)
                turnOne = True
            #print("Mouse down at (%d, %d)" % event.pos)


    windowSurface.blit(background, (0, 0))
    foreground.set_alpha(100)
    windowSurface.blit(foreground, (0, 0))


    pygame.display.update()
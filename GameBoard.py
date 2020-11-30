import pygame

pygame.init()

nBoxes = 19
boxMargin = 1
boxWidth = 30
boxLength = 30
windowWidth = (boxWidth + boxMargin) * nBoxes
windowLength = (boxLength + boxMargin) * nBoxes
print(windowLength)

pygame.display.set_caption('Gomoku')
window_surface = pygame.display.set_mode((windowLength, windowWidth))


background = pygame.Surface((windowWidth, windowLength))
background.fill(pygame.Color(0,0,0))


is_running = True

while is_running:
    x = 0
    y = 0
    rowDepth = 0

    for i in range(nBoxes * nBoxes):
        pygame.draw.rect(background, (255,255,255), (x,y,boxWidth, boxLength))
        x += (boxWidth + boxMargin)
        rowDepth += 1

        if rowDepth == 19:
            rowDepth = 0
            x = 0
            y = y + (boxLength + boxMargin)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    window_surface.blit(background, (0, 0))


    pygame.display.update()
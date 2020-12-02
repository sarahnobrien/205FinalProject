import pygame
import pygame_menu
import sys
import webbrowser
from Game import Game


pygame.init()
surface = pygame.display.set_mode((600, 400))
difficultyGet = [1]
globalMouse = pygame.mouse.get_pos()
def set_difficulty(value, difficulty):
    difficultyGet[0] = difficulty

def start_the_game():
    pygame.init()

    size = screenWidth,screenHeight = 1100,800

    # Start the gameboard
    game = Game()
    game.StartGameBoard()

    clickMarginOfError = 20

    screen = pygame.display.set_mode(size)

    font = pygame.font.Font('freesansbold.ttf', 50)
    cpuTurn = False

    textRestart = font.render('Restart', True, (0,0,0))
    textExit = font.render('Exit', True, (0,0,0))
    textMenu = font.render('Menu', True, (0, 0, 0))

    # Display who is going first
    playerFont = pygame.font.Font('freesansbold.ttf', 25)
    CPUColor = (0, 128, 128)
    PlayerColor = (128, 0, 128)

    # See which player goes first and output it
    playerText = playerFont.render("First Player: Player", True, PlayerColor)
    if game.getFirstPlayer() == "CPU":
        playerText = playerFont.render("First Player: CPU", True, CPUColor)


    def draw():
        global rows, cols, boxWidth
        rows = 15
        cols = 15
        boxWidth = 50

        # drawing the lines for the intersections
        for i in range(cols):
            for j in range(rows):
                pygame.draw.line(screen,(0,0,0),(0,boxWidth + boxWidth*i),(800,boxWidth + boxWidth*i),2)
                pygame.draw.line(screen,(0,0,0),(boxWidth + boxWidth*j,0),(boxWidth + boxWidth*j,800),2)
        pygame.draw.line(screen,(0,0,0),(800,0),(800,800),20)

        # Drawing the stones on the board
        for i in range(cols):
            for j in range(rows):
                game.getGameBoard()[i][j].draw(screen)

        # Restart and exit button
        if 860 <= globalMousePos[0] <= 1090 and 255 <= globalMousePos[1] <= 305:
            pygame.draw.rect(screen,(255, 0, 0),[860,255,180,55])
        else: 
            pygame.draw.rect(screen,(255, 255, 255),[860,255,180,55])


        if 900 <= globalMousePos[0] <= 1090 and 465 <= globalMousePos[1] <= 520:
            pygame.draw.rect(screen,(255, 0, 0),[900,465,102,55])
        else: 
            pygame.draw.rect(screen,(255, 255, 255),[900,465,102,55])

        if 880 <= globalMousePos[0] <= 1090 and 360 <= globalMousePos[1] <= 405: #this one is for "go back to menu"
            pygame.draw.rect(screen, (255, 0, 0), [880, 360, 140, 55])
        else:
            pygame.draw.rect(screen, (255, 255, 255), [880, 360, 140, 55])

        screen.blit(textRestart, (860,255))
        screen.blit(textExit, (900,465))
        screen.blit(textMenu, (880, 360))

        # Check which player wins and output it
        if game.gameOver:
            if game.playerWins:
                winningText = playerFont.render("You Win!!!", True, PlayerColor)
            if game.computerWins:
                winningText = playerFont.render("CPU Wins :(", True, CPUColor)
            screen.blit(winningText, (840, 80))

        # Check if we want to display the first player
        screen.blit(playerText, (840, 50))

        pygame.display.flip()

    def restart():
        start_the_game()

    def menuFromGame():
        surface = pygame.display.set_mode((600, 400))
        menu.mainloop(surface)

    def exitGame():
        sys.exit()

    while True:
        globalMousePos = pygame.mouse.get_pos()
        screen.fill((255, 255, 255))
        draw()

        if game.getFirstPlayer() == "CPU":
            game.placePieceCPU()
            game.firstPlayer = "NULL"
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                menu.mainloop(surface)
                screen = pygame.display.set_mode((600, 400))
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(cols):
                    for j in range(rows):
                        # finding the intersection that was clicked

                        if boxWidth + boxWidth*i - clickMarginOfError <= globalMousePos[0] <= boxWidth + boxWidth*i + clickMarginOfError \
                                and boxWidth + boxWidth*j - clickMarginOfError <= globalMousePos[1] <= boxWidth + boxWidth*j+clickMarginOfError:
                            if game.getCurrTurn() == "Player":
                                game.placePieceGeneric(i, j) # Place players piece
                            if game.getCurrTurn() == "CPU":
                                game.placePieceGeneric(i, j)

            # Detect if restart or exit button are clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 860 <= globalMousePos[0] <= 1090 and 255 <= globalMousePos[1] <= 305:
                    restart()
                elif 880 <= globalMousePos[0] <= 1090 and 360 <= globalMousePos[1] <= 405:
                    surface = pygame.display.set_mode((600, 400))
                    menu.mainloop(surface)

                elif 900 <= globalMousePos[0] <= 1090 and 465 <= globalMousePos[1] <= 520:
                    pygame.quit()
                    exitGame()
            if event.type == pygame.QUIT:
                screen = pygame.display.set_mode((600, 400))
                return False
            pygame.display.update()


def about_us():
    def githubLink():
        webbrowser.open("https://github.com/sarahnobrien/205FinalProject")

    def trelloLink():
        webbrowser.open("https://trello.com/b/pvtiJr5s/cs205-team-2")
    green = (0, 255, 0) 
    blue = (0, 0, 225) 
    pygame.init()
    display_surface = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('CS205 Team 2')
    font = pygame.font.Font('freesansbold.ttf', 32)
    font1 = pygame.font.Font('freesansbold.ttf', 80)
    text0 = font.render('CS205 Team 2', True, (0,0,0))
    textRect0 = text0.get_rect()
    textRect0.center = (300, 60)
    text1 = font.render('Zhixin', True, green, (0,0,0))
    textRect1 = text1.get_rect()
    textRect1.center = (300, 150)
    text2 = font.render('Sarah', True, green, (0,0,0))
    textRect2 = text2.get_rect()
    textRect2.center = (300, 200)
    text3 = font.render('Ben', True, green, (0,0,0))
    textRect3 = text3.get_rect()
    textRect3.center = (300, 250)
    text4 = font.render('Nevin', True, green, (0,0,0))
    textRect4 = text4.get_rect()
    textRect4.center = (300, 300)
    textGit = font.render('Github Link', True, (0,0,0))
    textMenu = font.render('Menu', True, (0, 0, 0))
    textTrello = font.render('Trello Link', True, (0,0,0))

    # Button behavior
    while True:
        globalMouse = pygame.mouse.get_pos()
        display_surface.fill((220,220,220))
        display_surface.blit(text0, textRect0)
        display_surface.blit(text1, textRect1)
        display_surface.blit(text2, textRect2)
        display_surface.blit(text3, textRect3)
        display_surface.blit(text4, textRect4)
        if 50 <= globalMouse[0] <= 50+190 and 350 <= globalMouse[1] <= 350+40:
            pygame.draw.rect(display_surface,(255, 0, 0),[50,350,190,40]) 
        else: 
            pygame.draw.rect(display_surface,(0, 255, 0),[50,350,190,40])

        if 270 <= globalMouse[0] <= 270+110 and 350 <= globalMouse[1] <= 350+40:
            pygame.draw.rect(display_surface,(255, 0, 0),[260,350,110,40])
        else:
            pygame.draw.rect(display_surface,(0, 255, 0),[260,350,110,40])

        if 400 <= globalMouse[0] <= 400+170 and 350 <= globalMouse[1] <= 350+40:
            pygame.draw.rect(display_surface,(255, 0, 0),[400,350,170,40]) 
        else: 
            pygame.draw.rect(display_surface,(0, 255, 0),[400,350,170,40]) 
        display_surface.blit(textGit, (50,350))

        display_surface.blit(textMenu, (270, 350))
        display_surface.blit(textTrello, (400,350))
        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 50 <= globalMouse[0] <= 50+190 and 350 <= globalMouse[1] <= 350+40:
                    githubLink()
                elif 270 <= globalMouse[0] <= 270+110 and 350 <= globalMouse[1] <= 350+40:
                    menu.mainloop(surface)
                elif 400 <= globalMouse[0] <= 400+170 and 350 <= globalMouse[1] <= 350+40:
                    trelloLink()

            if event.type == pygame.QUIT:
                screen = pygame.display.set_mode((600, 400))
                return False
            pygame.display.update()



def gomoku_rules():
    pygame.init()
    rule_display = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('Rules')
    font = pygame.font.Font('freesansbold.ttf', 16)
    fontBig = pygame.font.Font('freesansbold.ttf', 30)
    text0 = fontBig.render('RULES', True, (255, 0, 0))
    textRect0 = text0.get_rect()
    textRect0.center = (300, 50)
    text1 = font.render('Stones are placed in the board’s intersections.', True, (0, 0, 0))
    textRect1 = text1.get_rect()
    textRect1.center = (300, 100)
    text2 = font.render('During the game, player 1 and the CPU will alternate turns, ' , True, (0, 0, 0))
    textRect2 = text2.get_rect()
    textRect2.center = (300, 150)
    text3 = font.render('each placing one of their stones on the board.' , True, (0, 0, 0))
    textRect3 = text3.get_rect()
    textRect3.center = (300, 200)
    text4 = font.render('To win, you must be the first player to create ', True, (0, 0, 0))
    textRect4 = text4.get_rect()
    textRect4.center = (300, 250)
    text5 = font.render('an unbroken line of 5 of your stones, in any direction. ', True, (0, 0, 0))
    textRect5 = text5.get_rect()
    textRect5.center = (300, 300)
    textMenu = fontBig.render('Menu', True, (255, 255, 255))

    while True :

        globalMouse = pygame.mouse.get_pos()

        rule_display.fill((255, 255, 255))
        rule_display.blit(text0, textRect0)
        rule_display.blit(text1, textRect1)
        rule_display.blit(text2, textRect2)
        rule_display.blit(text3, textRect3)
        rule_display.blit(text4, textRect4)
        rule_display.blit(text5, textRect5)


        if 245 <= globalMouse[0] <= 245 + 90 and 350 <= globalMouse[1] <= 350 + 30:
            pygame.draw.rect(rule_display, (100, 100, 100), [245, 350, 90, 30])
        else:
            pygame.draw.rect(rule_display, (0, 0, 0), [245, 350, 90, 30])

        rule_display.blit(textMenu, (250, 350))

        for event in pygame.event.get() : 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 245 <= globalMouse[0] <= 245 + 90 and 350 <= globalMouse[1] <= 350 + 30:
                    menu.mainloop(surface)
            if event.type == pygame.QUIT:
                screen = pygame.display.set_mode((600, 400))
                return False
            pygame.display.update()


    if 270 <= globalMouse[0] <= 270 + 80 and 350 <= globalMouse[1] <= 350 + 40:
        pygame.draw.rect(rule_display, (255, 0, 0), [270, 350, 80, 40])
    else:
        pygame.draw.rect(rule_display, (0, 255, 0), [270, 350, 80, 40])
        rule_display.blit(textMenu, (280, 360))

    for event in pygame.event.get() :
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 250 <= globalMouse[0] <= 250 + 80 and 350 <= globalMouse[1] <= 350 + 40:
                menu.mainloop(surface)
        pygame.display.update()


menu = pygame_menu.Menu(400, 600, 'GOMOKU',
                       theme=pygame_menu.themes.THEME_GREEN)


menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)

menu.add_button('Play', start_the_game)
menu.add_button('About us', about_us)
menu.add_button('Rules', gomoku_rules)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)

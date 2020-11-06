import pygame
import random
import pygame_menu
import sys
import time
import webbrowser
<<<<<<< HEAD:GUI.py
from Intersection import Intersection
from Game import Game
=======
>>>>>>> 146c304bd33885edc338fce1c383f2700b2c8ac4:menu.py

pygame.init()
surface = pygame.display.set_mode((600, 400))
difficultyGet = [1]
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

    # Creates game board TODO: Move to Game.py
    textRestart = font.render('Restart', True, (0,0,0))
    textExit = font.render('Exit', True, (0,0,0))


    def draw():
        global rows, cols, boxWidth
        rows = 15
        cols = 15
        boxWidth = 50
        #drawing the lines for the intersections
        for i in range(cols):
            for j in range(rows):
                pygame.draw.line(screen,(0,0,0),(0,boxWidth + boxWidth*i),(800,boxWidth + boxWidth*i),2)
                pygame.draw.line(screen,(0,0,0),(boxWidth + boxWidth*j,0),(boxWidth + boxWidth*j,800),2)
        pygame.draw.line(screen,(0,0,0),(800,0),(800,800),20)

        #Drawing the stones on the board

        for i in range(cols):
            for j in range(rows):
                game.getGameBoard()[i][j].draw(screen)

        # Restart and exit button
        if 900 <= mousePos[0] <= 1090 and 300 <= mousePos[1] <= 355:
            pygame.draw.rect(screen,(255, 0, 0),[900,300,190,55]) 
        else: 
            pygame.draw.rect(screen,(0, 255, 0),[900,300,190,55])
        if 900 <= mousePos[0] <= 1090 and 600 <= mousePos[1] <= 655:
            pygame.draw.rect(screen,(255, 0, 0),[900,600,110,55]) 
        else: 
            pygame.draw.rect(screen,(0, 255, 0),[900,600,110,55]) 

        screen.blit(textRestart, (900,300))
        screen.blit(textExit, (900,600))
        pygame.display.flip()

    def restart():
        start_the_game()
    def exitGame():
        sys.exit()
    #For first sprint, we assume user first (black), and computer part will be sprint 2
    
    while True:
        mousePos = pygame.mouse.get_pos()
        screen.fill((255, 255, 0))
        draw()

        for event in pygame.event.get() : 
            if event.type == pygame.KEYDOWN:
                screen = pygame.display.set_mode((600, 400))
                menu.mainloop(surface)
            if event.type == pygame.MOUSEBUTTONDOWN: 
                for i in range(cols):
                    for j in range(rows):
                        #finding the intersection that was clicked
                        #not sure what the 20 is for
                        if boxWidth + boxWidth*i - clickMarginOfError <= mousePos[0] <= boxWidth + boxWidth*i + clickMarginOfError \
                                and boxWidth + boxWidth*j - clickMarginOfError <= mousePos[1] <= boxWidth + boxWidth*j+clickMarginOfError:
                            if game.getTurn() == "player":
                                game.getGameBoard()[i][j].click("player")
                                game.countfive()
                                print(game.checkGet())
                                if game.checkGet() == True:
                                    print("good")
                                game.setTurn("CPU")
                                game.placePieceCPU()





            # Detect if restart or exit button are clicked
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if 900 <= mousePos[0] <= 1090 and 300 <= mousePos[1] <= 355:
                    restart()
                elif 900 <= mousePos[0] <= 1090 and 600 <= mousePos[1] <= 655:
                    pygame.quit()
                    exitGame()

                        
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
    textTrello = font.render('Trello Link', True, (0,0,0))

    # Button behavior
    while True :
        mouse = pygame.mouse.get_pos()
        display_surface.fill((220,220,220))
        display_surface.blit(text0, textRect0)
        display_surface.blit(text1, textRect1)
        display_surface.blit(text2, textRect2)
        display_surface.blit(text3, textRect3)
        display_surface.blit(text4, textRect4)
        if 50 <= mouse[0] <= 50+190 and 350 <= mouse[1] <= 350+40: 
            pygame.draw.rect(display_surface,(255, 0, 0),[50,350,190,40]) 
        else: 
            pygame.draw.rect(display_surface,(0, 255, 0),[50,350,190,40])
        if 400 <= mouse[0] <= 400+170 and 350 <= mouse[1] <= 350+40: 
            pygame.draw.rect(display_surface,(255, 0, 0),[400,350,170,40]) 
        else: 
            pygame.draw.rect(display_surface,(0, 255, 0),[400,350,170,40]) 
        display_surface.blit(textGit, (50,350))
        display_surface.blit(textTrello, (400,350))
        for event in pygame.event.get() : 
            if event.type == pygame.KEYDOWN: 
                menu.mainloop(surface)
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if 50 <= mouse[0] <= 50+190 and 350 <= mouse[1] <= 350+40:  
                    githubLink()
                elif 400 <= mouse[0] <= 400+170 and 350 <= mouse[1] <= 350+40:
                    trelloLink()
            pygame.display.update()
    
def gomoku_rules():
    pygame.init()
    rule_display = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('Rules')
    font = pygame.font.Font('freesansbold.ttf', 16)
    fontBig = pygame.font.Font('freesansbold.ttf', 20)
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

    while True :
        rule_display.fill((255, 255, 255))
        rule_display.blit(text0, textRect0)
        rule_display.blit(text1, textRect1)
        rule_display.blit(text2, textRect2)
        rule_display.blit(text3, textRect3)
        rule_display.blit(text4, textRect4)
        rule_display.blit(text5, textRect5)
        for event in pygame.event.get() : 
            if event.type == pygame.KEYDOWN: 
                menu.mainloop(surface)  
            pygame.display.update()
    
    

<<<<<<< HEAD:GUI.py
menu = pygame_menu.Menu(400, 600, 'GOMOKU',
=======
menu = pygame_menu.Menu(300, 600, 'GOMOKU',
>>>>>>> 146c304bd33885edc338fce1c383f2700b2c8ac4:menu.py

                       theme=pygame_menu.themes.THEME_GREEN)


menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)

menu.add_button('Play', start_the_game)
menu.add_button('About us', about_us)
menu.add_button('Rules', gomoku_rules)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)

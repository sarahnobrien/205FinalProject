import pygame
import pygame_menu
import webbrowser
pygame.init()
surface = pygame.display.set_mode((600, 400))
difficultyGet = [1]
def set_difficulty(value, difficulty):
    difficultyGet[0] = difficulty

def start_the_game():
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
            if event.type == pygame.KEYDOWN:
                windowSurface = pygame.display.set_mode((600, 400))
                menu.mainloop(surface) 
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
    font = pygame.font.Font('freesansbold.ttf', 32)
    text1 = font.render('First get five chain will win', True, (255, 0, 0))
    textRect1 = text1.get_rect()
    textRect1.center = (300, 200)
    while True :
        rule_display.fill((0, 255, 0))  
        rule_display.blit(text1, textRect1)
        for event in pygame.event.get() : 
            if event.type == pygame.KEYDOWN: 
                menu.mainloop(surface)  
            pygame.display.update()
    
    
    
menu = pygame_menu.Menu(300, 600, 'GOMOKU',
                       theme=pygame_menu.themes.THEME_GREEN)


menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)

menu.add_button('Play', start_the_game)
menu.add_button('About us', about_us)
menu.add_button('Rules', gomoku_rules)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)

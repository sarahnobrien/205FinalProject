import pygame
import pygame_menu
pygame.init()
surface = pygame.display.set_mode((600, 400))
difficultyGet = [1]
def set_difficulty(value, difficulty):
    difficultyGet[0] = difficulty

def start_the_game():
    if difficultyGet[0] == 1:
        print("hard")
    elif difficultyGet[0] == 2:
        print("easy")
    

    

def about_us():
    green = (0, 255, 0) 
    blue = (0, 0, 225) 
    pygame.init()
    display_surface = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('CS205 Team 2')
    font = pygame.font.Font('freesansbold.ttf', 32)
    text1 = font.render('Zhixin', True, green, blue)
    textRect1 = text1.get_rect()
    textRect1.center = (300, 50)
    text2 = font.render('Sarah', True, green, blue)
    textRect2 = text2.get_rect()
    textRect2.center = (300, 150)
    text3 = font.render('Ben', True, green, blue)
    textRect3 = text3.get_rect()
    textRect3.center = (300, 250)
    text4 = font.render('Nevin', True, green, blue)
    textRect4 = text4.get_rect()
    textRect4.center = (300, 350)
    while True : 
        display_surface.fill(green)  
        display_surface.blit(text1, textRect1)
        display_surface.blit(text2, textRect2)
        display_surface.blit(text3, textRect3)
        display_surface.blit(text4, textRect4) 
        for event in pygame.event.get() : 
            if event.type == pygame.KEYDOWN: 
                menu.mainloop(surface)  
            pygame.display.update()
    
def gomoku_rules():
    pygame.init()
    rule_display = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('Rules')
    font = pygame.font.Font('freesansbold.ttf', 32)
    text1 = font.render('First get five chain will win', True, (255, 255, 0))
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

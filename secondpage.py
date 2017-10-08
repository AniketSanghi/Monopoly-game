import pygame

pygame.init()


red = (255,0,0)
black = (0,0,0)

display_width = 1430
display_height = 800

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Monopoly")
pygame.display.update()

def message_to_screen(msg, color,x,y):
    font = pygame.font.SysFont(None, 25)
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x,y])

def screen2():
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
        gameDisplay.fill(black)
        img = pygame.image.load('image.png')
        gameDisplay.blit(img, (800,200))
        
        message_to_screen("Number of players (1-4) : ", red, 50, 200)
        message_to_screen("Winnning Amount : ", red, 50, 300)

        
        
        pygame.display.update()
        
                
screen2()

pygame.quit()
quit()

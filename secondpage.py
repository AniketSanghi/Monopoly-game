import pygame
import mainboard,functions

pygame.init()

yellow = (255,255,0)
red = (255,0,0)
black = (0,0,0)
back = (100,10,100)

display_width = 1430
display_height = 800

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Monopoly")
pygame.display.update()

   



def screen2():
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
        gameDisplay.fill(black)
        img = pygame.image.load('images/image.png')
        gameDisplay.blit(img, (800,200))
        
        functions.message_to_screen("Number of players (1-4) : ", red, 50, 200)
        functions.message_to_screen("Winnning Amount : ", red, 50, 300)

        functions.button("NEXT",300,600,200,50,yellow,back,"next")

        pygame.display.update()
        
                




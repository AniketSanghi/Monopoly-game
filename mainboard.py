import pygame

pygame.init()

display_width = 1430
display_height = 800
card_length = 120
card_breadth = 70

white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
red = (200,0,0)
blue = (0,0,255)
green = (0,150,0)
lblue = (0,0,100)
maroon = (100,10,100)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Monopoly")
pygame.display.update()

def addimage(link,x,y):
     img = pygame.image.load(link)
     gameDisplay.blit(img, [x,y])
     pygame.display.update()

def mainscreen():
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
        gameDisplay.fill(lblue)
        pygame.draw.rect(gameDisplay, white, [0,0,display_height,display_height])
        pygame.draw.rect(gameDisplay, maroon, [card_length,card_length,display_height-2*card_length,display_height-2*card_length])

        addimage('go.png',display_height-card_length,display_height-card_length)
        addimage('gotojail.png',display_height-card_length,0)
        addimage('parking.png',0,0)
        addimage('jail.png',0,display_height-card_length)

        

mainscreen()

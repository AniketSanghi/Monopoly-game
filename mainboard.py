import pygame

pygame.init()

display_width = 1430
display_height = 800
card_length = 130
card_breadth = 60

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

#def property_sketcher(name, price, )

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

        addimage('images/go.png',display_height-card_length,display_height-card_length)
        addimage('images/gotojail.png',display_height-card_length,0)
        addimage('images/parking.png',0,0)
        addimage('images/jail.png',0,display_height-card_length)
        addimage('images/chance1.png',card_length+2*card_breadth,display_height-card_length)
        addimage('images/chance3.png',display_height-card_length,card_length+5*card_breadth)
        addimage('images/chance2.png',card_breadth+card_length,0)
        addimage('images/commChest1.png',7*card_breadth+card_length,display_height-card_length)
        addimage('images/commChest2.png',0,2*card_breadth+card_length)
        addimage('images/commChest2.png',display_height-card_length,2*card_breadth+card_length)
        addimage('images/water.png',7*card_breadth+card_length,0)
        addimage('images/elec.png',0,7*card_breadth+card_length)
        addimage('images/luxury.png',display_height-card_length,7*card_breadth+card_length)
        addimage('images/income.png',card_length+5*card_breadth,display_height-card_length)



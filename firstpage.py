import pygame
import secondpage
import functions



pygame.init()

display_width = 1430
display_height = 800

white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
red = (255,50,0)
blue = (0,0,255)
green = (0,255,0)
back = (100,10,100)

clock = pygame.time.Clock()


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Monopoly")
pygame.display.update()




def screen1():
    

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        x = 615
        y1=200
        y2=300
        y3=400
        l=200
        h=50

        gameDisplay.fill(back)
        img = pygame.image.load('images/monopolyimage.png')
        gameDisplay.blit(img, (200,0))
       
        functions.button("START",x,y1,l,h,yellow,blue,"screen2")        
        functions.button("LEADERBOARD",x,y2,l,h,yellow,blue,"leaderboard")
        functions.button("QUIT",x,y3,l,h,yellow,blue,"quit1")

        
        pygame.display.update()
        clock.tick(60)
        



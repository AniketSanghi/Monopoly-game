import pygame
import secondpage


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


def button(msg,x,y,l,h,ac,ic,function):
    
    pygame.draw.rect(gameDisplay, ic, [x,y,l,h])
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
        
    if x < mouse[0] < x+l and y < mouse[1] < y+h:
           pygame.draw.rect(gameDisplay, ac, [x,y,l,h])
           if click[0]==1:
                if function == "screen2":
                    secondpage.screen2()
                    
#                if function == "leaderboard":
#                    leaderboard.leaderboard()
                if function == "quit1":
                    quit()
    _font = pygame.font.Font('freesansbold.ttf',20)
    textSurface, textRect = text_in_box(msg, _font)
    textRect.center = (x+l/2,y+h/2)
    gameDisplay.blit(textSurface, textRect)      
    
    
def text_in_box(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()
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
        img = pygame.image.load('monopolyimage.png')
        gameDisplay.blit(img, (200,0))
       
        button("START",x,y1,l,h,yellow,blue,"screen2")        
        button("LEADERBOARD",x,y2,l,h,yellow,blue,"leaderboard")
        button("QUIT",x,y3,l,h,yellow,blue,"quit1")

        
        pygame.display.update()
        clock.tick(60)
        
screen1()
pygame.quit()
quit()

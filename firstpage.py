import pygame

pygame.init()

display_width = 1430
display_height = 800

white = (255,255,255)
black = (0,0,0)

yellow = (255,255,0)
red = (255,50,0)
blue = (0,0,255)
green = (0,255,0)

clock = pygame.time.Clock()


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Monopoly")
pygame.display.update()

def button(msg,x,y,l,h,ac,ic):
    
    pygame.draw.rect(gameDisplay, ic, [x,y,l,h])
    mouse = pygame.mouse.get_pos()
    if x < mouse[0] < x+l and y < mouse[1] < y+h:
           pygame.draw.rect(gameDisplay, ac, [x,y,l,h])
    _font = pygame.font.Font('freesansbold.ttf',20)
    textSurface, textRect = textbox(msg, _font)
    textRect.center = (x+l/2,y+h/2)
    gameDisplay.blit(textSurface, textRect)      
    
    
def textbox(text, font):
    textSurface = font.render(text, True, green)
    return textSurface, textSurface.get_rect()

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
 
    gameDisplay.fill(yellow)
   
    button("START",x,y1,l,h,red,blue)        
    button("LEADERBOARD",x,y2,l,h,red,blue)
    button("QUIT",x,y3,l,h,red,blue)

    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

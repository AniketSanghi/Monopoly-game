import pygame
import mainboard

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

def button2(msg,x,y,l,h,ac,ic,function):
    
    pygame.draw.rect(gameDisplay, ic, [x,y,l,h])
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
        
    if x < mouse[0] < x+l and y < mouse[1] < y+h:
           pygame.draw.rect(gameDisplay, ac, [x,y,l,h])
           if click[0]==1:
                
                if function == "next":
                    mainboard.mainscreen()

    _font = pygame.font.Font('freesansbold.ttf',20)
    textSurface, textRect = text_in_box2(msg, _font)
    textRect.center = (x+l/2,y+h/2)
    gameDisplay.blit(textSurface, textRect)

def text_in_box2(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()    

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
        img = pygame.image.load('images/image.png')
        gameDisplay.blit(img, (800,200))
        
        message_to_screen("Number of players (1-4) : ", red, 50, 200)
        message_to_screen("Winnning Amount : ", red, 50, 300)

        button2("NEXT",300,600,200,50,yellow,back,"next")

        pygame.display.update()
        
                




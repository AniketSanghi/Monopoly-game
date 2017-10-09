import pygame
import secondpage,mainboard

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

def addimage(link,x,y):
     img = pygame.image.load(link)
     gameDisplay.blit(img, [x,y])
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
                if function == "next":
                    mainboard.mainscreen()
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

def message_to_screen(msg, color,x,y):
    font = pygame.font.SysFont(None, 25)
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x,y])



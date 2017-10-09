import pygame
import firstpage

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

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Monopoly")
pygame.display.update()

firstpage.screen1()




pygame.quit()
quit()

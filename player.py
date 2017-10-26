import pygame,functions

pygame.init()

display_width = 1430
display_height = 800
card_length = 130
card_breadth = 60

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

class Player:
    def __init__(self,color,no):
        self.cash = 300000
        self.posx = display_height-card_length/2
        self.posy = display_height-card_length/2
        self.total_wealth = 300000
        self.properties = []
        self.getoutofjailcard = 0
        self.color = color
        self.no = no
    def draw(self):
            _font = pygame.font.Font('freesansbold.ttf',20)
            pygame.draw.circle(functions.gameDisplay,self.color,[(int)(self.posx),(int)(self.posy)],20)
            textSurface = _font.render(self.no, True, black)
            textRect = textSurface.get_rect()
            textRect.center = (self.posx,self.posy)
            gameDisplay.blit(textSurface, textRect)
            pygame.display.update()        
    
        
    def movement(self,n):
        while n>0:
            if card_length+card_breadth/2<self.posx < display_height-card_length/2 and self.posy == display_height-card_length/2:
                self.posx -= card_breadth
            elif card_length/2<self.posx < display_height-(card_length+card_breadth/2) and self.posy == card_length/2:
                self.posx += card_breadth
            elif self.posx == card_length/2 and  card_length+card_breadth/2 < self.posy < display_height-card_length/2:
                self.posy -= card_breadth
            elif self.posx == display_height-card_length/2 and  card_length/2 < self.posy < display_height-(card_length+card_breadth/2):
                self.posy += card_breadth
            elif self.posx == display_height-card_length/2  and self.posy == display_height-card_length/2:
                self.posx -= (card_breadth+card_length)/2
            elif self.posx == card_length/2  and self.posy == display_height-card_length/2:
                self.posy -= (card_breadth+card_length)/2
            elif self.posx == card_length/2  and self.posy == card_length/2:
                self.posx += (card_breadth+card_length)/2
            elif self.posx == display_height-card_length/2  and self.posy == card_length/2:
                self.posy += (card_breadth+card_length)/2
            elif self.posx == card_length+card_breadth/2  and self.posy == display_height-card_length/2:
                self.posx -= (card_breadth+card_length)/2
            elif self.posx == display_height-(card_length+card_breadth/2)  and self.posy == card_length/2:
                self.posx += (card_breadth+card_length)/2
            elif self.posx == display_height-card_length/2  and self.posy == display_height-(card_length+card_breadth/2):
                self.posy += (card_breadth+card_length)/2
            elif self.posx == card_length/2  and self.posy ==  card_length+card_breadth/2:
                self.posy -= (card_breadth+card_length)/2    
            n-=1
            
player = [Player(blue,'1'),Player(red,'2')]

import pygame,time
import functions,Property,player
 

pygame.init()

display_width = 1430
display_height = 800
card_length = 130
card_breadth = 60
blockl = 120
blockh = 50

white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
red = (200,0,0)
blue = (0,0,255)
green = (0,150,0)
lblue = (0,0,100)
llblue = (0,160,160)
maroon = (100,10,100)
grey = (160,160,160)
orange = (228,142,88)





def mainscreen():
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                gameExit = True
        
        
        drawing()
            
                
           
def drawing():        
            functions.gameDisplay.fill(lblue)
            pygame.draw.rect(functions.gameDisplay, white, [0,0,display_height,display_height])
            functions.addimage('images/back.png',card_length,card_length)

            functions.addimage('images/go.png',display_height-card_length,display_height-card_length)
            functions.addimage('images/gotojail.png',display_height-card_length,0)
            functions.addimage('images/parking.png',0,0)
            functions.addimage('images/jail.png',0,display_height-card_length)
            functions.addimage('images/chance1.png',card_length+2*card_breadth,display_height-card_length)
            functions.addimage('images/chance3.png',display_height-card_length,card_length+5*card_breadth)
            functions.addimage('images/chance2.png',card_breadth+card_length,0)
            functions.addimage('images/commChest1.png',7*card_breadth+card_length,display_height-card_length)
            functions.addimage('images/commChest2.png',0,2*card_breadth+card_length)
            functions.addimage('images/commChest2.png',display_height-card_length,2*card_breadth+card_length)
            functions.addimage('images/water.png',7*card_breadth+card_length,0)
            functions.addimage('images/elec.png',0,7*card_breadth+card_length)
            functions.addimage('images/luxury.png',display_height-card_length,7*card_breadth+card_length)
            functions.addimage('images/income.png',card_length+5*card_breadth,display_height-card_length)

            functions.button("ROLE DICE",(display_height-blockl)/2,(display_height/2+card_length)/2 - 2*blockh,blockl,blockh,yellow,llblue,"roll",red)

            Property._property["delhi"].locmaker()
            Property._property["mumbai"].locmaker()
            Property._property["banglore"].locmaker()
            player.player[1].draw()
            player.player[0].draw()

            pygame.display.update()       
def move():
        n = functions.rolldice()
        while n>0:
            drawing()
            player.player[0].movement()
            player.player[1].draw()
            pygame.display.update()
            n = n-1
 
        mainscreen()


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

player_index = 0
rollonce = 0
#card_display = 0
#place

clock = pygame.time.Clock()


def mainscreen():
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                gameExit = True
        
        
        drawing()
        clock.tick(15)    
                
           
def drawing():        
            functions.gameDisplay.fill(lblue)
            pygame.draw.rect(functions.gameDisplay, white, [0,0,display_height,display_height])
            functions.addimage('images/back.png',card_length,card_length)
            _font = pygame.font.Font('freesansbold.ttf',20)

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

            functions.text_in_box("Player %r's turn "%(player_index+1),_font,blue,card_length,card_length,display_height-2*card_length,blockh)

            Button("ROLE DICE",(display_height-blockl)/2,(display_height/2+card_length)/2 - 1.25*blockh,blockl,blockh,yellow,llblue,"roll",red)
            Button("END TURN",(display_height-blockl)/2,(display_height/2+card_length)/2 + 0.25*blockh,blockl,blockh,yellow,llblue,"endturn",red)
            

            Property._property["delhi"].locmaker()
            Property._property["mumbai"].locmaker()
            Property._property["banglore"].locmaker()
            Property._property["newyork"].locmaker()
            Property._property["washingtondc"].locmaker()
            Property._property["sanfrancisco"].locmaker()
            Property._property["london"].locmaker()
            Property._property["manchester"].locmaker()
            Property._property["oxford"].locmaker()
            Property._property["melbourne"].locmaker()
            Property._property["canberra"].locmaker()
            Property._property["sydney"].locmaker()
            Property._property["tokyo"].locmaker()
            Property._property["osaka"].locmaker()
            Property._property["hiroshima"].locmaker()
            Property._property["beijing"].locmaker()
            Property._property["hongkong"].locmaker()
            Property._property["shanghai"].locmaker()
            Property._property["moscow"].locmaker()
            Property._property["saintpetersburg"].locmaker()
            Property._property["capetown"].locmaker()
            Property._property["durban"].locmaker()
            #if card_display == 1:
#                Property._property[place].card()
                
            
            player.player[1].draw()
            player.player[0].draw()

            pygame.display.update()       

def Button(msg,x,y,l,h,ac,ic,function,tc):
            global player_index,place,card_display
            global rollonce 
            pygame.draw.rect(functions.gameDisplay, ic, [x,y,l,h])
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if x < mouse[0] < x+l and y < mouse[1] < y+h:
                pygame.draw.rect(functions.gameDisplay, ac, [x,y,l,h])
                if click[0]==1:
                    if function == "roll" and rollonce == 0:
                        n = functions.rolldice()
                        player.player[player_index].movement(n)
                        rollonce = 1
 #                           for place in Property._property:
#                                if Property._property[place].locx == player.player[player_index].posx and Property._property[place].locy == player.player[player_index].posy:
#                                    card_display = 1
                           
                            
                    if function == "endturn":
                        if player_index == 0:
                            player_index+=1
                        elif player_index == 1:
                            player_index-=1
                        rollonce = 0
                        
            _font = pygame.font.Font('freesansbold.ttf',20)
            functions.text_in_box(msg, _font,tc,x,y,l,h)

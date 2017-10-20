import pygame,time
import functions,Property,player
 

pygame.init()

display_width = 1430
display_height = 800
card_length = 130
card_breadth = 60
blockl = 120
blockh = 50
boxl = 350
boxb = 215
gapv = (display_height - 2*boxl)/3
gaph = (display_width - display_height - 2*boxb)/3

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
card_display = 0
endturn = 0
key = 0
place = " "
timer = 5

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
            global key,timer
            functions.gameDisplay.fill(lblue)
            pygame.draw.rect(functions.gameDisplay, white, [0,0,display_height,display_height])
            functions.addimage('images/back.png',card_length,card_length)
            _font = pygame.font.Font('freesansbold.ttf',20)

            pygame.draw.rect(functions.gameDisplay,white, [display_height + gaph,gapv,boxb,boxl])
            pygame.draw.rect(functions.gameDisplay,white, [display_height + gaph,boxl + 2*gapv,boxb,boxl])
            

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

            if card_display == 1:
                
                Property._property[place].card()
                __font = pygame.font.Font('freesansbold.ttf',15)
                if Property._property[place].owner != None and key == 0 and player_index != Property._property[place].owner:
                    if Property._property[place].no_of_houses == 0:
                        rent_paid = Property._property[place].rent
                    elif Property._property[place].no_of_houses == 1:
                        rent_paid = Property._property[place].house1
                    elif Property._property[place].no_of_houses == 2:
                        rent_paid = Property._property[place].house2
                    elif Property._property[place].no_of_houses == 3:
                        rent_paid = Property._property[place].house3
                    elif Property._property[place].no_of_houses == 4:
                        rent_paid = Property._property[place].hotel
                    if timer == 5:
                        player.player[player_index].cash -= rent_paid
                        player.player[player_index].total_wealth -= rent_paid
                        player.player[Property._property[place].owner].cash += rent_paid
                        player.player[Property._property[place].owner].total_wealth += rent_paid
                        functions.text_in_box("You paid rent of %r to player %r?"%(rent_paid,Property._property[place].owner+1),__font,orange,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
                    timer -= 1
                    if timer == 0:
                        key = 1
                        timer = 5

                if Property._property[place].owner == None and key == 0:    
                    functions.text_in_box("Do you want to purchase %r ?"%Property._property[place].name,__font,orange,display_height/2,display_height/2 - blockh,display_height/2-card_length,display_height/2-card_length)
                    Button("YES",display_height*3/4 - card_length/2-blockl,display_height*3/4 - card_length/2 + blockh/2,blockl/2,blockh,yellow,llblue,"yes",red)
                    Button("NO",display_height*3/4 - card_length/2 + blockl/2,display_height*3/4 - card_length/2 + blockh/2,blockl/2,blockh,yellow,llblue,"no",red)

                        

                if key == 2:
                    functions.text_in_box("Successfully purchased %r"%(Property._property[place].name),__font,orange,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
                    timer -= 1
                    if timer == 0:
                        key = 1
                        timer = 5

                    
            player.player[1].draw()
            player.player[0].draw()

            functions.text_in_box("Player 1",_font,maroon,display_height + gaph,gapv,boxb,0.1*boxl)
            functions.text_in_box("Cash %r"%player.player[0].cash,_font,maroon,display_height + gaph,gapv + 0.1*boxl ,boxb,0.1*boxl)
            functions.text_in_box("Net Worth %r"%player.player[0].total_wealth,_font,maroon,display_height + gaph,gapv+0.9*boxl,boxb,0.1*boxl)
            functions.text_in_box("Player 2",_font,maroon,display_height + gaph,2*gapv + boxl,boxb,0.1*boxl)
            functions.text_in_box("Cash %r"%player.player[1].cash,_font,maroon,display_height + gaph,2*gapv+boxl + 0.1*boxl ,boxb,0.1*boxl)
            functions.text_in_box("Net Worth %r"%player.player[1].total_wealth,_font,maroon,display_height + gaph,2*gapv+boxl+0.9*boxl,boxb,0.1*boxl)

            pygame.display.update()       

def Button(msg,x,y,l,h,ac,ic,function,tc):
            global player_index,place,card_display
            global rollonce,endturn,key 
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
                        for tplace,tempo in Property._property.items():
                            if Property._property[tplace].locx == player.player[player_index].posx and Property._property[tplace].locy == player.player[player_index].posy:
                                card_display = 1
                                key = 0
                                place = tplace
                        endturn = 0   
                            
                    if function == "endturn" and endturn == 0:
                        if player_index == 0:
                            player_index+=1
                        elif player_index == 1:
                            player_index-=1
                        rollonce = 0
                        card_display = 0
                        endturn = 1
                    if function == "yes":
                        player.player[player_index].cash -= Property._property[place].cost
                        Property._property[place].owner = player_index
                        player.player[player_index].properties.append(place)
                        key = 2
                        
                            
            _font = pygame.font.Font('freesansbold.ttf',20)
            functions.text_in_box(msg, _font,tc,x,y,l,h)

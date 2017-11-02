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
timer = 8
n=0
incometax = 0
gotojail = 0
cround = [0,0]
round_complete = 0


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
            global key,timer,incometax,gotojail,round_complete,cround
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

            functions.text_in_box("Player %r's turn "%(player_index+1),_font,blue,card_length,card_length,(display_height-2*card_length)/2,blockh)
            functions.text_in_box("( %r , %r )"%(functions.a,functions.b),_font,blue,card_length,card_length,display_height-2*card_length,blockh)

            Button("ROLE DICE",(display_height-blockl)/2,(display_height/2+card_length)/2 - 1.25*blockh,blockl,blockh,yellow,llblue,"roll",red)
            Button("END TURN",(display_height-blockl)/2,(display_height/2+card_length)/2 + 0.25*blockh,blockl,blockh,yellow,llblue,"endturn",red)
            Button("BUILD",(display_height-3*blockl)/2 - 0.2*blockl,(display_height/2+card_length)/2 - 0.5*blockh,blockl,blockh,yellow,llblue,"build",red)
            Button("SELL",(display_height+1*blockl)/2 + 0.2*blockl,(display_height/2+card_length)/2 - 0.5*blockh,blockl,blockh,yellow,llblue,"sell",red)
            
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

            __font = pygame.font.Font('freesansbold.ttf',15)

            if round_complete == 1:
                functions.text_in_box("You Crossed Go , You gained $20000",__font,orange,card_length,(display_height/2+card_length)/2 + 1.25*blockh,display_height- 2*card_length,display_height/2 - ((display_height/2+card_length)/2 + 1.25*blockh))
                if timer == 8:
                    player.player[player_index].cash += 20000
                    player.player[player_index].total_wealth += 20000
                    cround[player_index]-=40
                timer-=1
                if timer == 0:
                        
                        round_complete = 0
                        timer = 8

            if card_display == 1:
                if Property._property[place].owner != None and key == 0 and player_index != Property._property[place].owner:
                    Property._property[place].card()
                    if timer == 8:
                        player.player[player_index].cash -= Property._property[place].houses[Property._property[place].no_of_houses]
                        player.player[player_index].total_wealth -= Property._property[place].houses[Property._property[place].no_of_houses]
                        player.player[Property._property[place].owner].cash += Property._property[place].houses[Property._property[place].no_of_houses]
                        player.player[Property._property[place].owner].total_wealth += Property._property[place].houses[Property._property[place].no_of_houses]
                    functions.text_in_box("You paid rent of %r to player %r?"%(Property._property[place].houses[Property._property[place].no_of_houses],Property._property[place].owner+1),__font,orange,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
                    timer -= 1
                    if timer == 0:
                        key = 1
                        timer = 8
                if Property._property[place].owner == None and key == 0:
                    Property._property[place].card()
                    functions.text_in_box("Do you want to purchase %r ?"%Property._property[place].name,__font,orange,display_height/2,display_height/2 - blockh,display_height/2-card_length,display_height/2-card_length)
                    Button("YES",display_height*3/4 - card_length/2-blockl,display_height*3/4 - card_length/2 + blockh/2,blockl/2,blockh,yellow,llblue,"yes",red)
                    Button("NO",display_height*3/4 - card_length/2 + blockl/2,display_height*3/4 - card_length/2 + blockh/2,blockl/2,blockh,yellow,llblue,"no",red)
                if key == 2:
                    Property._property[place].card()
                    functions.text_in_box("Successfully purchased %r"%(Property._property[place].name),__font,orange,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
                    timer -= 1
                    if timer == 0:
                        key = 1
                        timer = 8
            

            if incometax == 1:
                if key == 0:
                    player.player[player_index].total_wealth = 0.9*player.player[player_index].total_wealth
                    player.player[player_index].cash = 0.9*(player.player[player_index].total_wealth*10/9)
                    key = 2
                if key == 2:
                    timer-=1
                    functions.text_in_box("You paid income tax of %r"%(0.1*(player.player[player_index].total_wealth*10/9)),__font,orange,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
                    if timer == 0:
                        incometax = 0
                        timer = 8
                        key = 1
            elif incometax == 2:
                if key == 0:
                    player.player[player_index].total_wealth -= 30000 
                    player.player[player_index].cash -= 30000
                    key = 2
                if key == 2:
                    timer-=1
                    functions.text_in_box("You paid luxury tax of $30000",__font,orange,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
                    if timer == 0:
                        incometax = 0
                        timer = 8
                        key = 1                               
            player.player[1].draw()
            player.player[0].draw()

            for item,tempo in Property._property.items():
                Property._property[item].squares()
            if Property.tflag == 1:
                Property.temo.card()
                
            if gotojail == 1:
                timer -= 1
                functions.text_in_box("Oops! You landed on gotojail",__font,orange,display_height/2,display_height/2 ,display_height/2-card_length,display_height/2-card_length)
                if timer == 0:
                    
                    gotojail = 0
                    timer = 8

            functions.text_in_box("Player 1",_font,maroon,display_height + gaph,gapv,boxb,0.1*boxl)
            functions.text_in_box("Cash %r"%player.player[0].cash,_font,maroon,display_height + gaph,gapv + 0.1*boxl ,boxb,0.1*boxl)
            functions.text_in_box("Net Worth %r"%player.player[0].total_wealth,_font,maroon,display_height + gaph,gapv+0.9*boxl,boxb,0.1*boxl)
            functions.text_in_box("Player 2",_font,maroon,display_height + gaph,2*gapv + boxl,boxb,0.1*boxl)
            functions.text_in_box("Cash %r"%player.player[1].cash,_font,maroon,display_height + gaph,2*gapv+boxl + 0.1*boxl ,boxb,0.1*boxl)
            functions.text_in_box("Net Worth %r"%player.player[1].total_wealth,_font,maroon,display_height + gaph,2*gapv+boxl+0.9*boxl,boxb,0.1*boxl)

            pygame.display.update()       

def Button(msg,x,y,l,h,ac,ic,function,tc):
            global player_index,place,card_display
            global rollonce,endturn,key,n,incometax,gotojail,cround,round_complete 
            pygame.draw.rect(functions.gameDisplay, ic, [x,y,l,h])
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if x < mouse[0] < x+l and y < mouse[1] < y+h:
                pygame.draw.rect(functions.gameDisplay, ac, [x,y,l,h])
                if click[0]==1:
                    if function == "roll" and rollonce == 0:
                        n = functions.rolldice()
                        cround[player_index] += n
                        player.player[player_index].movement(n)
                        rollonce = 1

                        if cround[player_index] >= 40:
                            round_complete = 1
                        
                        for tplace,tempo in Property._property.items():
                            if Property._property[tplace].locx == player.player[player_index].posx and Property._property[tplace].locy == player.player[player_index].posy:
                                card_display = 1
                                key = 0
                                place = tplace
                        if player.player[player_index].posx == (card_length+5*card_breadth + 0.5*card_breadth) and player.player[player_index].posy == (display_height-card_length/2):
                            incometax = 1
                            key = 0
                        if player.player[player_index].posx == display_height-card_length/2 and player.player[player_index].posy == 7*card_breadth+card_length+0.5*card_breadth :
                            incometax = 2
                            key = 0
                        if player.player[player_index].posx == display_height-card_length/2 and player.player[player_index].posy == card_length/2:
                            
                            player.player[player_index].posx = card_length/2
                            player.player[player_index].posy = display_height-card_length/2
                            cround[player_index] -= 20
                            gotojail = 1
                        endturn = 0   
                            
                    if function == "endturn" and endturn == 0:
                        if player_index == 0:
                            player_index+=1
                        elif player_index == 1:
                            player_index-=1
                        rollonce = 0
                        card_display = 0
                        endturn = 1
                        Property.tflag = 0
                    if function == "yes":
                        player.player[player_index].cash -= Property._property[place].cost
                        Property._property[place].owner = player_index
                        player.player[player_index].properties.append(place)
                        
                        key = 2
                    if function == "no":
                        pass
                    if function == "build":
                        valid = 1
                        if Property.temo.owner != player_index or Property.temo.no_of_houses == 4:
                            valid = 0
                        for xplace,tempo in Property._property.items():
                            if Property._property[xplace].country == Property.temo.country:
                                if (Property._property[xplace].no_of_houses < Property.temo.no_of_houses) or Property._property[xplace].owner != player_index:
                                    valid = 0
                                    break
                        if valid == 1:
                            Property.temo.no_of_houses += 1
                            player.player[player_index].cash -= Property.temo.cost 
                    if function == "sell":
                        valid = 1
                        if Property.temo.owner != player_index or Property.temo.no_of_houses == 0:
                            valida = 0
                        for xplace,tempo in Property._property.items():
                            if Property._property[xplace].country == Property.temo.country:
                                if (Property._property[xplace].no_of_houses > Property.temo.no_of_houses) or Property._property[xplace].owner != player_index:
                                    valida = 0
                                    break
                        if valida == 1:
                            Property.temo.no_of_houses -= 1
                            player.player[player_index].cash += 0.5*Property.temo.cost 
                    
                        
                        
                            
            _font = pygame.font.Font('freesansbold.ttf',20)
            functions.text_in_box(msg, _font,tc,x,y,l,h)

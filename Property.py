import pygame,functions

pygame.init()

display_width = 1430
display_height = 800
card_length = 130
card_breadth = 60
boxl = 350
boxb = 215
gapv = (display_height - 2*boxl)/3
gaph = (display_width - display_height - 2*boxb)/3
cardl = 0.1*boxb
cardh = 0.1*boxl
cgaph = ((boxb/2)-(3*cardl))/4
cgapv = 0.03*boxl
c2gaph = ((boxb/2)-(2*cardl))/3
c3gaph = ((boxb/2)-(4*cardl))/5
tflag = 0
temo = None
timer = 8



white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
red = (255,50,0)
blue = (0,0,255)
green = (50,255,50)
back = (100,10,100)
new = (10,100,100)
new1 = (200,150,50)
new2 = (67,234,169)
orange = (228,142,88)
grey = (160,160,160)
c1 = (69,43,122)
c2 = (255,102,255)
c3 = (102,0,0)
c4 = (102,255,255)

clock = pygame.time.Clock()



class Property():                                                                   #creating a class property which will contain all data of properties and their respective functions

    def __init__(self,name,color,country,locx,locy,cost,x1,y1,x2,y2):              #initialising every object(property) with its basic information
        self.name = name
        self.color = color
        self.country = country
        self.locx = locx
        self.locy = locy
        self.cost = cost
        self.houses = [0.1*self.cost,0.4*self.cost,0.5*self.cost,0.6*self.cost,self.cost]    #A list keeping track of rents to be paid v/s no. of houses
        self.mortgage = 0.4*self.cost
        self.mort = 0
        self.no_of_houses = 0
        self.owner = None
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def locmaker(self):                                         #it creates the respective property on the board 
        lfont = pygame.font.Font('freesansbold.ttf',10)
        if self.locx == card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[0,self.locy-card_breadth/2,card_length,card_breadth],1)
            functions.text_in_box(self.name,lfont,black,0,self.locy-card_breadth/2,0.7*card_length,card_breadth)
            functions.gameDisplay.fill(self.color, rect = [0.7*card_length,self.locy-card_breadth/2,0.3*card_length,card_breadth]) #draws houses on the site depending on the no. of houses
            if  self.no_of_houses >= 1:
                functions.gameDisplay.fill(c1, rect = [0.7*card_length,self.locy-card_breadth/4,0.3*card_length/4,card_breadth/2])
            if self.no_of_houses >= 2:
                functions.gameDisplay.fill(c2, rect = [0.7*card_length + 0.3*card_length/4,self.locy-card_breadth/4,0.3*card_length/4,card_breadth/2])
            if self.no_of_houses >= 3:
                functions.gameDisplay.fill(c3, rect = [0.7*card_length + 0.6*card_length/4,self.locy-card_breadth/4,0.3*card_length/4,card_breadth/2])
            if self.no_of_houses == 4:
                functions.gameDisplay.fill(c4, rect = [0.7*card_length + 0.9*card_length/4,self.locy-card_breadth/4,0.3*card_length/4,card_breadth/2])    
        elif self.locx == display_height -  card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[display_height -  card_length,self.locy-card_breadth/2,card_length,card_breadth],1)
            functions.text_in_box(self.name,lfont,black,display_height -  0.7*card_length,self.locy-card_breadth/2,0.7*card_length,card_breadth)
            functions.gameDisplay.fill(self.color, rect = [display_height -  card_length,self.locy-card_breadth/2,0.3*card_length,card_breadth])
            if self.no_of_houses >= 1:
                functions.gameDisplay.fill(c1, rect = [display_height -  card_length + 0.9*card_length/4 ,self.locy-card_breadth/4,0.3*card_length/4,card_breadth/2])
            if self.no_of_houses >= 2:
                functions.gameDisplay.fill(c2, rect = [display_height -  card_length + 0.6*card_length/4 ,self.locy-card_breadth/4,0.3*card_length/4,card_breadth/2])
            if self.no_of_houses >= 3:
                functions.gameDisplay.fill(c3, rect = [display_height -  card_length + 0.3*card_length/4 ,self.locy-card_breadth/4,0.3*card_length/4,card_breadth/2])
            if self.no_of_houses == 4:
                functions.gameDisplay.fill(c4, rect = [display_height -  card_length  ,self.locy-card_breadth/4,0.3*card_length/4,card_breadth/2])
        elif self.locy == card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[self.locx-card_breadth/2,0,card_breadth,card_length],1)
            a = self.name.split(' ')
            temp = 0
            for x in a:
                functions.text_in_box(x,lfont,black,self.locx-card_breadth/2,temp,card_breadth,0.35*card_length)
                temp += 0.35*card_length
            functions.gameDisplay.fill(self.color, rect = [self.locx-card_breadth/2,0.7*card_length,card_breadth,0.3*card_length])
            if self.no_of_houses >= 1:
                functions.gameDisplay.fill(c1, rect = [self.locx-card_breadth/4,0.7*card_length,card_breadth/2,0.3*card_length/4])
            if self.no_of_houses >= 2:
                functions.gameDisplay.fill(c2, rect = [self.locx-card_breadth/4,0.7*card_length + 0.3*card_length/4,card_breadth/2,0.3*card_length/4])
            if self.no_of_houses >= 3:
                functions.gameDisplay.fill(c3, rect = [self.locx-card_breadth/4,0.7*card_length + 0.6*card_length/4,card_breadth/2,0.3*card_length/4])
            if self.no_of_houses == 4:
                functions.gameDisplay.fill(c4, rect = [self.locx-card_breadth/4,0.7*card_length + 0.9*card_length/4,card_breadth/2,0.3*card_length/4])
        elif self.locy ==  display_height -  card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[self.locx-card_breadth/2,display_height -  card_length,card_breadth,card_length],1)
            functions.text_in_box(self.name,lfont,black,self.locx-card_breadth/2,display_height -  0.7*card_length,card_breadth,0.7*card_length)
            functions.gameDisplay.fill(self.color, rect = [self.locx-card_breadth/2,display_height -  card_length,card_breadth,0.3*card_length])
            if self.no_of_houses >= 1:
                functions.gameDisplay.fill(c1, rect = [self.locx-card_breadth/4,display_height -  card_length + 0.9*card_length/4,card_breadth/2,0.3*card_length/4])
            if self.no_of_houses >= 2:
                functions.gameDisplay.fill(c2, rect = [self.locx-card_breadth/4,display_height -  card_length + 0.6*card_length/4,card_breadth/2,0.3*card_length/4])
            if self.no_of_houses >= 3:
                functions.gameDisplay.fill(c3, rect = [self.locx-card_breadth/4,display_height -  card_length + 0.3*card_length/4,card_breadth/2,0.3*card_length/4])
            if self.no_of_houses == 4:
                functions.gameDisplay.fill(c4, rect = [self.locx-card_breadth/4,display_height -  card_length ,card_breadth/2,0.3*card_length/4])
        pygame.display.update() 

    def card(self):                     #this draws the card of the property with the respective details on it
        functions.gameDisplay.fill(white, rect = [170,400,200,250])
        lfont = pygame.font.Font('freesansbold.ttf',25)
        functions.text_in_box(self.name,lfont,self.color,170,410,200,30)
        functions.message_to_screen("Cost: $ %d"%self.cost,black,180,460,20)
        functions.message_to_screen("Rent: $ %d"%self.houses[0],black,180,480,20)
        functions.message_to_screen("1st floor: $ %d"%self.houses[1],black,180,500,20)
        functions.message_to_screen("2nd floor: $ %d"%self.houses[2],black,180,520,20)
        functions.message_to_screen("3rd floor: $ %d"%self.houses[3],black,180,540,20)
        functions.message_to_screen("Hotel: $ %d"%self.houses[4],black,180,560,20)
        functions.message_to_screen("Mortgage value: $ %d"%self.mortgage,black,190,600,20)
        pygame.display.update()

    def squares(self):                      #this draws the links of the property on the respective player boxes depending on the owner 
        global tflag ,timer,temo
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if self.owner == 0:
            pygame.draw.rect(functions.gameDisplay, self.color, [self.x1,self.y1,cardl,cardh])
            if self.x1 < mouse[0] < self.x1+cardl and self.y1 < mouse[1] < self.y1 + cardh:
                if click[0]==1:
                    tflag = 1
                    temo = self
            
        if self.owner == 1:
            pygame.draw.rect(functions.gameDisplay, self.color, [self.x2,self.y2,cardl,cardh])
            if self.x2 < mouse[0] < self.x2+cardl and self.y2 < mouse[1] < self.y2 + cardh:
                if click[0]==1:
                    tflag = 1
                    temo = self

class special_cards():                          #for special cards that is utilities and railway

    def __init__(self,name,cost,locx,locy,x1,y1,x2,y2):
        self.name = name
        self.cost = cost
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.locx = locx
        self.locy = locy
        self.mortgage = 0.4*self.cost
        self.owner = None
    def card(self):                                     #this sketches the card of the utility when called upon
        functions.gameDisplay.fill(white, rect = [170,400,200,250])
        lfont = pygame.font.Font('freesansbold.ttf',25)
        functions.text_in_box(self.name,lfont,black,170,410,200,30)
        functions.message_to_screen("Cost: $ %d"%self.cost,black,180,460,20)
        functions.message_to_screen("If one utility is owned",black,180,480,20)
        functions.message_to_screen("Rent = 1000*(sum on dice)",black,180,500,20)
        functions.message_to_screen("If both utilities are owned",black,180,520,20)
        functions.message_to_screen("Rent = 3000*(sum on dice)",black,180,540,20)
        
        
        pygame.display.update()
        
    def locmaker(self):                                             #this draws the railways at there respective positions on the board
        lfont = pygame.font.Font('freesansbold.ttf',10)
        if self.locx == card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[0,self.locy-card_breadth/2,card_length,card_breadth],1)
            functions.text_in_box(self.name,lfont,black,0,self.locy-card_breadth/2,0.7*card_length,card_breadth)
            functions.gameDisplay.fill(black, rect = [0.7*card_length,self.locy-card_breadth/2,0.3*card_length,card_breadth])
            
        elif self.locx == display_height -  card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[display_height -  card_length,self.locy-card_breadth/2,card_length,card_breadth],1)
            functions.text_in_box(self.name,lfont,black,display_height -  0.7*card_length,self.locy-card_breadth/2,0.7*card_length,card_breadth)
            functions.gameDisplay.fill(black, rect = [display_height -  card_length,self.locy-card_breadth/2,0.3*card_length,card_breadth])
            
        elif self.locy == card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[self.locx-card_breadth/2,0,card_breadth,card_length],1)
            a = self.name.split(' ')
            temp = 0
            for x in a:
                functions.text_in_box(x,lfont,black,self.locx-card_breadth/2,temp,card_breadth,0.35*card_length)
                temp += 0.35*card_length
            functions.gameDisplay.fill(black, rect = [self.locx-card_breadth/2,0.7*card_length,card_breadth,0.3*card_length])
            
        elif self.locy ==  display_height -  card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[self.locx-card_breadth/2,display_height -  card_length,card_breadth,card_length],1)
            functions.text_in_box(self.name,lfont,black,self.locx-card_breadth/2,display_height -  0.7*card_length,card_breadth,0.7*card_length)
            functions.gameDisplay.fill(black, rect = [self.locx-card_breadth/2,display_height -  card_length,card_breadth,0.3*card_length])
            
        pygame.display.update()
    def rcard(self):                            #this draws the card of the railway when called upon
        functions.gameDisplay.fill(white, rect = [170,400,200,250])
        lfont = pygame.font.Font('freesansbold.ttf',25)
        functions.text_in_box(self.name,lfont,black,170,410,200,30)
        functions.message_to_screen("Cost: $ %d"%self.cost,black,180,460,20)
        functions.message_to_screen("Owned          Rent",black,180,480,20)
        functions.message_to_screen("1 Railway      $2500",black,180,500,20)
        functions.message_to_screen("2 Railway      $5000",black,180,520,20)
        functions.message_to_screen("3 Railway      $10000",black,180,540,20)
        functions.message_to_screen("4 Railway      $20000",black,180,560,20)
        
        pygame.display.update()
    def squares(self):                      #this draws the links of the property on the respective owner boxes
        global tflag ,timer,temo
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if self.owner == 0:
            pygame.draw.rect(functions.gameDisplay, black, [self.x1,self.y1,cardl,cardh])
            if self.x1 < mouse[0] < self.x1+cardl and self.y1 < mouse[1] < self.y1 + cardh:
                if click[0]==1:
                    tflag = 1
                    temo = self
            
        if self.owner == 1:
            pygame.draw.rect(functions.gameDisplay, black, [self.x2,self.y2,cardl,cardh])
            if self.x2 < mouse[0] < self.x2+cardl and self.y2 < mouse[1] < self.y2 + cardh:
                if click[0]==1:
                    tflag = 1
                    temo = self
#initialising special card's objects
sproperty = {  "electric":special_cards("Electric Company",80000,card_length/2,7*card_breadth+card_breadth/2+card_length,display_height + gaph + c2gaph,gapv + 0.2*boxl + 5*cgapv + 4*cardh,display_height + gaph + c2gaph,2*gapv + boxl + 0.2*boxl + 5*cgapv + 4*cardh)
             , "water":special_cards("Water Works",70000,7*card_breadth+card_breadth/2+card_length,card_length/2,display_height + gaph + 2*c2gaph + cardl,gapv + 0.2*boxl + 5*cgapv + 4*cardh,display_height + gaph + 2*c2gaph + cardl,2*gapv + boxl + 0.2*boxl + 5*cgapv + 4*cardh)
             , "rail1":special_cards("Railway",40000,card_length + 9*card_breadth/2,display_height - card_length/2,display_height + gaph + boxb/2+  c3gaph,gapv + 0.2*boxl + 5*cgapv + 4*cardh,display_height + gaph + boxb/2+ c3gaph,2*gapv + boxl + 0.2*boxl + 5*cgapv + 4*cardh)
             , "rail2":special_cards("Railway",40000,card_length/2,card_length + 9*card_breadth/2,display_height + gaph + boxb/2+  2*c3gaph + cardl,gapv + 0.2*boxl + 5*cgapv + 4*cardh,display_height + gaph + boxb/2+ 2*c3gaph + cardl,2*gapv + boxl + 0.2*boxl + 5*cgapv + 4*cardh)  
             , "rail3":special_cards("Railway",40000,card_length + 9*card_breadth/2,card_length/2,display_height + gaph + boxb/2+  3*c3gaph + 2*cardl,gapv + 0.2*boxl + 5*cgapv + 4*cardh,display_height + gaph + boxb/2+ 3*c3gaph + 2*cardl,2*gapv + boxl + 0.2*boxl + 5*cgapv + 4*cardh)
             , "rail4":special_cards("Railway",40000,display_height - card_length/2,card_length + 9*card_breadth/2,display_height + gaph + boxb/2+  4*c3gaph + 3*cardl,gapv + 0.2*boxl + 5*cgapv + 4*cardh,display_height + gaph + boxb/2+ 4*c3gaph + 3*cardl,2*gapv + boxl + 0.2*boxl + 5*cgapv + 4*cardh)
            }
#initialising the property objects
_property = { "delhi":Property("Delhi",red,"India",card_length + card_breadth/2,card_length/2,80000,display_height + gaph + cgaph,gapv + 0.2*boxl + cgapv,display_height + gaph + cgaph,2*gapv + boxl + 0.2*boxl + cgapv )
            , "mumbai":Property("Mumbai",red,"India",card_length + 5*(card_breadth/2),card_length/2,60000,display_height + gaph + 2*cgaph + cardl,gapv + 0.2*boxl + cgapv,display_height + gaph + 2*cgaph + cardl,2*gapv + boxl + 0.2*boxl + cgapv )
            , "banglore":Property("Banglore",red,"India",card_length + 7*(card_breadth/2),card_length/2,40000,display_height + gaph + 3*cgaph + 2*cardl,gapv + 0.2*boxl + cgapv,display_height + gaph + 3*cgaph + 2*cardl,2*gapv + boxl + 0.2*boxl + cgapv )  
            , "newyork":Property("New York",yellow,"America",card_length + 11*(card_breadth/2),card_length/2,70000,display_height + gaph + boxb/2 + cgaph,gapv + 0.2*boxl + cgapv,display_height + gaph + boxb/2 + cgaph,2*gapv + boxl + 0.2*boxl + cgapv)
            , "washingtondc":Property("Washington D.C.",yellow,"America",card_length + 13*(card_breadth/2),card_length/2,40000,display_height + gaph + boxb/2 + 2*cgaph + cardl,gapv + 0.2*boxl + cgapv,display_height + gaph + boxb/2 + 2*cgaph + cardl,2*gapv + boxl + 0.2*boxl + cgapv)
            , "sanfrancisco":Property("San Francisco",yellow,"America",card_length + 17*(card_breadth/2),card_length/2,60000,display_height + gaph + boxb/2 + 3*cgaph + 2*cardl,gapv + 0.2*boxl + cgapv,display_height + gaph + boxb/2 + 3*cgaph + 2*cardl,2*gapv + boxl + 0.2*boxl + cgapv)
            , "london":Property("London",blue,"England",display_height -  card_length/2,card_length + 1*(card_breadth/2),80000 ,display_height + gaph + cgaph,gapv + 0.2*boxl + 2*cgapv + cardh,display_height + gaph +2*cgapv + cardh,2*gapv + boxl + 0.2*boxl + 2*cgapv + cardh )
            , "manchester":Property("Manchester",blue,"England",display_height -  card_length/2,card_length + 3*(card_breadth/2),30000,display_height + gaph + 2*cgaph + cardl,gapv + 0.2*boxl + 2*cgapv + cardh,display_height + gaph + 2*cgaph + cardl,2*gapv + boxl + 0.2*boxl + 2*cgapv + cardh )
            , "oxford":Property("Oxford",blue,"England",display_height -  card_length/2,card_length + 7*(card_breadth/2),40000,display_height + gaph + 3*cgaph + 2*cardl,gapv + 0.2*boxl + 2*cgapv + cardh,display_height + gaph + 3*cgaph + 2*cardl,2*gapv + boxl + 0.2*boxl + 2*cgapv + cardh)
            , "melbourne":Property("Melbourne",green,"Australia",card_length/2,card_length + 1*(card_breadth/2),40000,display_height + gaph + boxb/2 + cgaph,gapv + 0.2*boxl + 2*cgapv + cardh,display_height + gaph + boxb/2 + cgaph,2*gapv + boxl + 0.2*boxl + 2*cgapv + cardh)
            , "canberra":Property("Canberra",green,"Australia",card_length/2,card_length + 3*(card_breadth/2),50000,display_height + gaph + boxb/2 + 2*cgaph + cardl,gapv + 0.2*boxl + 2*cgapv + cardh,display_height + gaph + boxb/2 + 2*cgaph + cardl,2*gapv + boxl + 0.2*boxl + 2*cgapv + cardh)           
            , "sydney":Property("Sydney",green,"Australia",card_length/2,card_length + 7*(card_breadth/2),70000,display_height + gaph + boxb/2 + 3*cgaph + 2*cardl,gapv + 0.2*boxl + 2*cgapv + cardh,display_height + gaph + boxb/2 + 3*cgaph + 2*cardl,2*gapv + boxl + 0.2*boxl + 2*cgapv + cardh)
            , "tokyo":Property("Tokyo",back,"Japan",card_length/2,card_length + 11*(card_breadth/2),70000,display_height + gaph + cgaph,gapv + 0.2*boxl + 3*cgapv + 2*cardh,display_height + gaph +2*cgapv + cardh,2*gapv + boxl + 0.2*boxl + 3*cgapv + 2*cardh )
            , "osaka":Property("Osaka",back,"Japan",card_length/2,card_length + 13*(card_breadth/2),50000,display_height + gaph + 2*cgaph + cardl,gapv + 0.2*boxl +3*cgapv + 2*cardh,display_height + gaph + 2*cgaph + cardl,2*gapv + boxl + 0.2*boxl + 3*cgapv + 2*cardh )
            , "hiroshima":Property("Hiroshima",back,"Japan",card_length/2,card_length + 17*(card_breadth/2),30000,display_height + gaph + 3*cgaph + 2*cardl,gapv + 0.2*boxl + 3*cgapv + 2*cardh,display_height + gaph + 3*cgaph + 2*cardl,2*gapv + boxl + 0.2*boxl + 3*cgapv + 2*cardh)
            , "beijing":Property("Beijing",new,"China",card_length + 1*(card_breadth/2),display_height - card_length/2,50000,display_height + gaph + boxb/2 + cgaph,gapv + 0.2*boxl + 3*cgapv + 2*cardh,display_height + gaph + boxb/2 + cgaph,2*gapv + boxl + 0.2*boxl + 3*cgapv + 2*cardh)
            , "hongkong":Property("Hong Kong",new,"China",card_length + 3*(card_breadth/2),display_height - card_length/2,40000,display_height + gaph + boxb/2 + 2*cgaph + cardl,gapv + 0.2*boxl + 3*cgapv + 2*cardh,display_height + gaph + boxb/2 + 2*cgaph + cardl,2*gapv + boxl + 0.2*boxl + 3*cgapv + 2*cardh)
            , "shanghai":Property("Shanghai",new,"China",card_length + 7*(card_breadth/2),display_height - card_length/2,60000,display_height + gaph + boxb/2 + 3*cgaph + 2*cardl,gapv + 0.2*boxl + 3*cgapv + 2*cardh,display_height + gaph + boxb/2 + 3*cgaph + 2*cardl,2*gapv + boxl + 0.2*boxl + 3*cgapv + 2*cardh)
            , "moscow":Property("Moscow",grey,"Russia",display_height - card_length/2,card_length + 13*(card_breadth/2),60000,display_height + gaph + c2gaph,gapv + 0.2*boxl + 4*cgapv + 3*cardh,display_height + gaph + c2gaph,2*gapv + boxl + 0.2*boxl + 4*cgapv + 3*cardh)
            , "saintpetersburg":Property("Saint Petersberg",grey,"Russia",display_height - card_length/2,card_length + 17*(card_breadth/2),40000,display_height + gaph + 2*c2gaph + cardl,gapv + 0.2*boxl + 4*cgapv + 3*cardh,display_height + gaph + 2*c2gaph + cardl,2*gapv + boxl + 0.2*boxl + 4*cgapv + 3*cardh)
            , "capetown":Property("Cape Town",orange,"SouthAfrica",card_length + 13*(card_breadth/2),display_height - card_length/2,80000,display_height + gaph + boxb/2+  c2gaph,gapv + 0.2*boxl + 4*cgapv + 3*cardh,display_height + gaph + boxb/2+ c2gaph,2*gapv + boxl + 0.2*boxl + 4*cgapv + 3*cardh)
            , "durban":Property("Durban",orange,"SouthAfrica",card_length + 17*(card_breadth/2),display_height - card_length/2,60000,display_height + gaph + boxb/2+ 2*c2gaph + cardl,gapv + 0.2*boxl + 4*cgapv + 3*cardh,display_height + gaph + boxb/2+ 2*c2gaph + cardl,2*gapv + boxl + 0.2*boxl + 4*cgapv + 3*cardh)              
            }


        

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
green = (50,255,50)
back = (100,10,100)
new = (10,100,100)
new1 = (200,150,50)
new2 = (67,234,169)
clock = pygame.time.Clock()



class Property():

    def __init__(self,name,color,country,locx,locy,cost):
        self.name = name
        self.color = color
        self.country = country
        self.locx = locx
        self.locy = locy
        self.cost = cost
        self.rent = 0.01*self.cost
        self.house1 = 0.1*self.cost
        self.house2 = 0.2*self.cost
        self.house3 = 0.3*self.cost
        self.hotel = 0.5*self.cost
        self.mortgage = 0.4*self.cost
        self.no_of_houses = 0
        self.owner = None
    
    def locmaker(self):
        lfont = pygame.font.Font('freesansbold.ttf',10)
        if self.locx == card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[0,self.locy-card_breadth/2,card_length,card_breadth],1)
            functions.text_in_box(self.name,lfont,black,0,self.locy-card_breadth/2,0.7*card_length,card_breadth)
            functions.gameDisplay.fill(self.color, rect = [0.7*card_length,self.locy-card_breadth/2,0.3*card_length,card_breadth])
        elif self.locx == display_height -  card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[display_height -  card_length,self.locy-card_breadth/2,card_length,card_breadth],1)
            functions.text_in_box(self.name,lfont,black,display_height -  0.7*card_length,self.locy-card_breadth/2,0.7*card_length,card_breadth)
            functions.gameDisplay.fill(self.color, rect = [display_height -  card_length,self.locy-card_breadth/2,0.3*card_length,card_breadth])
        elif self.locy == card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[self.locx-card_breadth/2,0,card_breadth,card_length],1)
            a = self.name.split(' ')
            temp = 0
            for x in a:
                functions.text_in_box(x,lfont,black,self.locx-card_breadth/2,temp,card_breadth,0.35*card_length)
                temp += 0.35*card_length
            functions.gameDisplay.fill(self.color, rect = [self.locx-card_breadth/2,0.7*card_length,card_breadth,0.3*card_length])
        elif self.locy ==  display_height -  card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[self.locx-card_breadth/2,display_height -  card_length,card_breadth,card_length],1)
            functions.text_in_box(self.name,lfont,black,self.locx-card_breadth/2,display_height -  0.7*card_length,card_breadth,0.7*card_length)
            functions.gameDisplay.fill(self.color, rect = [self.locx-card_breadth/2,display_height -  card_length,card_breadth,0.3*card_length])
        pygame.display.update() 

    def card(self):
        functions.gameDisplay.fill(white, rect = [170,400,200,250])
        lfont = pygame.font.Font('freesansbold.ttf',25)
        functions.text_in_box(self.name,lfont,self.color,170,410,200,30)
        functions.message_to_screen("Cost: $ %d"%self.cost,black,180,460,20)
        functions.message_to_screen("Rent: $ %d"%self.rent,black,180,480,20)
        functions.message_to_screen("1st floor: $ %d"%self.house1,black,180,500,20)
        functions.message_to_screen("2nd floor: $ %d"%self.house2,black,180,520,20)
        functions.message_to_screen("3rd floor: $ %d"%self.house3,black,180,540,20)
        functions.message_to_screen("Hotel: $ %d"%self.hotel,black,180,560,20)
        functions.message_to_screen("Mortgage value: $ %d"%self.mortgage,black,190,600,20)
        pygame.display.update()


_property = { "delhi":Property("Delhi",red,"India",card_length + card_breadth/2,card_length/2,80000)
            , "mumbai":Property("Mumbai",red,"India",card_length + 5*(card_breadth/2),card_length/2,60000)
            , "banglore":Property("Banglore",red,"India",card_length + 7*(card_breadth/2),card_length/2,40000)  
            , "newyork":Property("New York",yellow,"America",card_length + 11*(card_breadth/2),card_length/2,70000)
            , "washingtondc":Property("Washington D.C.",yellow,"America",card_length + 13*(card_breadth/2),card_length/2,40000)
            , "sanfrancisco":Property("San Francisco",yellow,"America",card_length + 17*(card_breadth/2),card_length/2,60000)
            , "london":Property("London",blue,"England",display_height -  card_length/2,card_length + 1*(card_breadth/2),80000)
            , "manchester":Property("Manchester",blue,"England",display_height -  card_length/2,card_length + 3*(card_breadth/2),30000)
            , "oxford":Property("Oxford",blue,"England",display_height -  card_length/2,card_length + 7*(card_breadth/2),40000)
            , "melbourne":Property("Melbourne",green,"Australia",card_length/2,card_length + 1*(card_breadth/2),40000)
            , "canberra":Property("Canberra",green,"Australia",card_length/2,card_length + 3*(card_breadth/2),50000)           
            , "sydney":Property("Sydney",green,"Australia",card_length/2,card_length + 7*(card_breadth/2),70000)
            , "tokyo":Property("Tokyo",back,"Japan",card_length/2,card_length + 11*(card_breadth/2),70000)
            , "osaka":Property("Osaka",back,"Japan",card_length/2,card_length + 13*(card_breadth/2),50000)
            , "hiroshima":Property("Hiroshima",back,"Japan",card_length/2,card_length + 17*(card_breadth/2),30000)
            , "beijing":Property("Beijing",new,"China",card_length + 1*(card_breadth/2),display_height - card_length/2,50000)
            , "hongkong":Property("Hong Kong",new,"China",card_length + 3*(card_breadth/2),display_height - card_length/2,40000)
            , "shanghai":Property("Shanghai",new,"China",card_length + 7*(card_breadth/2),display_height - card_length/2,60000)
            , "moscow":Property("Moscow",new1,"Russia",display_height - card_length/2,card_length + 13*(card_breadth/2),60000)
            , "saintpetersburg":Property("Saint Petersberg",new1,"Russia",display_height - card_length/2,card_length + 17*(card_breadth/2),40000)
            , "capetown":Property("Cape Town",new2,"SouthAfrica",card_length + 13*(card_breadth/2),display_height - card_length/2,80000)
            , "durban":Property("Durban",new2,"SouthAfrica",card_length + 17*(card_breadth/2),display_height - card_length/2,60000)              
            }

        

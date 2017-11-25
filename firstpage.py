
class leaderboard():
    winamount = 600000
    def __init__(self):
        
        self.name = "Aniket"
        
        
    
p = [leaderboard(),leaderboard()]

def screen1(a,b,c):    #for running screen 1
    import pygame
    global p
    import functions
    leaderboard.winamount = (int)(c.get())
    p[1].name = b.get()
    p[0].name = a.get()





    
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



    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        x = 615
        y1=200
        y2=300
        y3=400
        l=200
        h=50

        functions.gameDisplay.fill(back)
        img = pygame.image.load('images/monopolyimage.png')  #adding image
        functions.gameDisplay.blit(img, (200,0))
        #adding start button
        functions.button("START",x,y1,l,h,yellow,blue,"next",red)        
        #adding quit button
        functions.button("QUIT",x,y3,l,h,yellow,blue,"quit1",red)

        
        pygame.display.update()
   
        



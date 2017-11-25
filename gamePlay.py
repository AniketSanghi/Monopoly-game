from tkinter import *
import os
import firstpage

p1name = None
p2name = None
winamount = None

def screenn1():  #for running screen 1
    global p1name,p2name,winamount
    firstpage.screen1(p1name,p2name,winamount)
def data():  #for taking data
    global p1name,p2name,winamount
    root = Tk()   #window created
    root.title('Monopoly Love')#adding title
    intro = Label(root, text = 'Welcome to the amazing world of monopoly\n')
    intro.grid(row = 0, column = 0, sticky = E)
    #creating text boxes and respective askers
    p1name = Label(root, text = 'Player 1 name: ')
    p2name = Label(root, text = 'Player 2 name: ')
    winamount = Label(root, text = 'Winning Amount: ')
    p1name.grid(row = 1,column = 0, sticky = W)
    p2name.grid(row = 2,column = 0, sticky = W)
    winamount.grid(row = 3, column = 0, sticky = W)

    p1name = Entry(root)
    p2name = Entry(root)
    winamount = Entry(root)

    p1name.grid(row=1,column = 1)
    p2name.grid(row = 2,column =1)
    winamount.grid(row = 3,column = 1)

    nextt = Button(root, text = 'Done',command = screenn1)
    nextt.grid(columnspan = 2, sticky = W)
    root.mainloop()

    


#firstpage.screen1()     #calling the function to call the first screen


    
data()    


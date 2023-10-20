from tkinter import *
import os
import firstpage

p1name = None
p2name = None
winamount = None


class configWindow():

    def __init__(self):
        # create the window
        self.root = Tk()   #window created
        self.root.title('Monopoly Love')#adding title
        self.intro = Label(self.root, text = 'Welcome to the amazing world of monopoly\n')
        self.intro.grid(row = 0, column = 0, sticky = E)
        #creating text boxes and respective askers
        self.p1name = Label(self.root, text = 'Player 1 name: ')
        self.p2name = Label(self.root, text = 'Player 2 name: ')
        self.winamount = Label(self.root, text = 'Winning Amount: ')
        self.p1name.grid(row = 1,column = 0, sticky = W)
        self.p2name.grid(row = 2,column = 0, sticky = W)
        self.winamount.grid(row = 3, column = 0, sticky = W)

        # make entry boxes for the text boxes with default values
        self.p1name = Entry(self.root)
        self.p1name.insert(0, 'Player 1')
        self.p2name = Entry(self.root)
        self.p2name.insert(0, 'Player 2')
        self.winamount = Entry(self.root)
        self.winamount.insert(0, '600000')

        self.winAmount = self.winamount.get()
        self.p1Name = self.p1name.get()
        self.p2Name = self.p2name.get()

        self.p1name.grid(row=1, column=1)
        self.p2name.grid(row=2, column=1)
        self.winamount.grid(row=3, column=1)

        # make a button to move to the next screen, using the screenn1 function and passing the root window as an argument
        self.nextt = Button(self.root, text='Done', command=self.screenn1 )
        # nextt = Button(root, text='Done', command = screenn1)
        self.nextt.grid(columnspan=2, sticky=W)



    def screenn1(self):  # for running screen 1
        # to get updated values if changed
        self.winAmount = self.winamount.get()
        self.p1Name = self.p1name.get()
        self.p2Name = self.p2name.get()
        # kill the window
        self.root.destroy()
        firstpage.screen1(self.p1Name, self.p2Name, self.winAmount)




# start the program by creating the config window
_configWindow = configWindow()
_configWindow.root.mainloop()
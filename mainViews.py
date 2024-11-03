import tkinter as tk
from tkinter import *

# Label: Just text, there is an option called Message but it just does the same thing.
# Entry: Just an empty box to be filled, can be referenced in commands.
# Button: A button. Their big thing is commands, which can execute a function
# mainloop(): kind of like Unity's update function, keeps things updating
# grid(): The grid system organizes our window into rows and columns to be filled.
# If we don't like this option, there is also pack(), which operates more relative
# to the widgets in the window.
class mainViews():

    def __init__(self):
        self.controller = None
        self.window=Tk()
        self.task=""
        self.sheep=""
        self.workTime=0
        self.restTime=0

    def setController(self,controller):
        self.controller = controller

    def checkForShammy(self):
        root=self.window
        sheep = self.getSheep()
        print(sheep)
        if(sheep == "Shammy"):
            shammy = PhotoImage(file='SheepAnimations\\Shammy.png')
            root.iconphoto(True,shammy)

    def assignVals(self,sheep,task,wHrs,wMins,rHrs,rMins):
        self.setSheep(sheep)
        self.setTask(task)
        self.setWorkTime((wHrs*3600)+(wMins*60))
        print(self.sheep)
        print(self.workTime)
        self.setRestTime((rHrs*3600)+(rMins*60))
        self.checkForShammy()

    # main menu/view(s)
    def MainMenu(self):
        root = self.window
        sName = tk.StringVar() # var to hold sheep
        taskItem = tk.StringVar() # var to hold task

        title = Label(root, text='Welcome to Flock Focus!')
        title.grid(row=0) # row 0 is just the top

        query = Label(root, text='Name your sheep: ')
        query.grid(row=1)
        sheepName = Entry(root,textvariable=sName)
        sheepName.grid(row=1,column=1, columnspan=4) # query and sheepName are both row 1, but the name is next
        # to query so it has column 1

        task = Label(root, text='Enter your task: ')
        task.grid(row=2)
        taskEntry = Entry(root, textvariable=taskItem)
        taskEntry.grid(row=2,column=1,columnspan=4)
        
        # Time inputs. 2 small inline number inputs for minutes and hours in each with preset times of 25 and 5
        wHours = tk.IntVar()
        wMinutes = tk.IntVar()
        Label(root, text='Work time: ').grid(row=3)
        workTimeHours = Entry(root, width=2,textvariable=wHours)
        workTimeHours.insert(0, '0')  # preset number
        workTimeHours.grid(row=3, column=1)
        Label(root, text='hour(s)').grid(row=3, column=2)
        workTimeMinutes = Entry(root, width=2, textvariable=wMinutes)
        workTimeMinutes.insert(0, '25')  # preset number
        workTimeMinutes.grid(row=3, column=3)
        Label(root, text='minute(s)').grid(row=3, column=4)
        
        rHours = tk.IntVar()
        rMinutes = tk.IntVar()
        Label(root, text='Break time: ').grid(row=4)
        breakTimeHours = Entry(root, width=2, textvariable=rHours)
        breakTimeHours.insert(0, '0')  # preset number
        breakTimeHours.grid(row=4, column=1)
        Label(root, text='hour(s)').grid(row=4, column=2)
        breakTimeMinutes = Entry(root, width=2, textvariable=rMinutes)
        breakTimeMinutes.insert(0, '5')  # preset number
        breakTimeMinutes.grid(row=4, column=3)
        Label(root, text='minute(s)').grid(row=4, column=4)
        
        
        # button info
        quit = Button(root, text='EXIT', command=root.quit)
        quit.grid(row=6,column=0)
        # go = Button(root, text='GO',command = lambda: self.controller.setTaskAndSheep(sheepName.get(),taskEntry.get(),workTimeHours.get(),workTimeMinutes.get(),breakTimeHours.get(),breakTimeMinutes.get()))
        go = Button(root,text="GO",command=lambda:self.assignVals(sName.get(),taskItem.get(),wHours.get(),wMinutes.get(),rHours.get(),rMinutes.get()))
        go.grid(row=6,column=1) # starts the little sheep animation guy thing I am very tired
        root.mainloop()

    def setSheep(self,sheep):
        self.sheep=sheep

    def getSheep(self):
        return self.sheep

    def setTask(self,task):
        self.task=task
    
    def setWorkTime(self,wTime):
        self.workTime=wTime

    def setRestTime(self,rTime):
        self.restTime=rTime

    #MainMenu()
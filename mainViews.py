import tkinter as tk
from tkinter import *
import mainController

# Label: Just text, there is an option called Message but it just does the same thing.
# Entry: Just an empty box to be filled, can be referenced in commands.
# Button: A button. Their big thing is commands, which can execute a function
# mainloop(): kind of like Unity's update function, keeps things updating
# grid(): The grid system organizes our window into rows and columns to be filled.
# If we don't like this option, there is also pack(), which operates more relative
# to the widgets in the window.

root = Tk()
taskList = list()

# main menu/view(s)
def MainMenu():
    taskItem = tk.StringVar() # var to hold task
    title = Label(root, text='Welcome to the Pomodoro Flock!').grid(row=0) # row 0 is just the top
    query = Label(root, text='Name your sheep: ').grid(row=1)
    sheepName = Entry(root).grid(row=1,column=1) # query and sheepName are both row 1, but the name is next
    # to query so it has column 1
    task = Label(root, text='Enter your task: ').grid(row=2)
    taskEntry = Entry(root, textvariable=taskItem).grid(row=2,column=1)
    
    # Time inputs. 2 small inline number inputs for minutes and hours in each with preset times of 25 and 5
    Label(root, text='Work time: ').grid(row=3)
    workTimeHours = Entry(root, width=2)
    workTimeHours.insert(0, '0')  # preset number
    workTimeHours.grid(row=3, column=1)
    Label(root, text='hour(s)').grid(row=3, column=2)
    workTimeMinutes = Entry(root, width=2)
    workTimeMinutes.insert(0, '25')  # preset number
    workTimeMinutes.grid(row=3, column=3)
    Label(root, text='minute(s)').grid(row=3, column=4)
    
    Label(root, text='Break time: ').grid(row=4)
    breakTimeHours = Entry(root, width=2)
    breakTimeHours.insert(0, '0')  # preset number
    breakTimeHours.grid(row=4, column=1)
    Label(root, text='hour(s)').grid(row=4, column=2)
    breakTimeMinutes = Entry(root, width=2)
    breakTimeMinutes.insert(0, '5')  # preset number
    breakTimeMinutes.grid(row=4, column=3)
    Label(root, text='minute(s)').grid(row=4, column=4)
    
    

    quit = Button(root, text='EXIT', command=root.quit).grid(row=6,column=0)
    go = Button(root, text='GO').grid(row=6,column=1) # starts the little sheep animation guy thing I am very tired
    root.mainloop()


MainMenu()
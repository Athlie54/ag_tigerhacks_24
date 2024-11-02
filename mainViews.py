from tkinter import *

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
    title = Label(root, text='Welcome to the Pomodoro Flock!').grid(row=0) # row 0 is just the top
    query = Label(root, text='Name your sheep: ').grid(row=1)
    sheepName = Entry(root).grid(row=1,column=1) # query and sheepName are both row 1, but the name is next
    # to query so it has column 1
    tQuery = Label(root, text='What is your task?').grid(row=2, column=0)
    task = Entry(root).grid(row=2,column=1)
    tString = task.get()
    
    tlBox = Listbox(root).grid(row=3)
    for t in taskList:
        tlBox.insert(END,t)

    newTask = Button(root, text='ADD', command=FillTaskList(task,taskList)).grid(row=6,column=0)

    quit = Button(root, text='EXIT', command = root.quit).grid(row=6,column=1)
    root.mainloop()

def FillTaskList(task, taskList):
    taskList.append(str(task) + '\n')


MainMenu()
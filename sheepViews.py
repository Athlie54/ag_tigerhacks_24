from tkinter import *

# Label: Just text, there is an option called Message but it just does the same thing.
# Entry: Just an empty box to be filled, can be referenced in commands.
# Button: A button. Their big thing is commands, which can execute a function
# mainloop(): kind of like Unity's update function, keeps things updating
# grid(): The grid system organizes our window into rows and columns to be filled.
# If we don't like this option, there is also pack(), which operates more relative
# to the widgets in the window.

root = Tk()

# main menu/view(s)
def mainMenu():
    title = Label(root, text='Welcome to the Flock!').grid(row=0) # row 0 is just the top
    query = Label(root, text='Name your sheep: ').grid(row=1)
    sheepName = Entry(root).grid(row=1,column=1) # query and sheepName are both row 1, but the name is next
    # to query so it has column 1
    done = Button(root, text='DONE', command = root.quit).grid(row=2)
    root.mainloop()


mainMenu()
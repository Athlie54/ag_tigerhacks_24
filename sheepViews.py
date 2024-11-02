from tkinter import *

root = Tk()

# main menu/view(s)
def mainMenu():
    title = Label(root, text='Welcome to the Flock!').grid(row=0)
    query = Label(root, text='Name your sheep: ').grid(row=1)
    sheepName = Entry(root).grid(row=1,column=1)
    done = Button(root, text='DONE', command = root.quit).grid(row=2)
    root.mainloop()


mainMenu()
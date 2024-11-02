# sheep window! sheep window!
import tkinter
from tkinter import *
import mainController

window = tkinter.Tk()
path = 'SheepAnimations\\'



def SheepWindow():
    window.config(highlightbackground='#ffa3bb') 
    label = tkinter.Label(window,bd=0,bg='#ffa3bb')
    window.overrideredirect(True)
    window.wm_attributes('-transparentcolor','#ffa3bb') # make the background transparent based on hex code of the background color
    label.pack()
    animation = [tkinter.PhotoImage(file=path+'Growth.gif',format = 'gif -index %i' %(i)) for i in range(3)]#idle gif
    frame = animation[0]
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    #TODO: calculate this bigFrame size based on screen size becuase whiteboxing is bad. thanks github
    window.geometry(str(int(width/20))+'x'+str(int(width/20))) #GROSS.
    bigFrame = frame.zoom(int((width/20)/32),int((width/20)/32))
    label.configure(image=bigFrame)
    window.mainloop()
    #make it stay on top

# SheepWindow()

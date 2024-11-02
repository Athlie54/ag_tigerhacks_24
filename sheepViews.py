# sheep window! sheep window!
import tkinter
import win32api

window = tkinter.Tk()
path = 'SheepAnimations\\'

def SheepWindow():
    window.config(highlightbackground='#ffa3bb')
    label = tkinter.Label(window,bd=0,bg='#ffa3bb')
    window.overrideredirect(True)
    window.wm_attributes('-transparentcolor','#ffa3bb')
    label.pack()
    idle = [tkinter.PhotoImage(file=path+'Growth.gif',format = 'gif -index %i' %(i)) for i in range(3)]#idle gif
    frame = idle[0]
    bigFrame = frame.zoom(2,2)
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry(str(int(width/20))+'x'+str(int(width/20)))
    label.configure(image=bigFrame)
    window.mainloop()
    #make it stay on top

SheepWindow()

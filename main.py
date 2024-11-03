import tkinter
from tkinter import *
import mainViews
import mainController
import sheepViews
import animationController
import time

def update_animation(root, sheep_view, current_frame=0):
    sheep_view.update_frames(0, 2, 0)
    root.after(1000, lambda: update_animation(root, sheep_view, (current_frame + 1) % 3))

if __name__ == '__main__':
    root = tkinter.Tk()
    
    mainView = mainViews.mainViews()
    sheepView = sheepViews.sheepViews(root)
    maincontroller = mainController.mainController(mainView, sheepView)
    
    mainView.setController(maincontroller)
    sheepView.setController(maincontroller)
    
    # Start the animation loop
    update_animation(root, sheepView)
    
    # Start the main event loop
    root.mainloop()
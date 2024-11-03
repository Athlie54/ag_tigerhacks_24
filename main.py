import tkinter
from tkinter import *
import mainViews
import mainController
import sheepViews
import animationController
import time

def update_animation(root, sheep_view, frame_indexes=[0,0,0]):
    # Update each layer's frame index
    frame_indexes[0] = (frame_indexes[0] + 1) % len(sheep_view.layer1)
    frame_indexes[1] = (frame_indexes[1] + 1) % len(sheep_view.layer2)
    frame_indexes[2] = (frame_indexes[2] + 1) % len(sheep_view.layer3)
    
    sheep_view.update_frames(*frame_indexes)
    root.after(100, lambda: update_animation(root, sheep_view, frame_indexes))

if __name__ == '__main__':
    root = tkinter.Tk()
    
    mainView = mainViews.mainViews()
    sheepView = sheepViews.sheepViews(root)
    maincontroller = mainController.mainController(mainView, sheepView)
    animationcontroller = animationController.animationController(sheepView)

    mainView.setController(maincontroller)
    sheepView.setController(maincontroller)
    sheepView.setAnimationController(animationcontroller)

    mainView.MainMenu()
    # Start the animation loop with initial frame indexes
    update_animation(root, sheepView, [0,0,0])
    
    # Start the main event loop
    root.mainloop()
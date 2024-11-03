import tkinter
from tkinter import *
import mainViews
import mainController
import sheepViews
import animationController
import time

class AnimationState:
    IDLE = "idle"
    EATING = "eating"
    SHOCKED = "shocked"
    
def get_frames_for_state(state, frame_counter):
    if state == AnimationState.IDLE:
        return (0, 2, 0)  # idle pose: base body, max growth, base head
    elif state == AnimationState.EATING:
        head_frame = frame_counter % 15  # cycle through eating head frames
        return (0, 2, head_frame)
    elif state == AnimationState.SHOCKED:
        if frame_counter < 18:  # lightning animation
            return (1, 2, frame_counter + 15)  # offset for lightning frames
        else:
            shock_frame = min((frame_counter - 18) % 24, 23)  # shocked face animation
            return (shock_frame + 2, 2, 32)  # offset for shocked frames
    return (0, 2, 0)  # default to idle

def update_animation(root, sheep_view, current_state=AnimationState.IDLE, frame_counter=0):
    frames = get_frames_for_state(current_state, frame_counter)
    sheep_view.update_frames(*frames)
    
    # Update frame counter
    frame_counter = (frame_counter + 1) % 50  # arbitrary max frames
    
    # Example of how to change states (you can add your own triggers)
    if frame_counter == 0:  # Reset to idle after animation completes
        current_state = AnimationState.IDLE
    
    root.after(100, lambda: update_animation(root, sheep_view, current_state, frame_counter))

if __name__ == '__main__':
    root = tkinter.Tk()
    
    mainView = mainViews.mainViews()
    sheepView = sheepViews.sheepViews(root)
    maincontroller = mainController.mainController(mainView, sheepView)
    
    mainView.setController(maincontroller)
    sheepView.setController(maincontroller)
    
    mainView.MainMenu()
    # Start with idle animation
    update_animation(root, sheepView, AnimationState.IDLE)
    
    # Start the main event loop
    root.mainloop()
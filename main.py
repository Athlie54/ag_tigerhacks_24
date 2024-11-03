import tkinter
from tkinter import *
import mainViews
import mainController
import sheepViews
import animationController
import time

if __name__ == '__main__':
    window = tkinter.Tk()
    canvas = tkinter.Canvas(window, width=200, height=100, bg='#ffa3ba', highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    window.attributes('-topmost', True)
    window.overrideredirect(True)
    
    mainView = mainViews.mainViews()
    #sheepView = sheepViews.sheepViews(window)
    maincontroller = mainController.mainController(mainView)
    mainView.setController(maincontroller)
    #sheepView.setController(maincontroller)
    animation = animationController.animationController()

    def TransWindow(self, gif_path, gif_file_name, current_frame, gif_path2, gif_file_name2, current_frame2, gif_path3, gif_file_name3, current_frame3):
        # Load frames for the first GIF
        animation_frames1 = []
        frame_index = 0
        while True:
            try:
                frame = tkinter.PhotoImage(file=gif_path + gif_file_name, format='gif -index %i' % frame_index)
                animation_frames1.append(frame.subsample(1, 1))
                frame_index += 1
            except tkinter.TclError:
                break

        # Load frames for the second GIF
        animation_frames2 = []
        frame_index = 0
        while True:
            try:
                frame = tkinter.PhotoImage(file=gif_path2 + gif_file_name2, format='gif -index %i' % frame_index)
                animation_frames2.append(frame.subsample(1, 1))
                frame_index += 1
            except tkinter.TclError:
                break

        # Load frames for the third GIF
        animation_frames3 = []
        frame_index = 0
        while True:
            try:
                frame = tkinter.PhotoImage(file=gif_path3 + gif_file_name3, format='gif -index %i' % frame_index)
                animation_frames3.append(frame.subsample(1, 1))
                frame_index += 1
            except tkinter.TclError:
                break

        # Set the current frame for each GIF
        current_gif_frame1 = animation_frames1[current_frame]
        current_gif_frame2 = animation_frames2[current_frame2]
        current_gif_frame3 = animation_frames3[current_frame3]
        
        # Get screen dimensions
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - 200) / 2
        y = (screen_height - 100) / 2
        window.geometry('%dx%d+%d+%d' % (200, 100, x, y))
        canvas.create_image(100, 50, image=current_gif_frame1, anchor=CENTER)
        canvas.create_image(100, 50, image=current_gif_frame2, anchor=CENTER)
        canvas.create_image(100, 50, image=current_gif_frame3, anchor=CENTER)
        window.update()
        
        
    #test animation
    TransWindow('TransSheep\\', 'SheepEatBodyTrans.gif', 0, 'TransSheep\\', 'GrowthTrans.gif', 0, 'TransSheep\\', 'SheepEatHeadTrans.gif',
                0)
    time.sleep(2)
    TransWindow('TransSheep\\', 'SheepEatBodyTrans.gif', 0, 'TransSheep\\', 'GrowthTrans.gif', 2, 'TransSheep\\', 'SheepEatHeadTrans.gif',
                4)
    
    
    window.mainloop()
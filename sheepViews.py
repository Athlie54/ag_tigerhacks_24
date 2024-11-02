# sheep window! sheep window!
import tkinter
from tkinter import *
import win32api

bg = '#ffa3bb'
#animation_frames = [[tkinter.PhotoImage(file='SheepAnimations\\SheepEatBodyOnly.gif', format='gif -index %i' % i) for i in range(3)],
#                    [tkinter.PhotoImage(file='SheepAnimations\\growth.gif', format='gif -index %i' % i) for i in range(3)],
#                    [tkinter.PhotoImage(file='SheepAnimations\\SheepEatHeadOnly.gif', format='gif -index %i' % i) for i in range(3)]]

class sheepViews():
    def __init__(self,gif_path,gif_file_name,total_frames):
        self.animation_frames = [tkinter.PhotoImage(file=gif_path + gif_file_name, format='gif -index %i' % i) for i in range(total_frames)]

    def TransWindow(self, current_frame):
        window = tkinter.Tk()
        window.config(highlightbackground=bg) 
        label = tkinter.Label(window, bd=0, bg=bg)
        canvas = tkinter.Canvas(window, width=1920, height=1080, bg=bg)
        canvas.pack(fill="both", expand=True)
        window.wm_attributes('-transparentcolor', bg)  # make the background transparent based on hex code of the background color
        window.config(highlightbackground=bg)
        window.overrideredirect(True)
        window.wm_attributes('-transparentcolor', bg)  # make the background transparent based on hex code of the background color
        
        # Load the GIF frames
        #animation_frames = [tkinter.PhotoImage(file=gif_path + gif_file_name, format='gif -index %i' % i) for i in range(total_frames)]
        current_gif_frame = self.animation_frames[current_frame]
        
        # Get screen dimensions
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        # Calculate window size based on screen size
        window_size = int(screen_width / 2)
        window.geometry(f'{window_size}x{window_size}')
        
        # Resize the GIF frame
        resized_frame = current_gif_frame.zoom(window_size // 32, window_size // 32)
        label.configure(image=resized_frame)
        label.pack()
        canvas.create_image(100, 100, anchor=NW, image=resized_frame)
        
        resized_frame2 = tkinter.PhotoImage(file="SheepAnimations\\Shammy.png").zoom(window_size // 32, window_size // 32)
        canvas.create_image(50, 50, anchor=NW, image=resized_frame2)
        
        # Keep the window on top
        window.attributes('-topmost', True)
        
        window.mainloop()
        #make it stay on top

    # def bodyWindow(self):
    # SheepWindow()
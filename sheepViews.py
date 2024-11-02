# sheep window! sheep window!
import tkinter
from tkinter import *
import win32api

bg = '#ffa3bb'
animation_frames = [[tkinter.PhotoImage(file='SheepAnimations\\SheepEatBodyOnly.gif', format='gif -index %i' % i) for i in range(3)],
                    [tkinter.PhotoImage(file='SheepAnimations\\growth.gif', format='gif -index %i' % i) for i in range(3)],
                    [tkinter.PhotoImage(file='SheepAnimations\\SheepEatHeadOnly.gif', format='gif -index %i' % i) for i in range(3)]]

class sheepViews():

    def TransWindow(self, gif_path, gif_file_name, current_frame, total_frames,layer):
        window = tkinter.Tk()
        window.config(highlightbackground=bg) 
        label = tkinter.Label(window, bd=0, bg=bg)
        window.overrideredirect(True)
        window.wm_attributes('-transparentcolor', bg)  # make the background transparent based on hex code of the background color
        
        # Load the GIF frames
        #animation_frames = [tkinter.PhotoImage(file=gif_path + gif_file_name, format='gif -index %i' % i) for i in range(total_frames)]
        current_gif_frame = animation_frames[layer][current_frame]
        
        # Get screen dimensions
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        # Calculate window size based on screen size
        window_size = int(screen_width / 20)
        window.geometry(f'{window_size}x{window_size}')
        
        # Resize the GIF frame
        resized_frame = current_gif_frame.zoom(window_size // 32, window_size // 32)
        label.configure(image=resized_frame)
        label.pack()
        
        # Keep the window on top
        window.attributes('-topmost', True)
        
        window.mainloop()
        #make it stay on top

    # def bodyWindow(self):
    # SheepWindow()
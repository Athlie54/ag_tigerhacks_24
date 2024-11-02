# sheep window! sheep window!
import tkinter
from tkinter import *
#import win32api

bg = '#ffa3bb'

class sheepViews():

    def TransWindow(self, gif_path, gif_file_name, current_frame, total_frames):
        window = tkinter.Tk()
        canvas = tkinter.Canvas(window, width=200, height=100, bg=bg)
        canvas.pack(fill="both", expand=True)
        window.wm_attributes('-transparentcolor', bg)  # make the background transparent based on hex code of the background color
        window.config(highlightbackground=bg) 
        label = tkinter.Label(canvas, text="label1", bd=0, bg=bg)
        canvas.create_window(10,10, window=label)
        label2 = tkinter.Label(canvas, text="label2", bd=0, bg=bg)
        canvas.create_window(50,50, window=label2)
        window.overrideredirect(True)
                
        # Load the GIF frames
        animation_frames = [tkinter.PhotoImage(file=gif_path + gif_file_name, format='gif -index %i' % i) for i in range(total_frames)]
        current_gif_frame = animation_frames[current_frame]
        
        # Get screen dimensions
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        # Calculate window size based on screen size
        window_size = int(screen_width / 20)
        window.geometry(f'{window_size}x{window_size}')
        
        # Resize the GIF frame
        resized_frame = current_gif_frame.zoom(window_size // 32, window_size // 32)
        label.configure(image=resized_frame)
        label.image = resized_frame
        
        
        resized_frame2 = tkinter.PhotoImage(file="SheepAnimations\\Shammy.png").zoom(window_size // 32, window_size // 32)
        label2.configure(image=resized_frame2)
        label2.image = resized_frame2
        label.pack()
        label2.pack()
        
        
        # Keep the window on top
        window.attributes('-topmost', True)
        
        window.mainloop()
        #make it stay on top

    # def bodyWindow(self):
    # SheepWindow()
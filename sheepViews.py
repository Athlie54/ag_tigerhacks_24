import tkinter
from tkinter import *
import os


bg = '#ffa3ba'

class sheepViews():
    def __init__(self):
        self.controller = None

    def setController(self,controller):
        self.controller = controller

    def TransWindow(self, gif_path, gif_file_name, current_frame):
        window = tkinter.Tk()
        canvas = tkinter.Canvas(window, width=200, height=100, bg=bg, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        window.wm_attributes('-transparentcolor', bg)  # make the background transparent based on hex code of the background color
        window.overrideredirect(True)
        
        # Load the GIF frames
        animation_frames = []
        frame_index = 0
        while True:
            try:
                frame = tkinter.PhotoImage(file=gif_path + gif_file_name, format='gif -index %i' % frame_index)
                animation_frames.append(frame.subsample(1, 1))  # Ensure full frames are rendered
                frame_index += 1
            except tkinter.TclError:
                break
        
        current_gif_frame = animation_frames[current_frame]
        
        # Get screen dimensions
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        # Calculate window size based on screen size
        window_size = int(screen_width / 16)
        window.geometry(f'{window_size}x{window_size}')
        
        # Resize the GIF frame
        resized_frame = current_gif_frame.zoom(window_size // 32, window_size // 32)
        canvas.create_image(10, 10, anchor=NW, image=resized_frame)
        
        resized_frame2 = tkinter.PhotoImage(file="SheepAnimations\\Shammy.png").zoom(window_size // 32, window_size // 32)
        canvas.create_image(10, 10, anchor=NW, image=resized_frame2)
        
        # Position the window at the bottom right corner, above the taskbar and slightly to the left
        x_position = screen_width - window_size - 50  # 50 pixels to the left
        y_position = screen_height - window_size - 30  # 30 pixels above the taskbar
        window.geometry(f'+{x_position}+{y_position}')
        
        # Keep the window on top
        window.attributes('-topmost', True)

        
        # right-click menu (to return to mainViews)
        sheepMenu = Menu(window, tearoff=0, bg='lightgreen')
        sheepMenu.add_command(label="Return to Main Menu", command=self.controller.openMainMenu)
        sheepMenu.add_separator()
        sheepMenu.add_command(label="Temp-hide (15 secs)")#command=self.controller.tempHideSheep
        sheepMenu.add_separator()
        sheepMenu.add_command(label="Completed Task", command=self.controller.completeTask)
        sheepMenu.add_command(label="Failed Task")


        def popup(event):
            try:
                sheepMenu.tk_popup(event.x_root, event.y_root)
            finally:
                sheepMenu.grab_release()
        
        window.bind("<Button-3>", popup)

        window.mainloop()

# Example usage
# sheep_view = sheepViews()
# sheep_view.TransWindow('path_to_gif/', 'gif_file_name.gif', 0, 10)

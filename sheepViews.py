import tkinter
from tkinter import *
import time
import os

bg = '#ffa3ba'

class sheepViews():
    def __init__(self):
        self.controller = None

    def setController(self,controller):
        self.controller = controller
        
    def TransWindow(self, gif_path, gif_file_name, current_frame, gif_path2, gif_file_name2, current_frame2, gif_path3, gif_file_name3, current_frame3):
        window = tkinter.Tk()
        canvas = tkinter.Canvas(window, width=200, height=100, bg=bg, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        window.wm_attributes('-transparentcolor', bg)
        window.overrideredirect(True)
        
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
        
        # Calculate window size
        window_size = int(screen_width / 16)
        window.geometry(f'{window_size}x{window_size}')
        
        # Resize and display each GIF layer
        resized_frame1 = current_gif_frame1.zoom(window_size // 32, window_size // 32)
        canvas.create_image(10, 10, anchor=NW, image=resized_frame1)

        resized_frame2 = current_gif_frame2.zoom(window_size // 32, window_size // 32)
        canvas.create_image(10, 10, anchor=NW, image=resized_frame2)

        resized_frame3 = current_gif_frame3.zoom(window_size // 32, window_size // 32)
        canvas.create_image(10, 10, anchor=NW, image=resized_frame3)
        
        
        # Position window in bottom right corner
        x_position = screen_width - window_size - 50
        y_position = screen_height - window_size - 30
        window.geometry(f'+{x_position}+{y_position}')
        
        # Keep window on top
        window.attributes('-topmost', True)
        
        # Right-click menu
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

        
        window.update_idletasks()
        window.update()
        

# Example usage
# sheep_view = sheepViews()
# sheep_view.TransWindow('path_to_first_gif/', 'first_gif_name.gif', 0, 'path_to_second_gif/', 'second_gif_name.gif', 0, 'path_to_third_gif/', 'third_gif_name.gif', 0)

import tkinter
from tkinter import *
import os

bg = '#ffa3ba'

class sheepViews():
    def TransWindow(self, gif_path, gif_file_name, current_frame, gif_path2, gif_file_name2, current_frame2):
        window = tkinter.Tk()
        canvas = tkinter.Canvas(window, width=200, height=100, bg=bg, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        window.wm_attributes('-transparentcolor', bg)
        window.overrideredirect(True)
        
        # Load the first GIF frames
        animation_frames1 = []
        frame_index = 0
        while True:
            try:
                frame = tkinter.PhotoImage(file=gif_path + gif_file_name, format='gif -index %i' % frame_index)
                animation_frames1.append(frame.subsample(1, 1))
                frame_index += 1
            except tkinter.TclError:
                break

        # Load the second GIF frames
        animation_frames2 = []
        frame_index = 0
        while True:
            try:
                frame = tkinter.PhotoImage(file=gif_path2 + gif_file_name2, format='gif -index %i' % frame_index)
                animation_frames2.append(frame.subsample(1, 1))
                frame_index += 1
            except tkinter.TclError:
                break

        current_gif_frame1 = animation_frames1[current_frame]
        current_gif_frame2 = animation_frames2[current_frame2]
        
        # Get screen dimensions
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        # Calculate window size based on screen size
        window_size = int(screen_width / 16)
        window.geometry(f'{window_size}x{window_size}')
        
        # Resize and display the first GIF frame
        resized_frame1 = current_gif_frame1.zoom(window_size // 32, window_size // 32)
        canvas.create_image(10, 10, anchor=NW, image=resized_frame1)
        
        # Resize and display the second GIF frame
        resized_frame2 = current_gif_frame2.zoom(window_size // 32, window_size // 32)
        canvas.create_image(10, 10, anchor=NW, image=resized_frame2)
        
        # Position the window at the bottom right corner
        x_position = screen_width - window_size - 50
        y_position = screen_height - window_size - 30
        window.geometry(f'+{x_position}+{y_position}')
        
        # Keep the window on top
        window.attributes('-topmost', True)
        
        # Right-click menu (to return to mainViews)
        sheepMenu = Menu(window, tearoff=0, bg='lightgreen')
        sheepMenu.add_command(label="Return to Main Menu")
        sheepMenu.add_separator()
        sheepMenu.add_command(label="Temp-hide (15 secs)")

        def popup(event):
            try:
                sheepMenu.tk_popup(event.x_root, event.y_root)
            finally:
                sheepMenu.grab_release()
        
        window.bind("<Button-3>", popup)

        window.mainloop()

# Example usage
# sheep_view = sheepViews()
# sheep_view.TransWindow('path_to_first_gif/', 'first_gif_name.gif', 0, 'path_to_second_gif/', 'second_gif_name.gif', 0)

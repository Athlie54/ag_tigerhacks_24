import tkinter
from tkinter import *
import time
import os

bg = '#ffa3ba'

class sheepViews():
    def __init__(self):
        self.controller = None
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.window, width=200, height=100, bg=bg, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.window.wm_attributes('-transparentcolor', bg)
        self.window.overrideredirect(True)
        
        self.layer1_1 = [tkinter.PhotoImage(file="TransSheep\\SheepEatBodyTrans.gif",format = 'gif -index %i' %(i)) for i in range(1)]
        self.layer1_2 = [tkinter.PhotoImage(file="TransSheep\\SheepEatTrans.gif",format = 'gif -index %i' %(i)) for i in range(1)]
        self.layer1_3 = [tkinter.PhotoImage(file="TransSheep\\ShockedSheep.gif",format = 'gif -index %i' %(i)) for i in range(24)]
        self.layer1 = [self.layer1_1]+[self.layer1_2]+[self.layer1_3]
        
        self.layer2_1 = [tkinter.PhotoImage(file="TransSheep\\GrowthTrans.gif",format = 'gif -index %i' %(i)) for i in range(3)]
        self.layer2 = [self.layer2_1]
        
        self.layer3_1 = [tkinter.PhotoImage(file="TransSheep\\SheepEatHeadTrans.gif",format = 'gif -index %i' %(i)) for i in range(15)]
        self.layer3_2 = [tkinter.PhotoImage(file="TransSheep\\LightningTrans.gif",format = 'gif -index %i' %(i)) for i in range(18)]
        self.layer3 = [self.layer3_1]+[self.layer3_2]#"TransSheep\\", "SheepEatHeadTrans.gif", 0

    def setController(self,controller):
        self.controller = controller
        
    def TransWindow(self, indexLayer1,indexLayer2,indexLayer3):#gif_path, gif_file_name, current_frame, gif_path2, gif_file_name2, current_frame2, gif_path3, gif_file_name3, current_frame3
        # Load frames for the first GIF
        animation_frames1 = []
        frame_index = 0
        while True:
            try:
                frame = self.layer1[indexLayer1] #tkinter.PhotoImage(file=gif_path + gif_file_name, format='gif -index %i' % frame_index)
                animation_frames1.append(frame.subsample(1, 1))
                frame_index += 1
            except tkinter.TclError:
                break

        # Load frames for the second GIF
        animation_frames2 = []
        frame_index = 0
        while True:
            try:
                frame = self.layer2[indexLayer2] #tkinter.PhotoImage(file=gif_path2 + gif_file_name2, format='gif -index %i' % frame_index)
                animation_frames2.append(frame.subsample(1, 1))
                frame_index += 1
            except tkinter.TclError:
                break

        # Load frames for the third GIF
        animation_frames3 = []
        frame_index = 0
        while True:
            try:
                frame = self.layer3[indexLayer3] #tkinter.PhotoImage(file=gif_path3 + gif_file_name3, format='gif -index %i' % frame_index)
                animation_frames3.append(frame.subsample(1, 1))
                frame_index += 1
            except tkinter.TclError:
                break

        # Set the current frame for each GIF
        # current_gif_frame1 = animation_frames1[current_frame]
        # current_gif_frame2 = animation_frames2[current_frame2]
        # current_gif_frame3 = animation_frames3[current_frame3]
        
        # Get screen dimensions
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        
        # Calculate window size
        window_size = int(screen_width / 16)
        self.window.geometry(f'{window_size}x{window_size}')
        self.window.geometry(f'{window_size}x{window_size}')
        
        # Resize and display each GIF layer
        resized_frame1 = frame.zoom(window_size // 32, window_size // 32)
        self.canvas.create_image(10, 10, anchor=NW, image=resized_frame1)

        resized_frame2 = frame.zoom(window_size // 32, window_size // 32)
        self.canvas.create_image(10, 10, anchor=NW, image=resized_frame2)

        resized_frame3 = frame.zoom(window_size // 32, window_size // 32)
        self.canvas.create_image(10, 10, anchor=NW, image=resized_frame3)
        
        
        # Position window in bottom right corner
        x_position = screen_width - window_size - 50
        y_position = screen_height - window_size - 30
        self.window.geometry(f'+{x_position}+{y_position}')
        self.window.geometry(f'+{x_position}+{y_position}')
        
        # Keep window on top
        self.window.attributes('-topmost', True)
        self.window.attributes('-topmost', True)
        
        # Right-click menu
        sheepMenu = Menu(self.window, tearoff=0, bg='lightgreen')
        sheepMenu = Menu(self.window, tearoff=0, bg='lightgreen')
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
        
        self.window.bind("<Button-3>", popup)

        
        self.window.update_idletasks()
        self.window.update()
        

# Example usage
# sheep_view = sheepViews()
# sheep_view.TransWindow('path_to_first_gif/', 'first_gif_name.gif', 0, 'path_to_second_gif/', 'second_gif_name.gif', 0, 'path_to_third_gif/', 'third_gif_name.gif', 0)

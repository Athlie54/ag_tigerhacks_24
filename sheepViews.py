import tkinter
from tkinter import *
import time
import os

bg = '#ffa3ba'

class sheepViews():
    def __init__(self, parent_window):
        self.controller = None
        self.window = parent_window
        
        # Load image layers
        self.layer1_1 = [tkinter.PhotoImage(file="TransSheep\\SheepEatBodyTrans.gif",format = 'gif -index %i' %(i)) for i in range(1)]
        self.layer1_2 = [tkinter.PhotoImage(file="TransSheep\\SheepEatTrans.gif",format = 'gif -index %i' %(i)) for i in range(1)]
        self.layer1_3 = [tkinter.PhotoImage(file="TransSheep\\ShockedSheepTrans.gif",format = 'gif -index %i' %(i)) for i in range(24)]
        self.layer1 = self.layer1_1+self.layer1_2+self.layer1_3
        
        self.layer2_1 = [tkinter.PhotoImage(file="TransSheep\\GrowthTrans.gif",format = 'gif -index %i' %(i)) for i in range(3)]
        self.layer2 = self.layer2_1
        
        self.layer3_1 = [tkinter.PhotoImage(file="TransSheep\\SheepEatHeadTrans.gif",format = 'gif -index %i' %(i)) for i in range(15)]
        self.layer3_2 = [tkinter.PhotoImage(file="TransSheep\\LightningTrans.gif",format = 'gif -index %i' %(i)) for i in range(18)]
        self.layer3 = self.layer3_1+self.layer3_2

        # Create canvas
        self.canvas = tkinter.Canvas(self.window, width=200, height=100, bg=bg, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        # Setup window properties
        self.window.wm_attributes('-transparentcolor', bg)
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        
        # Setup menu
        self.setup_menu()
        
        # Calculate and set window position
        self.position_window()

    def setController(self, controller):
        self.controller = controller
        
    def setup_menu(self):
        sheepMenu = Menu(self.window, tearoff=0, bg='lightgreen')
        sheepMenu.add_command(label="Return to Main Menu", command=lambda: self.controller.openMainMenu())
        sheepMenu.add_separator()
        sheepMenu.add_command(label="Temp-hide (15 secs)")
        sheepMenu.add_separator()
        sheepMenu.add_command(label="Completed Task", command=lambda: self.controller.completeTask())
        sheepMenu.add_command(label="Failed Task")
        
        self.window.bind("<Button-3>", lambda e: self.show_popup(e, sheepMenu))
        
    def show_popup(self, event, menu):
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()
            
    def position_window(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_size = int(screen_width / 16)
        
        x_position = screen_width - window_size - 50
        y_position = screen_height - window_size - 30
        
        self.window.geometry(f'{window_size}x{window_size}+{x_position}+{y_position}')
        
    def update_frames(self, indexLayer1, indexLayer2, indexLayer3):
        self.canvas.delete("all")
        window_size = int(self.window.winfo_screenwidth() / 16)
        
        # Store resized frames references
        self.current_frames = []
        
        # Create layers in correct order (bottom to top)
        layers = [
            (self.layer1[indexLayer1], "layer1"),
            (self.layer2[indexLayer2], "layer2"),
            (self.layer3[indexLayer3], "layer3")
        ]
        
        # Center position calculation
        center_x = window_size // 2
        center_y = window_size // 2
        
        for frame, layer_name in layers:
            resized_frame = frame.zoom(window_size // 32, window_size // 32)
            self.current_frames.append(resized_frame)  # Prevent garbage collection
            self.canvas.create_image(center_x, center_y, anchor=CENTER, image=resized_frame, tags=layer_name)

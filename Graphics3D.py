from tkinter import *
import GUI
import Graphics2D

class Graphics3D(GUI.Application,Graphics2D.Graphics2D):
    def __init__(self, root):
        super().__init__(root)
        self.root=root
        self.create_grid_pixel()
    
    def create_grid_pixel(self):
        super().create_grid_pixel()
        
    
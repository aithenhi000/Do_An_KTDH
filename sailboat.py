from Graphics2D import Graphics2D
from tkinter import *

class sailboat(Graphics2D):
    def __init__(self, master):
        super().__init__(master)
        self.canvas.create_rectangle(5,5,50,50, fill='red')
        
    def draw_sailboat_parts(self):
        self.dr
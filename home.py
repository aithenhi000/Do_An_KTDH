from tkinter import *
import math as m 
import numpy as np


class Home(Frame):
    def __init__(self, master, width, height):
        super().__init__(master)
        self.master=master
        self.width=width
        self.height=height
        self.grid_size = 5
        self.origin=(self.width//2, self.height//2)
        self.create_canvas()
        self.create_grid_pixel()
        self.write_name()
        #self.create_circle()
        #self.move_circle()
        
    def tinh_tien(self, pos, delta_x, delta_y):

        mul_matrix = np.array(([1, 0, 0], [0, 1, 0], [delta_x, delta_y, 1]))

        #for x in range(0, pos.shape[0]):
        pos = np.matmul(pos, mul_matrix)

        return pos    

        
        
    def move_circle(self):
        self.pos1=self.tinh_tien(self.pos1, 0, -5)    
        print(self.pos1) 
        self.canvas.delete(*self.p1)
        self.pos1, self.p1 = self.draw_circle(self.pos1[0],self.pos1[1], 50)
        
        self.after(100, self.move_circle)
        
    def create_circle(self):
        self.pos1, self.p1 = self.draw_circle(0, 80, 50)

    
    def write_name(self):
        center_x = self.width // 2
        center_y = self.height // 2
        text = "THÀNH VIÊN\nPhan Hữu Thiên Phúc - N21DCPT075\nNguyễn Hoàng Khánh - N21DCPT038\n Phạm Nhật Ánh - N21DCPT007\n Lê Huy Hoàng - N21DCPT027\n Nguyễn Nhật Quang - N19DCPT055\n Nguyễn Viết Khang - N..DCPT..."
        text_id = self.canvas.create_text(center_x, center_y, text=text, font=("Courier", 14), justify="center")
        
    def create_canvas(self):
        self.canvas = Canvas(self, width=self.width, height=self.height, bg="#FEFAF6")
        self.canvas.pack()
        
    
            
    def put_pixel(self, x, y, color="green"):
            adjusted_x = self.width/2 + x*5
            adjusted_y = self.height/2 - y*5
            pixel_id=self.canvas.create_rectangle(adjusted_x-2, adjusted_y-2, adjusted_x+2, adjusted_y+2, fill=color, outline=None)
            return pixel_id
    
    def draw_circle(self, x_center, y_center, radius):
        x_center=round(x_center)
        y_center=round(y_center)
        x = radius
        y = 0
        p = 1 - radius

        points = []

        while x >= y:
            points.extend([
                self.put_pixel(x_center + x, y_center + y),
                self.put_pixel(x_center - x, y_center + y),
                self.put_pixel(x_center + x, y_center - y),
                self.put_pixel(x_center - x, y_center - y),
                self.put_pixel(x_center + y, y_center + x),
                self.put_pixel(x_center - y, y_center + x),
                self.put_pixel(x_center + y, y_center - x),
                self.put_pixel(x_center - y, y_center - x)
            ])

            y += 1

            if p <= 0:
                p = p + 2*y + 1
            else:
                x -= 1
                p = p + 2*y - 2*x + 1
            
        return np.array(([x_center, y_center, 1])), points
    
    def create_grid_pixel(self):
        canvas=self.canvas   
        # draw grid
        for x in range(0, self.width, self.grid_size):
            canvas.create_line(x, 0, x, self.height, fill="#EADBC8")
        for y in range(0, self.height, self.grid_size):
            canvas.create_line(0, y, self.width, y, fill="#EADBC8")
        # # X axis
        # canvas.create_line(0, self.origin[1], self.width, self.origin[1])
        # for x in range(0, self.width, 50):
        #     canvas.create_rectangle(
        #         x - 1, self.origin[1] - 1, x + 1, self.origin[1] + 1, fill="red"
        #     )
        #     canvas.create_text(
        #         x,
        #         self.origin[1] + 8,
        #         text=str(int((x - self.width / 2) / 5)),
        #         font=("Arial", 7),
        #     )

        # # Y axis
        # canvas.create_line(self.origin[0], 0, self.origin[0], self.height)
        # for y in range(0, self.height, 50):
        #     canvas.create_rectangle(
        #         self.origin[0] - 1, y - 1, self.origin[0] + 1, y + 1, fill="red"
        #     )
        #     canvas.create_text(
        #         self.origin[0] + 9,
        #         y,
        #         text=str(int(-(y - self.height / 2) / 5)),
        #         font=("Arial", 7),
        #     )
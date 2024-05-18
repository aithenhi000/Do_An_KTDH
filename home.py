from tkinter import *

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
        
    def write_name(self):
        center_x = self.width // 2
        center_y = self.height // 2
        text = "Phan Hữu Thiên Phúc - N21DCPT075\nNguyễn Hoàng Khánh - N21DCPT038\n Phạm Nhật Ánh - N21DCPT007\n Lê Huy Hoàng - N21DCPT027\n Nguyễn Nhật Quang - N19DCPT055"
        text_id = self.canvas.create_text(center_x, center_y, text=text, font=("Arial", 12), justify="center")
        
    def create_canvas(self):
        self.canvas = Canvas(self, width=self.width, height=self.height, bg="#FEFAF6")
        self.canvas.pack()
        
    def create_grid_pixel(self):
        canvas=self.canvas   
        # draw grid
        for x in range(0, self.width, self.grid_size):
            canvas.create_line(x, 0, x, self.height, fill="#EADBC8")
        for y in range(0, self.height, self.grid_size):
            canvas.create_line(0, y, self.width, y, fill="#EADBC8")

        # X axis
        canvas.create_line(0, self.origin[1], self.width, self.origin[1])
        for x in range(0, self.width, 50):
            canvas.create_rectangle(
                x - 1, self.origin[1] - 1, x + 1, self.origin[1] + 1, fill="red"
            )
            canvas.create_text(
                x,
                self.origin[1] + 8,
                text=str(int((x - self.width / 2) / 5)),
                font=("Arial", 7),
            )

        # Y axis
        canvas.create_line(self.origin[0], 0, self.origin[0], self.height)
        for y in range(0, self.height, 50):
            canvas.create_rectangle(
                self.origin[0] - 1, y - 1, self.origin[0] + 1, y + 1, fill="red"
            )
            canvas.create_text(
                self.origin[0] + 9,
                y,
                text=str(int(-(y - self.height / 2) / 5)),
                font=("Arial", 7),
            )
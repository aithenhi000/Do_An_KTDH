from tkinter import *
import math as m
import numpy as np


class Graphics2D(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.width=1200
        self.height=750
        self.grid_size = 5
        self.origin=(self.width//2, self.height//2)
        self.configure(padx=20, pady=20)
        self.create_canvas()
        self.create_grid_pixel()
        self.create_menu()
        self.create_info_panel()

    def create_menu(self):
        self.btn_draw_2d = Button(
            self, text="Vẽ cảnh 2D", bg='#FFC470', font=("Arial", 12, "bold"), command=self.draw_2d_main
        )
        self.btn_draw_2d.pack()
        self.btn_move_2d = Button(
            self, text="Chuyển động vật thể",bg='#FFC470', font=("Arial", 12, "bold"), command=self.move_2d
        )
        self.btn_move_2d.pack()

    def create_info_panel(self):
        self.fr=LabelFrame(self, text='THÔNG TIN VẬT THỂ DI CHUYỂN',borderwidth=2, relief="ridge", width=200, height=100)
        self.fr.pack()
    def create_canvas(self):
        self.canvas = Canvas(self, width=self.width, height=self.height, bg="#FEFAF6")
        self.canvas.pack(side=LEFT)
    
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
    def clear_canvas(self):
        self.canvas.delete('all')
        self.create_grid_pixel()

        
        
    def move_2d(self):
            
        self.tinh_tien_sailboat(1, 0)
        
        # Use a lambda to pass the callable to self.after
        self.after(120, self.move_2d)
        
    def tinh_tien_sailboat(self, x, y):
        
        self.tria_body_left = self.tinh_tien(self.tria_body_left, x, y)
        self.canvas.delete(*self.tria_body_left_id) #Xóa đi hình trước vẽ
        self.canvas.delete(*self.tria_body_left_fill_id)
        self.tria_body_left , self.tria_body_left_id, self.tria_body_left_fill_id=self.draw_right_triangle(self.tria_body_left[0,0],self.tria_body_left[0,1],-10,-10)

        self.tria_body_right = self.tinh_tien(self.tria_body_right, x, y)
        self.canvas.delete(*self.tria_body_right_id) #Xóa đi hình trước vẽ
        self.canvas.delete(*self.tria_body_right_fill_id)
        self.tria_body_right , self.tria_body_right_id, self.tria_body_right_fill_id=self.draw_right_triangle(self.tria_body_right[0,0],self.tria_body_right[0,1],10,-10)
        
        self.rec_body = self.tinh_tien(self.rec_body, x, y)
        self.canvas.delete(*self.rec_body_id) #Xóa đi hình trước vẽ
        self.canvas.delete(*self.rec_body_fill_id)
        self.rec_body , self.rec_body_id, self.rec_body_fill_id=self.draw_rectangle(self.rec_body[0,0],self.rec_body[0,1],self.rec_body[1,0], self.rec_body[1,1])

    def draw_sailboat(self, x0, y0):

        self.rec_body, self.rec_body_id, self.rec_body_fill_id = self.draw_rectangle (x0+30, y0, x0, y0-10)

        self.tria_body_left, self.tria_body_left_id, self.tria_body_left_fill_id = self.draw_right_triangle(x0, y0, -10, -10)
               
        self.tria_body_right, self.tria_body_right_id, self.tria_body_right_fill_id = self.draw_right_triangle(x0+30, y0, 10, -10)

    def draw_2d_main(self):
        self.draw_sailboat(-30, -30)
        
    def draw_rectangle(self, x1, y1, x2, y2):

        arr, arr_fill=self.draw_line_background(x1, y1, x2, y1, 'down', y2)
        arr.extend(self.draw_line(x2, y1, x2, y2))
        arr.extend(self.draw_line(x2, y2, x1, y2))
        arr.extend(self.draw_line(x1, y2, x1, y1))
        return np.array(([x1,y1,1], [x2,y2,1])), arr, arr_fill

    def draw_right_triangle(self, x1, y1, base, height):
        x2 = x1 + base
        y2 = y1
        x3 = x1
        y3 = y1 + height

        arr, arr_fill= self.draw_line_background(x2, y2, x3, y3, direction='up', draw_to=y1) # Cạnh huyền
        arr.extend(self.draw_line_special(x3, y3, x1, y1))  # Cạnh kề
        arr.extend(self.draw_line(x1, y1, x2, y2))  # Cạnh đáy
        return np.array(([x1,y1,1],[x2,y2,1],[x3,y3,1])), arr, arr_fill
        
##############################################################################
        
    def put_pixel(self, x, y, color="green", border='black'):
        adjusted_x = self.width/2 + x*5
        adjusted_y = self.height/2 - y*5
        pixel_id=self.canvas.create_rectangle(adjusted_x-2, adjusted_y-2, adjusted_x+2, adjusted_y+2, fill=color, outline=border)
        return pixel_id

    def draw_line(self, x1, y1, x2, y2):
        arr=[]
        x1=round(x1)
        y1=round(y1)
        x2=round(x2)
        y2=round(y2)
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        x, y = x1, y1
        x_step=1 if x1<x2 else -1
        y_step=1 if y1<y2 else -1
        f1 = 2 * (dy - dx)
        f2 = 2 * dy 
        p = 2 * dy - dx
        if dx>dy:
            while x != x2:
                x += x_step
                if p < 0:
                    p += f2
                else:
                    p += f1
                    y += y_step
                arr.append(self.put_pixel(x,y))
        else:
            p=2*dx-dy
            f1 = 2 * (dx - dy)
            f2 = 2 * dx
            while y!=y2:
                y+=y_step
                if p < 0:
                    p += f2
                else:
                    p += f1
                    x += x_step
                arr.append(self.put_pixel(x,y))

        return arr
    def draw_line_special(self, x1, y1, x2, y2):
        arr=[]
        x1=round(x1)
        y1=round(y1)
        x2=round(x2)
        y2=round(y2)
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        x, y = x1, y1
        x_step=1 if x1<x2 else -1
        y_step=1 if y1<y2 else -1
        f1 = 2 * (dy - dx)
        f2 = 2 * dy 
        p = 2 * dy - dx
        if dx>dy:
            while x != x2:
                x += x_step
                if p < 0:
                    p += f2
                else:
                    p += f1
                    y += y_step
                arr.append(self.put_pixel(x,y, 'red'))
        else:
            p=2*dx-dy
            f1 = 2 * (dx - dy)
            f2 = 2 * dx
            while y!=y2:
                y+=y_step
                if p < 0:
                    p += f2
                else:
                    p += f1
                    x += x_step
                arr.append(self.put_pixel(x,y, 'red'))

        return arr
    def draw_line_background(self, x1, y1, x2, y2, direction, draw_to):
        arr=[]
        arr_fill=[]
        x1=round(x1)
        y1=round(y1)
        x2=round(x2)
        y2=round(y2)
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        x, y = x1, y1
        x_step=1 if x1<x2 else -1
        y_step=1 if y1<y2 else -1
        f1 = 2 * (dy - dx)
        f2 = 2 * dy 
        p = 2 * dy - dx
        if dx>dy:
            while x != x2:
                x += x_step
                if p < 0:
                    p += f2
                else:
                    p += f1
                    y += y_step
                if direction=='up':
                    y_background=y+1
                    while(y_background<=draw_to-1):
                        arr_fill.append(self.put_pixel(x,y_background,'red','red'))
                        y_background+=1
                elif direction=='down':
                    y_background=y-1
                    while(y_background>=draw_to+1):
                        arr_fill.append(self.put_pixel(x,y_background,'red','red'))
                        y_background-=1
                elif direction=='right':
                    x_background=X+1
                    while(x_background<=draw_to-1):
                        arr_fill.append(self.put_pixel(x_background,y,'red','red'))
                        x_background+=1
                elif direction=='left':
                    x_background=X=1
                    while(x_background<=draw_to+1):
                        arr_fill.append(self.put_pixel(x_background,y,'red','red'))
                        x_background-=1
                arr.append(self.put_pixel(x,y))
        else:
            p=2*dx-dy
            f1 = 2 * (dx - dy)
            f2 = 2 * dx
            while y!=y2:
                y+=y_step
                if p < 0:
                    p += f2
                else:
                    p += f1
                    x += x_step
                if direction=='up':
                    y_background=y+1
                    while(y_background<=draw_to-1):
                        arr_fill.append(self.put_pixel(x,y_background,'red','red'))
                        y_background+=1
                elif direction=='down':
                    y_background=y-1
                    while(y_background>=draw_to+1):
                        arr_fill.append(self.put_pixel(x,y_background,'red','red'))
                        y_background-=1
                elif direction=='right':
                    x_background=X+1
                    while(x_background<=draw_to-1):
                        arr_fill.append(self.put_pixel(x_background,y,'red','red'))
                        x_background+=1
                elif direction=='left':
                    x_background=X=1
                    while(x_background<=draw_to+1):
                        arr_fill.append(self.put_pixel(x_background,y,'red','red'))
                        x_background-=1
                arr.append(self.put_pixel(x,y))
                    
        return arr, arr_fill
        
    def tinh_tien(self, pos, delta_x, delta_y):

        mul_matrix = np.array(([1, 0, 0], [0, 1, 0], [delta_x, delta_y, 1]))

        for x in range(0, pos.shape[0]):
            pos[x] = np.matmul(pos[x], mul_matrix)

        return pos

    def ti_le(self, pos, ratio):
        mul_matrix = np.array(([ratio, 0, 0], [0, ratio, 0], [0, 0, 1]))

        if pos.ndim == 1:
            pos = np.matmul(pos, mul_matrix)
        else:
            for x in range(0, pos.shape[0]):
                pos[x] = np.matmul(pos[x], mul_matrix)
        return pos

    def xoay_goc_x_do(self, pos, deg):

        cos=  m.cos(deg*m.pi/180)
        sin = m.sin(deg*m.pi/180)

        mul_matrix = np.array(( [cos,     sin,  0],
                                [-1*sin,  cos,  0],
                                [0,         0,  1]))
        if pos.ndim == 1:
            pos = np.matmul(pos, mul_matrix) 
        else:
            for x in range(0,pos.shape[0]):        
                pos[x]=np.matmul(pos[x],mul_matrix)

        return pos

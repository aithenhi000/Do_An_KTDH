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
        self.taohcn()
        
        self.create_info_panel()

        
    def taohcn(self):
        self.hcn1=self.canvas.create_rectangle(1,1,20,30, fill='red')
        self.canvas.delete(self.hcn1)
        self.hcn2=self.canvas.create_rectangle(50,50,80,80, fill='blue')
        
    
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

    def move_2d(self):

        rec1_1=self.tinh_tien(self.rec1, 5, 5)
        rec1_1=self.ti_le(rec1_1, 1.2)
        rec1_1=self.xoay_goc_x_do(rec1_1, 30)
        
        self.canvas.delete(*self.rec1_id) #Xóa đi hình trước vẽ
        self.rec1, self.rec1_id=self.draw_rectangle(rec1_1[0,0], rec1_1[0,1], rec1_1[1,0], rec1_1[1,1])

    def draw_2d_main(self):
        self.rec1, self.rec1_id=self.draw_rectangle(1,1,10,20)
        
        
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

    def put_pixel(self, x, y, color="green"):
        adjusted_x = self.width/2 + x*5
        adjusted_y = self.height/2 - y*5
        pixel_id=self.canvas.create_rectangle(adjusted_x-2, adjusted_y-2, adjusted_x+2, adjusted_y+2, fill=color, outline=None)
        return pixel_id

    def draw_line(self, x1, y1, x2, y2):
        arr=[]
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

    def draw_circle(self, x_center, y_center, radius):
        x = radius
        y = 0
        p = 1 - radius

        points = []

        while x >= y:
            points.extend([
                (x_center + x, y_center + y),
                (x_center - x, y_center + y),
                (x_center + x, y_center - y),
                (x_center - x, y_center - y),
                (x_center + y, y_center + x),
                (x_center - y, y_center + x),
                (x_center + y, y_center - x),
                (x_center - y, y_center - x)
            ])

            y += 1

            if p <= 0:
                p = p + 2*y + 1
            else:
                x -= 1
                p = p + 2*y - 2*x + 1

        for point in points:
            self.put_pixel(point[0], point[1])

    def draw_rectangle(self, x1, y1, x2, y2):
        
        arr=self.draw_line(x1, y1, x2, y1)
        arr.extend(self.draw_line(x2, y1, x2, y2))
        arr.extend(self.draw_line(x2, y2, x1, y2))
        arr.extend(self.draw_line(x1, y2, x1, y1))
        return np.array(([x1,y1,1], [x2,y2,1])), arr

    def draw_triangle(self, x1, y1, x2, y2, x3, y3):
        self.draw_line(x1, y1, x2, y2)
        self.draw_line(x2, y2, x3, y3)
        self.draw_line(x3, y3, x1, y1)

    def draw_isosceles_triangle(self, x1, y1, base, height):
        # Tính toán tọa độ của các đỉnh của tam giác cân
        x2 = x1 + base
        y2 = y1
        x3 = x1 + base / 2
        y3 = y1 + height

        # Vẽ các cạnh của tam giác
        self.draw_line(x1, y1, x2, y2)  # Cạnh đáy
        self.draw_line(x1, y1, x3, y3)  # Cạnh bên
        self.draw_line(x2, y2, x3, y3)  # Cạnh bên

    def draw_right_triangle(self, x1, y1, base, height):
        x2 = x1 + base
        y2 = y1
        x3 = x1
        y3 = y1 + height

        # Vẽ các cạnh của tam giác
        self.draw_line( x1, y1, x2, y2)  # Cạnh đáy
        self.draw_line(x2, y2, x3, y3)  # Cạnh kề
        self.draw_line(x3, y3, x1, y1)  # Cạnh huyền

    def draw_ellipse(self, x_center, y_center, a, b):
        # self.put_pixel()
        x = 0
        y = b
        # a2=a*a
        # b2=b*b
        fx=0
        fy=2*a*a*y

        self.put_pixel(x_center+x, y_center+y)
        self.put_pixel(x_center-x, y_center+y)
        self.put_pixel(x_center+x, y_center-y)
        self.put_pixel(x_center-x, y_center-y)

        p=b*b-a*a*b-a*a/4
        midb=round(m.pow(a,2)/m.sqrt(m.pow(a,2)+m.pow(b,2)))

        while fx<fy: #nửa đầu
            x+=1
            fx+=2*b*b
            if (p<0):
                p += b*b*(2*x+3)
            else:
                y -= 1
                p += b*b*(2*x+3)+a*a*(-2*y+2)
                fy -= 2*a*a
            self.put_pixel(x_center+x, y_center+y)
            self.put_pixel(x_center-x, y_center+y)
            self.put_pixel(x_center+x, y_center-y)
            self.put_pixel(x_center-x, y_center-y)

        while y>0:
            y -= 1
            fy -= 2*a*a
            if p >= 0:
                p += a*a*(3-2*y)
            else:
                x +=1
                fx += 2*b*b
                p += b*b*(2*x+2)+a*a*(-2*y+3)
            self.put_pixel(x_center+x, y_center+y)
            self.put_pixel(x_center-x, y_center+y)
            self.put_pixel(x_center+x, y_center-y)
            self.put_pixel(x_center-x, y_center-y)

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

    def clear_canvas(self):
        self.canvas.delete('all')
        self.create_grid_pixel()

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
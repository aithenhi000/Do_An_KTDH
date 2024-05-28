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

    def start_moving_2d(self):
        self.move_2d()
        
    def move_2d(self):
        '''
        self.rec1=self.tinh_tien(self.rec1, 5, 5)
        self.rec1=self.ti_le(*self.rec1, 1.2)
        self.rec1=self.xoay_goc_x_do(self.rec1, 30)
        
        self.canvas.delete(*self.rec1_id) #Xóa đi hình trước vẽ
        self.rec1, self.rec1_id=self.draw_rectangle(self.rec1[0,0], self.rec1[0,1], self.rec1[1,0], self.rec1[1,1])

        self.tria1=self.xoay_goc_x_do(self.tria1, 90)
        self.canvas.delete(*self.tria1_id)
        self.tria1, self.tria1_id=self.draw_triangle(self.tria1[0,0],self.tria1[0,1],self.tria1[1,0],self.tria1[1,1],self.tria1[2,0],self.tria1[2,1])
        '''
        self.tinh_tien_sailboat(1, 0)
        print(self.tria_body_left)
        print (self.tria_body_left_id)
        self.after(120, self.move_2d)
        
        
    def tinh_tien_sailboat(self, x, y):
        
        self.tria_body_left = self.tinh_tien(self.tria_body_left, x, y)
        self.canvas.delete(*self.tria_body_left_id) #Xóa đi hình trước vẽ
        self.tria_body_left , self.tria_body_left_id=self.draw_right_triangle(self.tria_body_left[0,0],self.tria_body_left[0,1],-10,-10)

        self.tria_body_right = self.tinh_tien(self.tria_body_right, x, y)
        self.canvas.delete(*self.tria_body_right_id) #Xóa đi hình trước vẽ
        self.tria_body_right , self.tria_body_right_id=self.draw_right_triangle(self.tria_body_right[0,0],self.tria_body_right[0,1],10,-10)
        
        self.tria_sail_left = self.tinh_tien(self.tria_sail_left, x, y)
        self.canvas.delete(*self.tria_sail_left_id) #Xóa đi hình trước vẽ
        self.tria_sail_left , self.tria_sail_left_id=self.draw_right_triangle(self.tria_sail_left[0,0],self.tria_sail_left[0,1],-10,20)
        
        self.tria_sail_right = self.tinh_tien(self.tria_sail_right, x, y)
        self.canvas.delete(*self.tria_sail_right_id) #Xóa đi hình trước vẽ
        self.tria_sail_right , self.tria_sail_right_id=self.draw_right_triangle(self.tria_sail_right[0,0],self.tria_sail_right[0,1],10,30)

        self.rec_body = self.tinh_tien(self.rec_body, x, y)
        self.canvas.delete(*self.rec_body_id) #Xóa đi hình trước vẽ
        self.rec_body , self.rec_body_id=self.draw_rectangle(self.rec_body[0,0],self.rec_body[0,1],self.rec_body[1,0], self.rec_body[1,1])

        self.rec_sail = self.tinh_tien(self.rec_sail, x, y)
        self.canvas.delete(*self.rec_sail_id) #Xóa đi hình trước vẽ
        self.rec_sail , self.rec_sail_id=self.draw_rectangle(self.rec_sail[0,0],self.rec_sail[0,1],self.rec_sail[1,0], self.rec_sail[1,1])
        print(x, y)

    def draw_sailboat(self, x0, y0):

        self.tria_body_left, self.tria_body_left_id = self.draw_right_triangle(x0, y0, -10, -10)
               
        self.tria_body_right, self.tria_body_right_id = self.draw_right_triangle(x0+30, y0, 10, -10)

        self.rec_body, self.rec_body_id = self.draw_rectangle (x0+30, y0, x0, y0-10)

        self.rec_sail, self.rec_sail_id = self.draw_rectangle (x0+14 ,y0+5,x0+16, y0)

        self.tria_sail_left, self.tria_sail_left_id = self.draw_right_triangle(x0+14, y0+5, x0+20, y0+50)
        self.tria_sail_right, self.tria_sail_right_id= self.draw_right_triangle(x0+16, y0+5, x0+40, y0+60)
        pass
##############bỏ
    def draw_sailboat_fill(self):
        #Điểm A(-30, -30)
        x_a = -30
        base_a = -10
        self.triangles_body_left = []  # Danh sách để lưu trữ các tam giác
        self.triangles_body_left_id = []  # Danh sách để lưu trữ các ID của tam giác

        #tria_body_left
        for value in range(x_a, -39, -1):
            self.triangle, self.triangle_id = self.draw_right_triangle(x_a, x_a, base_a, base_a)
            self.triangles_body_left.append(self.triangle)  # Thêm tam giác vào danh sách
            self.triangles_body_left_id.append(self.triangle_id)  # Thêm ID của tam giác vào danh sách
            base_a += 1
            
            if value == -38:
                break

        
        for i in range(len(self.triangles_body_left)):
            setattr(self, f"triangle_{i+1}", self.triangles_body_left[i])
            setattr(self, f"triangle_{i+1}_id", self.triangles_body_left_id[i])
        self.first_triangle = self.triangles_body_left[0]
        self.first_triangle_id = self.triangles_body_left_id[0]
        
        self.rec_body, self.rec_body = self.draw_rectangle (0, -30, -30, -40)

        self.rec_sail, self.rec_sail = self.draw_rectangle (-16 ,-25,-14, -30)

        self.tria_sail_left, self.tria_sail_left_id = self.draw_right_triangle(-16, -25, -10, 20)
        self.tria_sail_right, self.tria_sail_right_id= self.draw_right_triangle(-14, -25, 10, 30)
        pass
        
    def draw_2d_main(self):
        '''
        self.rec1, self.rec1_id = self.draw_rectangle(1, 1, 10, 20)
        self.tria1, self.tria1_id = self.draw_isosceles_triangle(50, 50, 30, 60)
        
        print(self.tria1)
        print(self.tria1_id)
        '''
        self.draw_sailboat(-30, -30)

        #self.pixel_id = self.put_pixel_stroke(x=70, y=70, width_stroke=3, f_color="red", o_color = "red")
        
##############################################################################
        
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
####3############
    def put_pixel_stroke(self, x, y, width_stroke, f_color="green", o_color = "green"):
        adjusted_x = self.width/2 + x*5
        adjusted_y = self.height/2 - y*5
        pixel_id = self.canvas.create_rectangle(adjusted_x-2, adjusted_y-2, adjusted_x+2, adjusted_y+2, fill=f_color, outline=o_color, width=width_stroke)
        return pixel_id

    def draw_line_stroke(self, x, y, x1, y1, x2, y2, f_color, o_color):
        arr = []
        x1 = round(x1)
        y1 = round(y1)
        x2 = round(x2)
        y2 = round(y2)
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        x, y = x1, y1
        x_step = 1 if x1 < x2 else -1
        y_step = 1 if y1 < y2 else -1
        f1 = 2 * (dy - dx)
        f2 = 2 * dy
        p = 2 * dy - dx
        if dx > dy:
            while x != x2:
                x += x_step
                if p < 0:
                    p += f2
                else:
                    p += f1
                    y += y_step
                arr.append(self.put_pixel_stroke(x, y, o_color))
        else:
            p = 2 * dx - dy
            f1 = 2 * (dx - dy)
            f2 = 2 * dx
            while y != y2:
                y += y_step
                if p < 0:
                    p += f2
                else:
                    p += f1
                    x += x_step
                arr.append(self.put_pixel_stroke(x, y, o_color))

        return arr

################################3
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
        arr=self.draw_line(x1, y1, x2, y2)
        arr.extend(self.draw_line(x2, y2, x3, y3))
        arr.extend(self.draw_line(x3, y3, x1, y1))
        return np.array(([x1,y1,1],[x2,y2,1],[x3,y3,1])), arr

    def draw_isosceles_triangle(self, x1, y1, base, height):
        # Tính toán tọa độ của các đỉnh của tam giác cân
        x2 = x1 + base
        y2 = y1
        x3 = x1 + base / 2
        y3 = y1 + height

        # Vẽ các cạnh của tam giác
        arr=self.draw_line(x1, y1, x2, y2)  # Cạnh đáy
        arr.extend(self.draw_line(x2, y2, x3, y3))  # Cạnh bên
        arr.extend(self.draw_line(x1, y1, x3, y3))  # Cạnh bên
        return np.array(([x1,y1,1],[x2,y2,1],[x3,y3,1])), arr

    def draw_right_triangle(self, x1, y1, base, height):
        x2 = x1 + base
        y2 = y1
        x3 = x1
        y3 = y1 + height

        # Vẽ các cạnh của tam giác
        pixel_ids = []
        arr=self.draw_line( x1, y1, x2, y2)  # Cạnh đáy
        arr.extend(self.draw_line(x2, y2, x3, y3))  # Cạnh kề
        arr.extend(self.draw_line(x3, y3, x1, y1))  # Cạnh huyền
        return np.array(([x1,y1,1],[x2,y2,1],[x3,y3,1])), arr#, pixel_ids
        
    def draw_ellipse(self, xc, yc, a, b):
        x = 0
        y = b

        # Decision parameter of region 1
        d1 = (b * b) - (a * a * b) + (0.25 * a * a)
        dx = 2 * b * b * x
        dy = 2 * a * a * y

        # For region 1
        while dx < dy:
            # Add the points corresponding to the 4 quadrants
            self.put_pixel(xc+x, yc+y)
            self.put_pixel(xc-x, yc+y)
            self.put_pixel(xc+x, yc-y)
            self.put_pixel(xc-x, yc-y)
            if d1 < 0:
                x += 1
                dx = dx + (2 * b * b)
                d1 = d1 + dx + (b * b)
            else:
                x += 1
                y -= 1
                dx = dx + (2 * b * b)
                dy = dy - (2 * a * a)
                d1 = d1 + dx - dy + (b * b)    

            # Decision parameter of region 2
        d2 = ((b * b) * ((x + 0.5) * (x + 0.5))) + ((a * a) * ((y - 1) * (y - 1))) - (a * a * b * b)

        # For region 2
        while y >= 0:
            # Add the points corresponding to the 4 quadrants
            self.put_pixel(xc+x, yc+y)
            self.put_pixel(xc-x, yc+y)
            self.put_pixel(xc+x, yc-y)
            self.put_pixel(xc-x, yc-y)

            if d2 > 0:
                y -= 1
                dy = dy - (2 * a * a)
                d2 = d2 + (a * a) - dy
            else:
                y -= 1
                x += 1
                dx = dx + (2 * b * b)
                dy = dy - (2 * a * a)
                d2 = d2 + dx - dy + (a * a)

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

from tkinter import *
import math as m
import numpy as np


class Graphics2D(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.font_famiy=("Courier",9)
        self.font_heading=("Courier",11, "bold")
        self.width=1200
        self.height=750
        self.grid_size = 5
        self.origin=(self.width//2, self.height//2)
        self.configure(padx=20, pady=20)
        self.create_canvas()
        self.create_grid_pixel()
        self.create_menu()
        self.create_info_panel()
        self.flag_axis=0
        

        ###
        self.moving_check = False
    
    def create_menu(self):
        self.btn_draw_2d = Button(
            self, text="VẼ CẢNH BIỂN 2D", bg='#FFC470', font=self.font_heading, command=self.draw_2d_main
        )
        self.btn_draw_2d.pack()
        self.btn_move_2d = Button(
            self, text="BẬT/TẮT CHUYỂN ĐỘNG",bg='#FFC470', font=self.font_heading, command=self.moving_button
        )
        self.btn_move_2d.pack()

        self.btn_grid = Button(
            self, text="BẬT/TẮT GRID PIXEL", bg='#FFC470', font=self.font_heading, command=self.create_axis
        )
        self.btn_grid.pack()

    def create_info_panel(self):
        self.fr=LabelFrame(self, text='THÔNG TIN VẬT THỂ DI CHUYỂN',borderwidth=2, relief="ridge", width=200, height=100)
        self.fr.pack()
    
    def moving_button(self):
        self.moving_check = not self.moving_check  # Đảo ngược trạng thái của moving_check
        if self.moving_check:
            self.move_2d()  # Nếu moving_check là True, bắt đầu di chuyển
        
    def move_2d(self):
        #self.moving_check = True
        #if self.moving_check:   #đặt flag moving_check kiểm tra xem có đang di chuyển không
        
        if self.moving_check:
            
            self.tinh_tien_sailboat(1, 0)
            #print(self.tria_body_left)
            #print (self.tria_body_left_id)
            self.after(120, self.move_2d)
        else:
            self.after_cancel(self.after(120, self.move_2d))
            
    def tinh_tien_sailboat(self, x, y):
        
        self.tria_body_left = self.tinh_tien(self.tria_body_left, x, y)
        self.canvas.delete(*self.tria_body_left_id) #Xóa đi hình trước vẽ
        self.canvas.delete(*self.tria_body_left_fill_id)
        self.tria_body_left, self.tria_body_left_id, self.tria_body_left_fill_id = self.draw_right_triangle(self.tria_body_left[0,0],self.tria_body_left[0,1],-10,-10, 'up', bool_canh_ke=0)
        
        self.tria_body_right = self.tinh_tien(self.tria_body_right, x, y)
        self.canvas.delete(*self.tria_body_right_id) #Xóa đi hình trước vẽ
        self.canvas.delete(*self.tria_body_right_fill_id)
        self.tria_body_right , self.tria_body_right_id, self.tria_body_right_fill_id=self.draw_right_triangle(self.tria_body_right[0,0],self.tria_body_right[0,1],10,-10, 'up', bool_canh_ke=0)
        
        self.tria_sail_left = self.tinh_tien(self.tria_sail_left, x, y)
        self.canvas.delete(*self.tria_sail_left_id) #Xóa đi hình trước vẽ
        self.canvas.delete(*self.tria_sail_left_fill_id)
        self.tria_sail_left , self.tria_sail_left_id, self.tria_sail_left_fill_id=self.draw_right_triangle(self.tria_sail_left[0,0],self.tria_sail_left[0,1],-10,20, 'down')
        
        self.tria_sail_right = self.tinh_tien(self.tria_sail_right, x, y)
        self.canvas.delete(*self.tria_sail_right_id) #Xóa đi hình trước vẽ
        self.canvas.delete(*self.tria_sail_right_fill_id)
        self.tria_sail_right , self.tria_sail_right_id, self.tria_sail_right_fill_id=self.draw_right_triangle(self.tria_sail_right[0,0],self.tria_sail_right[0,1],10,30, 'down')

        self.rec_body = self.tinh_tien(self.rec_body, x, y)
        self.canvas.delete(*self.rec_body_id) #Xóa đi hình trước vẽ
        self.canvas.delete(*self.rec_body_fill_id)
        self.rec_body , self.rec_body_id, self.rec_body_fill_id=self.draw_filled_rectangle(self.rec_body[0,0],self.rec_body[0,1],self.rec_body[1,0], self.rec_body[1,1], bool_left_right=0)

        self.rec_sail = self.tinh_tien(self.rec_sail, x, y)
        self.canvas.delete(*self.rec_sail_id) #Xóa đi hình trước vẽ
        self.rec_sail , self.rec_sail_id=self.draw_rectangle(self.rec_sail[0,0],self.rec_sail[0,1],self.rec_sail[1,0], self.rec_sail[1,1])
        #print(x, y)

    def draw_sailboat(self, x0, y0):
        self.tria_body_left, self.tria_body_left_id, self.tria_body_left_fill_id = self.draw_right_triangle(x0, y0, -10, -10, bool_canh_ke=0)
        self.tria_body_right, self.tria_body_right_id, self.tria_body_right_fill_id = self.draw_right_triangle(x0+30, y0, 10, -10, bool_canh_ke=0)
        self.rec_body, self.rec_body_id, self.rec_body_fill_id = self.draw_filled_rectangle (x0+30, y0, x0, y0-10, bool_left_right=0)
        
        self.rec_sail, self.rec_sail_id = self.draw_rectangle (x0+14 ,y0+5,x0+16, y0)
        self.tria_sail_left, self.tria_sail_left_id, self.tria_sail_left_fill_id = self.draw_right_triangle(x0+14, y0+5, -10, 20, fill_direction='down')
        self.tria_sail_right, self.tria_sail_right_id, self.tria_sail_right_fill_id = self.draw_right_triangle(x0+16, y0+5, 10, 30, fill_direction='down')
        pass
        
    def draw_2d_main(self):
        self.clear_canvas()
    
        self.draw_mountain(-110, 55)
        self.draw_sun(40, 60)
        self.draw_bird1(-100, 65)
        self.draw_bird2(-80, 55)
        self.draw_bird3(-35, 70)
        self.draw_sea(-120,0)
        self.draw_sailboat(-110, -40)
            
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
            
    def create_axis(self):
        canvas=self.canvas 
        if self.flag_axis==1:
            self.flag_axis-=1
            self.canvas.delete(*self.arr)
            
        else:
            self.flag_axis+=1
            self.arr=[]

            # X axis
            self.arr.append(canvas.create_line(0, self.origin[1], self.width, self.origin[1]))
            for x in range(0, self.width, 50):
                self.arr.append(canvas.create_rectangle(
                    x - 1, self.origin[1] - 1, x + 1, self.origin[1] + 1, fill="red"
                ))
                self.arr.append(canvas.create_text(
                    x,
                    self.origin[1] + 8,
                    text=str(int((x - self.width / 2) / 5)),
                    font=("Arial", 7),
                ))
            # Y axis
            self.arr.append(canvas.create_line(self.origin[0], 0, self.origin[0], self.height))
            for y in range(0, self.height, 50):
                self.arr.append(canvas.create_rectangle(
                    self.origin[0] - 1, y - 1, self.origin[0] + 1, y + 1, fill="red"
                ))
                self.arr.append(canvas.create_text(
                    self.origin[0] + 9,
                    y,
                    text=str(int(-(y - self.height / 2) / 5)),
                    font=("Arial", 7),
                ))
        
    def put_pixel(self, x, y, color="green", outline="black"):
        adjusted_x = self.width/2 + x*5
        adjusted_y = self.height/2 - y*5
        pixel_id=self.canvas.create_rectangle(adjusted_x-2, adjusted_y-2, adjusted_x+2, adjusted_y+2, fill=color, outline=outline)
        return pixel_id
    
    def draw_line(self, x1, y1, x2, y2, color="green"):
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
                arr.append(self.put_pixel(x,y, color))
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
      
    def draw_line_background(self, x1, y1, x2, y2, direction, draw_to, color='red'):
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
                    if direction=='right':
                        x_background=x+1
                        while(x_background<=draw_to-1):
                            arr_fill.append(self.put_pixel(x_background,y,color,color))
                            x_background+=1
                    elif direction=='left':
                        x_background=x+1
                        while(x_background<=draw_to+1):
                            arr_fill.append(self.put_pixel(x_background,y,color,color))
                            x_background-=1
                if direction=='up':
                        y_background=y+1
                        while(y_background<=draw_to-1):
                            arr_fill.append(self.put_pixel(x,y_background,color,color))
                            y_background+=1
                elif direction=='down':
                    y_background=y-1
                    while(y_background>=draw_to+1):
                        arr_fill.append(self.put_pixel(x,y_background,color,color))
                        y_background-=1
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
                            arr_fill.append(self.put_pixel(x,y_background,color,color))
                            y_background+=1
                    elif direction=='down':
                        y_background=y-1
                        while(y_background>=draw_to+1):
                            arr_fill.append(self.put_pixel(x,y_background,color,color))
                            y_background-=1
                if direction=='right':
                    x_background=x+1
                    while(x_background<=draw_to-1):
                        arr_fill.append(self.put_pixel(x_background,y,color,color))
                        x_background+=1
                elif direction=='left':
                    x_background=x+1
                    while(x_background<=draw_to+1):
                        arr_fill.append(self.put_pixel(x_background,y,color,color))
                        x_background-=1
                arr.append(self.put_pixel(x,y))
                    
        return arr, arr_fill
    
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

    def draw_rectangle(self, x1, y1, x2, y2, color="green"):

        arr=self.draw_line(x1, y1, x2, y1)
        arr.extend(self.draw_line(x2, y1, x2, y2, color))
        arr.extend(self.draw_line(x2, y2, x1, y2, color))
        arr.extend(self.draw_line(x1, y2, x1, y1, color))

        return np.array(([x1,y1,1], [x2,y2,1])), arr
    
    def draw_filled_rectangle(self, x1, y1, x2, y2, bool_left_right=1):
        arr, arr_fill=self.draw_line_background(x1, y1, x2, y1, 'down', y2)
        arr.extend(self.draw_line(x2, y2, x1, y2))        
        if bool_left_right==1:
            arr.extend(self.draw_line(x2, y1, x2, y2))
            arr.extend(self.draw_line(x1, y2, x1, y1))
        else:
            arr.append(self.put_pixel(x1,y1))
            arr.append(self.put_pixel(x1,y2))

        return np.array(([x1,y1,1], [x2,y2,1])), arr, arr_fill

    def draw_triangle(self, x1, y1, x2, y2, x3, y3, color="green"):
        arr=self.draw_line(x1, y1, x2, y2, color)
        arr.extend(self.draw_line(x2, y2, x3, y3, color))
        arr.extend(self.draw_line(x3, y3, x1, y1, color))
        return np.array(([x1,y1,1],[x2,y2,1],[x3,y3,1])), arr

    def draw_isosceles_triangle(self, x1, y1, base, height, color="green"):
        # Tính toán tọa độ của các đỉnh của tam giác cân
        x2 = x1 + base
        y2 = y1
        x3 = x1 + base / 2
        y3 = y1 + height

        # Vẽ các cạnh của tam giác
        arr=self.draw_line(x1, y1, x2, y2, color)  # Cạnh đáy
        arr.extend(self.draw_line(x2, y2, x3, y3, color))  # Cạnh bên
        arr.extend(self.draw_line(x1, y1, x3, y3, color))  # Cạnh bên
        return np.array(([x1,y1,1],[x2,y2,1],[x3,y3,1])), arr

    def draw_right_triangle(self, x1, y1, base, height, fill_direction='up', bool_canh_ke=1):
        x2 = x1 + base
        y2 = y1
        x3 = x1
        y3 = y1 + height

        arr, arr_fill=self.draw_line_background(x2, y2, x3, y3, fill_direction, y1)  # Cạnh huyền
        arr.extend(self.draw_line( x1, y1, x2, y2))  # Cạnh đáy
        if bool_canh_ke==1:
            arr.extend(self.draw_line(x3, y3, x1, y1))  # Cạnh kề
        else:
            arr.append(self.put_pixel(x1,y1))
            arr.append(self.put_pixel(x3,y3))
        return np.array(([x1,y1,1],[x2,y2,1],[x3,y3,1])), arr, arr_fill
        
    def draw_ellipse(self, xc, yc, a, b, color="green"):
        x = 0
        y = b

        # Decision parameter of region 1
        d1 = (b * b) - (a * a * b) + (0.25 * a * a)
        dx = 2 * b * b * x
        dy = 2 * a * a * y

        arr=[]
        # For region 1
        while dx < dy:
            # Add the points corresponding to the 4 quadrants
            arr.append(self.put_pixel(xc+x, yc+y, color))
            arr.append(self.put_pixel(xc-x, yc+y, color))
            arr.append(self.put_pixel(xc+x, yc-y, color))
            arr.append(self.put_pixel(xc-x, yc-y, color))
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
            arr.append(self.put_pixel(xc+x, yc+y, color))
            arr.append(self.put_pixel(xc-x, yc+y, color))
            arr.append(self.put_pixel(xc+x, yc-y, color))
            arr.append(self.put_pixel(xc-x, yc-y, color))

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
        return np.array(([xc,yc,1])), a, b, arr

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

    def draw_mountain(self, x0, y0):
        truc_x = 0
        self.draw_line_background(x0, y0, -100, 35, 'down', truc_x, color='green')
        # self.draw_line(x0, y0, -100, 35)
        self.draw_line_background(-100, 35, -60, 45, 'down', truc_x, color='green')
        # self.draw_line(-100, 35, -60, 45)
        self.draw_line_background(-120, 35, -110, 55, 'down', truc_x, color='green')
        # self.draw_line(-120, 35, -110, 55)
        self.draw_line_background(-60, 45, -10, 25, 'down', truc_x, color='green')
        # self.draw_line(-60, 45, -10, 25)
        self.draw_line_background(-10, 25, 30, 42, 'down', truc_x, color='green')
        # self.draw_line(-10, 25, 30, 42)
        self.draw_line_background(30, 42, 70, 25, 'down', truc_x, color='green')
        # self.draw_line(30, 42, 70, 25)
        self.draw_line_background(70, 25, 120, 68, 'down', truc_x, color='green')
        # self.draw_line(70, 25, 120, 68)

    def draw_sun(self, x0, y0):
        self.draw_circle(x0, y0, 10)
        self.draw_line(40, 71, 40, 73)
        self.draw_line(51, 60, 53, 60)
        self.draw_line(40, 48, 40, 46)
        self.draw_line(29, 60, 27, 60)
        self.draw_line(32, 67, 30, 69)
        self.draw_line(48, 67, 50, 69)
        self.draw_line(48, 50, 50, 48)
        self.draw_line(32, 50, 30, 48)

    def draw_bird1(self, x0, y0):
        self.draw_ellipse(x0, y0, 1, 0)
        self.draw_ellipse(-99, 65, 1, 0)
        self.draw_ellipse(-98, 64, 1, 0)
        self.draw_ellipse(-97, 65, 1, 0)
        self.draw_ellipse(-96, 65, 1, 0)
        self.draw_ellipse(-101, 64, 1, 0)
        self.draw_ellipse(-95, 64, 1, 0)
        self.draw_ellipse(-98, 63, 1, 0)
        self.draw_ellipse(-102, 63, 1, 0)
        self.draw_ellipse(-94, 63, 1, 0)

    def draw_bird2(self, x0, y0):
        self.draw_ellipse(x0, y0, 1, 0)
        self.draw_ellipse(-99 + 20, 65 - 10, 1, 0)
        self.draw_ellipse(-98 + 20, 64 - 10, 1, 0)
        self.draw_ellipse(-97 + 20, 65 - 10, 1, 0)
        self.draw_ellipse(-96 + 20, 65 - 10, 1, 0)
        self.draw_ellipse(-101 + 20, 64 - 10, 1, 0)
        self.draw_ellipse(-95 + 20, 64 - 10, 1, 0)
        self.draw_ellipse(-98 + 20, 63 - 10, 1, 0)
        self.draw_ellipse(-102 + 20, 63 - 10, 1, 0)
        self.draw_ellipse(-94 + 20, 63 - 10, 1, 0)

    def draw_bird3(self, x0, y0):
        self.draw_ellipse(x0, y0, 1, 0)
        self.draw_ellipse(-99 + 65, 65 + 5, 1, 0)
        self.draw_ellipse(-98 + 65, 64 + 5, 1, 0)
        self.draw_ellipse(-97 + 65, 65 + 5, 1, 0)
        self.draw_ellipse(-96 + 65, 65 + 5, 1, 0)
        self.draw_ellipse(-101 + 65, 64 + 5, 1, 0)
        self.draw_ellipse(-95 + 65, 64 + 5, 1, 0)
        self.draw_ellipse(-98 + 65, 63 + 5, 1, 0)
        self.draw_ellipse(-102 + 65, 63 + 5, 1, 0)
        self.draw_ellipse(-94 + 65, 63 + 5, 1, 0)
   
    def draw_sea(self, x0, y0):
        bottom_screen = -70
        self.draw_line_background(x0,y0,120,0,direction='down',draw_to=bottom_screen, color='light blue')

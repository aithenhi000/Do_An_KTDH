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
        self.count=1

        ###
        self.moving_check = False
    
    def create_menu(self):
        self.btn_draw_2d = Button(
            self, text="VẼ CẢNH BIỂN 2D", bg='#FFC470', width=300, font=self.font_heading, command=self.draw_2d_main
            
        )
        self.btn_draw_2d.pack(padx=5, pady=5)
        self.btn_move_2d = Button(
            self, text="BẬT/TẮT CHUYỂN ĐỘNG",bg='#FFC470', width=300, font=self.font_heading, command=self.moving_button
        )
        self.btn_move_2d.pack(padx=5, pady=5)

        self.btn_grid = Button(
            self, text="BẬT/TẮT GRID PIXEL", width=300, bg='#FFC470', font=self.font_heading, command=self.create_axis
        )
        self.btn_grid.pack(padx=5, pady=5)

    def create_info_panel(self):
        self.fr=LabelFrame(self, text='THÔNG TIN VẬT THỂ DI CHUYỂN',borderwidth=2, relief="groove", width=400, height=400, font=("Courier", 12, "bold"))
        self.fr.pack(padx=5, pady=5, expand=True,fill="both")
            
        self.label_1 = Label(self.fr, text="Thuyền buồm (Mũi thuyền): (0, 0)", anchor='w')
        self.label_2 = Label(self.fr, text="Thuyền buồm (Điểm cuối): (0, 0)", anchor='w')
        self.label_3 = Label(self.fr, text="Thuyền buồm (Đỉnh buồm): (0, 0)", anchor='w')
        self.label_4 = Label(self.fr, text="Thuyền buồm (Đáy thuyền): (0, 0)", anchor='w')
        self.label_5 = Label(self.fr, text="Đám mây (Đầu): (0, 0)", anchor='w')
        self.label_6 = Label(self.fr, text="Đám mây (Cuối): (0, 0)", anchor='w')
        
        self.label_1.pack(fill='x')
        self.label_2.pack(fill='x')
        self.label_3.pack(fill='x')
        self.label_4.pack(fill='x')
        self.label_5.pack(fill='x')
        self.label_6.pack(fill='x')
        
    def moving_button(self):

        self.moving_check = not self.moving_check  # Đảo ngược trạng thái của moving_check
        if self.moving_check:
            self.move_2d()  # Nếu moving_check là True, bắt đầu di chuyển
     
    def move_2d(self):   
        self.count+=1
        if self.moving_check:
            
            if (self.count%7)== 0 or (self.count%7)==1:
                self.DoiXung_cloud([1,-1], color="#CAF4FF")
                self.tinh_tien_sailboat(1, 0)

            elif (self.count%7)==2 or (self.count%7)==3:

                self.DoiXung_cloud([-1,1], color="#CAF4FF")                
                self.tinh_tien_sailboat(1, 1)

            else:
                self.tinh_tien_sailboat(1, -1)
            self.label_1.config(text=f"Thuyền buồm (Mũi thuyền): {self.tria_body_right[1,0],self.tria_body_right[1,1]}")
            self.label_2.config(text=f"Thuyền buồm (Điểm cuối): {self.tria_body_left[1,0],self.tria_body_left[1,1]}")
            self.label_3.config(text=f"Thuyền buồm (Đỉnh buồm): {self.tria_sail_right[1,0],self.tria_sail_right[1,1]}")
            self.label_4.config(text=f"Thuyền buồm (Đáy thuyền): {round(self.rec_body[1,0]/2),self.rec_body[1,1]}")
            self.label_5.config(text=f"Đám mây (Đầu): {self.cloud_1[0], self.cloud_1[1]}")
            self.label_6.config(text=f"Đám mây (Cuối): {self.cloud_4[0], self.cloud_4[1]}")
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
        return x,y

    def rotate_sun_halo(self, andgle=10):
        pass    
        

    def draw_sailboat(self, x0, y0):
        self.tria_body_left, self.tria_body_left_id, self.tria_body_left_fill_id = self.draw_right_triangle(x0, y0, -10, -10, bool_canh_ke=0)
        self.tria_body_right, self.tria_body_right_id, self.tria_body_right_fill_id = self.draw_right_triangle(x0+30, y0, 10, -10, bool_canh_ke=0)
        print(self.tria_body_right)
        self.rec_body, self.rec_body_id, self.rec_body_fill_id = self.draw_filled_rectangle (x0+30, y0, x0, y0-10, bool_left_right=0)
        
        self.rec_sail, self.rec_sail_id = self.draw_rectangle (x0+14 ,y0+5,x0+16, y0)
        self.tria_sail_left, self.tria_sail_left_id, self.tria_sail_left_fill_id = self.draw_right_triangle(x0+14, y0+5, -10, 20, fill_direction='down')
        self.tria_sail_right, self.tria_sail_right_id, self.tria_sail_right_fill_id = self.draw_right_triangle(x0+16, y0+5, 10, 30, fill_direction='down')
        return x0, y0
        
    # HAM VE CAC VAT THE CHINH
    def draw_2d_main(self):
        self.clear_canvas()
        self.draw_sun(0, 0)
        self.draw_mountain(-110, 55)
        self.draw_bird1(-100, 65, fill='black')
        self.draw_bird2(-80, 55, fill='black')
        self.draw_bird3(-35, 70, fill='black')
        self.draw_sea(-120, 0, 120, -70)
        self.draw_cloud(-60, 25)
        self.draw_sailboat(-110, -20)
        
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
    
    def draw_line(self, x1, y1, x2, y2, color="green", outline='black'):
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
                arr.append(self.put_pixel(x,y, color=color, outline=outline))
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
                arr.append(self.put_pixel(x,y, color=color, outline=outline))
        return arr
      
    def draw_line_background(self, x1, y1, x2, y2, direction, draw_to, color='green', outline='black', fill='red'):
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
                            arr_fill.append(self.put_pixel(x_background,y,color=fill, outline=fill))
                            x_background+=1
                    elif direction=='left':
                        x_background=x-1
                        while(x_background>=draw_to+1):
                            arr_fill.append(self.put_pixel(x_background,y,color=fill, outline=fill))
                            x_background-=1
                if direction=='up':
                        y_background=y+1
                        while(y_background<=draw_to-1):
                            arr_fill.append(self.put_pixel(x,y_background,color=fill, outline=fill))
                            y_background+=1
                elif direction=='down':
                    y_background=y-1
                    while(y_background>=draw_to+1):
                        arr_fill.append(self.put_pixel(x,y_background,color=fill, outline=fill))
                        y_background-=1
                arr.append(self.put_pixel(x,y, color=color, outline=outline))
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
                            arr_fill.append(self.put_pixel(x,y_background,color=fill, outline=fill))
                            y_background+=1
                    elif direction=='down':
                        y_background=y-1
                        while(y_background>=draw_to+1):
                            arr_fill.append(self.put_pixel(x,y_background,color=fill, outline=fill))
                            y_background-=1
                if direction=='right':
                    x_background=x+1
                    while(x_background<=draw_to-1):
                        arr_fill.append(self.put_pixel(x_background,y,color=fill, outline=fill))
                        x_background+=1
                elif direction=='left':
                    x_background=x-1
                    while(x_background>=draw_to+1):
                        arr_fill.append(self.put_pixel(x_background,y,color=fill, outline=fill))
                        x_background-=1
                arr.append(self.put_pixel(x,y, color=color, outline=outline))
                    
        return arr, arr_fill
    
    def draw_1_line_background(self, x0, y0, direction, draw_to, color='red'):
        arr_fill=[]
        x=round(x0)
        y=round(y0)
        
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
        elif direction=='right':
            x_background=x+1
            while(x_background<=draw_to-1):
                arr_fill.append(self.put_pixel(x_background,y,color,color))
                x_background+=1
        elif direction=='left':
            x_background=x-1
            while(x_background>=draw_to+1):
                arr_fill.append(self.put_pixel(x_background,y,color,color))
                x_background-=1
                
        return arr_fill
 
    def draw_circle(self, x_center, y_center, radius, bool_upper='yes', bool_bottom='yes'):
        x = radius
        y = 0
        p = 1 - radius

        arr = []
        arr_fill = []

        while x >= y:
            if bool_upper=='yes':
                arr.append(self.put_pixel(x_center + y, y_center + x))
                arr_fill.extend(self.draw_1_line_background(x_center + y, y_center + x, 'down', y_center))
                arr.append(self.put_pixel(x_center + x, y_center + y))
                arr_fill.extend(self.draw_1_line_background(x_center + x, y_center + y, 'left', x_center))
                arr.append(self.put_pixel(x_center - y, y_center + x))
                arr_fill.extend(self.draw_1_line_background(x_center - x, y_center + y, 'right', x_center))
                arr.append(self.put_pixel(x_center - x, y_center - y))
                arr_fill.extend(self.draw_1_line_background(x_center - y, y_center + x, 'down', y_center))              
                
            if bool_bottom=='yes':
                arr.append(self.put_pixel(x_center + x, y_center - y))
                arr_fill.extend(self.draw_1_line_background(x_center + x, y_center - y, 'left', x_center))
                arr.append(self.put_pixel(x_center + y, y_center - x))
                arr_fill.extend(self.draw_1_line_background(x_center + y, y_center - x, 'up', y_center))
                arr.append(self.put_pixel(x_center - y, y_center - x))
                arr_fill.extend(self.draw_1_line_background(x_center - y, y_center - x, 'up', y_center))
                arr.append(self.put_pixel(x_center - x, y_center + y))
                arr_fill.extend(self.draw_1_line_background(x_center - x, y_center - y, 'right', x_center))  

            y += 1
            if p <= 0:
                p = p + 2*y + 1
            else:
                x -= 1
                p = p + 2*y - 2*x + 1
            
        return np.array(([x_center, y_center, 1])), arr, arr_fill

    def draw_dashed_circle(self, x_center, y_center, radius, dash_length):
        x = radius
        y = 0
        p = 1 - radius

        arr = []

        count = 0
        draw = True

        while x >= y:
            if draw:
                arr.append(self.put_pixel(x_center + y, y_center + x))
                arr.append(self.put_pixel(x_center + x, y_center + y))
                arr.append(self.put_pixel(x_center + x, y_center - y))
                arr.append(self.put_pixel(x_center + y, y_center - x))
                
                arr.append(self.put_pixel(x_center - y, y_center - x))
                arr.append(self.put_pixel(x_center - x, y_center + y))
                arr.append(self.put_pixel(x_center - y, y_center + x))
                arr.append(self.put_pixel(x_center - x, y_center - y))
            
            count += 1
            if count == dash_length:
                count = 0
                draw = not draw

            y += 1
            if p <= 0:
                p = p + 2 * y + 1
            else:
                x -= 1
                p = p + 2 * y - 2 * x + 1
            
        return np.array(([x_center, y_center, 1])), arr

    def draw_filled_circle(self, x_center, y_center, radius, color='black'):
        x = radius
        y = 0
        p = 1 - radius
        arr = []
        
        while x >= y:
            arr.append(self.put_pixel(x_center + x, y_center + y))
            arr.append(self.put_pixel(x_center - x, y_center + y))
            arr.append(self.put_pixel(x_center + x, y_center - y))
            arr.append(self.put_pixel(x_center - x, y_center - y))

            y += 1
            if p <= 0:
                p = p + 2*y + 1
            else:
                x -= 1
                p = p + 2*y - 2*x + 1
            
        return np.array(([x_center, y_center, radius])), arr

    def draw_rectangle(self, x1, y1, x2, y2, color="green"):

        arr=self.draw_line(x1, y1, x2, y1)
        arr.extend(self.draw_line(x2, y1, x2, y2, color))
        arr.extend(self.draw_line(x2, y2, x1, y2, color))
        arr.extend(self.draw_line(x1, y2, x1, y1, color))

        return np.array(([x1,y1,1], [x2,y2,1])), arr
    
    def draw_filled_rectangle(self, x1, y1, x2, y2, bool_left_right=1, color='green', outline='black', fill='red'):
        
        if y1<y2:
            arr, arr_fill=self.draw_line_background(x1, y1, x2, y1, 'up', y2, color=color, fill=fill, outline=outline)
        else:
            arr, arr_fill=self.draw_line_background(x1, y1, x2, y1, 'down', y2, color=color, fill=fill, outline=outline)
        
        arr.extend(self.draw_line(x2, y2, x1, y2, color=color, outline=outline))        
        if bool_left_right==1:
            arr.extend(self.draw_line(x2, y1, x2, y2, color=color, outline=outline))
            arr.extend(self.draw_line(x1, y2, x1, y1, color=color, outline=outline))
        else:
            arr.append(self.put_pixel(x1, y1, color=color, outline=outline))
            arr.append(self.put_pixel(x1, y2, color=color, outline=outline))

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
        
    def draw_ellipse(self, xc, yc, a, b, color='black', outline='black', fill='black'):
        x = 0
        y = b

        d1 = (b * b) - (a * a * b) + (0.25 * a * a)
        dx = 2 * b * b * x
        dy = 2 * a * a * y

        arr=[]
        arr_fill=[]
        
        while dx < dy:
            arr_fill.extend(self.draw_1_line_background(xc+x, yc+y, 'down', yc, color=fill))
            arr_fill.extend(self.draw_1_line_background(xc-x, yc+y, 'down', yc, color=fill))
            arr_fill.extend(self.draw_1_line_background(xc+x, yc-y, 'up', yc, color=fill))
            arr_fill.extend(self.draw_1_line_background(xc-x, yc-y, 'up', yc, color=fill))

            arr.append(self.put_pixel(xc+x, yc+y, color=color, outline=outline))
            arr.append(self.put_pixel(xc-x, yc+y, color=color, outline=outline))
            arr.append(self.put_pixel(xc+x, yc-y, color=color, outline=outline))
            arr.append(self.put_pixel(xc-x, yc-y, color=color, outline=outline))
            
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

        d2 = ((b * b) * ((x + 0.5) * (x + 0.5))) + ((a * a) * ((y - 1) * (y - 1))) - (a * a * b * b)

        while y >= 0:
            arr_fill.extend(self.draw_1_line_background(xc+x, yc+y, 'left', xc, color=fill))
            arr_fill.extend(self.draw_1_line_background(xc-x, yc+y, 'right', xc, color=fill))
            arr_fill.extend(self.draw_1_line_background(xc+x, yc-y, 'left', xc, color=fill))
            arr_fill.extend(self.draw_1_line_background(xc-x, yc-y, 'right', xc, color=fill))

            arr.append(self.put_pixel(xc+x, yc+y, color=color, outline=outline))
            arr.append(self.put_pixel(xc-x, yc+y, color=color, outline=outline))
            arr.append(self.put_pixel(xc+x, yc-y, color=color, outline=outline))
            arr.append(self.put_pixel(xc-x, yc-y, color=color, outline=outline))
            arr_fill.append(self.put_pixel(xc,yc,color=color, outline=color))
            
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
        return np.array(([xc,yc,1])), arr, arr_fill

    def tinh_tien(self, pos, delta_x, delta_y):

        mul_matrix = np.array(([1, 0, 0], [0, 1, 0], [delta_x, delta_y, 1]))
        if pos.ndim==1:
            pos=np.matmul(pos, mul_matrix)
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
        fill='green'
        self.draw_line_background(x0, y0, -100, 35, 'down', truc_x, color='green', fill=fill)
        # self.draw_line(x0, y0, -100, 35)
        self.draw_line_background(-100, 35, -60, 45, 'down', truc_x, color='green', fill=fill)
        # self.draw_line(-100, 35, -60, 45)
        self.draw_line_background(-120, 35, -110, 55, 'down', truc_x, color='green', fill=fill)
        # self.draw_line(-120, 35, -110, 55)
        self.draw_line_background(-60, 45, -10, 25, 'down', truc_x, color='green', fill=fill)
        # self.draw_line(-60, 45, -10, 25)
        self.draw_line_background(-10, 25, 30, 42, 'down', truc_x, color='green', fill=fill)
        # self.draw_line(-10, 25, 30, 42)
        self.draw_line_background(30, 42, 70, 25, 'down', truc_x, color='green', fill=fill)
        # self.draw_line(30, 42, 70, 25)
        self.draw_line_background(70, 25, 120, 68, 'down', truc_x, color='green', fill=fill)
        # self.draw_line(70, 25, 120, 68)

    def draw_sun(self, x0, y0):
        self.sun_1, self.sun_1_id, self.sun_1_id_fill = self.draw_circle(x0, y0, 50, bool_upper='yes', bool_bottom='no')
        self.sun_2, self.sun_2_id = self.draw_dashed_circle(x0, y0, 80, 5)

    def draw_bird1(self, x0, y0, color='black', outline='black', fill='black'):
        self.draw_ellipse(x0, y0, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-99, 65, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-98, 64, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-97, 65, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-96, 65, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-101, 64, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-95, 64, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-98, 63, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-102, 63, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-94, 63, 1, 0, color=color, outline=outline, fill=fill)

    def draw_bird2(self, x0, y0, color='black', outline='black', fill='black'):
        self.draw_ellipse(x0, y0, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-99 + 20, 65 - 10, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-98 + 20, 64 - 10, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-97 + 20, 65 - 10, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-96 + 20, 65 - 10, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-101 + 20, 64 - 10, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-95 + 20, 64 - 10, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-98 + 20, 63 - 10, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-102 + 20, 63 - 10, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-94 + 20, 63 - 10, 1, 0, color=color, outline=outline, fill=fill)

    def draw_bird3(self, x0, y0, color='black', outline='black', fill='black'):
        self.draw_ellipse(x0, y0, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-99 + 65, 65 + 5, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-98 + 65, 64 + 5, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-97 + 65, 65 + 5, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-96 + 65, 65 + 5, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-101 + 65, 64 + 5, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-95 + 65, 64 + 5, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-98 + 65, 63 + 5, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-102 + 65, 63 + 5, 1, 0, color=color, outline=outline, fill=fill)
        self.draw_ellipse(-94 + 65, 63 + 5, 1, 0, color=color, outline=outline, fill=fill)
   
    def draw_sea(self, x1, y1, x2, y2):
        x1,y1=self.adjust_to_screen(x1,y1)
        x2,y2=self.adjust_to_screen(x2,y2)
        self.canvas.create_rectangle(x1+2.5, y1, x2+0.5, y2, fill='blue', outline='blue')
        self.draw_line(-120,0,120,0)
 
    def doi_xung(self, pos, choice):
        mul_matrix = np.array(( [-choice[1], 0,          0],
                                [0,         -choice[0],  0],
                                [0,          0,          1]))
        
        if pos.ndim == 1:
            pos = np.matmul(pos, mul_matrix)
        else:
            for x in range(0,pos.shape[0]):        
                pos[x]=np.matmul(pos[x],mul_matrix)
        
        return pos
 
    def ti_le(self, pos, ratio):
    
        mul_matrix = np.array(( [ratio, 0,      0],
                                [0,     ratio,  0],
                                [0,     0,      1]))
        if pos.ndim == 1:
            pos = np.matmul(pos, mul_matrix)
        else :
            for x in range(0,pos.shape[0]):        
                pos[x]=np.matmul(pos[x],mul_matrix)
            
        return pos

    def DoiXung_cloud(self, choice, color="white"):
        # self.cloud_1=self.ti_le(self.cloud_1, 1.4)
        # self.cloud_2=self.ti_le(self.cloud_2, 1.4)
        # self.cloud_3=self.ti_le(self.cloud_3, 1.4)
        # self.cloud_4=self.ti_le(self.cloud_4, 1.4)
        # self.cloud_5=self.ti_le(self.cloud_5, 1.4)
        self.cloud_1=self.doi_xung(self.cloud_1, choice)
        self.cloud_2=self.doi_xung(self.cloud_2, choice)
        self.cloud_3=self.doi_xung(self.cloud_3, choice)
        self.cloud_4=self.doi_xung(self.cloud_4, choice)
        self.cloud_5=self.doi_xung(self.cloud_5, choice)
        
        self.canvas.delete(*self.cloud_1_id)
        self.canvas.delete(*self.cloud_2_id)
        self.canvas.delete(*self.cloud_3_id)
        self.canvas.delete(*self.cloud_4_id)
        self.canvas.delete(*self.cloud_5_id)
        self.canvas.delete(*self.cloud_1_id_fill)
        self.canvas.delete(*self.cloud_2_id_fill)
        self.canvas.delete(*self.cloud_3_id_fill)
        self.canvas.delete(*self.cloud_4_id_fill)
        self.canvas.delete(*self.cloud_5_id_fill)
        
        self.cloud_1, self.cloud_1_id, self.cloud_1_id_fill=self.draw_ellipse(self.cloud_1[0], self.cloud_1[1], 5, 5, color=color, outline=color, fill=color)
        self.cloud_2, self.cloud_2_id, self.cloud_2_id_fill=self.draw_ellipse(self.cloud_2[0], self.cloud_2[1], 5, 5, color=color, outline=color, fill=color)
        self.cloud_3, self.cloud_3_id, self.cloud_3_id_fill=self.draw_ellipse(self.cloud_3[0], self.cloud_3[1], 5, 5, color=color, outline=color, fill=color)
        self.cloud_4, self.cloud_4_id, self.cloud_4_id_fill=self.draw_ellipse(self.cloud_4[0], self.cloud_4[1], 5, 5, color=color, outline=color, fill=color)
        self.cloud_5, self.cloud_5_id, self.cloud_5_id_fill=self.draw_filled_rectangle(self.cloud_5[0,0],self.cloud_5[0,1],self.cloud_5[1,0],self.cloud_5[1,1], color=color, outline=color, fill=color)
    
    def draw_cloud(self, x, y):  
        arr=[]
        self.cloud_1, self.cloud_1_id, self.cloud_1_id_fill=self.draw_ellipse(x, y-5, 5, 5, color='white', outline='white', fill='white')       
        self.cloud_2, self.cloud_2_id, self.cloud_2_id_fill=self.draw_ellipse(x+15, y, 6, 6, color='white', outline='white', fill='white')
        self.cloud_3, self.cloud_3_id, self.cloud_3_id_fill=self.draw_ellipse(x + 8, y, 8, 8, color='white', outline='white', fill='white')
        self.cloud_4, self.cloud_4_id, self.cloud_4_id_fill=self.draw_ellipse(x+20, y -5, 5, 5, color='white', outline='white', fill='white')
        #self.draw_ellipse(x + 20, y + 10, 8, 4, color='white', outline='white', fill='white')
        
        self.cloud_5, self.cloud_5_id, self.cloud_5_id_fill=self.draw_filled_rectangle(x,y,x+20,y-10, color='white', outline='white', fill='white')

    

###########

    def adjust_to_screen(self, x, y):
        adjusted_x = self.width/2 + x*5
        adjusted_y = self.height/2 - y*5
        return adjusted_x, adjusted_y
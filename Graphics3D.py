from tkinter import *
from Graphics2D import Graphics2D
from math import cos, sin, radians, sqrt, pow, tan

class Graphics3D(Frame):
    def __init__(self, master, width, height):
        super().__init__(master)
        self.master=master
        self.width=width
        self.height=height
        self.width_canvas=1050
        self.height_canvas=750
        self.font_famiy=("Courier",9)
        self.font_heading=("Courier",11, "bold")
        self.grid_size = 5
        self.origin=(self.width_canvas//4, self.height_canvas//2)
        
        self.create_frame_of_canvas()
        self.create_frame_of_panel()
        self.create_canvas()
        self.create_grid_pixel_3D()
        self.create_panel()
        
        
    def create_frame_of_panel(self):
        self.frame_panel=Frame(self, width=500, height=self.height)
        self.frame_panel.pack(side=RIGHT)
    
        
    def create_panel(self):
        self.create_box_menu()
        self.create_cylinder_menu()
        self.btn_clear=Button(self.frame_panel, text="CLEAR ALL", font=self.font_heading, command=self.clear_canvas)
        self.btn_clear.pack()
        
    def create_box_menu(self):
        self.lbf_box=LabelFrame(self.frame_panel, text="Vẽ hình hộp chữ nhật",width=500, font=self.font_heading, relief="groove")
        self.lbf_box.pack(padx=5, pady=5, fill="both")
        self.lbf_box.columnconfigure(1, minsize=20) 
        lb_name_box=['Chiều Dài', 'Chiều Rộng', 'Chiều Cao', 'Góc tọa độ x', 'y', 'z']
        for i, lb in enumerate(lb_name_box):
            label=Label(self.lbf_box, text=f"{lb}:", font=self.font_famiy)
            label.grid(row=i, column=0, padx=5, pady=5, sticky=E)
            
        w_box=Entry(self.lbf_box)
        h_box=Entry(self.lbf_box)
        d_box=Entry(self.lbf_box)
        ox_box=Entry(self.lbf_box)
        oy_box=Entry(self.lbf_box)
        oz_box=Entry(self.lbf_box)
        w_box.grid(column=1, row=0)
        h_box.grid(column=1, row=1)
        d_box.grid(column=1, row=2)
        ox_box.grid(column=1, row=3)
        oy_box.grid(column=1, row=4)
        oz_box.grid(column=1, row=5)
        w_box.insert(0, "60")
        h_box.insert(0, "60")
        d_box.insert(0, "60")
        oy_box.insert(0, "0")
        ox_box.insert(0, "0")
        oz_box.insert(0, "0")        
        self.btn_box = Button(
            self.lbf_box,
            text="Vẽ HHCN",
            font=self.font_famiy,
            bg="grey",
            command=lambda: self.draw_rectangular(
                int(ox_box.get()),
                int(oy_box.get()),
                int(oz_box.get()),
                int(w_box.get()),
                int(h_box.get()),               
                int(d_box.get()),            
                )
        )
        self.btn_box.grid(column=1, row=6, sticky=(E, W))
        
    def create_cylinder_menu(self):
        self.lbf_cylinder=LabelFrame(self.frame_panel, text="Vẽ hình trụ",width=500, font=self.font_heading, relief="groove")
        self.lbf_cylinder.pack(padx=5, pady=5, fill="both")
        self.lbf_cylinder.columnconfigure(1, minsize=20) 
        lb_name_cylinder=['Bán kính', 'Chiều cao', 'Tọa độ đáy x', 'y', 'z']
        for i, lb in enumerate(lb_name_cylinder):
            label=Label(self.lbf_cylinder, text=f"{lb}:", font=self.font_famiy)
            label.grid(row=i, column=0, padx=5, pady=5, sticky=E)
            
        r_cylinder=Entry(self.lbf_cylinder)
        h_cylinder=Entry(self.lbf_cylinder)
        ox_cylinder=Entry(self.lbf_cylinder)
        oy_cylinder=Entry(self.lbf_cylinder)
        oz_cylinder=Entry(self.lbf_cylinder)
        r_cylinder.grid(column=1, row=0)
        h_cylinder.grid(column=1, row=1)
        ox_cylinder.grid(column=1, row=2)
        oy_cylinder.grid(column=1, row=3)
        oz_cylinder.grid(column=1, row=4)
        r_cylinder.insert(0, "60")
        h_cylinder.insert(0, "60")
        ox_cylinder.insert(0, "60")
        oy_cylinder.insert(0, "0")
        oz_cylinder.insert(0, "60")
        self.btn_cylinder = Button(
            self.lbf_cylinder,
            text="Vẽ hình trụ",
            font=self.font_famiy,
            bg="grey",
            command=lambda: self.draw_cylinder(
                int(ox_cylinder.get()),
                int(oy_cylinder.get()),
                int(oz_cylinder.get()),
                int(r_cylinder.get()),               
                int(h_cylinder.get()),            
                )
        )
        
        self.btn_cylinder.grid(column=1, row=6, sticky=(E, W))        



        
    def clear_canvas(self):
        for widget in self.frame_canvas.winfo_children():
            widget.pack_forget()
        self.create_canvas()
        self.create_grid_pixel_3D()

    def create_frame_of_canvas(self):
        self.frame_canvas=Frame(self, width=1050, height=750)
        self.frame_canvas.pack(side=LEFT)

    def create_canvas(self):
        canvas = Canvas(self.frame_canvas, width=1050, height=750, bg="#FEFAF6")
        self.canvas=canvas
        self.canvas.pack()

    def create_grid_pixel_3D(self):
        canvas=self.canvas

        # draw grids
        for x in range(0, self.width_canvas, self.grid_size):
            canvas.create_line(x, 0, x, self.height, fill="#EADBC8")
        for y in range(0, self.height_canvas, self.grid_size):
            canvas.create_line(0, y, self.width, y, fill="#EADBC8")

        # X AXIS
        self.create_axis_3D(100, 'x', 'red')

        # Y AXIS
        self.create_axis_3D(100, 'y', 'green')

        # Z AXIS
        self.create_axis_3D(100, 'z', 'blue')

    def create_axis_3D(self, do_dai_truc, ten_truc, color):
        x,y,z=0,0,0
        if ten_truc=='x':
            x,y,z=do_dai_truc,0,0
        elif ten_truc=='y':
            x,y,z=0,do_dai_truc,0
        else:
            x,y,z=0,0,do_dai_truc

        x_start, y_start=self.origin[0]+5*self.cabinet_projection(0, 0, 0)[0], self.origin[1]-5*self.cabinet_projection(0, 0, 0)[1]
        x_end, y_end=self.origin[0]+5*self.cabinet_projection(x, y, z)[0], self.origin[1]-5*self.cabinet_projection(x,y,z)[1]
        self.canvas.create_line(x_start, y_start, x_end, y_end, fill=color)
        self.canvas.create_text(
                x_end+5,
                y_end+5,
                text=ten_truc,
                font=("Arial", 15),
        )

    def put_pixel(self, x, y, color="green"):
        adjusted_x = self.origin[0] + x*5
        adjusted_y = self.origin[1] - y*5
        pixel_id=self.canvas.create_rectangle(adjusted_x-2, adjusted_y-2, adjusted_x+2, adjusted_y+2, fill=color, outline=None)
        return pixel_id

    def draw_line(self, p_start, p_end):
        arr=[]
        x1=round(p_start[0])
        y1=round(p_start[1])
        x2=round(p_end[0])
        y2=round(p_end[1])
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
    def cabinet_projection(self, x, y, z):
        x_prime = x - z/(2*sqrt(2))
        y_prime = y - z/(2*sqrt(2))
        return round(x_prime), round(y_prime)

    # def cabinet_projection(self, x, y, z):
    #     x_prime = x - y*(sqrt(2)/4)
    #     y_prime = z - y*(sqrt(2)/4)
    #     return round(x_prime), round(y_prime)

    def draw_cylinder(self, x, y, z, r, h):
        # hinh tron ben duoi (elip)
        p0 = self.cabinet_projection(x, y, z)
        p1 = self.cabinet_projection(x, y, z + r)
        p2 = self.cabinet_projection(x + r, y, z)
        p3 = self.cabinet_projection(x - r, y, z)

        # hinh tron ben tren (elip)
        p4 = self.cabinet_projection(x, y + h, z)
        p5 = self.cabinet_projection(x, y + h, z + r)
        p6 = self.cabinet_projection(x + r, y + h, z)
        p7 = self.cabinet_projection(x - r, y + h, z)

        r1=self.calculate_distance(p0,p1)
        r2=self.calculate_distance(p0,p2)
        
        self.draw_ellipse_dash(p0[0], p0[1], r2, r1)
        self.draw_ellipse(p4[0], p4[1], r2, r1)
        
        self.draw_line(p2, p6)
        self.draw_line(p3, p7)

        # 2 Tâm của hình trụ
        self.put_pixel(p4[0], p4[1], "red")
        self.put_pixel(p0[0], p0[1], "red")

    def calculate_distance(self, p1,p2):
        x1=p1[0]
        y1=p1[1]
        x2=p2[0]
        y2=p2[1]
        distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distance

    #       VẼ HÌNH HỘP CHỮ NHẬT
    def draw_rectangular(self, x, y, z, chieuDai, chieuRong, chieuCao):
        p1 = self.cabinet_projection(x, y, z)
        p2 = self.cabinet_projection(x + chieuDai, y, z)
        p3 = self.cabinet_projection(x + chieuDai, y + chieuRong, z)
        p4 = self.cabinet_projection(x, y + chieuRong, z)

        p5 = self.cabinet_projection(x, y, z + chieuCao)
        p6 = self.cabinet_projection(x + chieuDai, y, z + chieuCao)
        p7 = self.cabinet_projection(x + chieuDai, y + chieuRong, z + chieuCao)
        p8 = self.cabinet_projection(x, y + chieuRong, z + chieuCao)
        self.draw_dashed_line(p1,p5)
        self.draw_dashed_line(p1,p2)
        self.draw_dashed_line(p4,p1) 

        self.draw_line(p8,p5)  # sai
        self.draw_line(p7,p6)  # sai
        self.draw_line(p3,p2)  # sai
        self.draw_line(p4, p8)
        self.draw_line(p2, p6)
        self.draw_line(p3, p7)
        self.draw_line(p7, p8)
        self.draw_line(p3, p4)
        self.draw_line(p6, p5)

    def draw_dashed_line(self, p_start, p_end):
        x0=round(p_start[0])
        y0=round(p_start[1])
        x1=round(p_end[0])
        y1=round(p_end[1])
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy
        count = 0
        draw = True
        iterations = 0
        max_iterations = 1000
        dash_length = 5
        while iterations < max_iterations:
            if x0 == x1 and y0 == y1:
                break
            if draw:
                self.put_pixel(x0, y0)
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy
            count += 1
            if count == dash_length:
                count = 0
                draw = not draw

            iterations += 1

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

    def draw_ellipse_dash(self, xc, yc, a, b, dash_length=6,color = 'green'):
        x = 0
        y = b

        # Decision parameter of region 1
        d1 = (b * b) - (a * a * b) + (0.25 * a * a)
        dx = 2 * b * b * x
        dy = 2 * a * a * y
        

        counter = 0

        # Vùng 1
        while dx < dy:
            # Add the points corresponding to the 4 quadrants
            self.draw_points(xc, yc, x, y, dash_length, counter, dashed=(x >= 0 or x <= 0))
            counter += 1

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

        # Vùng 2
        while y >= 0:
            # Add the points corresponding to the 4 quadrants
            self.draw_points(xc, yc, x, y, dash_length, counter, dashed=(x >= 0 or x <= 0))
            counter += 1

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

    def draw_points(self, xc, yc, x, y, dash_length, counter, dashed=True, color='green'):
        self.put_pixel(xc + x, yc - y, color)  # Góc phần tư thứ tư
        self.put_pixel(xc - x, yc - y, color)  # Góc phần tư thứ ba

        # Sử dụng counter để xác định khi nào vẽ và khi nào không
        if not dashed or (counter // dash_length) % 2 == 0:
            if x >= 0 and y >= 0:
                self.put_pixel(xc + x, yc + y, color)  # Góc phần tư thứ nhất
                self.put_pixel(xc - x, yc + y, color)  # Góc phần tư thứ hai   
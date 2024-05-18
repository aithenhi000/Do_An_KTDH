from tkinter import *
from Graphics2D import Graphics2D
from math import cos, sin, radians, sqrt, pow, tan

class Graphics3D(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.width=1050
        self.height=750
        self.grid_size = 5
        self.origin=(self.width//2, self.height//2)
        self.configure(padx=20, pady=20)
        self.create_frame()
        self.create_canvas()
        self.create_grid_pixel_3D()
        self.create_menu3d()


    def create_menu3d(self):
        self.lbf_HHCN=LabelFrame(self, text="Vẽ hình hộp chữ nhật",width=200, height=300, relief="ridge")
        self.lbf_HHCN.pack()


        self.lb_chieuDai_HHCN=Label(self.lbf_HHCN, text='Chiều dài:')
        self.lb_chieuDai_HHCN.grid(column=0, row=0)
        self.value_chieuDai_HHCN=Entry(self.lbf_HHCN)
        self.value_chieuDai_HHCN.grid(column=1, row=0, columnspan=3, sticky=(E, W))

        self.lb_chieuRong_HHCN=Label(self.lbf_HHCN, text='Chiều Rộng:')
        self.lb_chieuRong_HHCN.grid(column=0, row=1)
        self.value_chieuRong_HHCN=Entry(self.lbf_HHCN)
        self.value_chieuRong_HHCN.grid(column=1, row=1,columnspan=3, sticky=(E, W))

        self.lb_chieuCao_HHCN=Label(self.lbf_HHCN, text='Chiều Rộng:')
        self.lb_chieuCao_HHCN.grid(column=0, row=2)
        self.value_chieuCao_HHCN=Entry(self.lbf_HHCN)
        self.value_chieuCao_HHCN.grid(column=1, row=2,columnspan=3, sticky=(E, W))

        self.lb_toaDoDinh_HHCN=Label(self.lbf_HHCN, text='Tọa độ đỉnh (x, y, z):')
        self.lb_toaDoDinh_HHCN.grid(column=0, row=3)

        self.value_toaDoDinhx_HHCN=Entry(self.lbf_HHCN)
        self.value_toaDoDinhx_HHCN.grid(column=1, row=3)

        self.value_toaDoDinhy_HHCN=Entry(self.lbf_HHCN)
        self.value_toaDoDinhy_HHCN.grid(column=2, row=3)

        self.value_toaDoDinhz_HHCN=Entry(self.lbf_HHCN)
        self.value_toaDoDinhz_HHCN.grid(column=3, row=3)      
        self.btn_HHCN = Button(
            self.lbf_HHCN,
            text="Vẽ HHCN",
            command=lambda: self.draw_rectangular(
                int(self.value_toaDoDinhx_HHCN.get()),
                int(self.value_toaDoDinhy_HHCN.get()),
                int(self.value_toaDoDinhz_HHCN.get()),
                int(self.value_chieuRong_HHCN.get()),
                int(self.value_chieuDai_HHCN.get()),               
                int(self.value_chieuCao_HHCN.get()),            
                )
        )
        self.btn_HHCN.grid(column=2, row=4)

        # PANEL HINH TRU
        self.lbf_HT=LabelFrame(self, text="Vẽ hình trụ",width=300, height=300, relief="ridge")
        self.lbf_HT.pack()

        self.lb_chieuCao_HT=Label(self.lbf_HT, text='Chiều cao:')
        self.lb_chieuCao_HT.grid(column=0, row=0)
        self.value_chieuCao_HT=Entry(self.lbf_HT)
        self.value_chieuCao_HT.grid(column=1, row=0, columnspan=3, sticky=(E, W))

        self.lb_bankinh_HT=Label(self.lbf_HT, text='Bán kính đáy:')
        self.lb_bankinh_HT.grid(column=0, row=1)
        self.value_bankinh_HT=Entry(self.lbf_HT)
        self.value_bankinh_HT.grid(column=1, row=1,columnspan=3, sticky=(E, W))

        self.lb_tamday_HT=Label(self.lbf_HT, text='Tâm đáy (x, y, z):')
        self.lb_tamday_HT.grid(column=0, row=3)

        self.value_tamdayx_HT=Entry(self.lbf_HT)
        self.value_tamdayx_HT.grid(column=1, row=3)

        self.value_tamdayy_HT=Entry(self.lbf_HT)
        self.value_tamdayy_HT.grid(column=2, row=3)

        self.value_tamdayz_HT=Entry(self.lbf_HT)
        self.value_tamdayz_HT.grid(column=3, row=3)        
        self.btn_HT=Button(self.lbf_HT, text="Vẽ hình trụ")
        self.btn_HT.grid(column=2, row=4)


        # CLEAR CANVAS
        self.clear_button = Button(self, text="Xóa Hình Vẽ", command=self.clear_canvas)
        self.clear_button.pack()
        
    def clear_canvas(self):
        # Xóa tất cả các hình vẽ trên Canvas
        # self.canvas.pack_forget()
        # self.lbf_HHCN.destroy()
        # self.lbf_HT.destroy()
        for widget in self.frame.winfo_children():
            widget.pack_forget()
        self.create_canvas()
        self.create_grid_pixel_3D()
        
    def create_frame(self):
        self.frame=Frame(self, width=self.width, height=self.height)
        self.frame.pack(side=LEFT)
        
    def create_canvas(self):
        canvas = Canvas(self.frame, width=self.width, height=self.height, bg="#FEFAF6")
        self.canvas=canvas
        self.canvas.pack()

    def create_grid_pixel_3D(self):
        canvas=self.canvas

        # draw grids
        for x in range(0, self.width, self.grid_size):
            canvas.create_line(x, 0, x, self.height, fill="#EADBC8")
        for y in range(0, self.height, self.grid_size):
            canvas.create_line(0, y, self.width, y, fill="#EADBC8")
        print(self.width/2+5*self.cabinet_projection(0, 0, 0)[0], self.height/2-5*self.cabinet_projection(0, 0, 0)[1])    
        print(self.width/2+5*self.cabinet_projection(0, 0, 70)[0], abs(self.height/2-5*self.cabinet_projection(0, 0, 70)[1]))
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

        x_start, y_start=self.width/2+5*self.cabinet_projection(0, 0, 0)[0], self.height/2-5*self.cabinet_projection(0, 0, 0)[1]
        x_end, y_end=self.width/2+5*self.cabinet_projection(x, y, z)[0], abs(self.height/2-5*self.cabinet_projection(x,y,z)[1])
        self.canvas.create_line(x_start, y_start, x_end, y_end, fill=color)
        self.canvas.create_text(
                x_end+5,
                y_end+5,
                text=ten_truc,
                font=("Arial", 15),
        )

    def put_pixel(self, x, y, color="green"):
        adjusted_x = self.width/2 + x*5
        adjusted_y = self.height/2 - y*5
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
        midb=round(pow(a,2)/sqrt(pow(a,2)+pow(b,2)))

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

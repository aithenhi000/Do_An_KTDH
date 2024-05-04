from tkinter import *

class Graphics3D(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.width=1050
        self.height=750
        self.grid_size = 5
        self.origin=(self.width//2, self.height//2)
        self.configure(padx=20, pady=20)
        self.create_grid_pixel_3D()
        self.create_menu3d()
        
        
    def focus_next_entry(event):
        event.widget.tk_focusNext().focus()
    
    
    def create_menu3d(self):
        self.lbf_HHCN=LabelFrame(self, text="Vẽ hình hộp chữ nhật",width=300, height=300, relief="ridge")
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
        self.btn_HHCN=Button(self.lbf_HHCN, text="Vẽ HHCN")
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

    def draw_3D_main():
        pass
        
    def create_grid_pixel_3D(self):
        canvas = Canvas(self, width=self.width, height=self.height, bg="#FEFAF6")
        self.canvas=canvas
        self.canvas.pack(side=LEFT)

        # draw grid
        for x in range(0, self.width, self.grid_size):
            canvas.create_line(x, 0, x, self.height, fill="#EADBC8")
        for y in range(0, self.height, self.grid_size):
            canvas.create_line(0, y, self.width, y, fill="#EADBC8")
            
        # X AXIS
        canvas.create_line(self.origin[0], self.origin[1], self.width, self.origin[1], fill='blue')    
        
        # Y AXIS 
        canvas.create_line(self.origin[0], self.origin[1], self.origin[0], 0, fill='red')
        
        # Z AXIS
        canvas.create_line(self.origin[0], self.origin[1], 0, self.height, fill='green')
            
    def draw_Hinh_hop_chu_nhat(self, toaDoDinh, chieuDai, chieuRong, chieuCao):
        pass
    
    

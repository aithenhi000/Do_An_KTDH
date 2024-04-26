from tkinter import *


class Application:
    def __init__(self, root):
        self.root=root
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.pixel_grid_width=1050
        self.pixel_grid_height=self.panel_height=750
        self.panel_width= self.screen_width -self.pixel_grid_width
        
        root.title("ĐỒ ÁN KỸ THUẬT ĐỒ HỌA")
        root.configure(padx=20, pady=20)
        root.geometry(f"{self.screen_width}x{self.pixel_grid_height}")
        self.create_grid_pixel()
        self.create_panel()
    
    def create_grid_pixel(self):
        grid_pixel = Frame(self.root, height= self.pixel_grid_height, width=self.pixel_grid_width)
        grid_pixel.pack(side=LEFT)
        self.root.update()

        canvas = Canvas(grid_pixel, width=grid_pixel.winfo_width(), height=grid_pixel.winfo_height(), bg="#FEFAF6")
        self.canvas=canvas
        canvas.pack(fill=BOTH, expand=True)
        canvas.update()
        canvas_width = (canvas.winfo_width()//10)*10
        canvas_height = (canvas.winfo_height()//10)*10
        self.canvas_width=canvas_width
        self.canvas_height=canvas_height

        goc_toa_do=(canvas_width/2, canvas_height/2)

        #draw grid
        grid_size=5
        for x in range(0,canvas_width, grid_size):
            canvas.create_line(x, 0, x, canvas_height, fill="#EADBC8")
        for y in range(0,canvas_height, grid_size):
            canvas.create_line(0, y, canvas_width, y, fill="#EADBC8")
            
            
        # X axis
        canvas.create_line(0, canvas_height/2, canvas_width, canvas_height/2)
        for x in range(0, canvas_width, 50):
            canvas.create_rectangle(x-1, canvas_height/2-1, x+1, canvas_height/2+1, fill='red')
            canvas.create_text(x, canvas_height/2+8, text=str(int((x- self.canvas_width/2)/5)), font=('Arial', 7))

        # Y axis
        canvas.create_line(canvas_width/2, 0, canvas_width/2, canvas_height, fill="black")
        for y in range(0, canvas_height, 50):
            canvas.create_rectangle(canvas_width/2-1, y-1 ,canvas_width/2+1,y+1,  fill='red')
            canvas.create_text(canvas_width/2+9,y, text=str(int(-(y-self.canvas_height/2)/5)), font=('Arial', 7))
    
    def create_panel(self):
        panel_root = Frame(self.root, height= self.panel_height, width=self.panel_width, padx=10)
        panel_root.pack(side=RIGHT)
        self.panel_root=panel_root
        self.root.update()
        self.create_menu()
        
        
        panel_show_info=LabelFrame(panel_root, height= self.panel_height/2, width=self.panel_width,text="INFORMATION")
        panel_show_info.pack(side=BOTTOM)
        panel_root.update()
        panel_show_info_canvas = Canvas(panel_show_info, width=panel_show_info.winfo_width(), height=panel_show_info.winfo_height(), bg="#FEFAF6")
        panel_show_info_canvas.pack(fill=BOTH, expand=True)
        panel_show_info_canvas.update()
   
    def create_menu(self):
        panel_menu=LabelFrame(self.panel_root, text="MENU",bg="#FEFAF6")
        panel_menu.pack(side=TOP)
        self.panel_menu=panel_menu
        self.panel_root.update()
        label1 = Label(panel_menu, width=self.panel_menu.winfo_width(), text="Number 1:")
        label1.pack()

        
    def re_create_grid_pixel(self, canvas):
        canvas_width = (canvas.winfo_width()//10)*10
        canvas_height = (canvas.winfo_height()//10)*10
        self.canvas_width=canvas_width
        self.canvas_height=canvas_height

        goc_toa_do=(canvas_width/2, canvas_height/2)

        #draw grid
        grid_size=5
        for x in range(0,canvas_width, grid_size):
            canvas.create_line(x, 0, x, canvas_height, fill="#EADBC8")
        for y in range(0,canvas_height, grid_size):
            canvas.create_line(0, y, canvas_width, y, fill="#EADBC8")
            
            
        # X axis
        canvas.create_line(0, canvas_height/2, canvas_width, canvas_height/2)
        for x in range(0, canvas_width, 50):
            canvas.create_rectangle(x-1, canvas_height/2-1, x+1, canvas_height/2+1, fill='red')
            canvas.create_text(x, canvas_height/2+8, text=str(int((x- self.canvas_width/2)/5)), font=('Arial', 7))

        # Y axis
        canvas.create_line(canvas_width/2, 0, canvas_width/2, canvas_height, fill="black")
        for y in range(0, canvas_height, 50):
            canvas.create_rectangle(canvas_width/2-1, y-1 ,canvas_width/2+1,y+1,  fill='red')
            canvas.create_text(canvas_width/2+9,y, text=str(int(-(y-self.canvas_height/2)/5)), font=('Arial', 7))

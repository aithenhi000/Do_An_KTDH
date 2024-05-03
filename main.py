from tkinter import *
from Graphics2D import Graphics2D
from Graphics3D import Graphics3D
from tkinter import messagebox

class Application(Tk):
    def __init__(self):
        super().__init__()
        self.width=1050
        self.height=750
        self.grid_size = 5
        self.origin=(self.width//2, self.height//2)
        self.title("ĐỒ ÁN KỸ THUẬT ĐỒ HỌA")
        self.iconbitmap('Do_An_KTDH\\icon_app.ico')
        self.geometry("1500x750")
        self.create_taskbar()


    def create_taskbar(self):
        # Tạo thanh taskbar
        button_font = ("Arial", 10, "bold")
        self.taskbar_frame = Frame(self, bg="lightgray", height=50)
        self.taskbar_frame.pack(fill="both")

        self.button_2d = Button(self.taskbar_frame, text="HOME PAGE", command=self.show_home_page, font=button_font)
        self.button_2d.pack(side="left", padx=5)
        
        # Tạo button 2D
        self.button_2d = Button(self.taskbar_frame, text="GRAPHICS 2D", command=self.show_2d_application, font=button_font, bg='#FFC470')
        self.button_2d.pack(side="left", padx=5)

        
        
        # Tạo button 3D
        self.button_3d = Button(self.taskbar_frame, text="GRAPHICS 3D", command=self.show_3d_application, font=button_font,bg='#4793AF')
        self.button_3d.pack(side="left", padx=5)
        
        self.close_button = Button(self.taskbar_frame, text="Close App", command=self.close_app, bg='#8B322C', fg='white',font=button_font)
        self.close_button.pack(side="left", padx=5)

        self.lb_title=Label(self.taskbar_frame, text="Đồ án kỹ thuật đồ họa", bg="lightgray", font=("Arial", 16, "bold"))
        self.lb_title.pack(side="left", padx=200)
        

        
    def close_app(self):
        confirm = messagebox.askyesno("Close Confirmation", "Are you sure you want to close the application?")
        if confirm:
            self.destroy()
            
    def show_home_page(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.create_taskbar()
    
    def show_2d_application(self):
        self.clear_application()
        self.app_2d = Graphics2D(master=self)
        self.lb_title.config(text='GIAO DIỆN ĐỒ HỌA 2D')
        self.app_2d.pack()

    def show_3d_application(self):
        self.clear_application()
        self.lb_title.config(text='GIAO DIỆN ĐỒ HỌA 3D')
        self.app_3d = Graphics3D(master=self)
        self.app_3d.pack()

    def clear_application(self):
        for widget in self.winfo_children():
            if isinstance(widget, (Graphics3D, Graphics2D)):
                widget.pack_forget()
    


def main():
    app = Application()
    app.mainloop()

if __name__ == "__main__":
    main()
    
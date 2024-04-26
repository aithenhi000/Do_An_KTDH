from tkinter import *
import GUI 
import Graphics2D
import numpy as np
import cacphepbiendoi

def draw_object(g2D, obj_array):
    for x in range(0,obj_array.shape[0]):
        if x == obj_array.shape[0]-1:
            next = 0
        else:
            next = x + 1
        g2D.draw_line(obj_array[x][0],obj_array[x][1],obj_array[next][0],obj_array[next][1])
        
def update_frame(g2D, m_head_rectangle, m_body): #Phương án hiện tại: Xóa toàn bộ nội dung trong canvas rồi tạo lại hệ tọa độ + vẽ hình ở vị trí mới

    g2D.canvas.delete('all')
    g2D.re_create_grid_pixel(g2D.canvas)
    
    cacphepbiendoi.tinh_tien(m_head_rectangle,3,0)
    cacphepbiendoi.tinh_tien(m_body,3,0)
    
    draw_object(g2D, m_head_rectangle)
    draw_object(g2D, m_body)
    
    g2D.root.after(1000,update_frame, g2D, m_head_rectangle, m_body) #Gọi lại hàm để tiếp tục cập nhật (kiểu kiểu như đệ quy)
    
def main():
    
    root=Tk()
    g2D=Graphics2D.Graphics2D(root)
     
    root.state('zoomed') #thêm cái này đặt cửa sổ tkinter ở trạng thái zoom
    
    #Missile, khai báo các mảng chứa tọa độ các điểm của từng bộ phận (mỗi bộ phận là một hình cơ sở)
    m_head_rectangle = np.array(([10,10,1],
                                 [10,20,1],
                                 [20,15,1]))
    m_body = np.array(([-10,10,1],
                       [ 10,10,1],
                       [ 10,20,1],
                       [-10,20,1]))
    
    draw_object(g2D, m_head_rectangle)
    draw_object(g2D, m_body)
    
    g2D.root.after(1000,update_frame, g2D, m_head_rectangle, m_body) #Cập nhật vị trí mỗi mỗi 1000 giây

    root.mainloop()

if __name__ == "__main__":
    main()
    
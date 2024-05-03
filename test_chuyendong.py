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
    
def main():
    
    root=Tk()
    #missile
    m_head_rectangle = np.array(([10,10,1],
                                 [10,20,1],
                                 [20,15,1]))
    m_body = np.array(([-10,10,1],
                       [ 10,10,1],
                       [ 10,20,1],
                       [-10,20,1]))
    
    g2D=Graphics2D.Graphics2D(root)
    
    draw_object(g2D, m_head_rectangle)
    draw_object(g2D, m_body)
    
    cacphepbiendoi.tinh_tien(m_head_rectangle,50,50)
    cacphepbiendoi.tinh_tien(m_body,50,50)
    
    draw_object(g2D, m_head_rectangle)
    draw_object(g2D, m_body)
    
    #g2D.draw_line(-10, -10, 50, -80)
    #g2D.put_pixel(-1, 10)
    #g2D.draw_line(-10, -10, 50, -80)
    #g2D.draw_circle(10,10,20)
    #g2D.draw_rectangle(5,10,20,20)
    #g2D.draw_isosceles_triangle(2,2,30,50)
    root.mainloop()

if __name__ == "__main__":
    main()
    
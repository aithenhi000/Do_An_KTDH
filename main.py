from tkinter import *
import GUI 
import Graphics2D
import Graphics3D

    
def main():
    
    root=Tk()
    
    
    # g2D=Graphics2D.Graphics2D(root)
    # g2D.draw_line(-10, -10, 50, -80)
    # g2D.put_pixel(-1, 10)
    # g2D.draw_line(-10, -10, 50, -80)
    # g2D.draw_circle(10,10,120)
    # g2D.draw_rectangle(5,10,20,20)
    # g2D.draw_isosceles_triangle(2,2,30,50)
    # g2D.draw_rectangle(65,-59,75,-69)
    # g2D.draw_isosceles_triangle(65,-59,5,5)
    g3d=Graphics3D.Graphics3D(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
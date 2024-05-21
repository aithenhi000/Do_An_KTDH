import tkinter as tk
import random

canvas_width = 500
canvas_height = 500
pixel_size = 10  # Kích thước mỗi pixel

root = tk.Tk()
root.title("2D Pixel Animation")

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Hàm vẽ một pixel tại (x, y) với màu color
def draw_pixel(x, y, color):
    x1 = x * pixel_size
    y1 = y * pixel_size
    x2 = x1 + pixel_size
    y2 = y1 + pixel_size
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

# Tạo hiệu ứng hoạt hình đơn giản
def animate():
    # Xóa canvas
    canvas.delete("all")
    
    # Tô màu ngẫu nhiên các pixel
    for i in range(canvas_width // pixel_size):
        for j in range(canvas_height // pixel_size):
            color = random.choice(["red", "green", "blue", "yellow", "purple", "orange"])
            draw_pixel(i, j, color)
    
    # Gọi lại hàm animate sau 100ms
    root.after(100, animate)

# Bắt đầu hoạt hình
animate()

root.mainloop()

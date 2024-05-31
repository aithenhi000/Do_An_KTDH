import tkinter as tk
import numpy as np

class ShapeTranslationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Translation to Origin")

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        # Define shapes with their vertices
        self.triangle = [(150, 150), (200, 250), (100, 250)]
        self.square = [(250, 150), (300, 150), (300, 200), (250, 200)]

        # Draw initial shapes
        self.draw_shape(self.triangle, 'blue')
        self.draw_shape(self.square, 'red')

        # Translate shapes to origin
        self.translate_to_origin(self.triangle)
        self.translate_to_origin(self.square)

    def draw_shape(self, shape, color):
        # Draw the shape on the canvas
        points = [coord for point in shape for coord in point]
        self.canvas.create_polygon(points, outline='black', fill=color, width=2)

    def translate_to_origin(self, shape):
        # Find the translation values (tx, ty)
        tx, ty = shape[0]  # Assuming we translate the first vertex to (0, 0)

        # Create translation matrix
        T = np.array([
            [1, 0, -tx],
            [0, 1, -ty],
            [0, 0, 1]
        ])

        # Translate each point in the shape
        translated_shape = []
        for (x, y) in shape:
            point = np.array([x, y, 1])
            translated_point = np.dot(T, point)
            translated_shape.append((translated_point[0], translated_point[1]))

        # Draw the translated shape
        self.draw_shape(translated_shape, 'green')

# Create the Tkinter window and run the app
root = tk.Tk()
app = ShapeTranslationApp(root)
root.mainloop()

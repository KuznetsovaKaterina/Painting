from random import randint
from tkinter import *

from Engine2D.engine2D import Engine2D
from Geometric_figure.geometric_figure import Circle, Triangle, Rectangle


class Painting(Engine2D):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.paint = []  # list for figures
        self.colors = []  # list for colors
        self.color = "red"
        self.figure = "circle"

    def set_ui(self):
        self.parent.title("Painting")

        figure_lab = Label(text="Figure: ")
        figure_lab.grid(row=0, column=0, padx=6, pady=6)

        circle_button = Button(text="Circle", width=10, command=lambda: self.set_figure("circle"))
        circle_button.grid(row=0, column=1, padx=6, pady=6)

        triangle_button = Button(text="Triangle", width=10, command=lambda: self.set_figure("triangle"))
        triangle_button.grid(row=0, column=2, padx=6, pady=6)

        rectangle_button = Button(text="Rectangle", width=10, command=lambda: self.set_figure("rectangle"))
        rectangle_button.grid(row=0, column=3, padx=6, pady=6)

        color_lab = Label(text="Color: ")
        color_lab.grid(row=1, column=0, padx=6, pady=6)

        red_button = Button(text="Red", width=10, command=lambda: self.change_color("red"))
        red_button.grid(row=1, column=1, padx=6, pady=6)

        green_button = Button(text="Green", width=10, command=lambda: self.change_color("green"))
        green_button.grid(row=1, column=2, padx=6, pady=6)

        blue_button = Button(text="Blue", width=10, command=lambda: self.change_color("blue"))
        blue_button.grid(row=1, column=3, padx=6, pady=6)

        add_button = Button(text="Add", width=10, command=lambda: self.add_figure())
        add_button.grid(row=3, column=2, padx=6, pady=6)

        draw_button = Button(text="Draw", width=10, command=lambda: self.draw(self.paint, self.colors))
        draw_button.grid(row=5, column=1, padx=6, pady=6)

        paint_lab = Label(text="Painting: ")
        paint_lab.grid(row=4, column=0, padx=6, pady=6)

        self.text_box = Text(width=25)
        self.text_box.grid(row=5, column=0, padx=6, pady=6)

        self.canv.grid(row=5, column=2, columnspan=10, padx=5, pady=5)

        clean_button = Button(text="Clean all", width=10, command=lambda: (self.canv.delete("all"),
                                                                           self.text_box.delete('1.0', END),
                                                                           self.paint.clear()))
        clean_button.grid(row=4, column=2, padx=6, pady=6)

    # Adding a figure and color for drawing
    def add_figure(self):
        figure = self.check_figure()
        self.paint.append(figure)
        self.colors.append(self.color)
        text = f"Drawing {self.color} {figure.name}: {figure.coordinates} \n"
        self.text_box.insert(END, str(text))

    def set_figure(self, figure):
        self.figure = figure

    # Check which figure is selected
    def check_figure(self):
        if self.figure == "circle":
            circle = Circle(self.canv, randint(0, 400), randint(0, 300), randint(1, 30))
            return circle
        if self.figure == "triangle":
            triangle = Triangle(self.canv, randint(0, 400), randint(0, 300), randint(0, 400), randint(0, 300),
                                randint(0, 400), randint(0, 300))
            return triangle
        if self.figure == "rectangle":
            rectangle = Rectangle(self.canv, randint(0, 400), randint(0, 300), randint(0, 400), randint(0, 300))
            return rectangle

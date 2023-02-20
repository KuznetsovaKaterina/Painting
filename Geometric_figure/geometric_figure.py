'''Classes of geometric figure'''


class Circle:
    def __init__(self, canvas, x, y, r):
        self.name = "Circle"
        self.canvas = canvas
        self.center_x, self.center_y = x, y
        self.radius = r
        self.coordinates = [self.center_x - self.radius, self.center_y - self.radius,
                            self.center_x + self.radius, self.center_y + self.radius]

    def draw(self, color):
        self.canvas.create_oval(self.coordinates, fill=color, outline='black')


class Triangle:
    def __init__(self, canvas, x1, y1, x2, y2, x3, y3):
        self.name = "Triangle"
        self.canvas = canvas
        self.coordinates = x1, y1, x2, y2, x3, y3

    def draw(self, color):
        self.canvas.create_polygon(self.coordinates, fill=color, outline='black')


class Rectangle:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.name = "Rectangle"
        self.canvas = canvas
        self.coordinates = x1, y1, x2, y2

    def draw(self, color):
        self.canvas.create_rectangle(self.coordinates, fill=color, outline='black')

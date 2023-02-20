import time
from tkinter import *


class Engine2D:
    def __init__(self):
        self.canv = Canvas(bg="white")
        self.color = "withe"

    def change_color(self, new_color):
        self.color = new_color

    def draw(self, paint, colors):
        dictionary = dict(zip(paint, colors))  # Two lists are combined into one dictionary
        for elem in dictionary:
            elem.draw(dictionary[elem])
            self.canv.update()
            time.sleep(1)

from random import randint
from tkinter import Canvas

from Engine2D.engine2D import Engine2D
from Geometric_figure.geometric_figure import Circle, Triangle, Rectangle


def test_draw(engine):
    canv = Canvas(bg="white")
    c1 = Circle(canv, randint(0, 400), randint(0, 400), randint(0, 40))
    t1 = Triangle(canv, randint(0, 400), randint(0, 400), randint(0, 400), randint(0, 400),
                  randint(0, 400), randint(0, 400))
    r1 = Rectangle(canv, randint(0, 400), randint(0, 400), randint(0, 400), randint(0, 400))
    figures = [c1, t1, r1]
    colors = ["green", "blue", "red"]
    Engine2D.draw(engine, figures, colors)
    all_items = canv.find_all()
    assert len(all_items) == len(figures), f"Canvas does not have element. Expected: {len(figures)}, " \
                                           f"actual {len(all_items)}"


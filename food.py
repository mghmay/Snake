import random
from turtle import Turtle
from settings import right_border, left_border, top_border, bottom_border


class Food(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.color("green")
        self.penup()
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.generate()

    def generate(self):
        x = random.randint(int(left_border + 20), int(right_border - 20))
        y = random.randint(int(bottom_border + 20), int(top_border - 20))
        self.setposition(x, y)


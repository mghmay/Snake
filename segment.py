from turtle import Turtle


class Segment(Turtle):
    def __init__(self, x, y):
        super().__init__(shape="square")
        self.setposition(x, y)
        self.color("white")
        self.penup()

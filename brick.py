from turtle import Turtle

class Brick(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=4, stretch_wid=1)
        self.color(color)
        self.goto(x, y)


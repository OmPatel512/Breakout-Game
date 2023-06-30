from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.goto(x=0, y=-310)

    def go_left(self):
        new_x = self.xcor() - 35
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 35
        self.goto(new_x, self.ycor())
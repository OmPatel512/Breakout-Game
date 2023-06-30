from turtle import Turtle
import random

COLOR_LIST = ['light blue', 'royal blue','light steel blue', 'steel blue',
              'light cyan', 'light sky blue','violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink','medium sea green', 'khaki']

class Brick(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.color(random.choice(COLOR_LIST))
        self.goto(x, y)

        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.upper_wall = self.ycor() + 15
        self.lower_wall = self.ycor() - 15





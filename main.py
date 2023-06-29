from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(height=700, width=500)
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_running = True
while game_running:
    screen.update()

screen.exitonclick()

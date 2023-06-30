import time
from turtle import Screen, Turtle
from paddle import Paddle
from brick import Brick
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(height=700, width=540)
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle()
ball = Ball()


screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")


def check_collision_walls():
    global ball

    if ball.xcor() < -260 or ball.xcor() > 260:
        ball.bounce(x_bounce=True, y_bounce=False)
        return

    if ball.ycor() > 340:
        ball.bounce(x_bounce=False, y_bounce=True)
        return

    if ball.ycor() < -330:
        ball.reset()
        return


def check_collision_paddle():

    global ball, paddle

    ball_x = ball.xcor()
    paddle_x = paddle.xcor()

    if ball.distance(paddle) < 50 and ball.ycor() < -290:

        #if Paddle is on right side of screen.
        if paddle_x > 0:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return

        #if Paddle is on left side of screen.
        elif paddle_x < 0:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return

        #Else paddle is in the middle.
        else:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            elif ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return

def check_collision_bricks():
    pass


game_running = True
while game_running:
    screen.update()
    time.sleep(0.05)
    ball.move()

    check_collision_walls()
    check_collision_paddle()

screen.exitonclick()

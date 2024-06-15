import turtle as t
from random import randint

t.colormode(255)
# t.tracer(0)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

def move_forward():
    tim.forward(8)

def move_backward():
    tim.backward(8)

def turn_left():
    tim.left(8)

def turn_right():
    tim.right(8)

def change_color():
    new_color = random_color()
    tim.color(new_color)


def clear_all():
    screen.resetscreen()


screen = t.Screen()
tim = t.Turtle()


screen.listen()

screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear_all)
screen.onkey(key='space', fun=change_color)


screen.exitonclick()
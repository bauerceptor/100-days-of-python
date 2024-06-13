import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
# tim.speed('fastest')
t.tracer(0)

def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_colors())
        tim.circle(80)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(12)
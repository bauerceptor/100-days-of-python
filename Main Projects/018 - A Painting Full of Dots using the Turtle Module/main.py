import turtle as t
import colorgram            # requires installing colorgram module
from random import choice

t.colormode(255)
# t.tracer(0)

colors = colorgram.extract("image1.webp", 20)
color_palette = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

# configuration for the turtle and the screen
screen = t.Screen()
tim = t.Turtle()
tim.penup()
tim.hideturtle()


# the turtle, by default, starts at the center of the screen
# this code below brings the turtle downward on the screen
tim.setheading(255)
tim.forward(60)
tim.setheading(0)
starting_pos = (tim.xcor(), tim.ycor())


# draws 10 rows of dots
for row in range(1, 11):
    for _ in range(10):
        tim.dot(20, choice(color_palette))
        tim.forward(35)
    tim.goto(starting_pos[0], starting_pos[1])
    tim.setheading(90)
    tim.forward(row * 30)
    tim.setheading(0)


screen.exitonclick()
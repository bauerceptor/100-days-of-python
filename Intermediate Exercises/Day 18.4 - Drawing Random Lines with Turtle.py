import turtle as t
import random


tim = t.Turtle()
tim.pensize(10)

colors = ['GoldenRod', 'DeepSkyBlue', 'DarkOrchid', 'LightSeaGreen', 'SlateGray', 'SeaGreen', 'IndianRed']

DIRECTIONS = {
    'east': 0,
    'north': 90,
    'west': 180,
    'south': 270
}

tim.speed(10)

########### Challenge 4 - Draw Random Lines ########


def draw_random_lines(num_lines):
    for _ in range(num_lines):
        tim.color(random.choice(colors))
        tim.forward(50)
        random_direction = random.choice([dir for dir in DIRECTIONS.values()])
        tim.setheading(random_direction)
    


draw_random_lines(50)

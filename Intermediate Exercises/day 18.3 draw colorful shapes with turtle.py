import turtle as t
import random


tim = t.Turtle()
colors = ['GoldenRod', 'DeepSkyBlue', 'DarkOrchid', 'LightSeaGreen', 'SlateGray', 'SeaGreen', 'IndianRed']
########### Challenge 3 - Draw Shapes ########

def draw_shapes(num_sides, is_circle=False):
    if is_circle == True:
        steps = 1
    else:
        steps = 50
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(steps)
        tim.right(angle)
    


for side in range(3, 11):
    tim.color(random.choice(colors))
    draw_shapes(side)


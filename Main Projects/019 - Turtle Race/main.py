from turtle import Turtle, Screen
from random import randint


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?\n- IndianRed\n- SlateBlue\n- GoldenRod\n- ChartReuse\n- Thistle\n- MediumSpringGreen\n\nEnter a color: ").lower()

colors = ["indianred", "slateblue", "goldenrod", "chartreuse", "thistle", "mediumspringgreen"]

x_pos = -230
y_pos = -100
turtles = []
for i in range(len(colors)):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=x_pos, y=y_pos)
    y_pos += 40


if user_bet:
    is_race_on = True

while is_race_on:
    for i in range(len(turtles)):
        turtles[i].forward(randint(0, 10))
        if (turtles[i].xcor() >= 235):
            is_race_on = False
            winner = i
            break

screen.exitonclick()

print(f"The race is over. The winner is {colors[winner]}!")
if (user_bet == colors[winner]):
    print("You won the bet.")
else:
    print("You lost the best.")


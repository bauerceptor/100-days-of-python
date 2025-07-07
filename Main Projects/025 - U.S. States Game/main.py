import turtle
import pandas

states_data = pandas.read_csv("./50_states.csv")
states_list = states_data.state.to_list()
states_guessed = 0

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.screensize(1200, 1000)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


while True:
    answer_state = screen.textinput(
        title=f"{states_guessed}/50 Guess the State",
        prompt="What's another State's name?",
    ).title()
    print(answer_state)

    if answer_state in states_list:
        states_list.remove(answer_state)
        states_guessed += 1
        state_info = states_data[states_data.state == answer_state]
        x_coor = int(state_info.x)
        y_coor = int(state_info.y)
        turtle.teleport(x_coor, y_coor)
        turtle.write(answer_state)
        turtle.teleport(0, 0)

    if len(states_list) == 0:
        turtle.teleport(-20, 0)
        turtle.write("Congratulations", font=("Courier", 20, "normal"))


screen.exitonclick()

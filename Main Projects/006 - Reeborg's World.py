def turn_right():
    turn_left()
    turn_left()
    turn_left()

def round_corner():
    turn_right()
    move()
    turn_right()

def jump():
    turn_left()
    while wall_on_right():
        move()
    round_corner()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
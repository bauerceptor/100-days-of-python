from turtle import Screen
from time import sleep
from snake import Snake


screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("New Snake Game")
screen.tracer(0)
snake = Snake()


screen.listen()
screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Down", fun=snake.down)
screen.onkeypress(key="Left", fun=snake.left)
screen.onkeypress(key="Right", fun=snake.right)

is_game_on = True
while is_game_on:
    screen.update()
    sleep(0.1)
    snake.move()



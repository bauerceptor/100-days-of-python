import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
tim.color('red')
tim.shape('turtle')

def dashed_line(units):
    for _ in range(units):
        tim.pendown()
        tim.forward(5)
        tim.penup()
        tim.forward(5)

for _ in range(4):
    dashed_line(10)
    tim.left(90)
    
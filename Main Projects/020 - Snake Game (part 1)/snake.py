from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self._segments = []
        self.create_snake()
        self._head = self._segments[0]

    @property
    def segments(self):
        return self._segments

    @property
    def head(self):
        return self._head

    def create_snake(self):
        y_coor = 0
        for _ in range(3):
            seg = Turtle(shape="square")
            seg.color("white")
            seg.penup()
            seg.sety(y=y_coor)
            seg.setheading(to_angle=90)
            y_coor -= 20
            self.segments.append(seg)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if (self.head.heading() != DOWN):
            self.head.setheading(UP)

    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(DOWN)

    def left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)

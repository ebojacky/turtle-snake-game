from turtle import Turtle

ONE_STEP_DISTANCE = 20
SPINE_WIDTH = 20


class Snake:

    def __init__(self, starting_snake_len=3):
        self.segments = []
        self.elongate(starting_snake_len, True)
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def elongate(self, how_many, is_young=False):
        for i in range(0, how_many):
            segment = Turtle("turtle")
            segment.color("dark green")
            segment.penup()
            if is_young:
                segment.goto(i * -SPINE_WIDTH, 0)
                self.segments.append(segment)
            else:
                segment.goto(self.tail.xcor(), self.tail.ycor())
                self.segments.append(segment)
        self.tail = self.segments[-1]

    def move(self):
        i = len(self.segments) - 1
        while not i < 0:
            if i > 0:
                self.segments[i].goto(self.segments[i - 1].xcor(), self.segments[i - 1].ycor())
                self.segments[i].setheading(self.segments[i - 1].heading())
            else:
                self.head.forward(ONE_STEP_DISTANCE)
            i = i - 1

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

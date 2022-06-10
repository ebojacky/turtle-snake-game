from turtle import Turtle
from random import randint

SIZE_FACTOR = (0.5, 0.5)
SCREEN = (600, 600)
FOOD_SCREEN_MARGIN = 20


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("olive drab")
        self.penup()
        self.speed("fastest")
        self.shapesize(SIZE_FACTOR[0], SIZE_FACTOR[1])
        self.appear_at_random()

    def appear_at_random(self):
        x = int((SCREEN[0] - FOOD_SCREEN_MARGIN) / 2)
        y = int((SCREEN[1] - FOOD_SCREEN_MARGIN) / 2)
        self.goto(randint(-x, x), randint(-y, y))

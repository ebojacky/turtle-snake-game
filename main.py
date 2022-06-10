from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

WIDTH = 600
HEIGHT = 600
BACKCOLOR = "black"
FOOD_COLLISION_MARGIN = 15
SNAKE_COLLISION_MARGIN = 10
SCORE_DISPLAY_MARGIN = 30
SNAKE_ELONGATION = 1
SCREEN_NAME = "TURTLE SNAKE"

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.title(SCREEN_NAME)
screen.bgcolor(BACKCOLOR)
screen.tracer(0)


def play_snake():
    my_snake = Snake()
    my_food = Food()
    my_score = ScoreBoard(HEIGHT, SCORE_DISPLAY_MARGIN)

    screen.update()

    screen.listen()
    screen.onkey(my_snake.up, "Up")
    screen.onkey(my_snake.down, "Down")
    screen.onkey(my_snake.left, "Left")
    screen.onkey(my_snake.right, "Right")

    game_on = True
    while game_on:
        time.sleep(my_score.level)
        screen.update()
        my_snake.move()

        if my_snake.head.distance(my_food) <= FOOD_COLLISION_MARGIN:
            my_score.update_score()
            my_food.appear_at_random()
            my_snake.elongate(SNAKE_ELONGATION)

        if abs(my_snake.head.xcor()) >= (WIDTH / 2) or abs(my_snake.head.ycor()) >= (HEIGHT / 2):
            game_on = False

        for segment in my_snake.segments[1:]:
            if my_snake.head.distance(segment) < SNAKE_COLLISION_MARGIN:
                game_on = False
                break

        screen.update()

    my_score.write_score(is_game_over=True)
    play_again = screen.textinput("Game Over !", "Press Y to play again !")
    if play_again.upper() == "Y":
        screen.clear()
        screen.setup(WIDTH, HEIGHT)
        screen.bgcolor(BACKCOLOR)
        screen.tracer(0)
        play_snake()


play_snake()
screen.exitonclick()



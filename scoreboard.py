from turtle import Turtle

GAME_LEVEL = {"EASY": 0.3, "MEDIUM": 0.2, "HARD": 0.1}


class ScoreBoard(Turtle):
    def __init__(self, height, margin):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")

        self.score = 0
        self.level = GAME_LEVEL["EASY"]
        self.goto(0, int(height/2 - margin))
        self.write_score()

    def write_score(self, is_game_over=False):
        self.clear()
        if not is_game_over:
            self.write(f"Score: {self.score}. Level: {self.show_level()}", align='center')
        else:
            self.write(f"Score: {self.score}. Level: {self.show_level()}. GAME OVER !", align='center')

    def update_score(self):
        if self.score < 5:
            self.score += 1
        elif 5 <= self.score < 15:
            self.score += 2
            self.level = GAME_LEVEL["MEDIUM"]
        else:
            self.score += 4
            self.level = GAME_LEVEL["HARD"]
        self.write_score()

    def show_level(self):
        if self.level == GAME_LEVEL["EASY"]:
            return "EASY"
        if self.level == GAME_LEVEL["MEDIUM"]:
            return "MEDIUM"
        if self.level == GAME_LEVEL["HARD"]:
            return "HARD"

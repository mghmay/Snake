from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")

    def update_score(self, score):
        self.clear()
        self.write(score, font=("Consolas", 20, "normal"))

    def game_over(self, score):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game over!, Your score is {score}", align="center", font=("Consolas", 20, "normal"))

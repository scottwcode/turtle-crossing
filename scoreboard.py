from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TOP = int(SCREEN_HEIGHT/2)
SCREEN_LEFT = -(int(SCREEN_WIDTH/2))
SCORE_X_BUFFER = 20
SCORE_Y_BUFFER = 50
SCORE_POS_X = SCREEN_LEFT + SCORE_X_BUFFER
SCORE_POS_Y = SCREEN_TOP - SCORE_Y_BUFFER


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(SCORE_POS_X, SCORE_POS_Y)
        # self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """ Update the score on the scoreboard"""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """ Make appropriate changes when the level increases """
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """ Make appropriate changes when the Game is Over """
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

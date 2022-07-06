from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Times New Romans', 12, 'normal')
FONT_GAME_OVER = ('Gothic', 50, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 315)
        self.penup()
        self.color('white')
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.clear()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write("Game Over", align=ALIGNMENT, font=FONT_GAME_OVER)


class Frame(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('gray', 'black')
        self.shapesize(stretch_wid=30, stretch_len=30, outline=15)
        self.get_shapepoly()



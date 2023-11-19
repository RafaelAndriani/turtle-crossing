from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.setposition(-250, 250)
        self.color("white")
        self.score = 0
        self.level = 0
        self.next_level()

    def next_level(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="GAME OVER", font=FONT, align=ALIGN)


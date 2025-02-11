from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Deaths(Turtle):  # monitorDeaths
    def __init__(self):
        super(Deaths, self).__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(200, 270)
        self.score = 0

    def show_deaths(self):
        self.write(f"DEATHS:{self.score}", align='left', font=FONT)

    def death(self):
        self.score += 1



class Scoreboard(Turtle):  # monitorsSCore
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(-200, -270)
        self.score = 0

    def show_score(self):
        self.write(f"Blocks Destroyed:{self.score}", align='left', font=FONT)

    def destroyed(self):
        self.score += 1

    def final_score(self):
        self.goto(x=-170, y=100)
        self.write(f"GAME OVER", align='left', font=("Courier", 50, "normal"))
        self.goto(x=-170, y=-100)
        self.write(f"your score was: {self.score}", align='left', font=FONT)

    def Win(self):
        self.goto(x=0, y=200)
        self.write(f"YOU WIN", align='left', font=("Courier", 50, "normal"))

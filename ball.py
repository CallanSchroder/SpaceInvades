from turtle import Turtle
from bats import Bats
bat = Bats


class Ball(Turtle):  # my Lazer Beam

    def create_lazer(self):
        super(Ball, self).__init__()
        self.shape("triangle")
        self.speed(30)
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(0.5,0.5)

    # def create_lazer(self):
    #     lazer = Turtle("turtle")
    #     lazer.shape("square")
    #     lazer.speed(30)
    #
    #     lazer.color("white")
    #     lazer.shapesize(stretch_wid=0.5, stretch_len=0.5)
    #     lazer.penup()
    #     # lazer.goto(x=bat.xcor(self), y=bat.ycor(self))
    #     self.lazers.append(lazer)

    def move(self):
        while self.ycor() < 420:
            self.y_move = 1
            new_y = self.ycor() + self.y_move
            self.goto(self.xcor(), new_y)




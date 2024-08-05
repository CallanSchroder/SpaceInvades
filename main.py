
from turtle import Screen
import random
from environment import Deaths, Scoreboard
from walls import Walls
from bats import Bats
from ball import Ball

bat = Bats()
ball = Ball()
deaths = Deaths()
wall = Walls()
score = Scoreboard()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Turtle Beach")
screen.listen()
screen.tracer(0)
timesleep = 0.1


RANDOM_Y = random.randint(150, 280)
FONT = ("Courier", 24, "normal")

died = 0
a = 10
wall.Setup()

screen.onkey(bat.go_left, "a")
screen.onkey(bat.go_right, "d")
# screen.onkey(ball.create_lazer, "m")
screen.onkey(ball.move, "m")

game_on = True
while game_on:



    wall.move_down()


    score.clear()
    deaths.clear()

    score.show_score()
    deaths.show_deaths()

    ball.create_lazer()
    x = bat.xcor()
    y = bat.ycor()
    ball.setposition(x, y)

    screen.update()

    for wall in wall.all_walls:
        if ball.distance(wall) < 40:
            wall.goto(10000,10000)
            ball.reset()
            score.destroyed()
    if score.score >= 10:
        for walls in wall.all_walls:
            walls.goto(1000, 1000)
        score.final_score()
        score.Win()
    # for walls in wall.all_walls:
    #     if walls.ycor() < -300:
    #         deaths.death()
    #         walls.reset()
    if deaths.score == 5:
        for walls in wall.all_walls:
            walls.reset()
        score.final_score()
        deaths.show_deaths()
        game_on = False

screen.exitonclick()
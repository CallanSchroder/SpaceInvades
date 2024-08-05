import turtle
from turtle import Turtle
import random


class Walls():  # makesBadTurtles

    def __init__(self):
        self.all_walls = []

    def Setup(self):  # createsBadTurtles
        choice = random.randint(1, 15)
        if choice == 2:
            new_wall = turtle.Turtle
            new_wall.right(90)
            new_wall.penup()
            new_wall.speed("fastest")
            new_wall.color("red")
            new_wall.goto(x=random.randint(-380, 380), y=250)
            self.all_walls.append(new_wall)

    def move_down(self):  # movesBadTurtlesDown
        for wall in self.all_walls:
            wall.speed("slow")
            wall.forward(0.5)
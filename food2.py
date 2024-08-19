from turtle import Turtle
import random
class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('circle')
        self.shapesize(1)
        self.fillcolor("red")
        # self.x = random.randint(- 280, 280)
        # self.y = random.randint(- 280, 280)
        # self.penup()
        # self.goto(self.x, self.y)
        self.move_food()
        self.showturtle()

    def move_food(self):
        self.x = random.randint(- 280, 280)
        self.y = random.randint(- 280, 280)
        self.penup()
        self.goto(self.x, self.y)




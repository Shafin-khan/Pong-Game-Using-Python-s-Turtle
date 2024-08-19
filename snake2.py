from turtle import Turtle, Screen

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANC = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
screen = Screen()
# screen.bgcolor('Black')

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake_body()
        self.head = self.segments[0]

    def create_snake_body(self):
        for position in STARTING_POSITION:
           new_segment = Turtle('square')
           new_segment.color("green")
           new_segment.penup()
           new_segment.goto(position)
           self.segments.append(new_segment)
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANC)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake_body()
        self.head = self.segments[0]


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
    def left(self):
        if self.head.heading() != RIGHT:
               self.head.setheading(180)

    def add_segment(self):
        self.segment = Turtle()
        self.segment.hideturtle()
        self.segment.shape("square")
        self.segment.color('green')
        self.new_x = self.segments[len(self.segments)-1].xcor()
        self.new_y = self.segments[len(self.segments)-1].ycor()
        self.segment.penup()
        self.segment.goto(self.new_x, self.new_y)
        self.segments.append(self.segment)
        self.segment.showturtle()





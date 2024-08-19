from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
       super().__init__()
       self.hideturtle()
       self.score = 0
       with open('data.txt') as data:
           self.high_score=int(data.read())
       # self.high_score = 0
       self.color('white')
       self.penup()
       self.goto(x=0, y=265)
       self.update_score()
    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} Highscore: {self.high_score}',align=ALIGNMENT,font= FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('GAME OVER',align=ALIGNMENT,font=FONT)

    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode="w") as file:
                file.write(f'{self.high_score}')
            self.score = 0

            self.update_score()
        else:
            self.score = 0
            self.update_score()

    def write_data(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode="a" ) as d_file:
                d_file.write(f" {(self.high_score)}\n")

    def read_data(self):
        with open('data.txt', mode="r" ) as read_file:
                 contents=read_file.read()
                 print(contents)








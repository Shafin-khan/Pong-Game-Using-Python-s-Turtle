# ToDo 1: Make a screen
from turtle import Screen
import time
from snake2 import Snake
from food2 import Food
from  scoreboard2 import Scoreboard
# with open('data.txt') as file:
#

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('grey')
screen.title('My Snake Game 2')

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

        # scoreboard.game_over()
        scoreboard.reset()
        # scoreboard.write_data()
        # scoreboard.read_data()
        snake.reset()
        # game_is_on=False


    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            # scoreboard.game_over()
            scoreboard.reset()
            # scoreboard.write_data()
            # scoreboard.read_data()
            snake.reset()
            # game_is_on = False



    if snake.head.distance(food) <15:
       food.move_food()
       snake.add_segment()
       scoreboard.increase_score()

# ToDo 4: Make food for the snake(done)

# Todo5:Make a scoreboard
# Todo6: Detect collision between snake and food(done)
#        -increase point
#        -Change the position of the food
# Todo7: Detect collision with snake and wall and snake and snake
screen.exitonclick()

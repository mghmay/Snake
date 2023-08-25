import time
from turtle import Screen

from scoreboard import Scoreboard
from settings import screen_width, screen_height
from food import Food
from snake import Snake

screen = Screen()
screen.setup(screen_width, screen_height)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
scoreboard = Scoreboard()
food = Food()

game_is_over = False

while not game_is_over:
    screen.update()
    screen.listen()
    screen.onkey(snake.move_up, "w")
    screen.onkey(snake.move_down, "s")
    screen.onkey(snake.move_left, "a")
    screen.onkey(snake.move_right, "d")
    snake.move_forward()
    if snake.eat(food):
        food.generate()
    scoreboard.update_score(snake.score)
    game_is_over = snake.check_game_over()
    time.sleep(0.1)

scoreboard.game_over(snake.score)
screen.exitonclick()










# video way

# segments = []
#
# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
#
#
#
#
# game_is_on = True
#
# while game_is_on:
#     screen.update()
#     time.sleep(0.8)
#     for seg_num in range(len(segments) - 1, 0, -1):
#         new_x = segments[seg_num - 1].xcor()
#         new_y = segments[seg_num - 1].ycor()
#         segments[seg_num].goto(new_x, new_y)
#     segments[0].forward(20)
#
# screen.exitonclick()





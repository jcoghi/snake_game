from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard, Frame

screen = Screen()
screen.setup(width=650, height=680)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

frame = Frame()
snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.05)
    snake.move()

# COLISION
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

# DETECTING COLLISION WITH WALL
    if snake.head.xcor() > 298 or snake.head.xcor() < -298 or snake.head.ycor() > 298 or snake.head.ycor() < -298:
        game_is_on = False
        score_board.game_over()
# DETECTING COLLISION WITH TAIL:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()

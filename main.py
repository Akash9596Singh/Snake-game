# 0. Set up screen
# 1. Create a snake Body
# 2. Move the Snake
# 3. Create Snake Food
# 4. Detect Collision with Food
# 5. Create Scoreboard
# 6. Detect Collision with Wall
# 7. Detect Collision with Tail
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)  # Turns turtle animation on/ off and set delay for update drawings

snake = Snake()
# snake.head.shape('circle')
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

game_is_on = True
user_score = 0
speed = 0.1
while game_is_on:
    screen.update()  # Perform a TurtleScreen update.
    time.sleep(speed)  # Delay execution for a given number of seconds.
    # The argument may be a floating point number for subsecond precision
    # Detect Collision with wall
    if snake.head.xcor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280:
        snake.reset()
        score.restart()

    snake.move()
    # Detect collision with the food
    # if score.score%10==0:
    #     speed*=0.9
    if snake.head.distance(food) < 18:
        food.refresh()
        score.increase_score()
        score.update_score()
        snake.extend()
        # snake.increase_speed()

    # Detect tail collision
    # it the head collide with any segment then game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            score.restart()

screen.exitonclick()

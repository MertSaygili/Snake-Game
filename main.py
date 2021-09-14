from turtle import Turtle, Screen
import time
import random

# Game Score
score = 0

# Screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Body parts of snake variables
parts_f_snake = []
first_snake_nums = 0
x_Starting_position = 0
y_Starting_position = 0

# ----    Methods    ----
# Movement of snake
def left_0():
    parts_f_snake[0].left(90)
def right_0():
    parts_f_snake[0].right(90)
def null():
    pass

def putting_null_a_d():
    screen.onkey(key="a", fun=null)
    screen.onkey(key="d", fun=null)
def putting_null_w_s():
    screen.onkey(key="w", fun=null)
    screen.onkey(key="s", fun=null)

# Adding snake parts
def adding_snake_part():
    add_snake_part = Turtle("square")
    add_snake_part.penup()
    add_snake_part.color("white")
    parts_f_snake.append(add_snake_part)

# Game Over
def game_over():
    text = Turtle()
    text.color("White")
    text.write(f"Game's over, your score is {score}", False, "center", ("Arial", 24, "normal"))
# Making main snake
for first_snake_nums in range(0, 3, 1):
    snake_s_part = Turtle("square")
    snake_s_part.penup()
    snake_s_part.color("white")
    snake_s_part.goto(x_Starting_position, y_Starting_position)
    x_Starting_position = x_Starting_position - 20
    parts_f_snake.append(snake_s_part)

# Adding ScoreBoard
score_board = Turtle()
score_board.penup()
score_board.hideturtle()
score_board.color("White")
score_board.goto(0, 270)
score_board.write(f"Score: {score}", False, "center", ("Arial", 12, "normal"))

# Adding first food
has_food_eaten = False
x_coordinate_f_food = random.randint(-270, 270)
y_coordinate_f_food = random.randint(-270, 270)
food = Turtle("circle")
food.turtlesize(0.5)
food.color("green")
food.penup()
food.goto(x_coordinate_f_food, y_coordinate_f_food)

# Movement of Snake
is_game_on = True
snake_s_speed = 20
screen.listen()
num = 2


while is_game_on:
    screen.update()
    time.sleep(0.1)

    for parts in range(len(parts_f_snake) - 1, 0, -1):
        if parts == len(parts_f_snake) - 1:
            parts_f_snake[parts].showturtle()
        x_position = parts_f_snake[parts - 1].xcor()
        y_position = parts_f_snake[parts - 1].ycor()
        parts_f_snake[parts].goto(x_position, y_position)

    # Movement of snake
    if parts_f_snake[0].heading() == 0:
        screen.onkey(key="w", fun=left_0)
        screen.onkey(key="s", fun=right_0)
        putting_null_a_d()
    elif parts_f_snake[0].heading() == 180:
        screen.onkey(key="w", fun=right_0)
        screen.onkey(key="s", fun=left_0)
        putting_null_a_d()
    elif parts_f_snake[0].heading() == 90:
        screen.onkey(key="a", fun=left_0)
        screen.onkey(key="d", fun=right_0)
        putting_null_w_s()
    elif parts_f_snake[0].heading() == 270:
        screen.onkey(key="a", fun=right_0)
        screen.onkey(key="d", fun=left_0)
        putting_null_w_s()

    # Border of gaming space
    x_position_t_border = parts_f_snake[0].xcor()
    y_position_t_border = parts_f_snake[0].ycor()
    if x_position_t_border > 280 or x_position_t_border < -285:
        is_game_on = False
        print(f"Game's over, your score is {score}")
        game_over()
    elif y_position_t_border > 285 or y_position_t_border < -285:
        is_game_on = False
        print(f"Game's over, your score is {score}")
        game_over()

    # Checking Food
    if parts_f_snake[0].distance(food) <= 15:
        has_food_eaten = True
        food.hideturtle()
        score = score + 1

        # Growth of snake
        adding_snake_part()
        parts_f_snake[len(parts_f_snake) - 1].hideturtle()

    # Adding Food
    while has_food_eaten:
        score_board.clear()
        score_board.write(f"Score: {score}", False, "center", ("Arial", 12, "normal"))
        x_coordinate_f_food = random.randint(-270, 270)
        y_coordinate_f_food = random.randint(-270, 270)
        food = Turtle("circle")
        food.turtlesize(0.5)
        food.color("green")
        food.penup()
        food.goto(x_coordinate_f_food, y_coordinate_f_food)
        has_food_eaten = False

    # if part of snake touch another parts of main snake
    for segment in parts_f_snake:
        if segment == parts_f_snake[0]:
            pass
        elif segment == parts_f_snake[1]:
            pass
        elif parts_f_snake[0].distance(segment) < 10:
            is_game_on = False
            print(f"Game's over, your score is {score}")
            game_over()

    parts_f_snake[0].forward(snake_s_speed)
screen.exitonclick()

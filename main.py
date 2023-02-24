# Turtle Crossing
# Basic Gameplay:
# -A player controls a "Turtle" that moves across a "road" by moving the turtle
# from the bottom of the screen to the top of the screen.
# -The turtle can move up, down, left or right using the arrow keys
# -There are "cars" that move from right to left that the turtle should not touch or
# the game ends
# -If the player makes it across the "road", the level increases, the turtle starts
# back at the bottom of the "road" to try to go across again and the cars move faster.
# -The goal is to get as high a level as you can

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TURTLE_WIDTH = 20

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Get the player's keystroke(s)
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_right, "Right")
screen.onkey(player.go_left, "Left")

game_on = True
while game_on:
    # Set speed via sleep
    time.sleep(0.1)
    screen.update()

    # Create the cars on the screen
    car_manager.create_car()
    car_manager.move_cars()

    # Detect turtle collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < TURTLE_WIDTH:
            game_on = False
            scoreboard.game_over()

    # Detect when turtle has successfully crossed the road
    if player.is_across_road():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()

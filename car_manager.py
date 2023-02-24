from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TOP = int(SCREEN_HEIGHT/2)
SCREEN_BOTTOM = -(int(SCREEN_HEIGHT/2))
ROAD_EDGE_BUFFER = 50
CARS_TOP = SCREEN_TOP - ROAD_EDGE_BUFFER
CARS_BOTTOM = SCREEN_BOTTOM + ROAD_EDGE_BUFFER


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """ Only create cars 1 out of 5 times this is called """
        if random.randint(1, 5) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(CARS_BOTTOM, CARS_TOP)
            new_car.goto(SCREEN_TOP, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """ Set 'cars' in motion """
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """ When leveling up, increase cars speed """
        self.car_speed += MOVE_INCREMENT

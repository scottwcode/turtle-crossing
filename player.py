from turtle import Turtle

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
TURTLE_WIDTH = 20
ROAD_TOP = int(SCREEN_HEIGHT/2 - TURTLE_WIDTH)
ROAD_BOTTOM = -(int(SCREEN_HEIGHT/2 - TURTLE_WIDTH))
STARTING_POSITION = (0, ROAD_BOTTOM)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        """ Move up on the screen"""
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        """ Move down on the screen"""
        self.backward(MOVE_DISTANCE)

    def go_left(self):
        """ Move left on the screen"""
        self.setheading(180)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)

    def go_right(self):
        """ Move right on the screen"""
        self.setheading(0)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)

    def go_to_start(self):
        """ Return to the starting position """
        self.goto(STARTING_POSITION)

    def is_across_road(self):
        """ Return True if the player has crossed the road, else False """
        if self.ycor() > ROAD_TOP:
            return True
        else:
            return False

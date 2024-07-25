import time
from turtle import Turtle, Screen

# screen=Screen()
# these are constant
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
SPEED = 10


class Snake:

    def __init__(self):
        self.segments = []
        self.snake_speed = MOVE_DISTANCE
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Used to create the snake this function is called by the constructor when the object is created"""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def move(self):
        """Move the snake"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # new_x = self.segments[seg_num - 1].xcor()
            # new_y = self.segments[seg_num - 1].ycor()
            position = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(position)
        self.head.forward(self.snake_speed)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        # new_segment.speed(3)
        new_segment.penup()  # has to be before goto else it will draw line
        new_segment.goto(position)
        # new_segment.xcor()
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    # def increase_speed(self):
    #     self.snake_speed+=SPEED

    def reset(self):
        for segment in self.segments:
            segment.reset()
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

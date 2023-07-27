import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    # def __init__(self):
    #     super().__init__()
    #     self.penup()
    #     self.color(COLORS[random.randint(0,5)])
    #     self.sety(random.randint(-250,250))
    #     self.setx(280)
    #     self.shape('square')
    #     self.width(40)
    #     self.shapesize(1,2)
    #     self.setheading(180)
    #     self.forward(STARTING_MOVE_DISTANCE)
    #
    # def move(self):
    #     while self.xcor() > -300:
    #         self.forward(MOVE_INCREMENT)
    def __init__(self):
        self.cars = []

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(COLORS[random.randint(0,5)])
        new_car.sety(random.randint(-250,250))
        new_car.setx(280)
        new_car.shapesize(1,2)
        new_car.setheading(180)
        self.cars.append(new_car)

    def move(self):
        for number_cars in range (0, len(self.cars)):
            self.cars[number_cars].forward(MOVE_INCREMENT)
    pass

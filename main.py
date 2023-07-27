import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
car_manager = CarManager()
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Tutle Crossing")
screen.tracer(0)
screen.listen()
player = Player()


screen.onkey(player.move_forward, "Up")

counter = 0
game_is_on = True
while game_is_on:
    counter += 1
    if counter == 6:
        counter = 0
        car_manager.create_car()
    car_manager.move()


    time.sleep(0.1)
    screen.update()

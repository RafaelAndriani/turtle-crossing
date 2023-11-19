import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
scoreboard = Scoreboard()
car = CarManager()


def start():
    for _ in range(50):
        car.move(scoreboard.level, turtle)


screen.onkeypress(turtle.move_forward, "Up")
screen.listen()

game_is_on = True
start()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if not car.move(scoreboard.level, turtle):
        scoreboard.game_over()
        game_is_on = False
    if turtle.ycor() >= FINISH_LINE_Y:
        turtle.reset_position()
        scoreboard.next_level()

screen.exitonclick()

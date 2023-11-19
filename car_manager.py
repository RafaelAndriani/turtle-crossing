from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.new_car()

    def new_car(self, number=70):
        for _ in range(number):
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=1.5)
            new_car.goto(x=random.randint(280, 2000), y=random.randint(-250, 260))
            new_car.setheading(180)
            self.cars.append(new_car)

    def move(self, level=0, turtle=None):
        for car in self.cars:
            if car.distance(turtle) < 20:
                return False
            if car.position()[0] < -330:
                self.cars.remove(car)
                self.new_car(1)
            car.forward(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (level-1)))
        return True





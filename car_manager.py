import random
from turtle import Turtle
COLORS = ["red","orange","yellow","green","blue","purple"]
MOVE_DISTANCES = 5
MOVE_INCREMENT = 10

class Car():
    def __init__(self):
        self.cars = []

    def create_car(self):
        chance = random.randint(1,6)
        if chance > 4:
            new = Turtle()
            new.color(random.choice(COLORS))
            new.shape("square")
            new.shapesize(stretch_len=2, stretch_wid=1)
            new.penup()
            y_pos = random.randint(-250,250)
            new.goto(312,y_pos)
            self.cars.append(new)
    
    
    def move(self):
        for new in self.cars:
            new.backward(MOVE_DISTANCES)
            
    def create_new(self):
        new = Car()
        self.cars.append(new)
    

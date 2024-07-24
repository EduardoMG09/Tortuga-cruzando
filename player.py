from turtle import Turtle

START_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE = (280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()

    def create_turtle(self):
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(START_POSITION)
    
    def up(self):
        self.forward(MOVE_DISTANCE)

    def restore(self):
        if self.ycor() > FINISH_LINE:
            self.setpos(START_POSITION)
        

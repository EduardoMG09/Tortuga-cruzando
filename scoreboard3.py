from turtle import Turtle
FONT = ("Courier",24,"normal")
ALLING = "right"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(0,210)
        self.hideturtle()
        
    def update(self):
        self.clear()
        self.write(f"Level : {self.level}",align=ALLING,font=FONT)
    
    def update_level(self):
        self.level += 1

    def game_over(self):
        self.clear()
        self.write(f" Game over! ",align=ALLING,font=FONT)
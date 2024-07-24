import time
from turtle import Screen
from car_manager import Car
from player import Player
from scoreboard3 import Scoreboard

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("white")
s.title("Turtle Cross")
s.tracer(0)

player = Player()
car = Car()
board = Scoreboard()

s.listen()
s.onkeypress(player.up, "Up")

space = 0
every = 0.01
timer = 0.2

game_on = True
while game_on:
    time.sleep(timer)
    board.update()
    s.update()

    car.create_car()
    car.move()

    #Detect the wall up
    if player.ycor() > 290:
        player.restore()
        board.update_level()
        timer -= every

    #Detect car collision
    for auto in car.cars:
        if auto.distance(player) < 20:
            game_on = False
            board.game_over()
            
s.exitonclick()

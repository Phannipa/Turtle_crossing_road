import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
scoreboard = Scoreboard()
screen = Screen()
car_manager = CarManager()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.go_up, "Up") #screen listens for the "Up" keypress to move the turtle north

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create cars and move.
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision wth car.
    for car in car_manager.all_cars:
        if car.distance(player) < 20: #20 means width of car
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing.
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.speed_up()
        scoreboard.increase_level()

screen.exitonclick()




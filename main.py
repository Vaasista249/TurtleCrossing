import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
player.create_player()
car_manager = CarManager()
car_manager.create_car()

score_board = Scoreboard()

screen.onkey(player.move_forward,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    ## DETECT COLLISION WITH CAR
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()
    
    # DETECT TURTLE WHEN REACHES OTHER SIDE
    if player.is_at_finishline():
        player.go_to_start()
        car_manager.level_up()
        score_board.increase_level()

    
    














screen.exitonclick()
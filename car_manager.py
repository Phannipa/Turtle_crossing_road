# CarManager class is going to generate all of the random cars and move them cross the screen
# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis
# and move from right to left edge of the screen. No cars should be generated in the top and bottom 50px of the screen
# (think of it as a safe zone for our little turtle).
# Hint: generate a new car only every 6th time the game loop runs


from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5 # Distance of each distance of each of the cars on each refresh.
MOVE_INCREMENT = 10 # move increase everytime when the user levels up.


class CarManager:
    # CarManager class's not inherit Turtle class because The other classes we created were a single object
    # of the Turtle class. The class we created was in fact a single Turtle Object.
    # But the CarManager wasn't just one single object, we created a list of Turtle Objects.
    # If the CarManager was a single object but was duplicated many times around the screen,
    # when we'd change the color it would change the color of every single duplication across the screen
    def __init__(self):
        self.all_cars = [] #Using self because it's defined in the class
        self.car_speed = STARTING_MOVE_DISTANCE #Using self because it's defined in the class

    def create_car(self): #This method creates just only one new car and add it on to the all_cars list.
        random_chance = random.randint(1, 6)

        # probability 1 out of 6 like a dice. The cars will get generated a lot and turtle object cannot cross the road.
        # So we use dice idea to reduce the number of cars.

        if random_chance == 1:
            new_car = Turtle("square") #Inherit from Turtle class.
            # all turtle start by 20 by 20 and this needs to be 20 by 100 so we need to stretch it.
            # So we want the width to be double the original size
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250) #randomly generated along the y-axis
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):#Move all of the cars from all_cars list from the right to the left side of the screen.
        for car in self.all_cars:
            car.setheading(180)
            car.forward(STARTING_MOVE_DISTANCE)
            # Or we can use this code---> car.backward(STARTING_MOVE_DISTANCE)

    def speed_up(self):
        self.car_speed = self.car_speed + MOVE_INCREMENT









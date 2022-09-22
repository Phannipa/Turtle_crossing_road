from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10 # How much of the turtle move each time.
FINISH_LINE_Y = 280


# Player class is going to be the turtle which we're controlling to cross
# Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup() #So the turtle just remains a shape and it's doesn't draw.
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)
        # We can use this code as below.
        # new_y = self.ycor() + MOVE_DISTANCE
        # self.goto(self.xcor(), new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False



from paddle import Paddle
from ball import Ball
from brick import Brick
from point import Point
from graphics import Graphics
from object import Object
from time import sleep
import keyboard

class Game():
    def __init__(self):
        # Init our game objects
        self.Exit = False
        self.PaddleSpeed = 10.0
        self.Graphics = Graphics(Point(800, 600))
        self.Objects = []

        # The following are the edges of the board so ball knows when it has hit an edge
        self.Objects.append(Object(Point(0,0), Point(800,1), "bordertop"))
        self.Objects.append(Object(Point(800,0), Point(1, 600), "borderright"))
        self.Objects.append(Object(Point(0,0), Point(1, 600), "borderleft"))
        self.Objects.append(Object(Point(0,600), Point(800, 1), "borderbottom"))
                            
        # Now add in the remaining game objects (order matters, this is what will get drawn bottom to top)
        self.Paddle = Paddle(Point(10, 500))
        self.Ball = Ball(Point(400, 300))
        self.Objects.append(self.Paddle)
        self.Objects.append(self.Ball)

        # Add the bricks row, column
        for brick_y in range(0, 100, 25):
            for brick_x in range(0, 800, 35):
                new_brick = Brick(Point(brick_x, brick_y))
                self.Objects.append(new_brick)

    def check_input(self):
        if keyboard.is_pressed("left"):
            # Move Paddle Left
            self.Paddle.moveX(-self.PaddleSpeed)
            if self.Paddle.Location.X < 0: 
                self.Paddle.Location.X = 0
        elif keyboard.is_pressed("right"):
            self.Paddle.moveX(self.PaddleSpeed)
            if self.Paddle.Location.X + self.Paddle.Size.X > 800: 
                self.Paddle.Location.X = 800 - self.Paddle.Size.X
        elif keyboard.is_pressed("esc"):
            print("Exiting")
            self.Exit = True
    
    def move_ball(self):
        ''' If it's time to move the ball, let's move it '''
        self.Ball.move_for_velocity()
        # Does the ball collide with anything?  If so, bounce the ball
        for obj in self.Objects:
            if obj != self.Ball and self.Ball.is_colliding_basic(obj):
                print(f"Colliding with {obj.Name}")
                self.Ball.bounce()
        

    def start(self):
        ''' Start the game '''
        while True:
            if self.Exit: 
                break
            sleep(1/60)
            self.check_input()
            self.move_ball()
            # if we have any objects that need updating
            # then update them all
            if len([obj for obj in self.Objects if obj.IsDirty]):
                self.Graphics.clear()
                for obj in self.Objects:
                    self.Graphics.render(obj)
                self.Graphics.update_display()
            
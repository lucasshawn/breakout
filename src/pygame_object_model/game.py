from paddle import Paddle
from ball import Ball
from brick import Brick
from point import Point
from graphics import Graphics
from object import Object
from time import sleep, time
import keyboard

class Game():
    def __init__(self):
        # Init our game objects
        self.Exit = False
        self.PaddleSpeed = 10.0
        self.screen_limit = Point(800, 600)
        self.Graphics = Graphics(self.screen_limit)
        self.Objects = []

        # The following are the edges of the board so ball knows when it has hit an edge
        self.Objects.append(Object(Point(0,0), Point(800,1), "bordertop"))
        self.Objects.append(Object(Point(800,0), Point(1, 600), "borderright"))
        self.Objects.append(Object(Point(0,0), Point(1, 600), "borderleft"))
        self.Objects.append(Object(Point(0,600), Point(800, 1), "borderbottom"))
                            
        # Now add in the remaining game objects (order matters, this is what will get drawn bottom to top)
        self.Paddle = Paddle(Point(10, 500))
        self.Ball = Ball(Point(0,0))
        self.Objects.append(self.Paddle)
        self.Objects.append(self.Ball)

        # Add the bricks row, column
        # for brick_y in range(0, 100, 40):
        #     for brick_x in range(0, 800, 45):
        #         new_brick = Brick(Point(brick_x, brick_y))
        #         self.Objects.append(new_brick)

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
        elif keyboard.is_pressed("up"):
            limit = 8
            self.Ball.Speed += .2
            self.Ball.Speed = limit if self.Ball.Speed > limit else self.Ball.Speed
            print(f"Ball Speed: {self.Ball.Speed}")
        elif keyboard.is_pressed("down"):
            self.Ball.Speed -= .2
            self.Ball.Speed = 0 if self.Ball.Speed < 0 else self.Ball.Speed
            print(f"Ball Speed: {self.Ball.Speed}")
        elif keyboard.is_pressed("esc"):
            print("Exiting")
            self.Exit = True
        elif keyboard.is_pressed("space"):
            print(f"Paddle{self.Paddle.Location} Ball{self.Ball.Location}")
            self.move_ball()
        elif keyboard.is_pressed("c"):
            print(f"Checking for collision:")
            found_collision = False
            #for obj in filter(lambda o: o != self.Ball, self.Objects):
            r = self.Ball.get_collision_intersect(self.Paddle)
            print(f"Collision: {r}")
            #self.Ball.collide(self.Paddle)
            
    
    def move_ball(self):
        self.Ball.move_for_velocity()
        for obj in filter(lambda o: o != self.Ball, self.Objects):
            r = self.Ball.get_collision_intersect(self.Paddle)
            # (is_collision, collision_rect, run_rise_point) = self.Ball.get_collision_details(obj)
            # if is_collision:
            #     self.Ball.collide(obj)
                
    # def move_ball_old(self):
    #     ''' If it's time to move the ball, let's move it '''
    #     self.Ball.move_for_velocity()
    #     # Does the ball collide with anything?  If so, bounce the ball
    #     for obj in self.Objects:
    #         # We make decision about the direction of ball bounce based on what it hit
    #         if obj != self.Ball and self.Ball.is_colliding_basic(obj):
    #             print(f"Colliding with {obj}")
    #             if obj.Name == "Brick" or obj.Name == "bordertop" or obj.Name == "borderbottom" or obj.Name == "paddle":
    #                 self.Ball.Direction.Y *= -1
    #             elif obj.Name == "borderleft" or obj.Name == "borderright":
    #                 self.Ball.Direction.X *= -1
    #             # Protect ball from falling off the screen
    #             if self.Ball.Location.X < 0 or self.Ball.Location.Y < 0:
    #                 self.Ball.Direction = Point(1,1)
    #             if self.Ball.Location.X > self.screen_limit.X or self.Ball.Location.Y > self.screen_limit.Y:
    #                 self.Ball.Direction = Point(-1,-1)

    def start(self):
        ''' Start the game '''
        while True:
            if self.Graphics.is_exit() or self.Exit:
                break
            self.check_input()
            # self.move_ball()
            # if we have any objects that need updating
            # then update them all
            #if len([obj for obj in self.Objects if obj.IsDirty]):
            self.Graphics.clear()
            for obj in self.Objects:
                self.Graphics.render(obj)
            self.Graphics.update_display()
            self.Graphics.tick()
            
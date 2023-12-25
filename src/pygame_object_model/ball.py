from object import Object
from point import Point
import random

class Ball(Object):
    def __init__(self, location: Point):
        super().__init__(location, Point(5,5), "ball")
        self.Color = (255,0,0)
        self.Velocity = Point(1,1)

    def bounce(self):
        ''' The "bounce" will deflect the ball in a random direction with
            more weighting for velocity in a certain direction.  For example:
            if the ball was moving 10 on X, then it should move -10 on X
        '''
        if random.random()> .5:
            self.Velocity.X *= -1
        else:
            self.Velocity.Y *= -1
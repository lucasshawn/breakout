from object import Object
from point import Point
import random

class Ball(Object):
    def __init__(self, location: Point):
        super().__init__(location, Point(5,5), "ball")
        self.Speed = 2
        self.Color = (255,0,0)
        self.Direction = Point(1,1)

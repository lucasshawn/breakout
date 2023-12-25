from object import Object
from point import Point

class Paddle(Object):
    def __init__(self, location: Point):
        super().__init__(location, Point(20, 10), "paddle")
        self.Color = (0,255,0)
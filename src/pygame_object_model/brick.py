from object import Object
from point import Point

class Brick(Object):
    def __init__(self, location: Point):
        super().__init__(location, Point(30,20), "Brick")
        self.Color = (100,100,100)
from point import Point
from rect import Rect

class Object():
    def __init__(self):
        self.__init__(Point(0,0),Point(0,0))

    def __init__(self, location: Point, size: Point, name: str):
        self.Location = location
        self.Size = size
        self.IsDirty = True
        self.Color = (0,0,0)
        self.Name = name
        # By default objects don't move on their own
        self.Velocity = Point(0,0)

    def move_for_velocity(self)->Point:
        old_location = self.Location
        self.Location.X += self.Velocity.X
        self.Location.Y += self.Velocity.Y
        self.IsDirty = True
        return old_location
    
    def is_colliding_basic(self, collider: 'Object'):
        this_rc = Rect(self.Location, self.Size)
        collider_rc = Rect(collider.Location, collider.Size)
        return this_rc.is_colliding_basic(collider_rc)

    def moveX(self, move: float):
        self.Location.X += move
        self.IsDrity = True

    def moveY(self, move: float):
        self.Location.Y += move
        self.IsDirty = True
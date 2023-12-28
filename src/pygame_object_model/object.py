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
        self.Direction = Point(0,0)
        self.Speed = 1
    
    def X(self): return self.Location.X
    def Y(self): return self.Location.Y
    def Width(self): return self.Size.X
    def Height(self): return self.Size.Y

    def move_for_velocity(self)->Point:
        old_location = self.Location
        self.Location.X += self.Direction.X * self.Speed
        self.Location.Y += self.Direction.Y * self.Speed
        self.IsDirty = True
        return old_location
    
    def is_colliding_basic(self, collider: 'Object'):
        # this_rc = Rect(self.Location, self.Size)
        # collider_rc = Rect(collider.Location, collider.Size)
        # return this_rc.is_colliding_basic(collider_rc)
        return self.is_colliding(collider)

    def moveX(self, move: float):
        self.Location.X += move
        self.IsDrity = True

    def moveY(self, move: float):
        self.Location.Y += move
        self.IsDirty = True
    
    def is_colliding(self, collider: 'Object'):
        min_x = min(self.X(), collider.X())
        max_x = max(self.X() + self.Width(), collider.X() + collider.Width())
        min_y = min(self.Y(), collider.Y())
        max_y = max(self.Y() + self.Height(), collider.Y() + collider.Height())
        #print(f"min_x:{min_x} max_x:{max_x} min_y:{min_y} max_y:{max_y}")
        if abs(max_x - min_x) > (self.Width() + collider.Width()):
            return False
            #return collided on the left side
        if abs(max_y - min_y) > (self.Height() + collider.Height()):
            #return collided on the right side
            return False
        return True
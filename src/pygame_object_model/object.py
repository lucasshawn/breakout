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
        #self.Rect = Rect(self.Location, self.Size)
    
    def X(self): return self.Location.X
    def Y(self): return self.Location.Y
    def Width(self): return self.Size.X
    def Height(self): return self.Size.Y
    def Rect(self): return Rect(self.Location, self.Size)

    def __str__(self):
        return f"{self.Name}:{self.Location}"

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

    def collide(self, obj: "Object"):
        ''' The "bounce" will deflect the ball in a random direction with
            more weighting for velocity in a certain direction.  For example:
            if the ball was moving 10 on X, then it should move -10 on X
        '''
        print(f"Colliding with {obj}")
        #self.Ball.bounce(obj)
        self.Direction.X *= -1
        self.Direction.Y *= -1
        # if random.random()> .5:
        #     self.Direction.X *= -1
        # else:
        #     self.Direction.Y *= -1

    def get_collision_intersect(self, collider: 'Object')->Rect:
        ''' Return the intersected rectangle of two rectangles colliding '''
        self_rect = self.Rect()
        collider_rect = self.Rect()
        x1 = max(self_rect.ul.X, collider_rect.ul.X)
        y1 = max(self_rect.ul.Y, collider_rect.ul.Y)
        x2 = min(self_rect.lr.X, collider_rect.lr.X)
        y2 = min(self_rect.lr.Y, collider_rect.lr.Y)
        ret = Rect.from_points(x1,y1,x2,y2) if (y2-y1 > 0 and x2-x1 > 0) else Rect.from_points(0,0,0,0)
        print(f"{self.Name}: ul{self_rect.ul} lr{self_rect.lr}  {collider.Name}: ul{collider_rect.ul}  lr{collider_rect.lr}")
        print(f"{self.Name}: Rect({self})    Input Rect: {collider}   Intersect: {x1},{y1},{x2},{y2}   Ret: {ret}")
        return ret
        #return Rect.from_points(x1,y1,x2,y2)
    # def get_collision_details(self, collider: 'Object')->tuple[bool,Rect, Point]:
    #     intersection = self.Rect().intersection(collider.Rect())
    #     print(f"self.Rect({self.Rect()}) collider.Rect({collider.Rect()}) intersection({intersection})")
    #     if intersection.get_points() == (0,0,0,0):
    #         print(f"no intersection")
    #         return (False, None, None)
    #     print(f"Intersection: {intersection}")
            
    #     # Return the slope (angle of impact) for the two objects
    #     return (True, intersection, self.Rect.center().get_slope(collider.Rect.center()))
        # min_x = min(self.X(), collider.X())
        # max_x = max(self.X() + self.Width(), collider.X() + collider.Width())
        # min_y = min(self.Y(), collider.Y())
        # max_y = max(self.Y() + self.Height(), collider.Y() + collider.Height())
       
        # #print(f"min_x:{min_x} max_x:{max_x} min_y:{min_y} max_y:{max_y}")
        # if abs(max_x - min_x) > (self.Width() + collider.Width()):
        #     return False
        # if abs(max_y - min_y) > (self.Height() + collider.Height()):
        #     return False
        # return True


from point import Point
class Rect:

    def __init__(self):
        pass

    def __init__(self, ul: Point, ll: Point, ur: Point, lr: Point):
        self.ul = ul
        self.ll = ll
        self.ur = ur
        self.lr = lr
        self.size = Point(lr.x - ul.x, lr.y - ul.y)
        print(f"Rect 4 points Initializing: ul{self.ul} ll{self.ll} ur{self.ur} lr{self.lr}")

    def __init__(self, location: Point, size: Point):
        self.size = size
        self.ul = location
        self.ll = Point(self.ul.X, self.ul.Y + size.Y)
        self.ur = Point(self.ul.X + size.X, self.ul.Y)
        self.lr = Point(self.ul.X + size.X, self.ul.Y + size.Y)
        print(f"Rect Point/Size Initializing: ul{self.ul} ll{self.ll} ur{self.ur} lr{self.lr}")

    [staticmethod]
    def from_points(x1: int, y1: int, x2: int, y2: int)->"Rect":
        print(f"Rect Class Factory")
        return Rect(Point(x1,y1), Point(x2-x1, y2-y1))
    
    def get_points(self)->tuple[int, int, int, int]:
        return self.ul.X, self.ul.Y, self.lr.X, self.lr.Y

    def size(self)->Point:
        ''' Returns a Point struct of (W, Y) '''
        return Point(self.ur.X - self.ul.X, 
            self.lr.Y - self.ur.Y)
    
    def is_colliding_basic(self, r: "Rect"):
        ''' This only works for flat 4 sided poly's
        '''
        return (r.ul.X < self.ur.X and r.ur.X > self.ul.X and
          r.ul.Y < self.ll.Y and r.ll.Y > self.ul.Y)

    def intersection(self, r: "Rect"):
        ''' Return the intersected rectangle of two rectangles colliding '''
        x1 = max(self.ul.X, r.ul.X)
        y1 = max(self.ul.Y, r.ul.Y)
        x2 = min(self.lr.X, r.lr.X)
        y2 = min(self.lr.Y, r.lr.Y)
        ret = Rect.from_points(x1,y1,x2,y2) if (y2-y1 > 0 and x2-x1 > 0) else Rect.from_points(0,0,0,0)
        print(f"Self Rect({self})    Input Rect: {r}   Intersect: {x1},{y1},{x2},{y2}   Ret: {ret}")
        return ret
        #return Rect.from_points(x1,y1,x2,y2)

    def center(self)->Point:
        ''' Return the exact center of the rectangle '''
        return Point((self.ul.X + self.ur.X)/2, (self.lr.Y + self.lr.Y)/2)


    def __str__(self)->str:
        return f"Loc({self.ul.X},{self.ul.Y}) Size({self.size.X},{self.size.Y})"
    

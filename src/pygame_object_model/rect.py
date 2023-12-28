from point import Point
class Rect:
    def __init__(self, ul: Point, ll: Point, ur: Point, lr: Point):
        self.ul = ul
        self.ll = ll
        self.ur = ur
        self.lr = lr

    def __init__(self, location: Point, size: Point):
        self.ul = location
        self.size = size
        self.ll = Point(self.ul.X, self.ul.Y + size.Y)
        self.ur = Point(self.ul.X + size.X, self.ul.Y)
        self.lr = Point(self.ur.X, self.ur.Y + size.Y)

    def size(self)->Point:
        ''' Returns a Point struct of (W, Y) '''
        return Point(self.ur.X - self.ul.X, 
            self.lr.Y - self.ur.Y)
    
    def is_colliding_basic(self, r: "Rect"):
        ''' This only works for flat 4 sided poly's
        '''
        return (r.ul.X < self.ur.X and r.ur.X > self.ul.X and
          r.ul.Y < self.ll.Y and r.ll.Y > self.ul.Y)

    def __str__(self)->str:
        return f"({self.ul.X},{self.ul.Y},{self.size.X},{self.size.Y})"

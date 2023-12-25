class Point():
    def __init__(self, x:float=0, y:float=0):
        self.X = x
        self.Y = y
    def __str__(self):
        return f"({self.X},{self.Y})"
    def offset_x(self, offset: float):
        self.X += offset
    def offset_y(self, offset: float):
        self.Y += offset
    def int_x(self): return int(self.X)
    def int_y(self): return int(self.Y)
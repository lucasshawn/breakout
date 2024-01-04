from enum import Flag, auto

class Direction(Flag):
    TOP = auto()
    BOTTOM = auto()
    LEFT = auto()
    RIGHT = auto()
    NONE = auto()
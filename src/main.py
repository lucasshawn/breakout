

# bricks array
# paddle array
# ball location

# run the game
from time import sleep
import keyboard
import sys

class Vector():
    def __init__(self, x:float=0, y:float=0):
        self.X = x
        self.Y = y
    def __str__(self):
        return f"({self.X},{self.Y})"
    def offset_x(self, offset: float):
        self.X += offset
    def offset_y(self, offset: float):
        self.Y += offset

PaddleSpeed = .5
BoardDirty = True

Exit = False
Bricks = [Vector(0,0),Vector(20,0), Vector(40,0)]
Ball = Vector(0.0,100.0)
Paddle = Vector(0.0,110.0)


def check_input():
    global Exit, BoardDirty, Paddle
    if keyboard.is_pressed("left"):
        # Move Paddle Left
        Paddle.offset_x(-PaddleSpeed)
        if Paddle.X < 0: 
            Paddle.X = 0
        else:
            BoardDirty = True
    elif keyboard.is_pressed("right"):
        Paddle.offset_x(PaddleSpeed)
        if Paddle.X > 100: 
            Paddle.X = 100
        else:
            BoardDirty = True
    elif keyboard.is_pressed("esc"):
        print("Exiting")
        Exit = True

def update_board():
    global BoardDirty
    if BoardDirty:
        print(f"Paddle({Paddle}) Ball({Ball})")
        BoardDirty = False

def main():
    while True:
        if Exit: 
            break
        sleep(1/60)
        check_input()
        update_board()

main()
print("Thank you for playing.")
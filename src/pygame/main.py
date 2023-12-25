

# bricks array
# paddle array
# ball location

# run the game
from time import sleep
import keyboard
import sys
import pygame

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
    def int_x(self): return int(self.X)
    def int_y(self): return int(self.Y)

PaddleSpeed = .5
BoardDirty = True

Exit = False
Bricks = [Vector(0,0),Vector(25,0), Vector(50,0)]

Ball = Vector(0.0,100.0)
Paddle = Vector(0.0,110.0)
PyGameSurface = None
PyGameScreen = None

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

def pygame_update_board():
    global BoardDirty

    gray = (100,100,100)
    black = (0,0,0)
    red = (255,0,0)
    dark_gray = (50,50,50)
    if BoardDirty:
        PyGameScreen.fill(black)
        # Draw the paddle
        pygame.draw.rect(PyGameScreen, gray, pygame.Rect(Paddle.int_x(), Paddle.int_y(), 20, 10))

        # Draw the ball
        pygame.draw.rect(PyGameScreen, red, pygame.Rect(Ball.int_x(), Ball.int_y(), 3, 3))
                         
        # Draw the bricks
        for brick in Bricks:
            pygame.draw.rect(PyGameScreen, dark_gray, pygame.Rect(brick.int_x(), brick.int_y(), 20, 10))
        
        pygame.display.update()
        BoardDirty = False
    
def pygame_init():
    global PyGameSurface, PyGameScreen

    pygame.init()
    PyGameSurface = pygame.Surface((500, 300))
    PyGameScreen = pygame.display.set_mode((800, 600))

def main():
    pygame_init()
    while True:
        if Exit: 
            break
        sleep(1/60)
        check_input()
        pygame_update_board()

main()
print("Thank you for playing.")
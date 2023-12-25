import pygame
from point import Point
from object import Object

class Graphics:
    def __init__(self, board_size: Point):
        pygame.init()
        #self.surface = pygame.Surface((board_size.X, board_size.Y))
        self.display = pygame.display.set_mode((board_size.X, board_size.Y))
        self.display_dirty = True

    def clear(self):
        self.display.fill((0,0,0))

    def render(self, obj: Object):
        pygame.draw.rect(self.display, obj.Color, 
            pygame.Rect(obj.Location.X, obj.Location.Y,
                        obj.Size.X, obj.Size.Y))
    
    def update_display(self):
        #pygame.display.update()
        pygame.display.flip()
        self.display_dirty = False
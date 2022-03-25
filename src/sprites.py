from pygame import Rect
from settings import *

class Player():
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.width = 10
        self.height = 20
        
    def update(self):
        self.x += 1
        
    def draw(self):
        pg.draw.rect(screen, BLUE, pg.Rect(self.x, self.y, self.width, self.height))
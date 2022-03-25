from abc import abstractmethod
from pygame import Rect
from settings import *

class GameObject(): # pretty useless at the minute but will becomu useful
    def __init__(self, x, y):
        self.x, self.y = x, y
    def draw(self, camera):
        self.x -= camera.x
        self.y -= camera.y
        self.drawObj()
        self.x += camera.x
        self.y +=camera.y
    @abstractmethod
    def drawObj(self):
        pass
        

class Player(GameObject):
    def __init__(self, x, y, width, height):
        GameObject.__init__(self, x, y)
        self.width = width
        self.height = height
        
    def update(self):
        self.x += 1
        
    def drawObj(self):
        pg.draw.rect(screen, BLUE, pg.Rect(self.x, self.y, self.width, self.height))
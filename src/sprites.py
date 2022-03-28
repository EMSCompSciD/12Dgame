from settings import *

# A game object class that all objects should inherit from.
class GameObject():
    def __init__(self, x, y):
        self.x, self.y = x, y
    def draw(self, camera):
        self.x -= camera.x
        self.y -= camera.y
        self.drawObj()
        self.x += camera.x
        self.y +=camera.y
        
    # all child classess need the method drawObj() so we can use the draw method
    def drawObj(self):
        pass
        

class Player(GameObject):
    def __init__(self, x, y, width, height):
        GameObject.__init__(self, x, y)
        self.width = width
        self.height = height
    # a sample update class     
    def update(self):
        self.x += 1
    # this is the method that all child classes of Game object need. It is designed to allow us to use the camera
    # system.
    def drawObj(self):
        pg.draw.rect(screen, BLUE, pg.Rect(self.x, self.y, self.width, self.height))
        
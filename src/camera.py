from turtle import width
from settings import *
class Camera():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def centerObj(self, obj):
        self.x = obj.x-WIDTH//2
        self.y = obj.y-HEIGHT//2
    def centerPos(self, x, y):
        self.x = x-WIDTH//2
        self.y = y-HEIGHT//2
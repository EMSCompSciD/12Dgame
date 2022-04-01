import pygame as pg
import ctypes

user32 = ctypes.windll.user32

WIDTH = user32.GetSystemMetrics(0) # window width
HEIGHT = user32.GetSystemMetrics(1) # window height

FPS = 30

# Define Colors for testing purposes - we can add sprites later
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pg.display.set_mode((WIDTH, HEIGHT)) # the reason I have put screen in setting is that to use the draw
# function in any sprites we need access to the screen variable.
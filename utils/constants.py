from os import path

#screen
SCREEN_HEIGHT = 480
SCREEN_WIDTH = 800
TITLE = "frutloops"

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#da en directorio del file
#los dos puntos son para retroceder
#join es para unir varias cosas
IMG_DIR = path.join(path.dirname(__file__), "..", "img")

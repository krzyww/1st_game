import pygame
import random
from assets.assets import img


class enemies:
    def enemy():
        return pygame.Rect(random.randint(1,1100), random.randint(1,300), img.ENEMY1_WIDTH, img.ENEMY1_HEIGHT)

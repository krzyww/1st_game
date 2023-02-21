import pygame
import random
from assets.assets import img

class DefaultEnemy:
    def __init__(self) -> None:
        self.start_x = random.randint(1,1100)
        self.start_y = random.randint(1,300)
        self.size_x = img.ENEMY1_WIDTH
        self.size_y = img.ENEMY1_HEIGHT


class Enemy(DefaultEnemy):
    def __init__(self) -> None:
        super().__init__()


    def small_enemy(self):
        
        return pygame.Rect(self.start_x, self.start_y,
                           self.size_x, self.size_y)

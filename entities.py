import pygame
import random, os


class DefaultEnemy:
    def __init__(self) -> None:
        self.width = 300
        self.height = 300

    def aaa(self):
        self.image = pygame.image.load(os.path.join('assets','enemy.png'))
        self.enemy = pygame.transform.scale(self.image, (self.width, self.height))
        self.start_x = random.randint(1,1100)
        self.start_y = random.randint(1,300)
        self.rect = pygame.Rect(self.start_x, self.start_y, self.width, self.height)

    def set_height(self, value):
        self.height = value

    def set_width(self, value):
        self.width = value


class SpawnSmallEnemy(DefaultEnemy):
    def __init__(self) -> None:
        super().__init__()
        self.set_height(30)
        self.set_width(30)
        self.aaa()




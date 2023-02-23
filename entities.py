import pygame
import random
import os


class DefaultEnemy:
    def __init__(self) -> None:
        self.width = 300
        self.height = 300
        self.image = pygame.image.load(os.path.join('assets', 'enemy.png'))
        self.start_x = random.randint(200, 1000)
        self.start_y = random.randint(1, 300)

    def calculations(self):
        self.enemy = pygame.transform.scale(
            self.image, (self.width, self.height))
        self.rect = pygame.Rect(
            self.start_x, self.start_y, self.width, self.height)

    def set_height(self, value):
        self.height = value

    def set_width(self, value):
        self.width = value


class SpawnSmallEnemy(DefaultEnemy):
    def __init__(self) -> None:
        super().__init__()
        self.set_height(30)
        self.set_width(30)
        self.calculations()


class SpawnRafal(DefaultEnemy):
    def __init__(self) -> None:
        super().__init__()
        self.set_height(60)
        self.set_width(60)
        self.image = pygame.image.load(os.path.join('assets', 'enemy2.png'))
        self.calculations()

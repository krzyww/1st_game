import pygame
import random, os


class DefaultEnemy:
    def __init__(self) -> None:
        self.image = pygame.image.load(os.path.join('assets','enemy.png'))
        self.enemy = pygame.transform.scale(self.image, (self.width, self.height))
        self.start_x = random.randint(1,1100)
        self.start_y = random.randint(1,300)
        self.rect = pygame.Rect(self.start_x, self.start_y, self.width, self.height)


class SpawnSmallEnemy(DefaultEnemy):
    def __init__(self) -> None:
        self.width = 30
        self.height = 30
        super().__init__()




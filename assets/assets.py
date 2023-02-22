import pygame, os

class img:
    pygame.font.init()
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    FPS = 60
    VEL = 10
    BULLET_VEL = 15

    HIT = pygame.USEREVENT + 1
    HIT_FONT = pygame.font.SysFont('consolas', 40)

    WIDTH, HEIGHT = 1200, 1200
    WIN = pygame.display.set_mode((WIDTH,HEIGHT))

    SHIP_WIDTH, SHIP_HIGHT = 80, 80
    SHIP_IMAGE = pygame.image.load(os.path.join('assets','craft.png'))
    SHIP = pygame.transform.scale(SHIP_IMAGE, (SHIP_WIDTH, SHIP_HIGHT))

    BULLET_WIDTH, BULLET_HEIGHT = 20, 20
    BULLET_IMAGE = pygame.image.load(os.path.join('assets','bullet.png'))
    BULLET = pygame.transform.scale(BULLET_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT))

    BKG_IMAGE = pygame.image.load(os.path.join('assets','background.png'))
    BKG = pygame.transform.scale(BKG_IMAGE, (WIDTH, HEIGHT))
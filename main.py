import pygame
import os
import random

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
FPS = 60
VEL = 10
BULLET_VEL = 15

WIDTH, HEIGHT = 1200, 1200
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

SHIP_WIDTH, SHIP_HIGHT = 80, 80
SHIP_IMAGE = pygame.image.load(os.path.join('assets','craft.png'))
SHIP = pygame.transform.scale(SHIP_IMAGE, (SHIP_WIDTH, SHIP_HIGHT))

ENEMY1_WIDTH, ENEMY1_HEIGHT = 30, 30
ENEMY1_IMAGE = pygame.image.load(os.path.join('assets','enemy.png'))
ENEMY1 = pygame.transform.scale(ENEMY1_IMAGE, (ENEMY1_WIDTH, ENEMY1_HEIGHT))

BULLET_WIDTH, BULLET_HEIGHT = 20, 20
BULLET_IMAGE = pygame.image.load(os.path.join('assets','bullet.png'))
BULLET = pygame.transform.scale(BULLET_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT))



def draw_window(player, enemy, bullets):
    WIN.fill((111,111,120))
    WIN.blit(SHIP, (player.x, player.y))
    WIN.blit(ENEMY1, (enemy.x, enemy.y))
    for bul in bullets:
        WIN.blit(BULLET, bul)
    pygame.display.update()

def player_movement(keys_pressed, player):
    if keys_pressed[pygame.K_LEFT] and player.x > 0:     #left
        player.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and player.x < WIDTH-SHIP_WIDTH:     #right
        player.x += VEL       
    if keys_pressed[pygame.K_DOWN] and player.y < HEIGHT-SHIP_HIGHT:     #down
        player.y += VEL
    if keys_pressed[pygame.K_UP] and player.y > 0:     #up
        player.y -= VEL

def enemy_movement_1(enemy):
    enemy.x += random.randint(-5,5)
    enemy.y += random.randint(-5,6)

def handle_bullets(bullets,enemy):
    for bul in bullets:
        bul[1] = int(bul[1]) - BULLET_VEL
        bullet = pygame.Rect(bul[0], bul[1], BULLET_WIDTH, BULLET_HEIGHT)
        if bullet.colliderect(enemy):
            bullets.remove(bul)
        elif bul[1] < 0:
            bullets.remove(bul)

def main():
    player = pygame.Rect(600, 800, SHIP_WIDTH, SHIP_HIGHT)
    enemy = pygame.Rect(600, 150, ENEMY1_WIDTH, ENEMY1_HEIGHT)
    
    bullets = []
    enemies = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    img_bull_position = [player.x + SHIP_WIDTH//2 - BULLET_WIDTH//2, player.y]
                    bullets.append(img_bull_position)

        keys_pressed = pygame.key.get_pressed()
        handle_bullets(bullets, enemy)
        player_movement(keys_pressed, player)
        enemy_movement_1(enemy)
        draw_window(player, enemy, bullets)

    pygame.quit()


if __name__ == "__main__":
    main()
import pygame
import random
from assets.assets import img


def draw_window(player, enemies, bullets, hits):
    img.WIN.blit(img.BKG,(0, 0))
    img.WIN.blit(img.SHIP, (player.x, player.y))
    for ene in enemies:
        img.WIN.blit(img.ENEMY1, (ene.x, ene.y))
    for bul in bullets:
        img.WIN.blit(img.BULLET, bul)

    aaa = img.HIT_FONT.render("Hits: " + str(hits), 1, img.WHITE)
    img.WIN.blit(aaa,(0,0))
    pygame.display.update()

def player_movement(keys_pressed, player):
    if keys_pressed[pygame.K_LEFT] and player.x > 0:     #left
        player.x -= img.VEL
    if keys_pressed[pygame.K_RIGHT] and player.x < img.WIDTH-img.SHIP_WIDTH:     #right
        player.x += img.VEL       
    if keys_pressed[pygame.K_DOWN] and player.y < img.HEIGHT-img.SHIP_HIGHT:     #down
        player.y += img.VEL
    if keys_pressed[pygame.K_UP] and player.y > 0:     #up
        player.y -= img.VEL

def enemy_movement_1(enemies):
    for ene in enemies:
        ene.x += random.randint(-5,5)
        ene.y += random.randint(-5,6)

def handle_bullets(bullets,enemies):
    for bul in bullets:
        bul[1] = int(bul[1]) - img.BULLET_VEL
        bullet = pygame.Rect(bul[0], bul[1], img.BULLET_WIDTH, img.BULLET_HEIGHT)
        for ene in enemies:
            if bul[1] < 0:
                try:
                    bullets.remove(bul)
                except ValueError:
                    pass
            elif bullet.colliderect(ene):
                bullets.remove(bul)
                enemies.remove(ene)
                pygame.event.post(pygame.event.Event(img.HIT))
                enemies.append(pygame.Rect(random.randint(1,1100), random.randint(1,300), img.ENEMY1_WIDTH, img.ENEMY1_HEIGHT))


def enemyy():
    return pygame.Rect(random.randint(1,1100), random.randint(1,300), img.ENEMY1_WIDTH, img.ENEMY1_HEIGHT)


def main():
    player = pygame.Rect(600, 800, img.SHIP_WIDTH, img.SHIP_HIGHT)    
    bullets = []
    enemies = [enemyy(), enemyy(), enemyy(), enemyy(), enemyy()]
    hits = 0
 
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(img.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    img_bull_position = [player.x + img.SHIP_WIDTH//2 - img.BULLET_WIDTH//2, player.y]
                    bullets.append(img_bull_position)
            if event.type == img.HIT:
                hits += 1

        keys_pressed = pygame.key.get_pressed()
        handle_bullets(bullets, enemies)
        player_movement(keys_pressed, player)
        enemy_movement_1(enemies)
        draw_window(player, enemies, bullets, hits)

    pygame.quit()


if __name__ == "__main__":
    main()
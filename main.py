import pygame
import random
from assets.assets import img
from entities import SpawnRafal, SpawnSmallEnemy


def draw_window(player, enemies: list, bullets: list, hits: int):
    img.WIN.blit(img.BKG, (0, 0))
    img.WIN.blit(img.SHIP, (player.x, player.y))
    for ene in enemies:
        img.WIN.blit(ene.enemy, (ene.rect.x, ene.rect.y))
    for bul in bullets:
        img.WIN.blit(img.BULLET, bul)

    aaa = img.HIT_FONT.render("Hits: " + str(hits), 1, img.WHITE)
    img.WIN.blit(aaa, (0, 0))
    pygame.display.update()


def player_movement(keys_pressed, player):
    # left
    if keys_pressed[pygame.K_LEFT] and player.x > 0:
        player.x -= img.VEL
    # right
    if keys_pressed[pygame.K_RIGHT] and player.x < img.WIDTH-img.SHIP_WIDTH:
        player.x += img.VEL
    # down
    if keys_pressed[pygame.K_DOWN] and player.y < img.HEIGHT-img.SHIP_HIGHT:
        player.y += img.VEL
    # up
    if keys_pressed[pygame.K_UP] and player.y > 0:
        player.y -= img.VEL


def enemy_movement_1(enemies: list):
    for ene in enemies:
        ene.rect.x += random.randint(-5, 5)
        ene.rect.y += random.randint(-5, 6)


def handle_bullets(bullets: list, enemies: list):
    for bul in bullets:
        bul[1] = int(bul[1]) - img.BULLET_VEL
        bullet = pygame.Rect(
            bul[0], bul[1], img.BULLET_WIDTH, img.BULLET_HEIGHT)
        for ene in enemies:
            if bul[1] < 0:
                try:
                    bullets.remove(bul)
                except ValueError:
                    pass
            elif bullet.colliderect(ene.rect):
                try:
                    bullets.remove(bul)
                except ValueError:
                    pass
                enemies.remove(ene)
                pygame.event.post(pygame.event.Event(img.HIT))
                enemies.append(SpawnSmallEnemy())
                enemies.append(SpawnRafal())


def main():
    player = pygame.Rect(img.WIDTH/2, img.HEIGHT*3/4,
                         img.SHIP_WIDTH, img.SHIP_HIGHT)
    bullets = []
    enemies = [SpawnSmallEnemy()]
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
                    img_bull_position = [
                        player.x + img.SHIP_WIDTH//2 - img.BULLET_WIDTH//2,
                        player.y]
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

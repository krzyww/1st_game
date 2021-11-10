import pygame

WIDTH, HEIGHT = 1024, 768
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

FPS = 60


def draw_window():
    WIN.fill((111,111,111))
    
    
    
    pygame.display.update()



def main():
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()




if __name__ == "__main__":
    main()
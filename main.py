import pygame

WIDTH, HEIGHT = 1024, 768
WIN = pygame.display.set_mode((WIDTH,HEIGHT))




def main():

    clock = pygame.time.Clock()
    run = True

    while run:
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()



if __name__ == "__main__":
    main()
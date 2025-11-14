"""Simple movable square demo for pygame2.

Guarded by `if __name__ == '__main__'` so importing this module won't
run the demo automatically.
"""

import pygame


def main():
    # init pygame
    pygame.init()

    # create screen
    WIDTH, HEIGHT = 500, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Second Pygame Game Game")
    clock = pygame.time.Clock()

    # running variable
    running = True

    x = 250
    y = 250
    speed = 5

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 0, 255), (x, y, 50, 50))
        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()

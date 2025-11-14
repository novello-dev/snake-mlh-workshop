"""Simple intro demo for Neon Snake.

This module draws shapes and listens for a keypress. It's safe to import
without running the demo because the execution is guarded by
`if __name__ == "__main__"`.
"""

import pygame


def main():
    pygame.init()

    # create the screen
    WIDTH, HEIGHT = 500, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Neon Snake")

    # loop control variable
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # this ends the main while

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("W key was pressed!")

        pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 100))
        pygame.draw.circle(screen, (0, 255, 0), (250, 250), 50)

        pygame.display.flip()

    # closes pygame
    pygame.quit()


if __name__ == "__main__":
    main()

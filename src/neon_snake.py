import random
import sys

import pygame

# Configuration constants
WINDOW_SIZE = 500
BLOCK = 10
FONT_NAME = "consolas"
FONT_SIZE = 20
DEFAULT_SPEED = 15


class NeonSnake:

    def __init__(self):
        # initialize pygame
        pygame.init()
        # player's score
        self.score = 0
        # set the window
        self.window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        # font object
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
        # important colors
        self.blue = pygame.Color(0, 0, 255)
        self.green = pygame.Color(149, 212, 122)
        self.red = pygame.Color(255, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.black = pygame.Color(0, 0, 0)
        self.pink = pygame.Color(246, 143, 160)
        self.aqua = pygame.Color(0, 176, 178)
        # set the speed of snake
        self.speed = DEFAULT_SPEED
        # head (start position)
        self.head = [100, 50]
        # initial snake blocks
        self.snake_blocks = [[100, 50], [90, 50], [80, 50], [70, 50]]
        # default direction of snake
        self.direction = "RIGHT"
        self.next_direction = self.direction
        # fruit control
        self.eaten = False
        # initial fruit position
        self.fruit_pos = self._random_fruit_pos()

    def show_score(self):
        """
        Function that shows the score of the player
        """
        score_surface = self.font.render(f"Score: {self.score}", True, self.black)
        score_rect = score_surface.get_rect()
        self.window.blit(score_surface, score_rect)

    def spawn_fruit(self):
        """
        Function that spawns fruit randomly in the window
        """
        self.fruit_pos = self._random_fruit_pos()

    def _random_fruit_pos(self):
        """Return a random fruit position that does not collide with the snake."""
        max_cells = WINDOW_SIZE // BLOCK
        while True:
            pos = (
                random.randrange(0, max_cells) * BLOCK,
                random.randrange(0, max_cells) * BLOCK,
            )
            # make sure fruit doesn't spawn on the snake
            if list(pos) not in self.snake_blocks:
                return pos

    def keyboard(self, key):
        """
        Function that handles keyboard events
        """
        if key == pygame.K_UP:
            self.next_direction = "UP"
        elif key == pygame.K_DOWN:
            self.next_direction = "DOWN"
        elif key == pygame.K_LEFT:
            self.next_direction = "LEFT"
        elif key == pygame.K_RIGHT:
            self.next_direction = "RIGHT"

        # prevent reversing into itself
        if self.next_direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif self.next_direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        elif self.next_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif self.next_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

    def snake_mech(self):
        """
        Function that takes care of the snake's mechanism.
        Since the snake's blocks are 10x10, i'll be adding by TENS
        """
        # draw the fruit
        pygame.draw.rect(
            self.window,
            self.pink,
            pygame.Rect(self.fruit_pos[0], self.fruit_pos[1], BLOCK, BLOCK),
        )

        # insert new head position
        self.snake_blocks.insert(0, list(self.head))

        # check if we ate the fruit
        if self.head[0] == self.fruit_pos[0] and self.head[1] == self.fruit_pos[1]:
            self.score += 10
            self.eaten = True
        else:
            # remove the last block if we didn't grow
            self.snake_blocks.pop()

        # draw snake
        for pos in self.snake_blocks:
            pygame.draw.rect(
                self.window, self.aqua, pygame.Rect(pos[0], pos[1], BLOCK, BLOCK)
            )

        # move the snake head
        if self.direction == "UP":
            self.head[1] -= BLOCK
        elif self.direction == "DOWN":
            self.head[1] += BLOCK
        elif self.direction == "LEFT":
            self.head[0] -= BLOCK
        elif self.direction == "RIGHT":
            self.head[0] += BLOCK

        # check if snake is out of the screen
        if self.head[0] < 0 or self.head[0] > WINDOW_SIZE - BLOCK:
            self.game_over()
        if self.head[1] < 0 or self.head[1] > WINDOW_SIZE - BLOCK:
            self.game_over()

        # touching the snake's body makes you lose
        for block in self.snake_blocks[1:]:
            if self.head[0] == block[0] and self.head[1] == block[1]:
                self.game_over()

    def game_over(self):
        """
        Function that handles when the game is over
        """
        game_over_surface = self.font.render("You lost!", True, self.red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (WINDOW_SIZE // 2, WINDOW_SIZE // 2)
        self.window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    def start(self):
        """
        Main function that runs the whole game
        """
        pygame.display.set_caption("MLH Snake Game")
        fps = pygame.time.Clock()
        running = True

        while running:
            self.window.fill(self.green)
            self.show_score()

            # check events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    self.keyboard(event.key)

            # snake mechanism
            self.snake_mech()

            # check if fruit was eaten
            if self.eaten:
                self.spawn_fruit()
                self.eaten = False

            pygame.display.update()
            fps.tick(self.speed)

        pygame.quit()


if __name__ == "__main__":
    game = NeonSnake()
    game.start()

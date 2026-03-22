import pygame
import sys
import random

# -------------------- settings --------------------
CELL = 20                # size of cell (pixels)
GRID_W, GRID_H = 32, 24  # field size in cells (width x height)
W, H = GRID_W * CELL, GRID_H * CELL


BG_COLOR = (18, 18, 18)
GRID_COLOR = (30, 30, 30)
SNAKE_HEAD = (80, 200, 120)
SNAKE_BODY = (60, 160, 100)
FOOD_COLOR = (220, 70, 70)
TEXT_COLOR = (230, 230, 230)
# --------------------------------------------------

def draw_grid(surface):
    """Draws the grid on the screen"""
    for x in range(0, W, CELL):
        pygame.draw.line(surface, GRID_COLOR, (x, 0), (x, H))
    for y in range(0, H, CELL):
        pygame.draw.line(surface, GRID_COLOR, (0, y), (W, y))



def main():
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 20)
    big_font = pygame.font.SysFont("consolas", 36)

    while True:
        # --------------- Events ----------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # --------------- Render ----------------
        screen.fill(BG_COLOR)
        draw_grid(screen)

        pygame.display.flip()



if __name__ == "__main__":
    main()
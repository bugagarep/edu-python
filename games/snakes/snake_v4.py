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

def draw_cell(surface, position, color):
    x, y = position
    rect = pygame.Rect(x * CELL, y * CELL, CELL, CELL)
    pygame.draw.rect(surface, color, rect, border_radius=3)
    
def rand_empty_cell(occupied):
    while True:
        x = random.randint(0, GRID_W - 1)
        y = random.randint(0, GRID_H - 1)
        if (x, y) not in occupied:
            return (x, y)
    

def main():
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 20)
    big_font = pygame.font.SysFont("consolas", 36)


    x, y = GRID_W//2, GRID_H//2
    snake = [(x, y), (x-1, y), (x-2, y)]
    
    food = rand_empty_cell(set(snake))

    dx = 1
    dy = 0
    while True:
        # --------------- Events ----------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dx = 0
                    dy = -1
                if event.key == pygame.K_DOWN:
                    dx = 0
                    dy = 1
                if event.key == pygame.K_LEFT:
                    dx = -1
                    dy = 0
                if event.key == pygame.K_RIGHT:
                    dx = 1
                    dy = 0

        # ---------------------------------------
        h_x, h_y = snake[0]
        new_head = (h_x + dx, h_y + dy)
        snake.insert(0, new_head)
        if new_head == food:
            food = rand_empty_cell(set(snake))
        else:
            snake.pop()
        # --------------- Render ----------------
        screen.fill(BG_COLOR)
        draw_grid(screen)
        
        draw_cell(screen, food, FOOD_COLOR)
        for i, seg in enumerate(snake):
            draw_cell(screen, seg, SNAKE_HEAD if i == 0 else SNAKE_BODY)                          
        
        
        pygame.display.flip()
        clock.tick(5)


if __name__ == "__main__":
    main()

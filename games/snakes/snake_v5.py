import pygame
import sys
import random

# -------------------- settings --------------------
CELL = 20                # size of cell (pixels)
GRID_W, GRID_H = 32, 24  # field size in cells (width x height)
W, H = GRID_W * CELL, GRID_H * CELL
FPS_START = 5          
SPEEDUP_EVERY = 3        
SPEEDUP_STEP = 1         

BG_COLOR = (18, 18, 18)
GRID_COLOR = (30, 30, 30)
SNAKE_HEAD = (80, 200, 120)
SNAKE_BODY = (60, 160, 100)
FOOD_COLOR = (220, 70, 70)
TEXT_COLOR = (230, 230, 230)
PAUSE_OVERLAY = (0, 0, 0, 120)

# direction (dx, dy)
UP    = (0, -1)
DOWN  = (0, 1)
LEFT  = (-1, 0)
RIGHT = (1, 0)
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
 
def text(surface, font, s, x, y, color=TEXT_COLOR, center=False):
    img = font.render(s, True, color)
    rect = img.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    surface.blit(img, rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 20)
    big_font = pygame.font.SysFont("consolas", 36)
    best_score = 0

    def new_game():
        snake = [(GRID_W // 2, GRID_H // 2)]
        direction = random.choice([UP, DOWN, LEFT, RIGHT])
        for _ in range(2):
            tail_dx, tail_dy = (-direction[0], -direction[1])
            tx = snake[-1][0] + tail_dx
            ty = snake[-1][1] + tail_dy
            snake.append((tx, ty))
        food = rand_empty_cell(set(snake))
        score = 0
        fps = FPS_START
        paused = False
        game_over = False
        return snake, direction, food, score, fps, paused, game_over

    snake, direction, food, score, fps, paused, game_over = new_game()

    pending_dir = direction

    while True:
        # --------------- Events ----------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_p and not game_over:
                    paused = not paused

                if event.key == pygame.K_r and game_over:
                    snake, direction, food, score, fps, paused, game_over = new_game()
                    pending_dir = direction
                    
                if event.key in (pygame.K_UP, pygame.K_w):
                    if direction != DOWN:
                        pending_dir = UP
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    if direction != UP:
                        pending_dir = DOWN
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    if direction != RIGHT:
                        pending_dir = LEFT
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    if direction != LEFT:
                        pending_dir = RIGHT

        if paused:
            screen.fill(BG_COLOR)
            draw_grid(screen)
            
            for i, seg in enumerate(snake):
                draw_cell(screen, seg, SNAKE_HEAD if i == 0 else SNAKE_BODY)
                
            draw_cell(screen, food, FOOD_COLOR)
            text(screen, big_font, "Pause", W//2, H//2-24, center=True)
            text(screen, font, "Press P to continue", W//2, H//2+12, center=True)
            pygame.display.flip()
            clock.tick(5)
            continue
        
        if not game_over:
            # --------------- Playing ----------------
            direction = pending_dir
            head_x, head_y = snake[0]
            dx, dy = direction
            new_head = (head_x + dx, head_y + dy)

            x, y = new_head
            if x < 0 or x >= GRID_W or y < 0 or y >= GRID_H:
                game_over = True
            elif new_head in snake:
                game_over = True
            else:
                snake.insert(0, new_head)
                if new_head == food:
                    score += 1
                    if score % SPEEDUP_EVERY == 0:
                        fps += SPEEDUP_STEP
                    food = rand_empty_cell(set(snake))
                else:
                    snake.pop()        
        
        # --------------- Render ----------------
        screen.fill(BG_COLOR)
        draw_grid(screen)
        
        draw_cell(screen, food, FOOD_COLOR)
        for i, seg in enumerate(snake):
            draw_cell(screen, seg, SNAKE_HEAD if i == 0 else SNAKE_BODY)                          
        
        # ------------- info --------------------
        best_score = max(best_score, score)
        text(screen, font, f"Score: {score}", 10, 8)
        text(screen, font, f"Best: {best_score}", 130, 8)
        text(screen, font, f"FPS: {fps}", 260, 8)
        
        if game_over:
            overlay = pygame.Surface((W, H), pygame.SRCALPHA)
            overlay.fill(PAUSE_OVERLAY)
            screen.blit(overlay, (0, 0))
            text(screen, big_font, "Game is over!", W//2,H//2-30, center=True)
            text(screen, font, "Press R - resume, Esc - exit", W//2, H//2+10, center=True)
        
        pygame.display.flip()
        clock.tick(fps if not game_over else 15)


if __name__ == "__main__":
    main()

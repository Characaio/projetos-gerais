import pygame
import random
import numpy as np

# Constantes
GRID_SIZE = 2
GRID_COLS = 400
GRID_ROWS = 300
WIDTH = GRID_COLS * GRID_SIZE
HEIGHT = GRID_ROWS * GRID_SIZE
FPS = 60

# Cores
WATER_COLOR = (0, 119, 190)
BG_COLOR = (20, 20, 20)

# Tipos
EMPTY = 0
WATER = 1

# Grid de partículas
grid = [[EMPTY for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

# Setup Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Surface de simulação (usada como tela de pixels)
sim_surface = pygame.Surface((GRID_COLS, GRID_ROWS))

def in_bounds(x, y):
    return 0 <= x < GRID_COLS and 0 <= y < GRID_ROWS

def update_particles():
    for y in reversed(range(GRID_ROWS)):
        for x in range(GRID_COLS):
            if grid[y][x] == WATER:
                below = (x, y + 1)
                down_left = (x - 1, y + 1)
                down_right = (x + 1, y + 1)
                left = (x - 1, y)
                right = (x + 1, y)

                moved = False

                if in_bounds(*below) and grid[below[1]][below[0]] == EMPTY:
                    grid[below[1]][below[0]] = WATER
                    grid[y][x] = EMPTY
                    moved = True

                if not moved:
                    directions = [(-1, down_left), (1, down_right), (-1, left), (1, right)]
                    random.shuffle(directions)
                    for dx, (nx, ny) in directions:
                        if in_bounds(nx, ny) and grid[ny][nx] == EMPTY:
                            grid[ny][nx] = WATER
                            grid[y][x] = EMPTY
                            break

def spawn_water(mouse_pos):
    mx, my = mouse_pos
    gx = mx // GRID_SIZE
    gy = my // GRID_SIZE
    if in_bounds(gx, gy):
        grid[gy][gx] = WATER

def draw_pixels():
    pixels = pygame.surfarray.pixels3d(sim_surface)
    pixels[:, :] = BG_COLOR  # Limpa a tela

    for y in range(GRID_ROWS):
        for x in range(GRID_COLS):
            if grid[y][x] == WATER:
                pixels[x, y] = WATER_COLOR

    del pixels  # Libera acesso ao array de pixels

    scaled = pygame.transform.scale(sim_surface, (WIDTH, HEIGHT))
    screen.blit(scaled, (0, 0))

# Loop principal
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]:
        spawn_water(pygame.mouse.get_pos())

    update_particles()
    draw_pixels()
    pygame.display.flip()

pygame.quit()

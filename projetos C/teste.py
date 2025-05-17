import pygame
from pygame.locals import QUIT

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Draw Polygon Example")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Define the points of the polygon
polygon_points = [(110, 110), (200, 50), (290, 110), (250, 200), (150, 200)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the polygon
    pygame.draw.polygon(screen, BLUE, polygon_points, 0)  # 0 for filled polygon

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

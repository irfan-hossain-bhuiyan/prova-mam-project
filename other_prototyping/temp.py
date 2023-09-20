
import pygame
import numpy as np

# Create a NumPy array of points
points_array = np.array([[100, 200], [150, 250], [200, 200], [250, 250]])

# Convert the NumPy array to a list of tuples
#points_list = points_array.tolist()

# Initialize Pygame
pygame.init()

# Create a Pygame window and surface
screen = pygame.display.set_mode((400, 400))
surface = pygame.Surface((400, 400))

# Draw the lines using the list of points
pygame.draw.lines(surface, (255, 0, 0), True, points_array, 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(surface, (0, 0))
    pygame.display.flip()

pygame.quit()

import numpy as np
import pygame

# Set the dimensions of the grid
N = 100

# Set the initial state of the grid
grid = np.random.randint(2, size=(N, N))

# Set the dimensions of the pygame window
width, height = 800, 800

# Initialize pygame
pygame.init()

# Set the window size
size = (width, height)

# Create the window
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Conway's Game of Life")

# Run the simulation until the user closes the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the grid
    for i in range(N):
        for j in range(N):
            if grid[i, j] == 1:
                pygame.draw.rect(screen, (255, 255, 255), (i * (width / N), j * (height / N), (width / N), (height / N)))

    # Update the state of the grid
    new_grid = np.copy(grid)
    for i in range(N):
        for j in range(N):
            n_neighbors = np.sum(grid[i - 1:i + 2, j - 1:j + 2]) - grid[i, j]
            if grid[i, j] == 1:
                if n_neighbors < 2 or n_neighbors > 3:
                    new_grid[i, j] = 0
            else:
                if n_neighbors == 3:
                    new_grid[i, j] = 1

    # Update the grid
    grid = new_grid

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()

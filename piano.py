import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NOTE_NAMES = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

# Initialize the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Virtual Piano')

# Key dimensions
key_width = int(WIDTH / 14)
key_height = HEIGHT

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Draw keys
    screen.fill(WHITE)
    for i, note in enumerate(NOTE_NAMES):
        key_color = BLACK if note in ['C', 'D', 'F', 'G', 'A'] else WHITE
        pygame.draw.rect(screen, key_color, (i * key_width, 0, key_width, key_height))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def generate_array(n, min_val=10, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(n)]

array = generate_array(50)  # 50 random numbers

def draw_array(array, color_positions={}):
    screen.fill(BLACK)
    bar_width = WIDTH // len(array)

    for i, val in enumerate(array):
        color = color_positions.get(i, BLUE)
        pygame.draw.rect(screen, color, (i * bar_width, HEIGHT - val * 5, bar_width, val * 5))
    
    pygame.display.update()

def bubble_sort(array):
    n = len(array)
    global running  # Allow modification of the main loop variable
    for i in range(n):
        for j in range(n - i - 1):
            for event in pygame.event.get():  # Handle events during sorting
                if event.type == pygame.QUIT:
                    running = False
                    return  # Exit sorting immediately

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                draw_array(array, {j: RED, j + 1: GREEN})  # Highlight swapping
                pygame.time.wait(50)  # Non-blocking delay

running = True
sorting = False

while running:
    screen.fill(BLACK)
    draw_array(array)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not sorting:
                sorting = True
                bubble_sort(array)
                sorting = False

pygame.quit()

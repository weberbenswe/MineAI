import pygame
from minesweeper import Minesweeper
import sys

rows, cols = 10, 10
cell_size = 30
mines = 20

minesweeper_game = Minesweeper(rows, cols, mines)
minesweeper_game.place_mines()

# pygame setup
pygame.init()
screen = pygame.display.set_mode((cols * cell_size, rows * cell_size))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row, col = y, x

            revealed_value = minesweeper_game.reveal_cell(row, col)

            if minesweeper_game.is_mine(row, col):
                print("Game Over! Mine hit.")
            else:
                print(f"Reveal value: {revealed_value}")
                print(f"Adjacent mines: {minesweeper_game.count_adjacent_mines(row, col)}")

    screen.fill(255, 255, 255)

    for i in range(rows):
        for j in range(cols):
            rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)

            if minesweeper_game.revealed[i, j]:
                pygame.draw.rect(screen, (200, 200, 200), rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
sys.exit()


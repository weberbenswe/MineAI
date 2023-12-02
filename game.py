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
font = pygame.font.Font(None, 36)
running = True

WHITE = (255, 255, 255)
GREY = (169, 169, 169)
RED = (255, 0, 0)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row, col = y // cell_size, x // cell_size  

            revealed_value = minesweeper_game.reveal_cell(row, col)

            if minesweeper_game.is_mine(row, col):
                text = font.render("Game Over! Mine hit.", True, RED)
                screen.blit(text, (10, rows*cell_size + 10))
            else:
                reveal_text = f"Reveal value: {revealed_value}"
                adjacent_mines_text = f"Adjacent mines: {minesweeper_game.count_adjacent_mines(row, col)}"

                reveal_surface = font.render(reveal_text, True, GREY)
                adjacent_mines_surface = font.render(adjacent_mines_text, True, GREY)

                screen.blit(reveal_surface, (10, rows * cell_size + 10))
                screen.blit(reveal_surface, (10, rows * cell_size + 40))

    screen.fill(WHITE)

    for i in range(rows):
        for j in range(cols):
            rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)

            if minesweeper_game.revealed[i, j]:
                pygame.draw.rect(screen, GREY, rect)
            
            if minesweeper_game.is_mine(i, j):
                pygame.draw.circle(screen, RED, rect.center, cell_size // 2)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
sys.exit()


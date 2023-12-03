import pygame
from minesweeper import Minesweeper_Board
import sys

rows, cols = 10, 10
cell_size = 50
mines = 20

minesweeper_game = Minesweeper_Board(rows, cols, mines)
minesweeper_game.place_mines()
minesweeper_game.calculate_adjacent_mines()

# pygame setup
pygame.init()
screen = pygame.display.set_mode((cols * cell_size, rows * cell_size))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
running = True

WHITE = (255, 255, 255)
GREY = (169, 169, 169)
BLACK = (0, 0, 0)
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
            cell = minesweeper_game.board[row][col]

            revealed_value = minesweeper_game.reveal_cell(cell)

            if minesweeper_game.is_mine(cell):
                print('Mine Hit')
            else:
                print('Safe')
    
    screen.fill(WHITE)

    for i in range(rows):
        for j in range(cols):
            rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
            cell = minesweeper_game.board[i][j]

            # Draw revealed cells in grey with black border
            if minesweeper_game.is_revealed(cell):

                if minesweeper_game.is_mine(cell):
                    pygame.draw.rect(screen, RED, rect)
                    pygame.draw.rect(screen, BLACK, rect, 1)

                else:
                    revealed_value = minesweeper_game.cell_adjacent_value(cell)
                    text_surface = font.render(str(revealed_value), True, BLACK)
                    text_rect = text_surface.get_rect(center=rect.center)
                    pygame.draw.rect(screen, WHITE, rect)
                    pygame.draw.rect(screen, BLACK, rect, 1)
                    screen.blit(text_surface, text_rect)

            # Draw hidden cells in grey
            else:
                pygame.draw.rect(screen, GREY, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
sys.exit()


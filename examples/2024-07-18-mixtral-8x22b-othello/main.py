import pygame
import sys

# Constants
WIDTH = 640
HEIGHT = 680
SQUARE_SIZE = 80
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BG_COLOR = GREY
LINE_COLOR = BLACK
BOARD_ROWS = BOARD_COLS = 8
EMPTY = '.'
BLACK_DISC = 'B'
WHITE_DISC = 'W'

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 40)

def draw_board():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            x, y = (col * SQUARE_SIZE), (row * SQUARE_SIZE) + 80
            pygame.draw.rect(screen, GREY, (x, y, SQUARE_SIZE, SQUARE_SIZE))
    draw_grid()

def draw_grid():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS + 1):
            x = col * SQUARE_SIZE
            y = (row * SQUARE_SIZE) + 80
            pygame.draw.line(screen, LINE_COLOR, (x, 80), (x, HEIGHT - 40))
    for row in range(BOARD_ROWS + 1):
        x = (row * SQUARE_SIZE) + 80
        pygame.draw.line(screen, LINE_COLOR, (0, x), (WIDTH, x))

def draw_discs(board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == BLACK_DISC:
                pygame.draw.circle(screen, BLACK, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2), int((row 
* SQUARE_SIZE) + SQUARE_SIZE - SQUARE_SIZE // 4)), SQUARE_SIZE // 3)
            elif board[row][col] == WHITE_DISC:
                pygame.draw.circle(screen, WHITE, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2), int((row 
* SQUARE_SIZE) + SQUARE_SIZE - SQUARE_SIZE // 4)), SQUARE_SIZE // 3)

def draw_status(msg):
    msg = font.render(msg, True, BLACK)
    screen.blit(msg, (50, HEIGHT-10))

# Initialize the game board with starting positions
board = [
    ['.' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)
]
board[3][4], board[4][3] = BLACK_DISC, BLACK_DISC
board[3][3], board[4][4] = WHITE_DISC, WHITE_DISC

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col, row = int((pos[0]-40) // SQUARE_SIZE), int(max(80 - 40 + (SQUARE_SIZE * BOARD_ROWS) 
- pos[1], 0)) // SQUARE_SIZE

    draw_board()
    draw_discs(board)
    pygame.display.flip()
    clock.tick(60)
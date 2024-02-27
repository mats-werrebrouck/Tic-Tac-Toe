import pygame, sys

# Initiating PyGame
pygame.init()

WIDTH, HEIGHT = 900, 900

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

BOARD = pygame.image.load("assets/board.png")
X = pygame.image.load("assets/x.png")
O = pygame.image.load("assets/o.png")

BG_COLOR = (255, 255, 255)

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
graphical_board = [[None, None, None], [None, None, None], [None, None, None]]

turn = "X"

SCREEN.fill(BG_COLOR)
SCREEN.blit(BOARD, (64, 64))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        pygame.display.update()
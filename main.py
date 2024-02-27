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

# 2-dimensional list to store the board
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 3-dimensional list to store the images and their positions
# graphical_board[i][j] = [image, rect]
# image: X or O
# rect: position of the image
# None if the position is empty
graphical_board = [[[None, None] for _ in range(3)] for _ in range(3)]

turn = "X"

SCREEN.fill(BG_COLOR)
SCREEN.blit(BOARD, (64, 64))

def update_graphical_board(board, xImg, oImg):
    global graphical_board
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                # Create an X image
                graphical_board[i][j][0] = xImg
                # Create a rect
                # The center of the rect is at (j*300+150, i*300+150)
                # 300 is the width and height of each cell
                # 150 is half of 300
                # y = mx + c
                graphical_board[i][j][1] = xImg.get_rect(center=(j*300+150, i*300+150))
            elif board[i][j] == "O":
                # Create an O image
                graphical_board[i][j][0] = oImg
                # Create a rect
                graphical_board[i][j][1] = oImg.get_rect(center=(j*300+150, i*300+150))

def add_x_o(board, graphical_board, turn):
    # Get the current position of the mouse and convert it to the position on the board
    current_pos = pygame.mouse.get_pos()
    converted_x = (current_pos[0]-65)/835*2
    converted_y = current_pos[1]/835*2

    # If the position is empty, add X or O
    if board[round(converted_y)][round(converted_x)] != "X" and board[round(converted_y)][round(converted_x)] != "O":
        board[round(converted_y)][round(converted_x)] = turn
        
        # Update the turn to the next player
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    
    # Update the graphical board
    update_graphical_board(board, X, O)

    for i in range(3):
        for j in range(3):
            # If the position is not empty, blit the image
            if graphical_board[i][j][0] != None:
                SCREEN.blit(graphical_board[i][j][0], graphical_board[i][j][1])

    return board, turn

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board, turn = add_x_o(board, graphical_board, turn)
        
        pygame.display.update()
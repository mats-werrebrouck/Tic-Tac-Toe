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

turn = "x"

SCREEN.fill(BG_COLOR)
SCREEN.blit(BOARD, (64, 64))

pygame.display.update()

def update_graphical_board(board, xImg, oImg):
    global graphical_board
    for i in range(3):
        for j in range(3):
            if board[i][j] == "x":
                # Create an X image
                graphical_board[i][j][0] = xImg
                # Create a rect
                # The center of the rect is at (j*300+150, i*300+150)
                # 300 is the width and height of each cell
                # 150 is half of 300
                # y = mx + c
                graphical_board[i][j][1] = xImg.get_rect(center=(j*300+150, i*300+150))
            elif board[i][j] == "o":
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
    if board[round(converted_y)][round(converted_x)] != "x" and board[round(converted_y)][round(converted_x)] != "o":
        board[round(converted_y)][round(converted_x)] = turn
        
        # Update the turn to the next player
        if turn == "x":
            turn = "o"
        else:
            turn = "x"
    
    # Update the graphical board
    update_graphical_board(board, X, O)

    for i in range(3):
        for j in range(3):
            # If the position is not empty, blit the image
            if graphical_board[i][j][0] != None:
                SCREEN.blit(graphical_board[i][j][0], graphical_board[i][j][1])

    return board, turn

game_over = False

def check_winner(board):
    # Check rows
    for i in range(3):
        if ((board[i][0] == board[i][1] == board[i][2]) and (board[i][0] is not None)):
            # Highlight the winning row
            for j in range(3):
                graphical_board[i][j][0] = pygame.image.load(f"assets/win_{board[i][0]}.png")
                SCREEN.blit(graphical_board[i][j][0], graphical_board[i][j][1])
            pygame.display.update()
            return board[i][0]
        
    # Check columns
    for i in range(3):
        if ((board[0][i] == board[1][i] == board[2][i]) and (board[0][i] is not None)):
            # Highlight the winning column
            for j in range(3):
                graphical_board[j][i][0] = pygame.image.load(f"assets/win_{board[0][i]}.png")
                SCREEN.blit(graphical_board[j][i][0], graphical_board[j][i][1])
            pygame.display.update()
            return board[0][i]
        
    # Check diagonals
    if ((board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None)):
        # Highlight the winning diagonal
        for i in range(3):
            graphical_board[i][i][0] = pygame.image.load(f"assets/win_{board[0][0]}.png")
            SCREEN.blit(graphical_board[i][i][0], graphical_board[i][i][1])
        pygame.display.update()
        return board[0][0]
    if ((board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None)):
        # Highlight the winning diagonal
        for i in range(3):
            graphical_board[i][2-i][0] = pygame.image.load(f"assets/win_{board[0][2]}.png")
            SCREEN.blit(graphical_board[i][2-i][0], graphical_board[i][2-i][1])
        pygame.display.update()
        return board[0][2]
    
    # Check for draw
    if all(board[i][j] == "X" and board[i][j] == "O" for i in range(3) for j in range(3)):
        return "Draw"

    return None

# Game loop
while True:
    for event in pygame.event.get():
        # If the user closes the window, quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # If the user clicks the mouse button, add X or O
        if event.type == pygame.MOUSEBUTTONDOWN:
            board, turn = add_x_o(board, graphical_board, turn)

            # If the game is over, reset the game
            if game_over:
                # Reset the game
                board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                graphical_board = [[[None, None] for _ in range(3)] for _ in range(3)]
                turn = "x"
                game_over = False
                SCREEN.fill(BG_COLOR)
                SCREEN.blit(BOARD, (64, 64))
                pygame.display.update()
            
            # If there is a winner, finish the game
            if check_winner(board) is not None:
                game_over = True
            
            pygame.display.update()
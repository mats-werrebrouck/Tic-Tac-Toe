import pygame, sys

class TicTacToe:
    def __init__(self):
        # Initiating PyGame
        pygame.init()

        self.width, self.height = 900, 900

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tic Tac Toe")

        self.board_img = pygame.image.load("assets/board.png")
        self.x_img = pygame.image.load("assets/x.png")
        self.o_img = pygame.image.load("assets/o.png")

        self.bg_color = (255, 255, 255)

        # 2-dimensional list to store the board
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        # 3-dimensional list to store the images and their positions
        # graphical_board[i][j] = [image, rect]
        # image: X or O
        # rect: position of the image
        # None if the position is empty
        self.graphical_board = [[[None, None] for _ in range(3)] for _ in range(3)]

        self.turn = "x"
        self.game_over = False

        self.screen.fill(self.bg_color)
        self.screen.blit(self.board_img, (64, 64))

        pygame.display.update()

    def update_graphical_board(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "x":
                    # Create an X image
                    self.graphical_board[i][j][0] = self.x_img
                    # Create a rect
                    # The center of the rect is at (j*300+150, i*300+150)
                    # 300 is the width and height of each cell
                    # 150 is half of 300
                    # y = mx + c
                    self.graphical_board[i][j][1] = self.x_img.get_rect(center=(j*300+150, i*300+150))
                elif self.board[i][j] == "o":
                    # Create an O image
                    self.graphical_board[i][j][0] = self.o_img
                    # Create a rect
                    self.graphical_board[i][j][1] = self.o_img.get_rect(center=(j*300+150, i*300+150))

    def add_x_o(self):
        # Get the current position of the mouse and convert it to the position on the board
        current_pos = pygame.mouse.get_pos()
        converted_x = (current_pos[0]-65)/835*2
        converted_y = current_pos[1]/835*2

        # If the position is empty, add X or O
        if self.board[round(converted_y)][round(converted_x)] != "x" and self.board[round(converted_y)][round(converted_x)] != "o":
            self.board[round(converted_y)][round(converted_x)] = self.turn
            
            # Update the turn to the next player
            if self.turn == "x":
                self.turn = "o"
            else:
                self.turn = "x"
        
        # Update the graphical board
        self.update_graphical_board()

        for i in range(3):
            for j in range(3):
                # If the position is not empty, blit the image
                if self.graphical_board[i][j][0] != None:
                    self.screen.blit(self.graphical_board[i][j][0], self.graphical_board[i][j][1])

        pygame.display.update()

    def check_winner(self):
        # Check rows
        for i in range(3):
            if ((self.board[i][0] == self.board[i][1] == self.board[i][2]) and (self.board[i][0] is not None)):
                # Highlight the winning row
                for j in range(3):
                    self.graphical_board[i][j][0] = pygame.image.load(f"assets/win_{self.board[i][0]}.png")
                    self.screen.blit(self.graphical_board[i][j][0], self.graphical_board[i][j][1])
                pygame.display.update()
                return self.board[i][0]
            
        # Check columns
        for i in range(3):
            if ((self.board[0][i] == self.board[1][i] == self.board[2][i]) and (self.board[0][i] is not None)):
                # Highlight the winning column
                for j in range(3):
                    self.graphical_board[j][i][0] = pygame.image.load(f"assets/win_{self.board[0][i]}.png")
                    self.screen.blit(self.graphical_board[j][i][0], self.graphical_board[j][i][1])
                pygame.display.update()
                return self.board[0][i]
            
        # Check diagonals
        if ((self.board[0][0] == self.board[1][1] == self.board[2][2]) and (self.board[0][0] is not None)):
            # Highlight the winning diagonal
            for i in range(3):
                self.graphical_board[i][i][0] = pygame.image.load(f"assets/win_{self.board[0][0]}.png")
                self.screen.blit(self.graphical_board[i][i][0], self.graphical_board[i][i][1])
            pygame.display.update()
            return self.board[0][0]
        if ((self.board[0][2] == self.board[1][1] == self.board[2][0]) and (self.board[0][2] is not None)):
            # Highlight the winning diagonal
            for i in range(3):
                self.graphical_board[i][2-i][0] = pygame.image.load(f"assets/win_{self.board[0][2]}.png")
                self.screen.blit(self.graphical_board[i][2-i][0], self.graphical_board[i][2-i][1])
            pygame.display.update()
            return self.board[0][2]
        
        # Check for draw
        if all(self.board[i][j] == "x" or self.board[i][j] == "o" for i in range(3) for j in range(3)):
            return "Draw"

        return None

    def reset_game(self):
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.graphical_board = [[[None, None] for _ in range(3)] for _ in range(3)]
        self.turn = "x"
        self.game_over = False
        self.screen.fill(self.bg_color)
        self.screen.blit(self.board_img, (64, 64))
        pygame.display.update()

    def run(self):
        # Game loop
        while True:
            for event in pygame.event.get():
                # If the user closes the window, quit the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # If the user clicks the mouse button, add X or O
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.add_x_o()

                    # If the game is over, reset the game
                    if self.game_over:
                        self.reset_game()
                    
                    # If there is a winner, finish the game
                    if self.check_winner() is not None:
                        self.game_over = True
                    
                    pygame.display.update()

game = TicTacToe()
game.run()
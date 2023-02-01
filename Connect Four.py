"""
Project Name: Connect Four
This game is basically a board game that two players can play together using pygame. It is a very
simple board game that is totally played on a static board. By using numpy, we can create the board
with width and length. Then we use draw method in pygame to separete two players with red and yellow
circle. When either one of them achieves "connect four" horizontally, vertically, or diagonally, the
game automatically stops and display the result of this game.

Technology Utilized: Python, Pygame, NumPy, Playsound

Author: Xiaoyang Wei
Course: Python Project
Date: Feb 1st, 2023
"""

import numpy as np
import pygame
import sys
import math
from playsound import playsound

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))
    
def winning_move(board, piece):
    # check horizontal locations
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return  True
    
    # check vertical locations
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return  True

    # check diagonal locations
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return  True
    return False

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (c*SQUARESIZE+SQUARESIZE//2, r*SQUARESIZE+SQUARESIZE+SQUARESIZE//2), RADIOUS)
            """
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (c*SQUARESIZE+SQUARESIZE//2, r*SQUARESIZE+SQUARESIZE+SQUARESIZE//2), RADIOUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (c*SQUARESIZE+SQUARESIZE//2, r*SQUARESIZE+SQUARESIZE+SQUARESIZE//2), RADIOUS)
            """
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (c*SQUARESIZE+SQUARESIZE//2, height - (r*SQUARESIZE+SQUARESIZE//2)), RADIOUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (c*SQUARESIZE+SQUARESIZE//2, height - (r*SQUARESIZE+SQUARESIZE//2)), RADIOUS)
    pygame.display.update()

board = create_board()
# print(board)
game_over = False
turns = 0

pygame.init()
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)

RADIOUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

playsound("Carry You.mp4", False)

# main loop of application
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turns == 0:
                pygame.draw.circle(screen, RED, (posx, SQUARESIZE//2), RADIOUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, SQUARESIZE//2), RADIOUS)
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            print(event.pos)
            posx = event.pos[0]
            col = int(math.floor(posx/SQUARESIZE))
            if turns == 0:
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
                    if winning_move(board, 1):
                        label = myfont.render("PLAYER 1 Wins!!! Congrats!!!", 1, RED)
                        screen.blit(label, (40, 10))
                        # print("PLAYER 1 Wins!!! Congrats!!!")
                        game_over = True
            else:
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
                    if winning_move(board, 2):
                        label = myfont.render("PLAYER 2 Wins!!! Congrats!!!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        # print("PLAYER 2 Wins!!! Congrats!!!")
                        game_over = True
            # print_board(board)
            draw_board(board)
            turns += 1
            turns %= 2
            if game_over:
                pygame.time.wait(3000)
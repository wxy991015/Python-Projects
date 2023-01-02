"""
This game 

Author: Xiaoyang Wei
Project Name: Snake Game
Date: December 30th, 2022
"""

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class Cube():
    rows = 20
    w = 500
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos(self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        # distance between each cube object
        dis = self.w // self.rows

        # pos => (rows, cols)
        i = self.pos[0]
        j = self.pos[1]

        # draw cube inside the grid
        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))
        if eyes:
            centre = dis // 2
            radius = 3

            # postion of each eye
            circleMiddle1 = i * dis + centre - radius, j * dis + 8
            circleMiddle2 = i * dis + dis - radius * 2, j * dis + 8

            # draw each eye based on color, position, and radius
            pygame.draw.circle(surface, (0,0,0), circleMiddle1, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)


class Snake():
    body = []
    turns = dict()

    # RGB color & x^y coordinates
    def __init__(self, color, pos):
        self.color = color

        # create a snake head when initialization
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            for key in keys:

                # move snake to the left
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                # move snake to the right
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                # move snake up
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                # move snake down
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]

                # move the cube object
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows-1)
                else:
                    c.move(c.dirnx, c.dirny)


    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    x = 0
    y = 0
    for l in range(rows):
        x += sizeBtwn
        y += sizeBtwn

        # draw horizontal line from (x,0) to (x,w)
        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))

        # draw vertical line from (0,y) to (w,y)
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y))

def redrawWindow(surface):
    global rows, width, s
    surface.fill((0, 0, 0))
    s.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()

# create main window of the game
def main():
    global width, rows, s
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = Snake((255, 0, 0), (10, 10))
    flag = True

main()
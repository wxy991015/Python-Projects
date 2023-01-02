"""
Pong Game:
This project is to create Pong game using Python Turtle. Pong is one of the first computer
games that ever created, this simple "tennis like" game features two paddles and a ball,
the goal is to defeat your opponent by being the first one to gain10 point, a player gets
a point once the opponent misses a ball. The game can be played with two human players, or
one player against a computer controlled paddle. The game was originally developed by Allan
Alcorn and released in 1972 by Atari corporations. Soon, Pong became a huge success, and became
the first commercially successful game, on 1975, Atari release a home edition of Pong (the first
version was played on Arcade machines) which sold 150,000 units. Today, the Pong Game is considered 
to be the game which started the video games industry, as it proved that the video games market can
produce significant revenues.

This game is created by Xiaoyang Wei. The author uses Python Turtle, a Python graphic tool to create
a simplified version of the Pong game. For creativity, the author adds background music and message
box to make this game look more fancy and enjoyable.

Author: Xiaoyang Wei
Project Name: Pong Game
Date: January 1st, 2023
"""

import turtle
from tkinter import *
from tkinter import messagebox
from playsound import playsound

# move paddle A up by specificed steps
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

# move paddle A down by specified steps
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# move paddle B up by specificed steps
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

# move paddle B down by specified steps
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

window = turtle.Screen()
window.title("Pong by Xiaoyang Wei")
window.bgcolor("powderblue")

# screen => width, height = 800, 600
window.setup(width=800, height=600)
window.tracer(0)

# score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # 
paddle_a.shape("square")
# stretch the square to five-times width and maintain the original length
paddle_a.shapesize(stretch_wid=10, stretch_len=1)
paddle_a.color("red")
paddle_a.penup() # search for meaning
paddle_a.goto(-350, 0) # search for meaning

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # 
paddle_b.shape("square")
# stretch the square to five-times width and maintain the original length
paddle_b.shapesize(stretch_wid=10, stretch_len=1)
paddle_b.color("green")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # 
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(-5, 0)

# 2px per move (speed)
ball.dx = 2
ball.dy = 1

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player A: 0  Player B: 0", align="center", font=("Times New Roman", 24, "normal"))

window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# play background music but not interfere the game
playsound("background.mp4", False)

# add messagebox here

while True:
    window.update()
    # Ball
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check y cooridinate
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        # add & to avoid delaying

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    # border check x coordinate
    if ball.xcor() > 390:
        ball.sety(-390)
        # ball goes to center when reach the border
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Times New Roman", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.setx(390)
        # ball goes to center when reach the border
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Times New Roman", 24, "normal"))

    # paddle and ball collisions
    # paddle A
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 100 and ball.ycor() > paddle_a.ycor() - 100):
        ball.setx(-340)
        ball.dx *= -1

    # paddle B
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 100 and ball.ycor() > paddle_b.ycor() - 100):
        ball.setx(340)
        ball.dx *= -1
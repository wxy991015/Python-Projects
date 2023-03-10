#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:11:39 2022

@author: xiaoyangwei
"""

import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors?\n")
    computer = random.choice(["r", "p", "s"])
    if user == computer:
        return "It's a tie"
    elif is_win(user, computer):
        return "You won!"
    return "You Lose!"

def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True
    return False

print(play())
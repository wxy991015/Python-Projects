#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 23:38:53 2022

Author: Xiaoyang Wei
Project Name: Number Guess
Date: December 19th, 2022
"""

import random

def user_guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guessing a number between 1 and {x} => "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    
    print(f"Yah, congrats. You have guessed the number {random_number} correctly!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ")
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    
    print(f"Yah, congrats! The computer guesses the number {guess} correctly!")

def random_guess(x, euqal): # make two numbers equal to EQUAL
    # input a random guess nunber "FIRST" in range(1, x)
    guess1 = random.randint(1, x)
    # input another random guess number "SECOND" in range(1, x)
    guess2 = random.randint(1, x)
    print(guess1, guess2)
    guess_num1 = 0
    guess_num2 = 0
    while guess1 != guess2:
        if guess1 > guess2:
            guess1 -= 1
            guess_num1 += 1
        elif guess2 > guess1:
            guess2 -= 1
            guess_num2 += 1
    num1 = guess1 + guess_num1
    num2 = guess2 + guess_num2
    print(f"Yah, congrats! Two numbers are both equal to {guess1} successfully!")
    print(f"Two original numbers are {num1} and {num2}")

def number_of_guesses(x):
    low = 1
    high = x
    # input a random guess number "RANDOM_NUMBER" in range(1, x)
    random_number = random.randint(low, high)
    print(f"Random Number: {random_number}")
    guess = 0
    guesses_num = 0
    while guess != random_number:
        # check if "GUESS NUMBER" is lower than random_number
        if guess < random_number:
            low = guess + 1
            guess = random.randint(low, high)
            print(guess)
        # check if "GUESS NUMBER" is higher than random_number
        elif guess > random_number:
            high = guess - 1
            guess = random.randint(low, high)
            print(guess)
        guesses_num += 1
    return guesses_num
    
# def orginal_guess(x):
    # input a random guess number "RANDOM_NUMBER" in range(1, x)
    # 
    

print(number_of_guesses(1000))
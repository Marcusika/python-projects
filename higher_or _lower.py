#i made this myself (surprisingly) and managed to fix all errors by myself :D
import random
from random import randint
print("Welcome to higher or lower!")
print("The computer generates a number between 0 and 100,and you have to guess it")
print("The computer will tell you higher or lower until you guess the number")
print("Good Luck!")
guesses = 0
computer = randint(0, 100)
while True:
    guess = input("Guess a number: ")
    guess = int(guess)
    if guess > computer:
        print("Lower")
        guesses += 1
    elif guess < computer:
        print("Higher")
        guesses += 1
    else:
        print("You win!")
        guesses += 1
        break

print("You had " + str(guesses) + " guesses!")

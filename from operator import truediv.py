from operator import truediv
from random import *
theNum = randrange(1,10)
print("Number Guessing Game \n Guess a number (between 1 and 9)")
guess = False
while(guess != True):
    currentGuess = input("Enter your guess: ")
    if(theNum < currentGuess):
        print("Your guess is too large, choose something smaller than " + currentGuess)
    elif(theNum == currentGuess):
        print("Congrats you have won!")
        guess = True
    else(theNum > currentGuess):
        print("Your guess is too small, chose something larger than "+ currentGuess)
print("Congrats you have completed the game!")
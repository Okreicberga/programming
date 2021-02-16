# Program that promts the user to guess a number
# the program should keep prompting the user to guess the number until the user gets the right on
import random

numberToGuess = 30

guess = int(random.randint(0,100))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again:"))
print ("Well done! Yes the number was ", numberToGuess) 
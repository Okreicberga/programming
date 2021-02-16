# Program that promts the user to guess a number
# the program tell the user if there to guess to high or too low, each time they guess. 

numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
  if guess < numberToGuess:
    print("too low")
  else:
    print("too high")
  guess = int(input("Please guess the number:"))
print ("Well done! Yes the number was", numberToGuess)
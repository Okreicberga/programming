# Programm that asks the user to enter in a number and tthe programm will tell if a number even or odd
# Author: Olga Kreicberga 

number = int(input("enter an integer:"))
if (number % 2) == 0:
    print ("{} is an even number".format (number))
else:
        print ("{} is an odd number".format (number))
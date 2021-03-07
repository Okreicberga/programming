number=int(input('Enter number:\n')) # If it's odd, multiply it by three and add one

# Program at each step calculate the next value by taking a current valulue
def collatz(number):

    while number !=1: # Program end if the current value is one 
        if number% 2 == 0: # If it's even, divide it by two
            number= number//2
            print(number) # Program outputs the successive values 

        else: # If it's odd, multiply it by three and add one
           number=  3 * number + 1
           print(number)    

collatz(number)
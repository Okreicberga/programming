# Program that puts 10 random numbers into a queue(list)
# Program output all the values in the queue
# After program take the numbers from the queue one at a time and print it. The current numbers still in the queue
# The command popo(0) takes the first element out of a list
# Author: Olga Kreicberga 

import random
queue = []
numberOfNumbers=10
rangeTo=100

for n in range (0,numberOfNumbers) :
    queue.append(random.randint (0,rangeTo)) 

print ("queue is {}".format (queue))
while len(queue) != 0:
    currentNumber = queue.pop(0)
    print ("currnet Number is {} and the queue is {} ".format(currentNumber, queue)) 
print ("the queue is niw empty")
